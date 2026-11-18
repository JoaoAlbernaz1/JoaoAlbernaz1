"""Offline FastAPI behavior tests with a deterministic substitute for the remote model."""
import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

pytest.importorskip("fastapi")
pytest.importorskip("httpx")
from fastapi.testclient import TestClient

MODULE = Path(__file__).resolve().parents[1] / "serving.py"
spec = importlib.util.spec_from_file_location("modelops_serving", MODULE)
api = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = api
spec.loader.exec_module(api)


class FakeModel:
    def __init__(self, *, invalid=False):
        self.named_steps = {"clf": SimpleNamespace(classes_=np.array([f"class_{i}" for i in range(77)]))}
        self.invalid = invalid

    def decision_function(self, texts):
        assert len(texts) == 1
        scores = np.linspace(-3, 1, 77).reshape(1, -1)
        if self.invalid:
            scores[0, 0] = np.nan
        return scores


@pytest.fixture()
def client():
    api.app.dependency_overrides[api.require_model] = lambda: FakeModel()
    with TestClient(api.app) as c:
        yield c
    api.app.dependency_overrides.clear()


def test_service_has_no_remote_loading_on_import(client):
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json()["status"] == "alive"
    assert client.get("/health/ready").json()["status"] == "ready"
    assert client.get("/model-info").json()["n_classes"] == 77


def test_prediction_returns_ranked_margins_but_never_probabilities(client):
    response = client.post("/predict", json={"text": "  transferência atrasada  "})
    assert response.status_code == 200
    body = response.json()
    assert body["intent"] == "class_76"
    assert [x["intent"] for x in body["candidates"]] == ["class_76", "class_75", "class_74"]
    assert body["candidates"][0]["margin"] > body["candidates"][1]["margin"]
    assert body["top_two_margin_gap"] > 0
    assert "not probabilities" in body["score_type"]


@pytest.mark.parametrize("text", ["", "  ", "x" * 1001])
def test_invalid_text_is_rejected(client, text):
    assert client.post("/predict", json={"text": text}).status_code == 422


def test_invalid_scores_do_not_return_predictions(client):
    api.app.dependency_overrides[api.require_model] = lambda: FakeModel(invalid=True)
    response = client.post("/predict", json={"text": "transferência"})
    assert response.status_code == 503
    assert "scores" in response.json()["detail"].lower()


def test_no_model_details_in_liveness(client):
    result = client.get("/health/live").json()
    assert "model" not in result


def test_model_loading_failure_is_sanitized():
    api.app.dependency_overrides.clear()
    def unavailable():
        raise RuntimeError("sensitive internal service exception")
    api.app.dependency_overrides[api.require_model] = unavailable
    with TestClient(api.app, raise_server_exceptions=False) as client:
        # Substituted dependency errors are deliberately not caught by FastAPI.
        # Only require_model catches real get_model() failures.
        response = client.get("/health/ready")
        assert response.status_code == 500
    api.app.dependency_overrides.clear()


def test_readiness_reports_503_for_missing_artifact(monkeypatch):
    api.app.dependency_overrides.clear()
    def fail():
        raise FileNotFoundError("private internal filepath")
    monkeypatch.setattr(api, "get_model", fail)
    with TestClient(api.app) as client:
        response = client.get("/health/ready")
    assert response.status_code == 503
    assert response.json()["detail"] == "Model temporarily unavailable"
