"""Validate a Titanic submission.csv before uploading it to Kaggle.

Example:
    python ml-lab/kaggle-titanic/validate_csv.py \
        --submission outputs/titanic/submission.csv --test path/to/test.csv
"""
from __future__ import annotations

import argparse
from pathlib import Path

from run_notebook import validate_submission


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a Titanic competition submission.csv")
    parser.add_argument("--submission", required=True, type=Path, help="CSV containing PassengerId,Survived")
    parser.add_argument("--test", required=True, type=Path, help="Official Titanic test.csv with PassengerId")
    args = parser.parse_args()
    try:
        rows = validate_submission(args.submission, args.test)
    except (OSError, ValueError) as exc:
        parser.exit(2, f"INVALID submission: {exc}\n")
    print(f"PASS: {rows} Titanic predictions have valid columns, IDs and integer labels.")


if __name__ == "__main__":
    main()
