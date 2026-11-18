# Retrieval Benchmark · Avaliação de recuperação para RAG

Projeto de avaliação **sem geração por LLM**: mede se a etapa de recuperação encontra os documentos certos antes de qualquer resposta. Isso isola uma fonte importante de falhas em aplicações RAG.

## Métodos

- **BM25** implementado em Python para baseline lexical sem serviços externos;
- **TF-IDF + similaridade cosseno** com scikit-learn;
- **Embeddings multilíngues opcionais** via Sentence Transformers (com download explícito).

Para cada consulta, o conjunto de relevância anotada permite calcular **Recall@1, Recall@3, MRR@3**. Métricas são produzidas somente quando o programa roda.

```bash
cd ml-lab
python retrieval-benchmark/benchmark.py --output outputs/retrieval.json
pip install -r requirements-embeddings.txt
python retrieval-benchmark/benchmark.py --with-embeddings --output outputs/retrieval-with-embeddings.json
pytest -q
```

## Design do experimento

Os **18 documentos e 12 consultas são sintéticos, com respostas relevantes anotadas manualmente**, para testar pipeline de avaliação e não estabelecer liderança entre métodos. Corpus real, consulta de usuários e anotação humana independente são necessários para conclusões de desempenho. Embeddings exigem rede ao primeiro download e podem demorar dependendo da máquina.

**Próximo experimento proposto:** aumentar o corpus, criar consultas para sinônimos e erros de digitação, testar significância estatística e latência p95. Não há resultados numéricos declarados antecipadamente.
