"""Treino Titanic com transformações dentro do CV para evitar leakage."""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

NUMERIC = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
CATEGORICAL = ["Sex", "Embarked"]
FEATURES = NUMERIC + CATEGORICAL
SEED = 42


def make_pipeline() -> Pipeline:
    preparation = ColumnTransformer(
        [
            ("num", SimpleImputer(strategy="median"), NUMERIC),
            ("cat", Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ]), CATEGORICAL),
        ]
    )
    return Pipeline([
        ("preprocess", preparation),
        ("model", RandomForestClassifier(
            n_estimators=300, min_samples_leaf=2, max_features="sqrt",
            random_state=SEED, n_jobs=-1,
        )),
    ])


def train_and_submit(train_path: Path, test_path: Path, output_path: Path) -> dict:
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    required_train = set(FEATURES + ["Survived"])
    required_test = set(FEATURES + ["PassengerId"])
    if not required_train.issubset(train) or not required_test.issubset(test):
        raise ValueError("Colunas obrigatórias não encontradas no CSV do Titanic")
    model = make_pipeline()
    folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    scores = cross_val_score(model, train[FEATURES], train["Survived"], cv=folds, scoring="accuracy")
    model.fit(train[FEATURES], train["Survived"])
    pred = model.predict(test[FEATURES]).astype(int)
    submission = pd.DataFrame({"PassengerId": test["PassengerId"].astype(int), "Survived": pred})
    output_path.parent.mkdir(parents=True, exist_ok=True)
    submission.to_csv(output_path, index=False)
    return {"cv_accuracy_mean": float(scores.mean()), "cv_accuracy_std": float(scores.std()), "rows": len(submission)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", required=True, type=Path)
    parser.add_argument("--test", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=Path("outputs/titanic/submission.csv"))
    args = parser.parse_args()
    print(train_and_submit(args.train, args.test, args.output))


if __name__ == "__main__":
    main()
