"""Metamorphic and synthetic-typo regression study on BANKING77-PTBR.

Uses published trained model and official test data without retraining or tuning.
The transformations are deterministic and outputs aggregate metrics only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

MODEL_ID = "JOAOOALBERNAZ/banking77-ptbr-intent-v1"
DATASET_ID = "c2d-usp/banking77-pt-br"
DATASET_REVISION = "85f51c4"
VARIANTS = ("accent_removed", "upper_whitespace", "adjacent_typo")


def transform(text: str, variant: str) -> str:
    if variant == "accent_removed":
        normalized = unicodedata.normalize("NFKD", text)
        return "".join(char for char in normalized if not unicodedata.combining(char))
    if variant == "upper_whitespace":
        return "   " + " ".join(text.upper().split()) + "   "
    if variant == "adjacent_typo":
        # Single transposition of different neighboring letters inside a long word.
        # Not guaranteed to preserve meaning: this is a controlled perturbation only.
        words = [
            m for m in re.finditer(r"\b[^\W\d_]{5,}\b", text, flags=re.UNICODE)
            if len(m.group(0)) >= 5
        ]
        if not words:
            return text
        best = sorted(words, key=lambda m: (-len(m.group(0)), m.start()))[0]
        word = best.group(0)
        positions = [
            i for i in range(1, len(word) - 2)
            if word[i] != word[i + 1] and word[i].isalpha() and word[i + 1].isalpha()
        ]
        if not positions:
            return text
        digest = hashlib.sha256(text.encode("utf-8")).digest()
        i = positions[int.from_bytes(digest[:4], "big") % len(positions)]
        shuffled = word[:i] + word[i+1] + word[i] + word[i+2:]
        return text[:best.start()] + shuffled + text[best.end():]
    raise ValueError(f"Unrecognized perturbation: {variant}")


def metrics(truth, predicted):
    return {
        "accuracy": float(accuracy_score(truth, predicted)),
        "macro_f1": float(f1_score(truth, predicted, average="macro", zero_division=0)),
    }


def evaluate(model, texts: list[str], truth: list[str]) -> dict:
    if not texts or len(texts) != len(truth):
        raise ValueError("Expected nonempty aligned texts and labels")
    baseline_pred = np.asarray(model.predict(texts))
    if len(baseline_pred) != len(texts):
        raise ValueError("Model returned wrong prediction count")
    baseline = metrics(truth, baseline_pred)
    variants = {}
    for variant in VARIANTS:
        changed = [transform(t, variant) for t in texts]
        predicted = np.asarray(model.predict(changed))
        score = metrics(truth, predicted)
        variants[variant] = {
            **score,
            "macro_f1_change": float(score["macro_f1"] - baseline["macro_f1"]),
            "prediction_flip_rate": float(np.mean(predicted != baseline_pred)),
            "text_change_rate": float(np.mean(np.asarray(changed) != np.asarray(texts))),
            "number_of_records": len(texts),
        }
    return {
        "dataset": DATASET_ID,
        "revision": DATASET_REVISION,
        "model": MODEL_ID,
        "split": "official test (nonempty texts and labels)",
        "samples": len(texts),
        "baseline": baseline,
        "perturbations": variants,
        "interpretation": [
            "Accent and uppercase/spacing are metamorphic robustness probes, not extra independent test sets.",
            "Adjacent transposition is deterministic, but may change the meaning of some inputs.",
            "Scores compare the same trained model on altered test inputs; NO retraining or tuning.",
            "Perturbed test results are a robustness diagnostic, not a Kaggle leaderboard or evidence of production quality.",
            "No raw inputs or individual predictions are published.",
        ],
    }


def render(report: dict) -> str:
    baseline = report["baseline"]
    names = {
        "accent_removed": "Remover acentos",
        "upper_whitespace": "Caixa alta + espaços",
        "adjacent_typo": "Transposição de letras",
    }
    lines = [
        "# BANKING77-PTBR · Robustness & Metamorphic Tests",
        "",
        f"Modelo publicado avaliado em **{report['samples']} mensagens do teste oficial** "
        "do dataset de pesquisa BANKING77-PTBR.",
        "",
        f"**Baseline sem alterações:** accuracy **{baseline['accuracy']:.4f}** · macro-F1 **{baseline['macro_f1']:.4f}**.",
        "",
        "| Perturbação | Macro-F1 | Variação F1 | Troca de previsão | Textos alterados |",
        "|:--|--:|--:|--:|--:|",
    ]
    for key in VARIANTS:
        row = report["perturbations"][key]
        lines.append(
            f"| {names[key]} | {row['macro_f1']:.4f} | {row['macro_f1_change']:+.4f} "
            f"| {row['prediction_flip_rate']:.1%} | {row['text_change_rate']:.1%} |"
        )
    lines.extend([
        "",
        "## O que esse experimento mostra",
        "",
        "As transformações são determinísticas. Remoção de acentos e caixa alta/espaçamento "
        "testam invariâncias esperadas da vetorização TF-IDF. A troca de duas letras "
        "testa sensibilidade a um erro de digitação simulado e **pode alterar o sentido da frase**.",
        "",
        "O estudo é uma avaliação pontual, não uma garantia de robustez adversarial. "
        "Não são usados dados de usuários reais nem rótulos ocultos do Kaggle.",
        "",
        "- [Métricas completas](./robustness.json)",
        "- [Código das transformações](../../model-ops/robustness.py)",
        "- [Modelo publicado](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1)",
        "",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("outputs/model-ops/robustness.json"))
    args = parser.parse_args()

    from huggingface_hub import hf_hub_download
    import skops.io as sio

    test_path = hf_hub_download(
        repo_id=DATASET_ID, repo_type="dataset",
        filename="test.csv", revision=DATASET_REVISION,
    )
    frame = pd.read_csv(test_path)[["frase", "rotulo"]].dropna()
    frame = frame[frame["frase"].astype(str).str.strip() != ""]
    path = hf_hub_download(repo_id=MODEL_ID, repo_type="model", filename="model.skops")
    if sio.get_untrusted_types(file=path):
        raise ValueError("Untrusted model types")
    model = sio.load(path, trusted=[])

    report = evaluate(model, frame["frase"].astype(str).tolist(), frame["rotulo"].astype(str).tolist())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output.parent / "ROBUSTNESS.md").write_text(render(report), encoding="utf-8")
    print(json.dumps({"baseline": report["baseline"], "perturbations": report["perturbations"]},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
