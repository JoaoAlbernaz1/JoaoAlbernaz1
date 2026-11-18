"""Offline dataset-shift monitoring; never claim PSI/JSD prove prediction quality.

Reference and comparison sets are public research splits, not production traffic.
Only aggregate histograms are saved; raw text is not included in the report.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path
from typing import Iterable

import numpy as np

LENGTH_BINS = [0, 20, 40, 60, 90, 130, 190, 300, float("inf")]
LENGTH_BIN_NAMES = [
    "0-19", "20-39", "40-59", "60-89",
    "90-129", "130-189", "190-299", "300+",
]


def histogram(values: Iterable[int]) -> list[int]:
    values = list(values)
    if not values:
        raise ValueError("Cannot monitor empty samples")
    if any(not isinstance(x, (int, np.integer)) or x < 0 for x in values):
        raise ValueError("All lengths must be nonnegative integers")
    counts, _ = np.histogram(values, bins=LENGTH_BINS)
    return [int(v) for v in counts]


def category_counts(values: Iterable[str], categories: list[str]) -> list[int]:
    if not categories or len(set(categories)) != len(categories):
        raise ValueError("Expected distinct nonempty categories")
    labels = list(values)
    if not labels:
        raise ValueError("Cannot monitor empty prediction sets")
    unknown = set(labels) - set(categories)
    if unknown:
        raise ValueError("Unknown predictions outside model vocabulary")
    frequencies = Counter(labels)
    return [frequencies.get(label, 0) for label in categories]


def proportions(counts: Iterable[int]) -> np.ndarray:
    counts = np.asarray(list(counts), dtype=float)
    if counts.ndim != 1 or not len(counts) or np.any(counts < 0) or not np.all(np.isfinite(counts)):
        raise ValueError("Invalid histogram counts")
    if counts.sum() <= 0:
        raise ValueError("Empty histogram")
    return counts / counts.sum()


def jensen_shannon_bits(left: Iterable[int], right: Iterable[int]) -> float:
    """Jensen-Shannon DIVERGENCE (not square-root JS distance) in bits: [0, 1]."""
    a, b = proportions(left), proportions(right)
    if len(a) != len(b):
        raise ValueError("Distribution dimensions do not match")
    midpoint = (a + b) / 2

    def kl(p):
        valid = p > 0
        return float(np.sum(p[valid] * np.log2(p[valid] / midpoint[valid])))

    return max(0.0, min(1.0, 0.5 * (kl(a) + kl(b))))


def population_stability_index(reference: Iterable[int], current: Iterable[int], smoothing: float = 1e-6) -> float:
    """PSI on fixed bins; zero bins smoothed, threshold is a heuristic only."""
    if smoothing <= 0:
        raise ValueError("Smoothing must be positive")
    a, b = proportions(reference), proportions(current)
    if len(a) != len(b):
        raise ValueError("Distribution dimensions do not match")
    aa = (a + smoothing) / (1 + len(a) * smoothing)
    bb = (b + smoothing) / (1 + len(b) * smoothing)
    result = float(np.sum((bb - aa) * np.log(bb / aa)))
    return max(0.0, result)


def evaluate(reference_texts: list[str], comparison_texts: list[str],
             reference_predictions: list[str], comparison_predictions: list[str],
             labels: list[str]) -> dict:
    if not reference_texts or not comparison_texts:
        raise ValueError("Both datasets must have samples")
    if len(reference_texts) != len(reference_predictions) or len(comparison_texts) != len(comparison_predictions):
        raise ValueError("Each prediction must match a text")
    if any(not isinstance(text, str) for text in reference_texts + comparison_texts):
        raise ValueError("Only strings are accepted")

    ref_lengths = histogram([len(t) for t in reference_texts])
    new_lengths = histogram([len(t) for t in comparison_texts])
    ref_labels = category_counts(reference_predictions, labels)
    new_labels = category_counts(comparison_predictions, labels)

    length_psi = population_stability_index(ref_lengths, new_lengths)
    length_js = jensen_shannon_bits(ref_lengths, new_lengths)
    label_js = jensen_shannon_bits(ref_labels, new_labels)

    # These thresholds are illustrative and MUST be calibrated for a real use case.
    return {
        "context": {
            "reference_rows": len(reference_texts),
            "comparison_rows": len(comparison_texts),
            "classes": len(labels),
            "reference": "official BANKING77-PTBR train (translated public research data)",
            "comparison": "official BANKING77-PTBR test (public research split)",
            "purpose": "offline distribution diagnostics, not real-time production monitoring",
        },
        "metrics": {
            "length_psi": round(length_psi, 6),
            "length_js_divergence_bits": round(length_js, 6),
            "predicted_label_js_divergence_bits": round(label_js, 6),
        },
        "heuristic_signals": {
            "length_distribution_shift": length_psi >= .2,
            "predicted_label_distribution_shift": label_js >= .05,
            "thresholds_are_calibrated": False,
        },
        "length_histograms": {
            "bins": LENGTH_BIN_NAMES,
            "reference": ref_lengths,
            "comparison": new_lengths,
        },
        "prediction_histograms": {
            "label_names": labels,
            "reference": ref_labels,
            "comparison": new_labels,
        },
        "limitations": [
            "These are aggregate unlabeled distribution statistics, NOT accuracy, macro-F1 or recall.",
            "Predicted label drift may reflect changes in the model, dataset composition or preprocessing.",
            "Official train vs test comparison is not evidence of a production incident.",
            "Fixed length bins and illustrative thresholds are not calibrated to business costs.",
            "Raw texts and individual predictions are intentionally not written to disk.",
        ],
    }


def render_report(report: dict) -> str:
    ctx = report["context"]
    metrics = report["metrics"]
    flags = report["heuristic_signals"]
    h = report["length_histograms"]
    lines = [
        "# BANKING77-PTBR · ModelOps Distribution Monitoring",
        "",
        "**Auditoria offline em dados públicos**, sem monitoramento de usuários reais.",
        "",
        f"Referência: **{ctx['reference_rows']}** textos do treino oficial. "
        f"Comparação: **{ctx['comparison_rows']}** textos do teste oficial.",
        "",
        "| Estatística | Valor |",
        "|:--|--:|",
        f"| PSI de comprimento | {metrics['length_psi']:.4f} |",
        f"| Jensen-Shannon de comprimento (bits) | {metrics['length_js_divergence_bits']:.4f} |",
        f"| Jensen-Shannon de intenções previstas (bits) | {metrics['predicted_label_js_divergence_bits']:.4f} |",
        "",
        "## Distribuição de comprimento de mensagens",
        "",
        "| Caracteres | Treino | Teste |",
        "|:--|--:|--:|",
    ]
    for bin_name, x, y in zip(h["bins"], h["reference"], h["comparison"]):
        lines.append(f"| {bin_name} | {x} | {y} |")
    lines.extend([
        "",
        "## Alertas demonstrativos (não calibrados)",
        "",
        f"- Shift no comprimento (PSI ≥ 0,2): **{flags['length_distribution_shift']}**.",
        f"- Shift nas intenções previstas (JSD ≥ 0,05): **{flags['predicted_label_distribution_shift']}**.",
        "",
        "Não há garantia estatística de detecção de incidentes. Os limiares são exemplos, "
        "não parâmetros validados para um sistema financeiro.",
        "",
        "## Interpretação",
        "",
        "PSI e Jensen-Shannon descrevem mudanças nas distribuições. "
        "Não avaliam verdade de rótulos, qualidade do atendimento, desempenho de LLMs ou erro do classificador. "
        "Comparar os splits oficiais de pesquisa NÃO equivale a monitorar produção.",
        "",
        "- [Dados agregados por classe e métricas](./metrics.json)",
        "- [Código de monitoramento e API](../../model-ops/)",
        "- [Modelo NLP utilizado](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1)",
        "- [Pesquisa e auditoria dos dados](../../docs/banking77-ptbr-results.md)",
        "",
        "O relatório omite deliberadamente textos e previsões individuais.",
        "",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("outputs/model-ops/metrics.json"))
    args = parser.parse_args()

    import pandas as pd
    import skops.io as sio
    from huggingface_hub import hf_hub_download

    dataset_id = "c2d-usp/banking77-pt-br"
    dataset_revision = "85f51c4"
    paths = {
        split: hf_hub_download(
            repo_id=dataset_id, repo_type="dataset",
            revision=dataset_revision, filename=split + ".csv",
        )
        for split in ("train", "test")
    }
    frames = {}
    for split, path in paths.items():
        df = pd.read_csv(path)[["frase", "rotulo"]].dropna()
        df = df[df["frase"].astype(str).str.strip() != ""].copy()
        frames[split] = df

    model_path = hf_hub_download(
        repo_id="JOAOOALBERNAZ/banking77-ptbr-intent-v1",
        repo_type="model", filename="model.skops",
    )
    if sio.get_untrusted_types(file=model_path):
        raise ValueError("Unexpected serialized object types")
    model = sio.load(model_path, trusted=[])
    labels = [str(v) for v in model.named_steps["clf"].classes_]

    reference_texts = frames["train"]["frase"].astype(str).tolist()
    current_texts = frames["test"]["frase"].astype(str).tolist()
    reference_preds = [str(v) for v in model.predict(reference_texts)]
    current_preds = [str(v) for v in model.predict(current_texts)]
    report = evaluate(reference_texts, current_texts, reference_preds, current_preds, labels)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    (args.output.parent / "README.md").write_text(render_report(report), encoding="utf-8")
    print(json.dumps({"context": report["context"], "metrics": report["metrics"],
                      "signals": report["heuristic_signals"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
