"""Offline output and execution-adapter tests (synthetic fixtures only)."""
import importlib.util
import json
import sys
from pathlib import Path

import pandas as pd
import pytest

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("titanic_run_notebook", HERE / "run_notebook.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


@pytest.mark.parametrize("name", ["titanic_baseline.ipynb", "titanic_feature_engineering.ipynb"])
def test_both_notebooks_save_kaggle_working_submission(name):
    notebook = json.loads((HERE / name).read_text(encoding="utf-8"))
    scripts = "\n".join("".join(c["source"]) for c in notebook["cells"] if c["cell_type"] == "code")
    assert "/kaggle/working/submission.csv" in scripts
    assert "Save & Run All" in "\n".join(
        "".join(c["source"]) for c in notebook["cells"] if c["cell_type"] == "markdown"
    )
    remapped = module.remap_notebook(notebook, Path("/tmp/train.csv"), Path("/tmp/test.csv"), Path("/tmp/submission.csv"))
    remapped_source = "\n".join("".join(c["source"]) for c in remapped["cells"] if c["cell_type"] == "code")
    assert "/tmp/submission.csv" in remapped_source
    assert "/kaggle/input/titanic/train.csv" not in remapped_source
    assert "/kaggle/input/titanic/test.csv" not in remapped_source
    # The original notebook must stay ready to run directly on Kaggle.
    assert "/kaggle/input/titanic/train.csv" in scripts


def test_submission_validator_rejects_incorrect_order_or_labels(tmp_path):
    source = tmp_path / "test.csv"
    result = tmp_path / "submission.csv"
    pd.DataFrame({"PassengerId": [4, 5, 6]}).to_csv(source, index=False)
    pd.DataFrame({"PassengerId": [4, 5, 6], "Survived": [1, 0, 1]}).to_csv(result, index=False)
    assert module.validate_submission(result, source) == 3
    pd.DataFrame({"PassengerId": [5, 4, 6], "Survived": [1, 0, 1]}).to_csv(result, index=False)
    with pytest.raises(ValueError, match="IDs/order"):
        module.validate_submission(result, source)
    pd.DataFrame({"PassengerId": [4, 5, 6], "Survived": [1, 0, 2]}).to_csv(result, index=False)
    with pytest.raises(ValueError, match="binary"):
        module.validate_submission(result, source)


def test_remapper_rejects_incomplete_notebook():
    notebook = {"cells": [{"cell_type": "code", "source": ["print('hello')"]}]}
    with pytest.raises(ValueError, match="required input/output"):
        module.remap_notebook(notebook, Path("train.csv"), Path("test.csv"), Path("submission.csv"))
