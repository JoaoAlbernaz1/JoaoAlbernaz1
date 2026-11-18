"""Pure monitoring tests: no model download, external API or network required."""
import importlib.util
import math
import sys
from pathlib import Path

import numpy as np
import pytest

FILE = Path(__file__).resolve().parents[1] / "monitor.py"
spec = importlib.util.spec_from_file_location("modelops_monitor", FILE)
monitor = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = monitor
spec.loader.exec_module(monitor)


def test_divergence_is_zero_for_identical_distributions():
    assert monitor.jensen_shannon_bits([10, 20, 30], [100, 200, 300]) == pytest.approx(0)
    assert monitor.population_stability_index([10, 20, 30], [100, 200, 300]) == pytest.approx(0)


def test_js_disjoint_distribution_is_one_bit():
    assert monitor.jensen_shannon_bits([10, 0], [0, 10]) == pytest.approx(1.0)


def test_psi_detects_shift_without_nan():
    assert monitor.population_stability_index([100, 0, 20], [0, 120, 0]) > 0.2
    assert math.isfinite(monitor.population_stability_index([100, 0, 20], [0, 120, 0]))


def test_fixed_length_buckets_cover_empty_and_long_strings():
    values = monitor.histogram([0, 19, 20, 300, 500])
    assert values[0] == 2
    assert values[1] == 1
    assert values[-1] == 2
    assert sum(values) == 5


def test_label_distribution_validates_unknown_values():
    assert monitor.category_counts(["a", "a", "b"], ["a", "b", "c"]) == [2, 1, 0]
    with pytest.raises(ValueError):
        monitor.category_counts(["a", "unknown"], ["a", "b"])
    with pytest.raises(ValueError):
        monitor.jensen_shannon_bits([0, 0], [0, 1])


def test_full_report_aggregates_without_exposing_personal_text():
    ref = ["pedido cancelado", "enviar cartão", "taxa de cambio", "saque bancario"]
    cur = ["pedido de cartão", "taxa cobrada"]
    result = monitor.evaluate(ref, cur, ["a", "b", "b", "a"], ["b", "a"], ["a", "b"])
    assert result["context"]["reference_rows"] == 4
    assert result["context"]["comparison_rows"] == 2
    assert "length_psi" in result["metrics"]
    assert 0 <= result["metrics"]["predicted_label_js_divergence_bits"] <= 1
    as_text = monitor.render_report(result)
    assert "Jensen-Shannon" in as_text
    assert "enviar cartão" not in as_text
    assert sum(result["length_histograms"]["reference"]) == 4


def test_prediction_count_mismatch_is_rejected():
    with pytest.raises(ValueError):
        monitor.evaluate(["a"], ["b"], [], ["x"], ["x"])


def test_unseen_category_and_bad_smoothing():
    with pytest.raises(ValueError):
        monitor.population_stability_index([1, 2], [2, 1], smoothing=0)
    with pytest.raises(ValueError):
        monitor.category_counts(["z"], ["a", "b"])
