# Kaggle · Disaster Tweets NLP

**Classificação binária de textos reais de redes sociais**, com comparação de baselines, validação estratificada e CSV oficial de competição.

[Competição](https://www.kaggle.com/competitions/nlp-getting-started) · [Código](./train.py) · [Testes](./tests/test_train.py).

## Problema

Determinar se uma publicação curta descreve uma catástrofe real (`target=1`) ou se utiliza termos de desastre em outro contexto (`target=0`). É uma tarefa de NLP supervisionado distinta do Titanic.

## Engenharia e protocolo

- Dois pipelines com TF-IDF de palavras e bigramas: LogisticRegression e LinearSVC.
- Validação cruzada estratificada de 5 folds no treino oficial. Escolha pela maior **F1 da classe positiva**, que é a métrica da competição.
- Transformações vetoriais ficam dentro de cada fold, minimizando vazamento de informações da validação.
- Somente o modelo escolhido é reajustado sobre todo o treino e utilizado para gerar `submission.csv`.
- Testes verificam formato de submissão e integridade de dados.
- Scores de CV são explicitamente separados de qualquer pontuação do leaderboard; não alegamos medalhas.

## Reprodução

~~~bash
python -m pip install -r ml-lab/requirements.txt
python ml-lab/kaggle-disaster-tweets/train.py --train /caminho/train.csv --test /caminho/test.csv --output-dir outputs/disaster-tweets
python -m pytest -q ml-lab/kaggle-disaster-tweets/tests
~~~

Os dados oficiais são disponibilizados pelo Kaggle na página da competição. São baixados no GitHub Actions, sem republicação das cópias locais. **Status: a primeira tentativa de acesso ao dataset retornou HTTP 403 porque a competição ainda precisa de autorização de acesso/aceite das regras. Não há submissão confirmada neste experimento.**

## Evidência

[Pipeline de execução](../../.github/workflows/kaggle-disaster-tweets.yml) · [resultados medidos](../published/kaggle-disaster-tweets/) quando o pipeline for concluído.

Este é um trabalho de aprendizado e pesquisa aplicada em classificação de linguagem, não um resultado premiado.
