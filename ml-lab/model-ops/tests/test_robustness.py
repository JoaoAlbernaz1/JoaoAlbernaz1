"""Metamorphic transformation and evaluation test suite (offline)."""
import importlib.util
import sys
from pathlib import Path

import numpy as np
import pytest

FILE = Path(__file__).resolve().parents[1] / "robustness.py"
spec = importlib.util.spec_from_file_location("modelops_robustness", FILE)
r = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = r
spec.loader.exec_module(r)


class FakeModel:
    def predict(self, texts):
        return np.array(["A" if "conta" in text.lower() else "B" for text in texts])


def test_accent_removal_preserves_ascii_and_removes_diacritics():
    assert r.transform("transferência não concluída", "accent_removed") == "transferencia nao concluida"


def test_uppercase_and_whitespace():
    result = r.transform("cartão   perdido", "upper_whitespace")
    assert result.strip() == "CARTÃO PERDIDO"
    assert result.startswith("   ")


def test_typo_is_deterministic_and_changes_sufficiently_long_word():
    text = "transferencia bancaria"
    first = r.transform(text, "adjacent_typo")
    assert first == r.transform(text, "adjacent_typo")
    assert first != text
    assert len(first) == len(text)
    assert r.transform("x a b", "adjacent_typo") == "x a b"


def test_unknown_transform_rejected():
    with pytest.raises(ValueError):
        r.transform("texto", "unknown")


def test_evaluation_returns_real_rates_and_no_text_leakage():
    texts = ["conta", "minha conta", "cartão", "transfêrencia"]
    labels = ["A", "A", "B", "B"]
    report = r.evaluate(FakeModel(), texts, labels)
    assert report["samples"] == 4
    assert set(report["perturbations"]) == set(r.VARIANTS)
    for variant in report["perturbations"].values():
        assert 0 <= variant["prediction_flip_rate"] <= 1
        assert 0 <= variant["text_change_rate"] <= 1
    assert "transfêrencia" not in r.render(report)
    assert r.evaluate(FakeModel(), texts, labels)["baseline"] == report["baseline"]


def test_mismatched_inputs_rejected():
    with pytest.raises(ValueError):
        r.evaluate(FakeModel(), ["a"], [])
