"""Compare two AI Evaluation Lab reports without external services or secrets.

Use this tool to inspect paired before/after quality metrics and individual
regressions. Reports must describe the same dataset, assistant, case IDs, and
evaluation settings. The comparison contains only case IDs, not user queries
or model responses.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

# All of these metrics use [0, 1]. A larger value is better except leak rate.
HIGHER_IS_BETTER = (
    "retrieval_hit_at_k",
    "retrieval_mrr_at_k",
    "answer_substring_accuracy",
    "abstention_accuracy",
    "answer_lexical_support_rate",
)
LOWER_IS_BETTER = ("attack_marker_leak_rate",)
QUALITY_METRICS = HIGHER_IS_BETTER + LOWER_IS_BETTER
CASE_FLAGS = (
    "hit_at_k",
    "expected_substring_match",
    "lexically_supported",
    "abstained",
    "attack_marker_leak",
)


def _metadata(report: dict) -> dict:
    metadata = report.get("metadata")
    if not isinstance(metadata, dict):
        raise ValueError("Report is missing metadata")
    for key in ("dataset", "assistant", "top_k", "cases", "positive_cases", "negative_cases"):
        if key not in metadata:
            raise ValueError(f"Report metadata is missing {key}")
    return metadata


def _case_map(report: dict) -> dict[str, dict]:
    results = report.get("results")
    if not isinstance(results, list) or not results:
        raise ValueError("Report must contain nonempty results")
    mapping: dict[str, dict] = {}
    for row in results:
        if not isinstance(row, dict):
            raise ValueError("Invalid case record")
        identifier = row.get("id")
        if not isinstance(identifier, str) or not identifier.strip() or identifier in mapping:
            raise ValueError("Missing or duplicate case ID")
        if not isinstance(row.get("category"), str):
            raise ValueError(f"Missing category for case {identifier}")
        for flag in CASE_FLAGS:
            if type(row.get(flag)) is not bool:
                raise ValueError(f"Missing boolean {flag} for case {identifier}")
        mapping[identifier] = row
    return mapping


def _quality_metrics(report: dict) -> dict[str, float | None]:
    metrics = report.get("metrics")
    if not isinstance(metrics, dict):
        raise ValueError("Report is missing metrics")
    result: dict[str, float | None] = {}
    for name in QUALITY_METRICS:
        value = metrics.get(name)
        if value is None:
            result[name] = None
        elif type(value) in (int, float) and math.isfinite(value) and 0 <= value <= 1:
            result[name] = float(value)
        else:
            raise ValueError(f"Invalid metric {name}: expected finite value in [0, 1]")
    return result


def compare_reports(before: dict, after: dict) -> dict:
    """Compare paired experiment reports without modifying either input."""
    a, b = _metadata(before), _metadata(after)
    for key in ("dataset", "assistant", "top_k", "cases", "positive_cases", "negative_cases"):
        if a[key] != b[key]:
            raise ValueError(f"Incompatible reports: {key} differs")
    old_cases, new_cases = _case_map(before), _case_map(after)
    if set(old_cases) != set(new_cases) or len(old_cases) != a["cases"]:
        raise ValueError("Incompatible reports: case IDs or counts differ")
    for case_id in old_cases:
        if old_cases[case_id]["category"] != new_cases[case_id]["category"]:
            raise ValueError(f"Case category changed: {case_id}")

    old_metrics = _quality_metrics(before)
    new_metrics = _quality_metrics(after)
    changes = []
    for metric in QUALITY_METRICS:
        old, new = old_metrics[metric], new_metrics[metric]
        delta = round(new - old, 5) if old is not None and new is not None else None
        if delta is None:
            direction = "not_applicable"
        elif delta == 0:
            direction = "unchanged"
        else:
            improved = delta > 0 if metric in HIGHER_IS_BETTER else delta < 0
            direction = "improved" if improved else "regressed"
        changes.append({
            "metric": metric, "before": old, "after": new,
            "delta": delta, "status": direction,
        })

    # Per-case diagnosis, based on the same case IDs. These flags are
    # observations, not interchangeable measurements of model accuracy.
    transitions = {}
    for flag in ("hit_at_k", "expected_substring_match", "lexically_supported", "attack_marker_leak"):
        gained = sorted(
            case_id for case_id in old_cases
            if not old_cases[case_id][flag] and new_cases[case_id][flag]
        )
        lost = sorted(
            case_id for case_id in old_cases
            if old_cases[case_id][flag] and not new_cases[case_id][flag]
        )
        transitions[flag] = {"false_to_true": gained, "true_to_false": lost}

    return {
        "dataset": a["dataset"],
        "assistant": a["assistant"],
        "top_k": a["top_k"],
        "cases": len(old_cases),
        "before_method": a.get("retrieval_method", "unknown"),
        "after_method": b.get("retrieval_method", "unknown"),
        "quality_metrics": changes,
        "case_transitions": transitions,
        "note": (
            "Only a paired descriptive comparison of recorded metrics. "
            "This is not statistical significance, semantic evaluation, "
            "or a claim about model performance in production."
        ),
    }


def markdown_report(comparison: dict) -> str:
    lines = [
        "# AI Evaluation Lab | comparação de experimentos",
        "",
        f"Dataset: {comparison['dataset']}; assistente: {comparison['assistant']}; "
        f"casos: {comparison['cases']}; top-k: {comparison['top_k']}.",
        f"Retrieval: {comparison['before_method']} -> {comparison['after_method']}.",
        "",
        "| Métrica | Antes | Depois | Delta | Interpretação |",
        "|:--|--:|--:|--:|:--|",
    ]
    for item in comparison["quality_metrics"]:
        fmt = lambda v: "n/a" if v is None else f"{v:.5f}"
        lines.append(
            f"| {item['metric']} | {fmt(item['before'])} | "
            f"{fmt(item['after'])} | {fmt(item['delta'])} | {item['status']} |"
        )
    lines += ["", "## Casos que mudaram", ""]
    for flag, values in comparison["case_transitions"].items():
        lines.append(f"### {flag}")
        lines.append(f"- False -> True ({len(values['false_to_true'])}): "
                     + (", ".join(values["false_to_true"]) or "nenhum"))
        lines.append(f"- True -> False ({len(values['true_to_false'])}): "
                     + (", ".join(values["true_to_false"]) or "nenhum"))
        lines.append("")
    lines += [comparison["note"], ""]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare two offline AI evaluation reports")
    parser.add_argument("--before", required=True, type=Path, help="First report JSON")
    parser.add_argument("--after", required=True, type=Path, help="Second report JSON")
    parser.add_argument("--output", required=True, type=Path, help="Output Markdown path")
    args = parser.parse_args()
    before = json.loads(args.before.read_text(encoding="utf-8"))
    after = json.loads(args.after.read_text(encoding="utf-8"))
    comparison = compare_reports(before, after)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown_report(comparison), encoding="utf-8")
    print(f"Compared {comparison['cases']} paired cases; report: {args.output}")


if __name__ == "__main__":
    main()
