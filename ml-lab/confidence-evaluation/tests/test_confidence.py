"""Fast, network-free tests for calibration, selection and leakage boundaries."""
import importlib.util
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

FILE = Path(__file__).resolve().parents[1] / "confidence.py"
spec = importlib.util.spec_from_file_location("confidence_evaluation_code", FILE)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def test_softmax_normalizes_and_preserves_class_rank():
    logits = np.array([[1.0, 2.0, -1.0], [3.0, 1.0, 0.0]])
    for temperature in (0.5, 1.0, 3.0):
        p = m.softmax_temperature(logits, temperature)
        assert np.allclose(p.sum(axis=1), 1)
        assert np.all(p.argmax(axis=1) == logits.argmax(axis=1))
    with pytest.raises(ValueError):
        m.softmax_temperature(logits, -1.0)


def test_temperature_minimizes_calibration_nll():
    logits = np.array([[4.0, 0.0, -1.0], [-1.0, 4.0, 0.0], [0.0, -1.0, 4.0]] * 4)
    y = np.array([0, 1, 2] * 4)
    fitted = m.fit_temperature(logits, y)
    assert 0.05 <= fitted <= 30.0
    assert m.nll(m.softmax_temperature(logits, fitted), y) <= m.nll(m.softmax_temperature(logits, 1.0), y) + 1e-5


def test_perfect_probabilities_have_zero_error():
    p = np.eye(3)
    y = np.array([0, 1, 2])
    assert m.ece(p, y) == pytest.approx(0)
    assert m.brier(p, y) == pytest.approx(0)
    assert m.nll(p, y) == pytest.approx(0)
    assert 0 <= m.ece(np.ones((3, 3))/3, np.array([0, 0, 0])) <= 1


def test_threshold_policy_uses_only_supplied_calibration():
    # Top 150 are correct and confidently classified; bottom 50 incorrect.
    p = np.array([[.99, .005, .005]] * 150 + [[.05, .05, .90]] * 50)
    labels = np.array([0]*150 + [1]*50)
    policy = m.choose_threshold(p, labels, target=.9, min_count=50)
    assert policy["threshold"] is not None
    assert policy["accepted"] == 150
    assert policy["wilson_lower"] >= .9
    selected = m.selective(p, labels, policy)
    assert selected["accepted"] == 150
    assert selected["accuracy_on_accepted"] == 1.0


def test_abstention_fallback():
    p = np.ones((20, 3))/3
    y = np.array([0,1,2,0,1]*4)
    policy = m.choose_threshold(p, y, min_count=50)
    assert policy["threshold"] is None
    assert m.selective(p, y, policy)["coverage"] == 0


def test_data_validation_and_leakage_protocol(tmp_path):
    df = pd.DataFrame({
        "frase": ([f"cartao perdido no banco {i}" for i in range(18)] +
                  [f"taxa cambio internacional {i}" for i in range(18)] +
                  [f"transferencia pendente hoje {i}" for i in range(18)]),
        "rotulo": ["card"]*18 + ["fx"]*18 + ["transfer"]*18
    })
    input_file = tmp_path / "train.csv"
    df.to_csv(input_file, index=False)
    assert len(m.load_data("train", input_file)) == 54
    test = df.iloc[[0, 1, 20, 21, 40, 41]].copy()
    test["frase"] = test["frase"] + " OUTRA CONSULTA"
    model, report = m.evaluate(df, test, min_accepted=3)
    assert model.named_steps["clf"].classes_.shape[0] == 3
    assert report["data"]["fit"] + report["data"]["calibration"] == len(df)
    assert report["data"]["test"] == len(test)
    assert report["data"]["test_rows_matching_any_train_text"] == 0
    assert 0 <= report["test_temperature_scaled"]["expected_calibration_error_10"] <= 1
    assert "model.skops" in m.model_card(report)
    with pytest.raises(ValueError):
        m.load_data("other", input_file)


def test_reject_unknown_labels():
    train = pd.DataFrame({"frase": ["um","dois","tres"]*3,
                          "rotulo": ["A"]*3+["B"]*3+["C"]*3})
    test = pd.DataFrame({"frase": ["quatro"], "rotulo": ["X"]})
    with pytest.raises(ValueError):
        m.evaluate(train, test)
