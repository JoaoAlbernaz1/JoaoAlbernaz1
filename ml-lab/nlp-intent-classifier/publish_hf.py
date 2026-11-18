"""Publicação opt-in do artefato treinado; exige credenciais do proprietário."""
from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

from huggingface_hub import HfApi


def model_card(repo_id: str, metrics: dict) -> str:
    score = metrics["holdout"]["macro_f1"]
    return f"""---
language:
- pt
tags:
- text-classification
- scikit-learn
- educational
license: mit
---

# {repo_id.split("/")[-1]}

Baseline de classificação de intenção de tickets em português usando TF-IDF e regressão logística.

## Dataset e avaliação

- Dados: **60 textos sintéticos criados para fins didáticos**; não representam usuários reais.
- Separação holdout estratificada (25%); validação cruzada de 3 folds no treino.
- Seed: 42
- Macro-F1 no holdout sintético desta execução: **{score:.4f}**
- Relatório completo no arquivo `metrics.json`.

**AVISO:** Este valor mede somente um conjunto artificial pequeno e não comprova desempenho em produção ou generalização para outros domínios.

## Uso

Modelo exportado em `model.skops`. Execute com Python, scikit-learn e skops; verifique tipos e origem do arquivo antes de carregar.

## Limitações

Idioma e cobertura limitados, dados sintéticos, ausência de avaliação humana, sem estimativa de justiça ou robustez. Não utilizar como ferramenta decisória sensível.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-dir", required=True, type=Path)
    parser.add_argument("--repo-id", required=True, help="username/model-name")
    parser.add_argument("--private", action="store_true")
    args = parser.parse_args()
    if not os.getenv("HF_TOKEN"):
        raise SystemExit("Configure HF_TOKEN no ambiente; não coloque tokens no código.")
    if "/" not in args.repo_id:
        raise SystemExit("Use --repo-id usuario/nome-do-modelo")
    required = ["model.skops", "metrics.json"]
    for name in required:
        if not (args.artifact_dir / name).is_file():
            raise SystemExit(f"Arquivo ausente: {args.artifact_dir / name}. Treine antes de publicar.")
    metrics = json.loads((args.artifact_dir / "metrics.json").read_text(encoding="utf-8"))
    with TemporaryDirectory() as temp_dir:
        folder = Path(temp_dir)
        for name in required:
            shutil.copy2(args.artifact_dir / name, folder / name)
        (folder / "README.md").write_text(model_card(args.repo_id, metrics), encoding="utf-8")
        client = HfApi(token=os.environ["HF_TOKEN"])
        client.create_repo(repo_id=args.repo_id, repo_type="model", private=args.private, exist_ok=True)
        client.upload_folder(repo_id=args.repo_id, repo_type="model", folder_path=str(folder))
    print(f"Publicado em https://huggingface.co/{args.repo_id}")


if __name__ == "__main__":
    main()
