# Publicação do notebook Titanic no Kaggle

Este repositório contém um [notebook independente](./titanic_feature_engineering.ipynb) que compara regressão logística e Random Forest com engenharia de atributos e validação cruzada estratificada. O notebook usa os arquivos oficiais da competição Titanic.

## Como será publicado

O workflow [`Publish Kaggle Titanic notebook`](../../.github/workflows/publish-titanic-notebook.yml) prepara os metadados a partir da conta autenticada no Kaggle e envia o notebook como **público** com a fonte de dados oficial `titanic`. Não faz submissão adicional nem instala segredos dentro do notebook.

**A publicação só estará confirmada quando a execução do workflow informar sucesso e um link para o notebook Kaggle.** Um commit no GitHub, isoladamente, não significa que o Kaggle aceitou a publicação.

## Estado real da publicação — 18/11/2026

A execução [GitHub Actions #44406328823](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44406328823) confirmou a conta **joaoalbernaz** ao executar `kaggle kernels init`, mas o envio `kaggle kernels push` falhou com **HTTP 403 Forbidden** em `SaveKernel`. **O notebook ainda não foi criado no Kaggle.** Isso pode decorrer das permissões do token/conta ou de restrições de acesso; os logs não confirmam a causa específica.

O workflow foi deixado para **execução manual**, sem tentativas automáticas repetidas. Após conferir as permissões de publicação de notebooks nas configurações do Kaggle, é possível executá-lo novamente em GitHub Actions. Como alternativa, abra o notebook `titanic_feature_engineering.ipynb` na interface do Kaggle, vincule a competição Titanic e salve uma versão pública. Não compartilhe os tokens.

## Evidência esperada

- Script e notebook são versionados publicamente e validados no CI.
- O Kaggle executa o notebook em seu ambiente. O workflow comprova o upload, não garante que a execução remota passou; se necessário, consultar o histórico no Kaggle.
- Scores dentro do notebook são de **validação local**. O score do leaderboard requer submissão e avaliação independentes.

## Teste independente

```bash
python -m pip install -r ml-lab/requirements.txt
python -m pytest -q ml-lab/kaggle-titanic/tests
```

O estudo complementa a [submissão Titanic anterior #58521092](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44368002721), sem declarar ranking ou pontuação oficial que ainda não foi verificada.
