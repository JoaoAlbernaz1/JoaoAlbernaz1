# Publicações e resultados · ML & Research Lab

Projetos com código reproduzível, documentação técnica, métricas e links verificáveis.

## Hugging Face

**[JOAOOALBERNAZ/intent-classifier-pt](https://huggingface.co/JOAOOALBERNAZ/intent-classifier-pt)**

Modelo supervisionado de classificação de intenção em português com TF-IDF e regressão logística. A execução automatizada validou o modelo e publicou os pesos e o cartão técnico. [Execução de referência](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44366606320).

- Macro-F1 de holdout em 60 exemplos sintéticos: **0,4933**.
- Os dados são sintéticos e o desempenho não deve ser extrapolado para ambientes reais.
- [Código-fonte](./nlp-intent-classifier/) · [Métricas](./published/intent-v1/metrics.json).

## Retrieval / RAG Benchmark

[Benchmark reproduzível](./retrieval-benchmark/) de BM25 e TF-IDF com Recall@k e MRR@k. [Resultados medidos](./published/retrieval-v1/metrics.json). Corpus sintético, usado para demonstrar avaliação.

## Kaggle Titanic

[Notebook e pipeline](./kaggle-titanic/) com validação cruzada, preprocessing seguro e baseline tabular. A submissão **foi realizada** em 18/11/2026. [Log de execução bem-sucedida](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44368002721) · ID `58521092`. A validação cruzada local obteve 84,06% (± 1,59 p.p.) de acurácia; **essa não é a nota do leaderboard**, ainda não verificada.

## Pesquisa técnica

[Artigo sobre avaliação reprodutível](./docs/avaliacao-reprodutivel-de-ml.md).

