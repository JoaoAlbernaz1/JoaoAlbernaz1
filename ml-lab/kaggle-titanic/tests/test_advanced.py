"""Offline regression tests for Titanic advanced notebook pipeline."""
import importlib.util
import sys
from pathlib import Path

import pandas as pd
import pytest

FILE = Path(__file__).resolve().parents[1] / "advanced.py"
spec = importlib.util.spec_from_file_location("titanic_advanced_experiment", FILE)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def fixture(n=20):
    rows = []
    for i in range(n * 2):
        survived = i % 2
        rows.append({
            "PassengerId": i + 1,
            "Survived": survived,
            "Pclass": 1 if survived else 3,
            "Name": "Test, " + ("Mrs. Alice" if survived else "Mr. John") + str(i),
            "Cabin": "B21" if survived else None,
            "Age": 18 + i % 30,
            "SibSp": i % 3, "Parch": i % 2,
            "Fare": 5.5 + i * 1.15,
            "Sex": "female" if survived else "male",
            "Embarked": "S" if i % 3 else "C",
        })
    return pd.DataFrame(rows)


def test_feature_engineering_is_stateless():
    frame = fixture(8)
    enriched = m.FeatureBuilder().fit_transform(frame[m.RAW])
    assert enriched.columns.tolist() == m.NUM + m.CAT
    assert enriched.loc[0, "Title"] == "Mr"
    assert enriched.loc[1, "Title"] == "Mrs"
    assert enriched.loc[0, "Deck"] == "Unknown"
    assert enriched.loc[1, "Deck"] == "B"
    assert enriched["FamilySize"].min() >= 1
    assert enriched["FarePerPerson"].notna().all()


def test_pipelines_work_without_hidden_test_labels():
    frame = fixture(9)
    for name in ("logistic", "random_forest"):
        p = m.pipeline(name).fit(frame[m.RAW], frame["Survived"])
        prediction = p.predict(frame[m.RAW].iloc[:4])
        assert len(prediction) == 4
        assert set(prediction) <= {0, 1}


def test_local_cv_and_valid_submission():
    train = fixture(8)
    test = train.drop(columns="Survived").iloc[:5].copy()
    test["PassengerId"] = list(range(100, 105))
    submission, report = m.run(train, test, folds=3)
    assert submission.columns.tolist() == ["PassengerId", "Survived"]
    assert submission.PassengerId.tolist() == list(range(100, 105))
    assert len(report["candidates"]) == 2
    assert report["selected"] == report["candidates"][0]["model"]
    assert len(report["oof_confusion_matrix"]) == 2
    assert "NOT Kaggle" in report["limitations"][0]
    assert "CV Accuracy" in m.render(report)


def test_reject_overlapping_id_and_test_labels(tmp_path):
    train = fixture(7)
    test = train.drop(columns="Survived").iloc[:3].copy()
    a, b = tmp_path / "train.csv", tmp_path / "test.csv"
    train.to_csv(a, index=False)
    test.to_csv(b, index=False)
    with pytest.raises(ValueError, match="Overlapping"):
        m.read_data(a, b)
    test["PassengerId"] = [110, 111, 112]
    test["Survived"] = [0, 1, 1]
    test.to_csv(b, index=False)
    with pytest.raises(ValueError, match="unlabeled"):
        m.read_data(a, b)


def test_reject_tiny_imbalanced_train():
    train = fixture(2)
    test = train.drop(columns="Survived")
    with pytest.raises(ValueError, match="Not enough"):
        m.run(train, test, folds=5)
