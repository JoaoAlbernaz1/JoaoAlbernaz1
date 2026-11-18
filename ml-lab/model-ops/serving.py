"""A small, inspectable inference service for a real published scikit-learn model.

Demo API, not a production gateway. No requests or customer text are persisted.
"""
from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import Annotated

import numpy as np
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

MODEL_REPO = "JOAOOALBERNAZ/banking77-ptbr-intent-v1"
MODEL_REVISION = os.getenv("MODEL_REVISION", "main")
MIN_MARGIN_GAP = 0.15  # Demonstration heuristic, NOT a validated confidence threshold.

app = FastAPI(
    title="BANKING77 PTBR · Model Serving",
    version="1.0.0",
    description="Inference API for an experimental 77-class NLP model; no business decisions.",
)


class PredictRequest(BaseModel):
    text: str = Field(min_length=1, max_length=1000, description="One Portuguese banking query")

    @field_validator("text")
    @classmethod
    def validate_text(cls, text: str) -> str:
        trimmed = text.strip()
        if not trimmed:
            raise ValueError("Text must not contain only whitespace")
        return trimmed


class Candidate(BaseModel):
    intent: str
    margin: float


class PredictResponse(BaseModel):
    intent: str
    candidates: list[Candidate]
    top_two_margin_gap: float
    low_separation: bool
    score_type: str
    model: str
    disclaimer: str


@lru_cache(maxsize=1)
def get_model():
    """Lazy-loading prevents accidental Hub network calls at import time."""
    import skops.io as sio

    configured_path = os.getenv("MODEL_PATH")
    if configured_path:
        path = Path(configured_path)
    else:
        from huggingface_hub import hf_hub_download
        path = Path(hf_hub_download(
            repo_id=MODEL_REPO, filename="model.skops",
            revision=MODEL_REVISION, repo_type="model",
        ))
    if not path.is_file():
        raise FileNotFoundError("Model artifact unavailable")
    # Reject unrecognized types instead of blindly trusting a serialized artifact.
    untrusted = sio.get_untrusted_types(file=path)
    if untrusted:
        raise ValueError("Serialized model contains unsupported/untrusted types")
    model = sio.load(path, trusted=[])
    if "clf" not in model.named_steps or len(model.named_steps["clf"].classes_) != 77:
        raise ValueError("Unexpected model architecture or labels")
    return model


ModelDependency = Annotated[object, Depends(get_model)]


@app.get("/health/live")
def liveness() -> dict[str, str]:
    return {"status": "alive"}


@app.get("/health/ready")
def readiness(model: ModelDependency) -> dict[str, str]:
    return {"status": "ready", "model": MODEL_REPO}


@app.get("/model-info")
def model_info(model: ModelDependency) -> dict:
    return {
        "repo": MODEL_REPO,
        "revision": MODEL_REVISION,
        "n_classes": len(model.named_steps["clf"].classes_),
        "score_type": "LinearSVC decision-function margins, NOT probabilities",
        "intended_use": "research demonstration; not for real financial decisions",
    }


@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest, model: ModelDependency) -> PredictResponse:
    raw = np.asarray(model.decision_function([payload.text]))
    margins = raw[0] if raw.ndim == 2 else raw
    labels = model.named_steps["clf"].classes_
    if margins.ndim != 1 or len(margins) != len(labels) or len(labels) < 3:
        raise HTTPException(status_code=503, detail="Incompatible model output")
    if not np.isfinite(margins).all():
        raise HTTPException(status_code=503, detail="Non-finite model scores")
    order = np.argsort(-margins, kind="stable")
    top = order[:3]
    candidates = [
        Candidate(intent=str(labels[int(idx)]), margin=round(float(margins[int(idx)]), 5))
        for idx in top
    ]
    gap = float(margins[int(order[0])] - margins[int(order[1])])
    return PredictResponse(
        intent=candidates[0].intent,
        candidates=candidates,
        top_two_margin_gap=round(gap, 5),
        low_separation=gap < MIN_MARGIN_GAP,
        score_type="unnormalized LinearSVC margins (not probabilities)",
        model=MODEL_REPO,
        disclaimer="Experimental banking intent model on translated research data; do not use for financial decisions.",
    )
