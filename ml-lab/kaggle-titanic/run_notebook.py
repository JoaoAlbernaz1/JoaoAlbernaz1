"""Execute a Kaggle-ready Titanic notebook in CI using the official competition CSVs.

Remaps Kaggle-only paths to runner paths in an *in-memory copy* of the notebook.
This validates the real, standalone notebook instead of just parsing its cells.
"""
from __future__ import annotations

import argparse
import copy
from pathlib import Path

import pandas as pd


def remap_notebook(notebook: dict, train: Path, test: Path, output: Path) -> dict:
    """Change only file paths in code cells, not notebook text or the committed source."""
    replacements = {
        "/kaggle/input/titanic/train.csv": str(train.resolve()),
        "/kaggle/input/titanic/test.csv": str(test.resolve()),
        "/kaggle/working/submission.csv": str(output.resolve()),
    }
    clone = copy.deepcopy(notebook)
    observed = {k: 0 for k in replacements}
    for cell in clone["cells"]:
        if cell["cell_type"] != "code":
            continue
        source = cell["source"]
        is_list = isinstance(source, list)
        script = "".join(source) if is_list else source
        for old, new in replacements.items():
            observed[old] += script.count(old)
            script = script.replace(old, new)
        cell["source"] = script.splitlines(keepends=True) if is_list else script
    missing = [name for name, count in observed.items() if count == 0]
    if missing:
        raise ValueError("Notebook lacks required input/output reference(s): " + ", ".join(missing))
    return clone


def validate_submission(output: Path, test: Path) -> int:
    """Match row order/IDs, binary targets and exact official column schema."""
    predictions = pd.read_csv(output)
    official_test = pd.read_csv(test)
    if predictions.columns.tolist() != ["PassengerId", "Survived"]:
        raise ValueError("Incorrect submission columns")
    if not predictions.PassengerId.equals(official_test.PassengerId):
        raise ValueError("Submission IDs/order do not match official test")
    if predictions.PassengerId.isna().any() or predictions.PassengerId.duplicated().any():
        raise ValueError("Missing/duplicate PassengerIds")
    if predictions.Survived.isna().any() or not set(predictions.Survived.unique()).issubset({0, 1}):
        raise ValueError("Survived column must contain binary integer values")
    if len(predictions) == 0:
        raise ValueError("Submission is empty")
    return len(predictions)


def execute(notebook: Path, train: Path, test: Path, output_dir: Path) -> Path:
    try:
        import nbformat
        from nbclient import NotebookClient
    except ImportError as exc:
        raise RuntimeError("Install notebook dependencies: nbformat nbclient ipykernel matplotlib") from exc

    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    csv = output_dir / "submission.csv"
    original = nbformat.read(notebook, as_version=4)
    patched = remap_notebook(original, train, test, csv)
    client = NotebookClient(
        nbformat.from_dict(patched), kernel_name="python3", timeout=1200,
        allow_errors=False, resources={"metadata": {"path": str(output_dir)}},
    )
    executed = client.execute()
    nbformat.write(executed, output_dir / "executed_notebook.ipynb")
    if not csv.is_file():
        raise FileNotFoundError(f"Notebook completed without expected output: {csv}")
    rows = validate_submission(csv, test)
    print(f"PASS: notebook executed and generated {rows} valid predictions at {csv}")
    return csv


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--notebook", required=True, type=Path)
    parser.add_argument("--train", required=True, type=Path)
    parser.add_argument("--test", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    execute(args.notebook, args.train, args.test, args.output_dir)


if __name__ == "__main__":
    main()
