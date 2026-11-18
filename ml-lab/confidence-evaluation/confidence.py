"""Calibrate a separate classifier on a held-out subset of the official training split."""
import argparse
import json
from pathlib import Path
import numpy as np
import pandas as pd
from huggingface_hub import hf_hub_download
from scipy.optimize import minimize_scalar
from scipy.special import logsumexp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

SOURCE = "c2d-usp/banking77-pt-br"
REVISION = "85f51c4"
SEED = 42

def load_data(split, path=None):
    if split not in ("train", "test"):
        raise ValueError("Only official splits")
    filename = path or hf_hub_download(repo_id=SOURCE, repo_type="dataset", revision=REVISION, filename=split + ".csv")
    frame = pd.read_csv(filename)
    if not {"frase", "rotulo"} <= set(frame):
        raise ValueError("Missing required columns")
    frame = frame[["frase", "rotulo"]].dropna().copy()
    for c in ("frase", "rotulo"):
        frame[c] = frame[c].astype(str).str.strip()
    frame = frame[(frame["frase"] != "") & (frame["rotulo"] != "")].reset_index(drop=True)
    if frame.empty:
        raise ValueError("No valid records")
    return frame

def model_pipeline():
    return Pipeline([
        ("tfidf", TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5),
                                  strip_accents="unicode", sublinear_tf=True,
                                  max_features=120000, min_df=2)),
        ("clf", LinearSVC(C=1.0, random_state=SEED)),
    ])

def softmax_temperature(logits, temperature):
    z = np.asarray(logits, dtype=float)
    if z.ndim != 2 or z.shape[1] < 3 or not np.isfinite(z).all():
        raise ValueError("Scores must be finite N-by-K (K>=3)")
    if not np.isfinite(temperature) or temperature <= 0:
        raise ValueError("Invalid temperature")
    z = z / temperature
    return np.exp(z - logsumexp(z, axis=1, keepdims=True))

def target_indices(classes, labels):
    names = {str(c): i for i, c in enumerate(classes)}
    if len(names) != len(classes):
        raise ValueError("Duplicate classes")
    if any(str(y) not in names for y in labels):
        raise ValueError("Unknown ground truth class")
    return np.array([names[str(y)] for y in labels], dtype=int)

def nll(prob, targets):
    p = np.asarray(prob)
    if p.ndim != 2 or len(targets) != len(p) or not len(p):
        raise ValueError("Mismatched probability shapes")
    return float(-np.log(np.clip(p[np.arange(len(p)), targets], 1e-15, 1)).mean())

def ece(prob, targets, bins=10):
    if bins < 1:
        raise ValueError("At least one bin")
    confidence = prob.max(axis=1)
    correct = prob.argmax(axis=1) == targets
    score = 0.0
    for j in range(bins):
        left, right = j / bins, (j + 1) / bins
        mask = (confidence >= left) & ((confidence <= right) if j == bins-1 else (confidence < right))
        if np.any(mask):
            score += float(mask.mean()) * abs(float(confidence[mask].mean())-float(correct[mask].mean()))
    return float(score)

def brier(prob, targets):
    onehot = np.zeros_like(prob)
    onehot[np.arange(len(prob)), targets] = 1
    return float(np.square(prob-onehot).sum(axis=1).mean())

def fit_temperature(cal_logits, cal_targets):
    res = minimize_scalar(
        lambda u: nll(softmax_temperature(cal_logits, float(np.exp(u))), cal_targets),
        bounds=(float(np.log(.05)), float(np.log(30.0))),
        method="bounded",
        options={"xatol": 1e-4},
    )
    if not res.success:
        raise RuntimeError("Failed to optimize temperature")
    return float(np.exp(res.x))

def wilson_lower(correct, total, z=1.96):
    if not 0 <= correct <= total or total < 1:
        raise ValueError("Invalid count")
    p = correct/total
    middle = p + z*z/(2*total)
    radius = z*np.sqrt(p*(1-p)/total + z*z/(4*total*total))
    return float((middle-radius)/(1+z*z/total))

def choose_threshold(cal_probs, cal_targets, target=.9, min_count=50):
    if not 0 < target <= 1 or min_count < 1:
        raise ValueError("Invalid target/min count")
    confidence = cal_probs.max(axis=1)
    correct = cal_probs.argmax(axis=1) == cal_targets
    # Ascending threshold maximizes coverage among qualifying policies.
    for threshold in sorted(set(float(x) for x in confidence)):
        mask = confidence >= threshold
        n = int(mask.sum())
        if n < min_count:
            continue
        good = int(correct[mask].sum())
        lower = wilson_lower(good, n)
        if lower >= target:
            return {"threshold": threshold, "coverage": n/len(confidence),
                    "accepted": n, "accuracy": good/n,
                    "wilson_lower": lower, "target": target}
    return {"threshold": None, "coverage": 0.0, "accepted": 0,
            "accuracy": None, "wilson_lower": None, "target": target}

def selective(prob, target, policy):
    cutoff = policy["threshold"]
    mask = prob.max(axis=1) >= cutoff if cutoff is not None else np.zeros(len(prob), dtype=bool)
    n = int(mask.sum())
    accuracy = float((prob.argmax(axis=1)[mask] == target[mask]).mean()) if n else None
    return {"accepted": n, "coverage": float(mask.mean()),
            "accuracy_on_accepted": accuracy,
            "risk_on_accepted": 1-accuracy if accuracy is not None else None}

def summary_scores(probs, target):
    return {"negative_log_likelihood": nll(probs, target),
            "expected_calibration_error_10": ece(probs, target),
            "multiclass_brier_sum": brier(probs, target)}

def evaluate(train, test, *, min_accepted=50):
    if train["rotulo"].nunique() < 3 or train["rotulo"].value_counts().min() < 3:
        raise ValueError("Insufficient class samples")
    if set(test["rotulo"]) - set(train["rotulo"]):
        raise ValueError("Unseen test labels")
    fit, cal = train_test_split(train, stratify=train["rotulo"], test_size=.2, random_state=SEED)
    clf = model_pipeline()
    clf.fit(fit["frase"], fit["rotulo"])
    classes = clf.named_steps["clf"].classes_
    cal_y = target_indices(classes, cal["rotulo"])
    cal_logits = clf.decision_function(cal["frase"])
    temp = fit_temperature(cal_logits, cal_y)
    policy = choose_threshold(softmax_temperature(cal_logits, temp), cal_y, min_count=min_accepted)
    test_y = target_indices(classes, test["rotulo"])
    test_logits = clf.decision_function(test["frase"])
    raw = softmax_temperature(test_logits, 1)
    calibrated = softmax_temperature(test_logits, temp)
    pred = calibrated.argmax(axis=1)

    train_texts = set(train["frase"].str.casefold())
    duplicates = test["frase"].str.casefold().isin(train_texts).to_numpy()
    independent = ~duplicates
    if not independent.any():
        raise ValueError("All test data duplicates official train")
    curve = []
    sorted_order = np.argsort(-calibrated.max(axis=1), kind="stable")
    correct_sorted = (pred == test_y)[sorted_order]
    for coverage in (.25, .5, .75, 1.0):
        n = max(1, int(len(test_y)*coverage))
        curve.append({"coverage": coverage, "accepted": n, "accuracy_on_accepted": float(correct_sorted[:n].mean())})
    report = {
        "experiment": "banking77-ptbr-calibration-v1",
        "data": {"source": SOURCE, "revision": REVISION, "license": "CC BY 4.0",
                 "train": len(train), "fit": len(fit), "calibration": len(cal),
                 "test": len(test), "test_rows_matching_any_train_text": int(duplicates.sum()),
                 "note": "Researcher-reviewed translations, not production-native Portuguese"},
        "model": "char_wb TF-IDF + LinearSVC, trained on 80% of OFFICIAL train only",
        "temperature": temp,
        "test_accuracy": float(accuracy_score(test_y, pred)),
        "test_macro_f1": float(f1_score(test_y, pred, average="macro", zero_division=0)),
        "test_uncalibrated_softmax": summary_scores(raw, test_y),
        "test_temperature_scaled": summary_scores(calibrated, test_y),
        "threshold_selected_on_calibration": policy,
        "test_selective_classification": selective(calibrated, test_y, policy),
        "test_risk_coverage_curve_diagnostic_only": curve,
        "test_nonexact_overlap": {"rows": int(independent.sum()),
            "accuracy": float((pred[independent] == test_y[independent]).mean()),
            **summary_scores(calibrated[independent], test_y[independent])},
        "limitations": [
            "This is NOT the previous published model refitted on all training rows.",
            "Temperature and threshold were both chosen using the same calibration split; lower-bound precision there is not an out-of-sample guarantee.",
            "Softmax of uncalibrated SVM margins is not a validated probability.",
            "The published confidence values need external-domain and temporal calibration studies.",
            "Official train and test have overlapping texts; duplicate-free diagnostic included.",
            "Risk-coverage points evaluated on test are descriptive; no threshold is selected using test.",
            "Threshold target 90% is illustrative, not an operational SLA.",
        ],
    }
    return clf, report

def model_card(report):
    r = report
    raw, scaled = r["test_uncalibrated_softmax"], r["test_temperature_scaled"]
    pol, sel = r["threshold_selected_on_calibration"], r["test_selective_classification"]
    def val(x):
        return "N/A" if x is None else f"{x:.4f}"
    return f"""---
language: pt
license: cc-by-4.0
tags:
- model-calibration
- selective-prediction
- intent-classification
- reproducible-research
datasets:
- c2d-usp/banking77-pt-br
---

# BANKING77-PTBR · Confidence Evaluation

**Modelo novo**, treinado em {r['data']['fit']} textos (80% do treino oficial). Outros {r['data']['calibration']} textos do treino oficial foram reservados para calibração. O teste independente tem {r['data']['test']} textos.

- Acurácia no teste: **{r['test_accuracy']:.4f}**.
- Macro-F1 no teste: **{r['test_macro_f1']:.4f}**.
- Temperatura ajustada apenas na calibração: **{r['temperature']:.4f}**.

| Avaliação no teste oficial | T=1 (softmax cru) | Temperatura calibrada |
|:--|--:|--:|
| NLL | {raw['negative_log_likelihood']:.4f} | {scaled['negative_log_likelihood']:.4f} |
| ECE em 10 bins | {raw['expected_calibration_error_10']:.4f} | {scaled['expected_calibration_error_10']:.4f} |
| Brier multiclass (soma) | {raw['multiclass_brier_sum']:.4f} | {scaled['multiclass_brier_sum']:.4f} |

## Abstenção seletiva

O limiar é definido na **divisão de calibração**, nunca no teste. Um limite inferior Wilson de 90% para precisão foi usado como alvo de demonstração, não como garantia.

- Limiar: **{val(pol['threshold'])}**.
- Cobertura de calibração: **{pol['coverage']:.1%}**.
- Cobertura de teste: **{sel['coverage']:.1%}**.
- Acurácia apenas nas previsões aceitas no teste: **{val(sel['accuracy_on_accepted'])}**.

A escolha de temperatura e de limiar usa o mesmo split de calibração, então esse método **não estabelece desempenho confiável em produção**. Foram identificadas {r['data']['test_rows_matching_any_train_text']} linhas de teste com texto idêntico a alguma linha do treino oficial.

## Artefatos e transparência

- model.skops: estimador distinto do modelo original.
- calibration.json: temperatura, ordem das classes e limiar de pesquisa.
- metrics.json: relatórios completos, cobertura, NLL, ECE, Brier, risco.
- Código reproduzível: https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/tree/main/ml-lab/confidence-evaluation

Dataset: BANKING77-PTBR, traduções do inglês revisadas por pesquisadores, CC BY 4.0 (Dimant et al., Poli/USP, 2025). Não usar para decisões financeiras reais.
"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", type=Path)
    parser.add_argument("--test", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/confidence-evaluation"))
    args = parser.parse_args()
    model, report = evaluate(load_data("train", args.train), load_data("test", args.test))
    import skops.io as sio
    args.output_dir.mkdir(parents=True, exist_ok=True)
    sio.dump(model, args.output_dir/"model.skops")
    (args.output_dir/"calibration.json").write_text(json.dumps({
        "temperature": report["temperature"], "classes": [str(x) for x in model.named_steps["clf"].classes_],
        "abstention": report["threshold_selected_on_calibration"],
        "warning": "Calibrated probabilities and threshold are not validated for production",
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output_dir/"metrics.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output_dir/"README.md").write_text(model_card(report), encoding="utf-8")
    print(json.dumps({"accuracy": report["test_accuracy"], "macro_f1": report["test_macro_f1"],
        "temperature": report["temperature"], "uncalibrated": report["test_uncalibrated_softmax"],
        "calibrated": report["test_temperature_scaled"],
        "selection": report["test_selective_classification"]}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
