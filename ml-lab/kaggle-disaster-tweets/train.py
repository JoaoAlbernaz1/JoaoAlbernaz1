"""Kaggle Disaster Tweets: genuine NLP baseline, stratified CV and one held-out submission.

Competition: https://www.kaggle.com/competitions/nlp-getting-started
Metric: F1 for target=1. Uses the official train/test CSV, no fabricated scores.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, make_scorer
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

SEED = 42


def load_datasets(train_path: Path, test_path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    if not {"id", "text", "target"}.issubset(train.columns):
        raise ValueError("Official train.csv requires id, text and target")
    if not {"id", "text"}.issubset(test.columns):
        raise ValueError("Official test.csv requires id and text")
    if train["text"].isna().any() or test["text"].isna().any():
        raise ValueError("Missing text")
    if train["target"].isna().any() or set(train["target"].unique()) != {0, 1}:
        raise ValueError("Targets must be binary labels 0 and 1")
    if test["id"].duplicated().any() or train["id"].duplicated().any():
        raise ValueError("Duplicate row identifiers")
    return train, test


def make_models() -> dict[str, Pipeline]:
    def tfidf():
        return TfidfVectorizer(
            strip_accents="unicode", lowercase=True, sublinear_tf=True,
            ngram_range=(1, 2), min_df=2, max_features=60000,
            token_pattern=r"(?u)\b\w+\b",
        )

    return {
        "tfidf_logreg": Pipeline([
            ("vectorizer", tfidf()),
            ("classifier", LogisticRegression(
                C=2.0, class_weight="balanced", max_iter=1500, random_state=SEED
            )),
        ]),
        "tfidf_linearsvc": Pipeline([
            ("vectorizer", tfidf()),
            ("classifier", LinearSVC(C=1.0, class_weight="balanced", random_state=SEED)),
        ]),
    }


def experiment(train: pd.DataFrame, test: pd.DataFrame, *, folds: int = 5) -> tuple[pd.DataFrame, dict]:
    if train["target"].value_counts().min() < folds:
        raise ValueError("Not enough records for stratified CV")
    kfold = StratifiedKFold(n_splits=folds, shuffle=True, random_state=SEED)
    models = make_models()
    results = []
    for name, model in models.items():
        scores = cross_validate(
            model, train["text"], train["target"], cv=kfold,
            scoring={"f1": make_scorer(f1_score, pos_label=1), "accuracy": "accuracy"},
            n_jobs=1,
        )
        results.append({
            "model": name,
            "f1_mean": float(scores["test_f1"].mean()),
            "f1_std": float(scores["test_f1"].std()),
            "accuracy_mean": float(scores["test_accuracy"].mean()),
        })
    results.sort(key=lambda x: (-x["f1_mean"], -x["accuracy_mean"], x["model"]))
    best = results[0]["model"]
    final = make_models()[best]
    final.fit(train["text"], train["target"])
    pred = final.predict(test["text"]).astype(int)
    submission = pd.DataFrame({"id": test["id"].astype(int), "target": pred})
    if submission["id"].duplicated().any() or len(submission) != len(test):
        raise AssertionError("Invalid prediction rows")
    metrics = {
        "competition": "nlp-getting-started",
        "methodology": "Stratified CV on competition training data; single final fit on all training data.",
        "metric": "positive-class F1",
        "seed": SEED,
        "folds": folds,
        "train_rows": len(train),
        "test_rows": len(test),
        "train_test_exact_duplicate_texts": len(
            set(train["text"].str.casefold()) & set(test["text"].str.casefold())
        ),
        "candidates": results,
        "selected": best,
        "limitations": [
            "CV F1 is not the public or private Kaggle leaderboard score.",
            "No Kaggle test labels were used to pick model or threshold.",
            "Competition contains social-media-language shortcuts and domain shift.",
            "This is a reproducible classical NLP baseline, not a competition-winning system.",
        ],
    }
    return submission, metrics


def render_report(metrics: dict) -> str:
    rows = "\n".join(
        f"| {r['model']} | {r['f1_mean']:.4f} ± {r['f1_std']:.4f} | {r['accuracy_mean']:.4f} |"
        for r in metrics["candidates"]
    )
    return f"""# Kaggle Disaster Tweets · experimento NLP

**Competição:** [Natural Language Processing with Disaster Tweets](https://www.kaggle.com/competitions/nlp-getting-started).

Pipeline TF-IDF com seleção entre regressão logística e LinearSVC por **F1 da classe positiva em validação cruzada estratificada**. A submissão não foi otimizada com os rótulos ocultos de teste.

| Candidato | F1 local ({metrics['folds']} folds) | Accuracy local |
|:--|--:|--:|
{rows}

**Modelo selecionado:** {metrics['selected']}  
**Treino:** {metrics['train_rows']} mensagens · **Teste sem rótulos:** {metrics['test_rows']} mensagens.  
**Textos exatamente coincidentes entre treino/teste:** {metrics['train_test_exact_duplicate_texts']} (casefold).

**Atenção:** essas são métricas de validação local. **Não são pontuações de Kaggle**, e nenhuma medalha ou vitória é alegada.

- [Código e metodologia](../../kaggle-disaster-tweets/).
- [Métricas completas desta execução](./metrics.json).
- [Histórico de submissões oficiais](https://www.kaggle.com/competitions/nlp-getting-started/submissions).
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", required=True, type=Path)
    parser.add_argument("--test", required=True, type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/disaster-tweets"))
    parser.add_argument("--folds", type=int, default=5)
    args = parser.parse_args()
    train, test = load_datasets(args.train, args.test)
    submission, metrics = experiment(train, test, folds=args.folds)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    submission.to_csv(args.output_dir / "submission.csv", index=False)
    (args.output_dir / "metrics.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (args.output_dir / "README.md").write_text(render_report(metrics), encoding="utf-8")
    print(json.dumps({
        "selected": metrics["selected"], "candidates": metrics["candidates"],
        "test_rows": metrics["test_rows"], "validation_metric": metrics["metric"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
