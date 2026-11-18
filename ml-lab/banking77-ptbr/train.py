"""Three classical intent models on the official BANKING77-PTBR research splits."""
import argparse
import json
from collections import Counter
from pathlib import Path

import pandas as pd
from huggingface_hub import hf_hub_download
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import f1_score, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

DATASET = "c2d-usp/banking77-pt-br"
REVISION = "85f51c4"
SEED = 42


def load_csv(path):
    df = pd.read_csv(path)
    if not {"frase", "rotulo"} <= set(df):
        raise ValueError("Missing frase/rotulo columns")
    df = df[["frase", "rotulo"]].copy()
    if df.isna().any().any():
        raise ValueError("Missing content")
    df["frase"] = df["frase"].astype(str).str.strip()
    df["rotulo"] = df["rotulo"].astype(str).str.strip()
    if (df["frase"] == "").any() or (df["rotulo"] == "").any():
        raise ValueError("Blank content")
    return df


def official_file(name):
    if name not in ("train", "test"):
        raise ValueError("Only official splits")
    return hf_hub_download(repo_id=DATASET, repo_type="dataset", revision=REVISION, filename=name + ".csv")


def make_models():
    def tfidf(mode):
        return TfidfVectorizer(
            lowercase=True, strip_accents="unicode", sublinear_tf=True,
            min_df=2, max_features=120000,
            analyzer="char_wb" if mode == "char" else "word",
            ngram_range=(3, 5) if mode == "char" else (1, 2),
        )
    return {
        "word_sgd": Pipeline([("tfidf", tfidf("word")), ("clf", SGDClassifier(loss="log_loss", alpha=1e-5, random_state=SEED))]),
        "word_svc": Pipeline([("tfidf", tfidf("word")), ("clf", LinearSVC(C=1.0, random_state=SEED))]),
        "char_svc": Pipeline([("tfidf", tfidf("char")), ("clf", LinearSVC(C=1.0, random_state=SEED))]),
    }


def experiment(train, test):
    if train["rotulo"].nunique() < 2 or train["rotulo"].value_counts().min() < 3:
        raise ValueError("Too few examples per label")
    if set(test["rotulo"]) - set(train["rotulo"]):
        raise ValueError("Unknown labels in test")
    x_train, x_val, y_train, y_val = train_test_split(
        train["frase"], train["rotulo"], test_size=0.2,
        stratify=train["rotulo"], random_state=SEED,
    )
    comparisons = []
    for name, model in make_models().items():
        model.fit(x_train, y_train)
        pred = model.predict(x_val)
        comparisons.append({
            "model": name, "macro_f1": float(f1_score(y_val, pred, average="macro", zero_division=0)),
            "accuracy": float(accuracy_score(y_val, pred)),
        })
    comparisons.sort(key=lambda r: (-r["macro_f1"], -r["accuracy"], r["model"]))
    winner = comparisons[0]["model"]
    final = make_models()[winner]
    final.fit(train["frase"], train["rotulo"])
    predicted = final.predict(test["frase"])
    errors = Counter((a, b) for a, b in zip(test["rotulo"], predicted) if a != b)
    metrics = {
        "source": DATASET, "revision": REVISION, "license": "CC BY 4.0",
        "nature": "researcher-reviewed translations of banking messages, NOT native Portuguese production logs",
        "n_train": len(train), "n_test": len(test), "classes": train["rotulo"].nunique(),
        "overlap_train_test_text": len(set(train["frase"].str.casefold()) & set(test["frase"].str.casefold())),
        "protocol": "compare models on stratified 20 percent of OFFICIAL train; refit winner on full train; evaluate official test once",
        "seed": SEED, "validation": comparisons, "selected": winner,
        "test": {
            "accuracy": float(accuracy_score(test["rotulo"], predicted)),
            "macro_f1": float(f1_score(test["rotulo"], predicted, average="macro", zero_division=0)),
            "weighted_f1": float(f1_score(test["rotulo"], predicted, average="weighted", zero_division=0)),
            "classification_report": classification_report(test["rotulo"], predicted, output_dict=True, zero_division=0),
            "top_confusions": [{"expected": a, "predicted": b, "count": n} for (a, b), n in errors.most_common(10)],
        },
        "limitations": [
            "Translated/reviewed text differs from originally authored Brazilian Portuguese.",
            "Benchmark restricted to banking domain; no evaluation on production messages.",
            "Three preselected baselines, one validation split, no repeated test-set tuning.",
        ],
    }
    return final, metrics


def model_card(m):
    table = "\n".join(
        "| %s | %.4f | %.4f |" % (r["model"], r["macro_f1"], r["accuracy"])
        for r in m["validation"]
    )
    return """---
language: pt
license: cc-by-4.0
tags:
- intent-classification
- scikit-learn
- portuguese
datasets:
- c2d-usp/banking77-pt-br
---

# Classificador BANKING77-PTBR · 77 intenções

Treinado no BANKING77-PTBR, corpus de pesquisa **traduzido e revisado** do inglês para português. Não são mensagens reais de clientes brasileiros.

## Teste oficial independente

- **Macro-F1:** %.4f
- **Accuracy:** %.4f
- **Weighted-F1:** %.4f
- **Modelo selecionado:** %s
- **Treino / teste oficiais:** %d / %d exemplos
- **Classes:** %d
- **Interseção textual entre treino e teste:** %d

## Validação (somente dentro do treino oficial)

| Baseline | Macro-F1 | Accuracy |
|:--|--:|--:|
%s

O modelo foi selecionado exclusivamente pelo macro-F1 de validação (split 80/20 estratificado, seed 42), reajustado no treino integral e avaliado no teste oficial uma única vez.

## Reprodução

Código e testes: https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/tree/main/ml-lab/banking77-ptbr

Artefatos: model.skops, metrics.json e este cartão. A modelagem e as métricas não garantem generalização a outros setores, linguagem de produção ou adversários.

## Dataset e créditos

BANKING77-PTBR: https://huggingface.co/datasets/c2d-usp/banking77-pt-br (CC BY 4.0). Dimant et al. (2025), Centro de Ciência de Dados Poli/USP. Corpus original: Casanueva et al. (2020), Efficient Intent Detection with Dual Sentence Encoders.
""" % (
        m["test"]["macro_f1"], m["test"]["accuracy"], m["test"]["weighted_f1"],
        m["selected"], m["n_train"], m["n_test"], m["classes"], m["overlap_train_test_text"], table
    )


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--train-csv", type=Path)
    p.add_argument("--test-csv", type=Path)
    p.add_argument("--output-dir", type=Path, default=Path("outputs/banking77-ptbr"))
    args = p.parse_args()
    train = load_csv(args.train_csv or official_file("train"))
    test = load_csv(args.test_csv or official_file("test"))
    model, metrics = experiment(train, test)
    import skops.io as sio
    args.output_dir.mkdir(parents=True, exist_ok=True)
    sio.dump(model, args.output_dir / "model.skops")
    (args.output_dir / "metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output_dir / "README.md").write_text(model_card(metrics), encoding="utf-8")
    print(json.dumps({"selected": metrics["selected"], "validation": metrics["validation"],
                      "test": {k: metrics["test"][k] for k in ("macro_f1", "accuracy", "weighted_f1")}},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
