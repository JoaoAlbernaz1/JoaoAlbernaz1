# Titanic · Feature Engineering

Experimento reproduzível com dados oficiais da competição. Métricas **locais de validação**, não leaderboard.

| Modelo | CV Accuracy | CV ROC-AUC |
|:--|--:|--:|
| random_forest | 0.8417 ± 0.0057 | 0.8825 ± 0.0196 |
| logistic | 0.8249 ± 0.0159 | 0.8712 ± 0.0226 |

**Modelo selecionado:** random_forest.

A matriz de confusão OOF está no JSON, mas reusa os folds da seleção.
A imputação, a normalização e o encoding são ajustados dentro de cada fold.
Nenhuma submissão adicional é feita automaticamente.

[Código e metodologia](../../kaggle-titanic/) · [Métricas completas](./metrics.json).
