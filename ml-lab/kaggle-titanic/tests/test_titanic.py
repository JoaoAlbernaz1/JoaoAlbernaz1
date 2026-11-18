"""Teste de smoke do pipeline sem distribuir dados proprietários do Kaggle."""
from pathlib import Path
import importlib.util

import pandas as pd

spec = importlib.util.spec_from_file_location("titanic_train", Path(__file__).resolve().parents[1] / "train.py")
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)
CATEGORICAL, FEATURES, NUMERIC = module.CATEGORICAL, module.FEATURES, module.NUMERIC
make_pipeline, train_and_submit = module.make_pipeline, module.train_and_submit


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
