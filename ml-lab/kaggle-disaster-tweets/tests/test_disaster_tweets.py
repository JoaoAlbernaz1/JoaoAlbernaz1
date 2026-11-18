"""Smoke and regression tests for the Kaggle NLP experiment (no Kaggle access needed)."""
import importlib.util
import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("disaster_tweets_baseline", ROOT / "train.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def train_fixture(n=18):
    words = (
        ["fire erupted near bridge evac emergency " + str(i) for i in range(n)] +
        ["weekend movie night home relaxing " + str(i) for i in range(n)]
    )
    return pd.DataFrame({
        "id": list(range(len(words))),
        "text": words,
        "target": [1] * n + [0] * n,
    })


def test_train_and_generate_correct_schema():
    train = train_fixture()
    test = pd.DataFrame({"id": [50, 51], "text": ["fire emergency", "nice weekend"]})
    output, report = module.experiment(train, test, folds=3)
    assert output.columns.tolist() == ["id", "target"]
    assert len(output) == len(test)
    assert set(output.target.unique()) <= {0, 1}
    assert len(report["candidates"]) == 2
    assert report["selected"] == report["candidates"][0]["model"]
    assert "CV F1" in report["limitations"][0]
    assert "not a" in module.render_report(report).lower() or "não são" in module.render_report(report).lower()


def test_invalid_target_raises(tmp_path):
    train = train_fixture()
    test = pd.DataFrame({"id": [90], "text": ["a safe sentence"]})
    train["target"] = 2
    train.to_csv(tmp_path / "train.csv", index=False)
    test.to_csv(tmp_path / "test.csv", index=False)
    with pytest.raises(ValueError):
        module.load_datasets(tmp_path / "train.csv", tmp_path / "test.csv")


def test_duplicate_test_ids_raise(tmp_path):
    train = train_fixture()
    test = pd.DataFrame({"id": [90, 90], "text": ["a safe sentence", "another"]})
    train.to_csv(tmp_path / "train.csv", index=False)
    test.to_csv(tmp_path / "test.csv", index=False)
    with pytest.raises(ValueError):
        module.load_datasets(tmp_path / "train.csv", tmp_path / "test.csv")
