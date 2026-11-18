"""Small no-network training tests."""
import importlib.util
import sys
from pathlib import Path
import pandas as pd
import pytest

P = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("banking77_ptbr_script", P / "train.py")
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def dataset(n=15):
    a = ["Meu cartão está perdido " + str(i) for i in range(n)]
    b = ["Qual é a taxa de câmbio " + str(i) for i in range(n)]
    c = ["Transferência ainda não chegou " + str(i) for i in range(n)]
    return pd.DataFrame({"frase": a+b+c, "rotulo": ["cartao"]*n + ["cambio"]*n + ["transferencia"]*n})


def test_csv_validation(tmp_path):
    f = tmp_path / "sample.csv"
    data = dataset()
    data.to_csv(f, index=False)
    assert len(m.load_csv(f)) == len(data)
    data.loc[0, "frase"] = None
    data.to_csv(f, index=False)
    cleaned = m.load_csv(f)
    assert len(cleaned) == len(data) - 1
    assert cleaned.attrs["excluded_incomplete_rows"] == 1


def test_model_choice_and_test_separation():
    model, result = m.experiment(dataset(), dataset(6))
    assert len(result["validation"]) == 3
    assert result["selected"] == result["validation"][0]["model"]
    assert 0 <= result["test"]["macro_f1"] <= 1
    assert "CC BY 4.0" in m.model_card(result)
    assert model is not None


def test_unseen_category():
    wrong = pd.DataFrame({"frase": ["qualquer coisa"], "rotulo": ["unknown"]})
    with pytest.raises(ValueError):
        m.experiment(dataset(), wrong)
