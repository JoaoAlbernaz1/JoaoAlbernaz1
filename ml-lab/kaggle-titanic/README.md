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

**Status real:** notebook e pipeline criados; nenhuma submissão, leaderboard ou colocação está sendo reivindicada. Só adicionar o link de seu perfil Kaggle após uma submissão de verdade.

## Próximos experimentos

Comparar logistic regression, gradient boosting, calibração de probabilidade e engenharia de atributos com a mesma estratégia de validação. Não otimizar repetidamente contra uma amostra de teste pública.
