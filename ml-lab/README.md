# ML & Research Lab

**Machine Learning aplicado, experimentos reproduzíveis e engenharia de avaliação.**

Este laboratório reúne implementações educacionais e protocolos de pesquisa. Cada projeto diferencia **código disponível** de **resultados efetivamente medidos**, **modelos publicados** e **submissões realizadas**. Nada aqui afirma pontuações ou publicações não verificadas.

| Projeto | Questão investigada | Evidência disponível | Situação |
|:--|:--|:--|:--|
| [NLP · classificação de intenção](./nlp-intent-classifier/) | Um classificador TF-IDF + regressão logística reconhece intenções de mensagens em português? | Código, dados sintéticos declarados, testes, validação estratificada, exportação segura | **Treinado e publicado no Hugging Face** · avaliação sintética |
| [Retrieval / RAG benchmark](./retrieval-benchmark/) | BM25 ou TF-IDF recupera melhor o contexto relevante? | Corpus sintético, relevância anotada, Recall@k e MRR@k, testes | Implementação disponível · executar benchmark |
| [Kaggle Titanic](./kaggle-titanic/) | Como criar uma baseline tabular sem vazamento de dados? | Pipeline, cross-validation, notebook e geração de submission.csv | Preparado para submissão · não é participação comprovada |
| [Artigo técnico](./docs/avaliacao-reprodutivel-de-ml.md) | O que constitui um experimento confiável de ML? | Texto metodológico publicado neste repositório | Disponível |

## Artefatos treinados e métricas publicadas no GitHub

A execução automática de treinamento foi concluída e gerou um [modelo scikit-learn serializado](./published/intent-v1/model.skops), [cartão técnico](./published/intent-v1/README.md), [métricas do classificador](./published/intent-v1/metrics.json) e [métricas de recuperação](./published/retrieval-v1/metrics.json). **Os dados são sintéticos e os resultados não representam desempenho real em produção.**

**Publicação no Hugging Face confirmada pelo workflow:** [JOAOOALBERNAZ/intent-classifier-pt](https://huggingface.co/JOAOOALBERNAZ/intent-classifier-pt). A submissão ao Kaggle ainda não foi executada. Veja o [procedimento de publicação](./PUBLISHING.md).

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

### Publicação posterior

- **Hugging Face:** o projeto NLP inclui `publish_hf.py`, documentação de limitações e cartão de modelo gerado junto aos pesos. Publicado em [JOAOOALBERNAZ/intent-classifier-pt](https://huggingface.co/JOAOOALBERNAZ/intent-classifier-pt), com registro no [GitHub Actions](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44366606320).
- **Kaggle:** o projeto Titanic usa os arquivos disponibilizados após aceitar os termos da [competição Titanic](https://www.kaggle.com/competitions/titanic). A execução gera `submission.csv`; submeter e obter score são etapas separadas.
- **Pesquisa:** resultados devem ser acrescentados com comando exato, data, versão, seed, tamanho de dataset e limitações. Não interprete a qualidade sobre dados sintéticos como desempenho em produção.

## Critérios de qualidade

1. Baselines transparentes antes de modelos complexos.
2. Separação de treino e teste e validação cruzada no treino.
3. Métricas alinhadas ao problema (macro-F1; Recall@k; MRR@k).
4. Sem expor dados sensíveis, credenciais ou métricas inventadas.
5. Código testável em CI (GitHub Actions).

**Autor:** João Victor Albernaz · Engenharia de Software · IA aplicada.
