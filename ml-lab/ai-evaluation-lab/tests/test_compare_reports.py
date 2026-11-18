"""Tests for reproducible, privacy-preserving comparison of evaluation runs."""
from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("ai_evaluation_compare", ROOT / "compare_reports.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def fixture_report():
    return {
        "metadata": {
            "cases": 2,
            "positive_cases": 1,
            "negative_cases": 1,
            "dataset": "synthetic_qa",
            "assistant": "ExtractiveAssistant",
            "retrieval_method": "word",
            "top_k": 3,
        },
        "metrics": {
            "retrieval_hit_at_k": 0.0,
            "retrieval_mrr_at_k": 0.0,
            "answer_substring_accuracy": 0.0,
            "abstention_accuracy": 1.0,
            "answer_lexical_support_rate": None,
            "attack_marker_leak_rate": 0.5,
        },
        "results": [
            {
                "id": "c1", "category": "answerable",
                "hit_at_k": False, "expected_substring_match": False,
                "lexically_supported": False, "abstained": True,
                "attack_marker_leak": False,
                "question": "private text should not be exposed",
                "response": "private response should not be exposed",
            },
            {
                "id": "c2", "category": "prompt_injection",
                "hit_at_k": False, "expected_substring_match": False,
                "lexically_supported": False, "abstained": True,
                "attack_marker_leak": True,
            },
        ],
    }


def test_paired_comparison_detects_improvements_and_protects_raw_text():
    before = fixture_report()
    after = copy.deepcopy(before)
    after["metadata"]["retrieval_method"] = "char"
    after["metrics"]["retrieval_hit_at_k"] = 1.0
    after["metrics"]["attack_marker_leak_rate"] = 0.0
    after["results"][0]["hit_at_k"] = True
    after["results"][1]["attack_marker_leak"] = False

    compared = MODULE.compare_reports(before, after)
    by_metric = {item["metric"]: item for item in compared["quality_metrics"]}
    assert by_metric["retrieval_hit_at_k"]["status"] == "improved"
    assert by_metric["retrieval_hit_at_k"]["delta"] == 1.0
    assert by_metric["attack_marker_leak_rate"]["status"] == "improved"
    assert by_metric["answer_lexical_support_rate"]["status"] == "not_applicable"
    assert compared["case_transitions"]["hit_at_k"]["false_to_true"] == ["c1"]
    assert compared["case_transitions"]["attack_marker_leak"]["true_to_false"] == ["c2"]
    rendered = MODULE.markdown_report(compared)
    assert "private text" not in rendered and "private response" not in rendered
    assert "c1" in rendered and "c2" in rendered
    assert "Retrieval: word -> char" in rendered


@pytest.mark.parametrize(
    "modify",
    [
        lambda b: b["metadata"].update({"dataset": "different"}),
        lambda b: b["metadata"].update({"top_k": 10}),
        lambda b: b["results"].pop(),
        lambda b: b["results"][1].update({"id": "c1"}),
        lambda b: b["results"][0].update({"category": "unanswerable"}),
        lambda b: b["results"][0].update({"hit_at_k": "yes"}),
        lambda b: b["metrics"].update({"retrieval_hit_at_k": float("nan")}),
        lambda b: b["metrics"].update({"attack_marker_leak_rate": 1.25}),
    ],
)
def test_rejects_incompatible_or_invalid_reports(modify):
    before = fixture_report()
    after = copy.deepcopy(before)
    modify(after)
    with pytest.raises(ValueError):
        MODULE.compare_reports(before, after)


def test_cli_writes_markdown_without_external_api(tmp_path):
    before = fixture_report()
    after = copy.deepcopy(before)
    left = tmp_path / "before.json"
    right = tmp_path / "after.json"
    output = tmp_path / "report.md"
    left.write_text(json.dumps(before), encoding="utf-8")
    right.write_text(json.dumps(after), encoding="utf-8")
    cmd = [
        sys.executable, str(ROOT / "compare_reports.py"),
        "--before", str(left),
        "--after", str(right),
        "--output", str(output),
    ]
    proc = subprocess.run(cmd, check=False, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    assert "# AI Evaluation Lab" in output.read_text(encoding="utf-8")
