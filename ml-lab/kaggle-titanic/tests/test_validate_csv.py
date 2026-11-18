"""Regression tests for Titanic submission validation (synthetic CSV data)."""
from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("titanic_notebook_runner_validation", ROOT / "run_notebook.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


@pytest.fixture
def csv_files(tmp_path: Path):
    test = tmp_path / "test.csv"
    submission = tmp_path / "submission.csv"
    test.write_text("PassengerId,Pclass\n4,3\n5,2\n", encoding="utf-8")
    submission.write_text("PassengerId,Survived\n4,1\n5,0\n", encoding="utf-8")
    return submission, test


def test_accepts_exact_binary_csv_and_order(csv_files):
    submission, test = csv_files
    assert MODULE.validate_submission(submission, test) == 2


@pytest.mark.parametrize(
    "csv_text,reason",
    [
        ("PassengerId,Survived\n4,1.0\n5,0\n", "binary"),
        ("PassengerId,Survived\n4,true\n5,0\n", "binary"),
        ("PassengerId,Survived\n4,2\n5,0\n", "binary"),
        ("PassengerId,Survived\n4,\n5,0\n", "binary"),
        ("PassengerId,Survived\n4,-1\n5,0\n", "binary"),
        ("PassengerId,Survived\n04,1\n5,0\n", "PassengerId"),
        ("PassengerId,Survived\n4.0,1\n5,0\n", "PassengerId"),
        ("PassengerId,Survived\n4,1\n4,0\n", "duplicate"),
        ("PassengerId,Survived\n5,1\n4,0\n", "IDs/order"),
        ("PassengerId,Survived\n4,1\n6,0\n", "IDs/order"),
        ("PassengerId,Survived,Extra\n4,1,x\n5,0,x\n", "columns"),
        ("PassengerId,Survived\n", "empty"),
    ],
)
def test_rejects_malformed_submissions(csv_files, csv_text, reason):
    submission, test = csv_files
    submission.write_text(csv_text, encoding="utf-8")
    with pytest.raises(ValueError, match=reason):
        MODULE.validate_submission(submission, test)


def test_rejects_reference_without_passenger_id(csv_files):
    submission, test = csv_files
    test.write_text("Pclass\n3\n2\n", encoding="utf-8")
    with pytest.raises(ValueError, match="Official test is missing PassengerId"):
        MODULE.validate_submission(submission, test)


def test_cli_reports_success_and_failure(csv_files):
    submission, test = csv_files
    command = [
        sys.executable, str(ROOT / "validate_csv.py"),
        "--submission", str(submission), "--test", str(test),
    ]
    ok = subprocess.run(command, capture_output=True, text=True, check=False)
    assert ok.returncode == 0
    assert "PASS: 2" in ok.stdout

    submission.write_text("PassengerId,Survived\n4,1.0\n5,0\n", encoding="utf-8")
    bad = subprocess.run(command, capture_output=True, text=True, check=False)
    assert bad.returncode == 2
    assert "INVALID submission" in bad.stderr
