"""Teste de smoke do pipeline sem distribuir dados proprietários do Kaggle."""
from pathlib import Path
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from train import CATEGORICAL, FEATURES, NUMERIC, make_pipeline, train_and_submit  # noqa: E402


def test_feature_columns_consistent():
    assert len(FEATURES) == 7
    assert not set(NUMERIC) & set(CATEGORICAL)


def test_train_and_submit_with_tiny_fixture(tmp_path: Path):
    rows = [
        {"PassengerId": i + 1, "Pclass": 1 + i % 3, "Age": 20 + i, "SibSp": i % 2,
         "Parch": 0, "Fare": 10 + i * 2, "Sex": ["male", "female"][i % 2],
         "Embarked": ["S", "C", "Q"][i % 3], "Survived": i % 2}
        for i in range(20)
    ]
    train = tmp_path / "train.csv"
    test = tmp_path / "test.csv"
    pd.DataFrame(rows).to_csv(train, index=False)
    pd.DataFrame(rows[:3]).drop(columns=["Survived"]).to_csv(test, index=False)
    output = tmp_path / "submission.csv"
    metrics = train_and_submit(train, test, output)
    result = pd.read_csv(output)
    assert metrics["rows"] == 3
    assert result.columns.tolist() == ["PassengerId", "Survived"]
    assert set(result["Survived"]).issubset({0, 1})


def test_pipeline_uses_train_only_imputation():
    assert "preprocess" in make_pipeline().named_steps
