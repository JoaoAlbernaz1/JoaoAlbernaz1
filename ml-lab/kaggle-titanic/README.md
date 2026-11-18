# Kaggle Titanic · baseline reprodutível

Projeto estruturado para a competição de entrada [Titanic — Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic).

O foco é **evitar vazamento de dados**: imputação, codificação categórica e modelo ficam dentro de um mesmo `Pipeline`. A validação cruzada estratificada aprende transformações separadamente em cada fold. `test.csv` só é usado depois da escolha da baseline, para exportar `submission.csv`.

## Executar

1. Entre na competição, aceite os termos e baixe `train.csv` e `test.csv`.
2. A partir de `ml-lab/`:

```bash
pip install -r requirements.txt
python kaggle-titanic/train.py --train /caminho/train.csv --test /caminho/test.csv --output outputs/titanic/submission.csv
```

O script apresenta médias e desvios-padrão do accuracy e produz colunas `PassengerId`, `Survived`. Também existe um [notebook para Kaggle](./titanic_baseline.ipynb) independente do script.

**Status real:** submissão para o Titanic enviada com sucesso em 18/11/2026, referência `58521092`. [Registro de execução](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44368002721). Validação local em 5 folds: **accuracy 0,8406 ± 0,0159**. Ainda não foi verificada nota oficial do leaderboard ou qualquer colocação.

## Engenharia de atributos · novo experimento concluído

[Notebook Kaggle-ready](./titanic_feature_engineering.ipynb) · [Código e protocolo](./ADVANCED.md) · [resultados públicos](../published/kaggle-titanic-advanced/) · [CI](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44406328882)

Comparação nos 891 passageiros do treino oficial, com 5 folds estratificados: **Random Forest 84,17% de accuracy CV (ROC-AUC 0,8825)** versus **regressão logística 82,49% (ROC-AUC 0,8712)**. A melhora sobre a baseline anterior de 84,06% é de aproximadamente 0,11 ponto percentual e não estabelece ganho estatisticamente significativo. As métricas são locais; o score oficial da competição continua não verificado.

O notebook foi preparado para publicação no Kaggle, mas a API retornou **403 Forbidden** em `SaveKernel`; ainda não foi publicado. Veja [status e procedimento de publicação](./KAGGLE_PUBLISHING.md).

## Próximos experimentos

Comparar logistic regression, gradient boosting, calibração de probabilidade e engenharia de atributos com a mesma estratégia de validação. Não otimizar repetidamente contra uma amostra de teste pública.

## Saída da versão Kaggle e CSV para submissão

**Ambos os notebooks** agora escrevem explicitamente `/kaggle/working/submission.csv`, com `PassengerId` e `Survived`. Na plataforma Kaggle, selecione **Save Version → Save & Run All**, aguarde concluir e selecione a versão que contenha o arquivo em **Output**. O modo **Quick Save** não executa todas as células e pode gerar o erro de versão sem arquivo de saída.

Caso a publicação do notebook ainda seja bloqueada pelo erro 403, o [GitHub Actions de pesquisa](../../.github/workflows/kaggle-titanic-research.yml) executa o notebook completo com os dados oficiais e disponibiliza `submission.csv` no artefato **titanic-notebook-output**, para download e envio manual na aba **Submit Predictions**. Este fluxo não gasta submissões nem simula nota no leaderboard.
