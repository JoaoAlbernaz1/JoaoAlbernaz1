"""Testes de validação de dados e treinamento, sem acesso à rede."""
from pathlib import Path
import sys

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from train import evaluate, load_data, make_pipeline  # noqa: E402


def test_dataset_is_balanced_and_has_no_duplicates():
    frame = load_data()
    assert frame["label"].nunique() == 5
    assert frame["label"].value_counts().min() >= 8
    assert frame["text"].is_unique


def test_training_returns_bounded_metrics():
    _, metrics = evaluate(load_data())
    assert 0 <= metrics["holdout"]["macro_f1"] <= 1
    assert 0 <= metrics["cross_validation"]["mean"] <= 1
    assert sum(sum(row) for row in metrics["holdout"]["confusion_matrix"]) == metrics["test_size"]


def test_reject_duplicate_texts(tmp_path: Path):
    bad = pd.concat([load_data(), load_data().iloc[[0]]], ignore_index=True)
    file = tmp_path / "bad.csv"
    bad.to_csv(file, index=False)
    with pytest.raises(ValueError, match="repetidos"):
        load_data(file)


def test_baseline_is_a_pipeline():
    assert list(make_pipeline().named_steps) == ["tfidf", "classifier"]
