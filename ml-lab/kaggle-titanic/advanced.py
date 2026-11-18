"""Titanic advanced baseline: row-level feature engineering and leakage-safe CV."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold, cross_val_predict, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

SEED = 42
RAW = ["PassengerId", "Name", "Cabin", "Pclass", "Age", "SibSp", "Parch", "Fare", "Sex", "Embarked"]
NUM = ["Pclass", "Age", "SibSp", "Parch", "Fare", "FamilySize", "IsAlone", "FarePerPerson"]
CAT = ["Sex", "Embarked", "Title", "Deck"]
TITLES = {"Mr", "Mrs", "Miss", "Master", "Dr", "Rev"}


class FeatureBuilder(BaseEstimator, TransformerMixin):
    """Stateless per-passenger features; no target or other records needed."""
    def fit(self, X, y=None):
        self._validate(X)
        return self

    @staticmethod
    def _validate(X):
        missing = set(RAW) - set(X.columns)
        if missing:
            raise ValueError("Missing columns: " + ", ".join(sorted(missing)))

    def transform(self, X):
        self._validate(X)
        df = X.copy()
        title = df.Name.fillna("").astype(str).str.extract(r",\s*([^.]+)\.", expand=False).fillna("Other").str.strip()
        df["Title"] = title.where(title.isin(TITLES), "Other")
        deck = df.Cabin.fillna("").astype(str).str[:1].str.upper()
        df["Deck"] = deck.where(deck.str.fullmatch(r"[A-GT]"), "Unknown")
        family = 1 + pd.to_numeric(df.SibSp, errors="coerce").fillna(0).clip(lower=0) + pd.to_numeric(df.Parch, errors="coerce").fillna(0).clip(lower=0)
        df["FamilySize"] = family
        df["IsAlone"] = (family == 1).astype(int)
        df["FarePerPerson"] = pd.to_numeric(df.Fare, errors="coerce") / family
        return df[NUM + CAT]


def pipeline(name):
    if name not in ("logistic", "random_forest"):
        raise ValueError("Unknown model")
    numerical = Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())])
    categorical = Pipeline([("impute", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))])
    prep = ColumnTransformer([("num", numerical, NUM), ("cat", categorical, CAT)])
    model = (LogisticRegression(max_iter=1000, random_state=SEED) if name == "logistic" else
             RandomForestClassifier(n_estimators=220, min_samples_leaf=2, random_state=SEED, n_jobs=1))
    return Pipeline([("features", FeatureBuilder()), ("prep", prep), ("model", model)])


def read_data(train_file, test_file):
    train, test = pd.read_csv(train_file), pd.read_csv(test_file)
    for name, data in [("train", train), ("test", test)]:
        missing = set(RAW) - set(data.columns)
        if missing:
            raise ValueError(name + " missing fields: " + str(sorted(missing)))
        if data.PassengerId.isna().any() or data.PassengerId.duplicated().any():
            raise ValueError("Duplicate or missing passenger IDs in " + name)
    if "Survived" not in train or train.Survived.isna().any() or set(train.Survived) != {0, 1}:
        raise ValueError("Train labels must contain 0 and 1")
    if "Survived" in test and test.Survived.notna().any():
        raise ValueError("Official competition test must be unlabeled")
    if set(train.PassengerId) & set(test.PassengerId):
        raise ValueError("Overlapping PassengerId between train and test")
    return train, test


def run(train, test, folds=5):
    y = train.Survived.astype(int)
    if y.value_counts().min() < folds:
        raise ValueError("Not enough samples for stratified CV")
    cv = StratifiedKFold(folds, shuffle=True, random_state=SEED)
    scores = []
    for name in ("logistic", "random_forest"):
        metric = cross_validate(pipeline(name), train[RAW], y, cv=cv,
                                scoring={"accuracy":"accuracy", "auc":"roc_auc"},
                                n_jobs=1, error_score="raise")
        scores.append({
            "model": name,
            "accuracy_mean": float(metric["test_accuracy"].mean()),
            "accuracy_std": float(metric["test_accuracy"].std()),
            "auc_mean": float(metric["test_auc"].mean()),
            "auc_std": float(metric["test_auc"].std()),
        })
    scores.sort(key=lambda m: (-m["accuracy_mean"], -m["auc_mean"], m["model"]))
    name = scores[0]["model"]
    # Same folds used for choice: OOF result is descriptive, not independent validation.
    oof = cross_val_predict(pipeline(name), train[RAW], y, cv=cv, n_jobs=1)
    model = pipeline(name).fit(train[RAW], y)
    pred = model.predict(test[RAW]).astype(int)
    submission = pd.DataFrame({"PassengerId": test.PassengerId.astype(int), "Survived": pred})
    report = {
        "experiment": "titanic_engineered_cv_v1",
        "dataset": "Kaggle Titanic official competition data",
        "seed": SEED, "folds": folds, "train_rows": len(train), "test_rows": len(test),
        "selected": name, "candidates": scores,
        "oof_confusion_matrix": confusion_matrix(y, oof, labels=[0, 1]).tolist(),
        "features": ["Title", "Deck", "FamilySize", "IsAlone", "FarePerPerson"],
        "limitations": [
            "CV accuracy and ROC-AUC are NOT Kaggle leaderboard scores.",
            "Model selection and OOF diagnostics reuse the same CV folds.",
            "No hidden test labels or repeated leaderboard tuning were used.",
            "Family relationships may create dependence across folds.",
        ],
    }
    return submission, report


def render(report):
    lines = ["# Titanic · Feature Engineering", "",
             "Experimento reproduzível com dados oficiais da competição. Métricas **locais de validação**, não leaderboard.",
             "", "| Modelo | CV Accuracy | CV ROC-AUC |", "|:--|--:|--:|"]
    for r in report["candidates"]:
        lines.append(f"| {r['model']} | {r['accuracy_mean']:.4f} ± {r['accuracy_std']:.4f} | {r['auc_mean']:.4f} ± {r['auc_std']:.4f} |")
    lines.extend(["", f"**Modelo selecionado:** {report['selected']}.", "",
                  "A matriz de confusão OOF está no JSON, mas reusa os folds da seleção.",
                  "A imputação, a normalização e o encoding são ajustados dentro de cada fold.",
                  "Nenhuma submissão adicional é feita automaticamente.",
                  "",
                  "[Código e metodologia](../../kaggle-titanic/) · [Métricas completas](./metrics.json)."])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", required=True, type=Path)
    parser.add_argument("--test", required=True, type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/titanic-advanced"))
    args = parser.parse_args()
    train, test = read_data(args.train, args.test)
    submission, report = run(train, test)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    submission.to_csv(args.output_dir / "submission_advanced.csv", index=False)
    (args.output_dir / "metrics.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output_dir / "README.md").write_text(render(report), encoding="utf-8")
    print(json.dumps({"selected": report["selected"], "candidates": report["candidates"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
