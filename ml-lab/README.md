# ML & Research Lab

**Machine Learning aplicado, experimentos reproduzíveis e engenharia de avaliação.**

Implementações práticas, experimentos reproduzíveis e evidências verificáveis. As métricas de datasets sintéticos são identificadas como tal e não representam desempenho em produção.

| Projeto | Questão investigada | Evidência disponível | Situação |
|:--|:--|:--|:--|
| [BANKING77-PTBR · dados públicos revisados](./banking77-ptbr/) | Qual baseline de NLP funciona melhor para 77 intenções financeiras em português? | 3 baselines, seleção por macro-F1 em treino, teste oficial, auditoria de duplicatas | **Modelo publicado no Hugging Face** · macro-F1 0,8964 no teste |
| [Confidence Evaluation · calibração e abstenção](./confidence-evaluation/) | A confiança de um classificador de 77 classes é útil para selecionar quais previsões aceitar? | Temperatura ajustada em holdout do treino, NLL, ECE, Brier e risco-cobertura | **Modelo publicado no Hugging Face** · [ECE 0,0134 e cobertura 94,42%](./published/confidence-evaluation/) no teste |
| [ModelOps · serving e drift](./model-ops/) | Como servir e monitorar tecnicamente um classificador publicado? | API FastAPI, contêiner, testes de contrato e [arquitetura](./docs/modelops-architecture-decisions.md) | **CI concluído** · [mudança de distribuição em corpus público](./published/model-ops/) e [robustez textual medida](./published/model-ops/ROBUSTNESS.md) |
| [AI Evaluation Lab](./ai-evaluation-lab/) | Recuperação correta implica resposta correta? | 32 testes, dois retrievers e [métricas reproduzidas](./published/ai-eval/) | **Benchmark e CI concluídos** · 100% Hit@3 com char TF-IDF, mas só 36% acerto lexical na resposta |
| [NLP · classificação de intenção](./nlp-intent-classifier/) | Um classificador TF-IDF + regressão logística reconhece intenções de mensagens em português? | Código, dados sintéticos declarados, testes, validação estratificada, exportação segura | **Treinado e publicado no Hugging Face** · avaliação sintética |
| [Retrieval / RAG benchmark](./retrieval-benchmark/) | BM25 ou TF-IDF recupera melhor o contexto relevante? | Corpus sintético, relevância anotada, Recall@k e MRR@k, testes | Implementação disponível · executar benchmark |
| [Kaggle Titanic](./kaggle-titanic/) | Como criar uma baseline tabular sem vazamento de dados? | Pipeline, cross-validation, notebook e geração de submission.csv | **Submissão enviada** (ref. 58521092) · resultado oficial não verificado |
| [Artigo técnico](./docs/avaliacao-reprodutivel-de-ml.md) | O que constitui um experimento confiável de ML? | Texto metodológico publicado neste repositório | Disponível |

## Calibração e avaliação de risco

- [Confidence Evaluation](./confidence-evaluation/) — [modelo treinado e publicado](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-confidence-v1) com treinamento, calibração e teste separados. Redução do ECE de **0,7844 para 0,0134** e precisão de **91,92% nas previsões aceitas**, cobrindo **94,42%** do teste. Essa política não é garantia fora da amostra; [análise crítica](./docs/confidence-and-selective-prediction.md).

## Engenharia de inferência e observabilidade

- [ModelOps: FastAPI, Docker e monitoramento de drift](./model-ops/) — implementação de serving do classificador de 77 classes, contêiner validado e [diagnóstico de distribuição publicado](./published/model-ops/). A [avaliação de robustez com erros de digitação artificiais](./published/model-ops/ROBUSTNESS.md) mediu uma queda de macro-F1 de **0,8964 para 0,8502** no teste oficial. [Decisões arquiteturais](./docs/modelops-architecture-decisions.md). Não é um serviço de produção.
- [Hugging Face · relatório de confiabilidade do modelo](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1/tree/main/evaluation/modelops) — métricas e relatórios completos de drift e robustez publicados junto ao modelo treinado.

## Pesquisa e experimentos com resultados medidos

- [Classificação de intenções com dados públicos: modelo BANKING77-PTBR no Hugging Face](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1) — [dashboard visual gratuito de pesquisa](https://huggingface.co/spaces/JOAOOALBERNAZ/banking77-ptbr-research) · avaliação oficial, 77 classes e macro-F1 **0,8964**. O dataset contém traduções revisadas; foram identificados **166 textos distintos repetidos entre treino e teste**, possível fonte de otimismo das métricas.
- [AI Evaluation Lab](./ai-evaluation-lab/) — [relatório comparativo real](./published/ai-eval/): o retriever por caracteres obteve Hit@3 **1,0** em 25 perguntas respondíveis, enquanto o extrator apresentou acerto lexical de apenas **0,36**. É uma regressão em dados fictícios, não teste de LLM.
- [Relatório de pesquisa: BANKING77-PTBR e auditoria de sobreposição](./docs/banking77-ptbr-results.md) — no teste sem coincidências textuais: **macro-F1 0,8910 em 2.887 registros** (193 excluídos).
- [Nota técnica: avaliação de NLP e sistemas com recuperação](./docs/experimental-note-nlp-rag-2026.md).

## Artefatos treinados e métricas publicadas no GitHub

A execução automática de treinamento foi concluída e gerou um [modelo scikit-learn serializado](./published/intent-v1/model.skops), [cartão técnico](./published/intent-v1/README.md), [métricas do classificador](./published/intent-v1/metrics.json) e [métricas de recuperação](./published/retrieval-v1/metrics.json). **Os dados são sintéticos e os resultados não representam desempenho real em produção.**

**Hugging Face:** [JOAOOALBERNAZ/intent-classifier-pt](https://huggingface.co/JOAOOALBERNAZ/intent-classifier-pt). **Kaggle:** [submissão Titanic confirmada](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44368002721) (ref. 58521092), com acurácia local em 5 folds de **84,06% ± 1,59 p.p.**. Esse valor não corresponde ao score da competição.

## Como executar

Requisitos: Python 3.11+ (preferencialmente ambiente virtual).

```bash
cd ml-lab
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
pytest -q
python nlp-intent-classifier/train.py --output-dir outputs/intent
python retrieval-benchmark/benchmark.py --output outputs/retrieval.json
```

O treinamento salva artefatos em `outputs/` (ignorado pelo Git), sem resultados fabricados ou dados privados. O benchmark aceita `--with-embeddings` após instalar `requirements-embeddings.txt`, exigindo download de modelo externo na primeira execução.

### Trabalhos e resultados

- **Hugging Face:** [modelo NLP publicado](https://huggingface.co/JOAOOALBERNAZ/intent-classifier-pt), acompanhado de um model card e métricas documentadas.
- **Kaggle:** [Titanic](https://www.kaggle.com/competitions/titanic) — [submissão comprovada](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44368002721), ref. `58521092`; score do leaderboard ainda não verificado.
- **Pesquisa:** resultados devem ser acrescentados com comando exato, data, versão, seed, tamanho de dataset e limitações. Não interprete a qualidade sobre dados sintéticos como desempenho em produção.

## Critérios de qualidade

1. Baselines transparentes antes de modelos complexos.
2. Separação de treino e teste e validação cruzada no treino.
3. Métricas alinhadas ao problema (macro-F1; Recall@k; MRR@k).
4. Sem expor dados sensíveis, credenciais ou métricas inventadas.
5. Código testável em CI (GitHub Actions).

**Autor:** João Victor Albernaz · Engenharia de Software · IA aplicada.
