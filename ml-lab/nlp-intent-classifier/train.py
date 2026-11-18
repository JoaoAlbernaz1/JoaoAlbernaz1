"""Treino reproduzível de baseline de classificação de tickets sintéticos."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline

DATA_PATH = Path(__file__).parent / "data" / "tickets.csv"
SEED = 42


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    frame = pd.read_csv(path)
    if not {"text", "label"}.issubset(frame.columns):
        raise ValueError("CSV deve conter as colunas text e label")
    if frame[["text", "label"]].isna().any().any():
        raise ValueError("Dados com valores ausentes")
    frame = frame.copy()
    frame["text"] = frame["text"].astype(str).str.strip()
    if (frame["text"] == "").any() or frame["text"].duplicated().any():
        raise ValueError("Textos vazios ou repetidos")
    if frame["label"].nunique() < 2 or frame["label"].value_counts().min() < 8:
        raise ValueError("Minimo de 2 classes e 8 exemplos por classe")
    return frame


def make_pipeline() -> Pipeline:
    return Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), lowercase=True, strip_accents="unicode")),
            ("classifier", LogisticRegression(max_iter=1500, class_weight="balanced", random_state=SEED)),
        ]
    )


def evaluate(frame: pd.DataFrame) -> tuple[Pipeline, dict]:
    x_train, x_test, y_train, y_test = train_test_split(
        frame["text"], frame["label"], test_size=0.25, stratify=frame["label"], random_state=SEED
    )
    estimator = make_pipeline()
    folds = StratifiedKFold(n_splits=3, shuffle=True, random_state=SEED)
    cv_scores = cross_val_score(estimator, x_train, y_train, scoring="f1_macro", cv=folds)
    estimator.fit(x_train, y_train)
    predictions = estimator.predict(x_test)
    labels = sorted(frame["label"].unique().tolist())
    metrics = {
        "dataset": "synthetic_support_tickets_pt_v1",
        "dataset_size": len(frame),
        "train_size": len(x_train),
        "test_size": len(x_test),
        "random_seed": SEED,
        "cross_validation": {"folds": 3, "metric": "f1_macro", "mean": float(cv_scores.mean()), "std": float(cv_scores.std())},
        "holdout": {
            "accuracy": float(accuracy_score(y_test, predictions)),
            "macro_f1": float(f1_score(y_test, predictions, average="macro", zero_division=0)),
            "labels": labels,
            "confusion_matrix": confusion_matrix(y_test, predictions, labels=labels).tolist(),
            "classification_report": classification_report(y_test, predictions, output_dict=True, zero_division=0),
        },
        "limitations": "Synthetic, small, author-created dataset; metrics are not evidence of real-world performance.",
    }
    return estimator, metrics


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=DATA_PATH)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/intent"))
    args = parser.parse_args()
    model, metrics = evaluate(load_data(args.data))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    import skops.io as sio

    sio.dump(model, args.output_dir / "model.skops")
    (args.output_dir / "metrics.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({k: metrics[k] for k in ("dataset_size", "cross_validation", "holdout")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
