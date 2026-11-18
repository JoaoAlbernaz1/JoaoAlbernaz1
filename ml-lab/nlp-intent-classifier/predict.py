"""Inferência local usando somente tipos confiáveis reconhecidos pelo skops."""
from __future__ import annotations

import argparse
from pathlib import Path

import skops.io as sio


def predict(model_path: Path, texts: list[str]) -> list[str]:
    untrusted = sio.get_untrusted_types(file=model_path)
    if untrusted:
        raise ValueError(f"O modelo contém tipos não aprovados: {untrusted}. Revise o arquivo antes de carregar.")
    model = sio.load(model_path, trusted=[])
    return model.predict(texts).tolist()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, type=Path)
    parser.add_argument("texts", nargs="+")
    args = parser.parse_args()
    for text, intent in zip(args.texts, predict(args.model, args.texts)):
        print(f"{intent}\t{text}")
