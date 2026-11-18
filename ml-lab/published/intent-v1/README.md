# Intent Classifier PT · v1

Treinado automaticamente no GitHub Actions com TF-IDF e regressão logística.

**DADOS SINTÉTICOS:** 60 mensagens inventadas para demonstrar o pipeline; os resultados não estimam desempenho no mundo real.

- Macro-F1 holdout (sintético): **0.4933**
- Acurácia holdout (sintética): **0.5333**
- Macro-F1 CV treino (sintético): **0.4178**
- Seed: 42
- Modelo: `model.skops`; demais métricas: `metrics.json`

[Fonte e limitações](../../nlp-intent-classifier/) · [Protocolo de avaliação](../../docs/avaliacao-reprodutivel-de-ml.md).
