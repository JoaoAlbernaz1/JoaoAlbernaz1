"""Testes determinísticos para métricas de retrieval."""
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from benchmark import bm25_scores, retrieval_metrics, run  # noqa: E402


def test_recall_and_reciprocal_rank():
    scores = retrieval_metrics(["b", "a", "c"], {"a", "c"}, 3)
    assert scores["recall@3"] == 1.0
    assert scores["mrr@3"] == 0.5


def test_missing_relevance_is_invalid():
    with pytest.raises(ValueError):
        retrieval_metrics(["a"], set(), 1)


def test_bm25_favors_matching_document():
    result = bm25_scores(["a senha expirou", "o pacote chegou"], "senha")
    assert result[0] > result[1]


def test_offline_benchmark_has_two_baselines():
    scores = run()
    assert set(scores["methods"]) == {"bm25", "tfidf"}
    assert scores["queries"] == 12
    for method in scores["methods"].values():
        assert 0 <= method["mean_metrics"]["recall@3"] <= 1
