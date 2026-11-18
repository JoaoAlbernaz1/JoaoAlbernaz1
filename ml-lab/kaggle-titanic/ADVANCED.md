# Kaggle Titanic · pesquisa avançada em engenharia de atributos

Este experimento estende a [baseline inicial](./README.md) com uma comparação entre **regressão logística e Random Forest**, usando **dados oficiais da competição** e validação cruzada estratificada.

## Questão de pesquisa

A engenharia de atributos por passageiro — título, deck da cabine, tamanho da família, indicador de viagem sozinho e preço por pessoa — melhora a capacidade de classificação dos modelos? Como comparar isso sem usar os rótulos ocultos da competição?

## Implementação e validação

- [`advanced.py`](./advanced.py): pipeline reprodutível com transformação dos dados, imputação, escala, codificação categórica e seleção de dois candidatos por acurácia média de 5 folds.
- [`titanic_feature_engineering.ipynb`](./titanic_feature_engineering.ipynb): notebook independente e visual, preparado para o ambiente Kaggle, incluindo gráfico comparativo e geração do CSV de submissão.
- [Testes offline](./tests/test_advanced.py): verificam features, schema, execução de CV e separação de dados.
- [Workflow de pesquisa](../../.github/workflows/kaggle-titanic-research.yml): valida o pull request e, no branch principal, calcula **métricas reais com os dados autorizados da competição**, publicando JSON e relatório sem criar submissões repetidas.

O conjunto `test.csv` da competição permanece sem rótulos. Métricas de accuracy e ROC-AUC são **validações locais**, não scores oficiais do Kaggle.

## Executar localmente

```bash
python -m pip install -r ml-lab/requirements.txt
python -m pytest -q ml-lab/kaggle-titanic/tests
python ml-lab/kaggle-titanic/advanced.py \
  --train /caminho/train.csv \
  --test /caminho/test.csv \
  --output-dir outputs/titanic-advanced
```

O script gera `submission_advanced.csv`, `metrics.json` e um relatório `README.md` com valores medidos.

## Limitações e próximos passos

A escolha do modelo e os diagnósticos OOF compartilham os mesmos folds, de modo que a avaliação do vencedor pode ser otimista. Parentes e grupos com informações relacionadas também podem aparecer em folds diferentes. Um experimento futuro deve reservar uma partição independente para estimar qualidade pós-seleção.

A **submissão oficial já confirmada** no Titanic continua sendo a da baseline anterior: [registro #58521092](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44368002721). Não declarar nota oficial ou medalha inexistente. Para publicar este notebook no Kaggle, a conta deve estar autorizada na competição.

## Saída da versão Kaggle e CSV para submissão

**Ambos os notebooks** agora escrevem explicitamente `/kaggle/working/submission.csv`, com `PassengerId` e `Survived`. Na plataforma Kaggle, selecione **Save Version → Save & Run All**, aguarde concluir e selecione a versão que contenha o arquivo em **Output**. O modo **Quick Save** não executa todas as células e pode gerar o erro de versão sem arquivo de saída.

Caso a publicação do notebook ainda seja bloqueada pelo erro 403, o [GitHub Actions de pesquisa](../../.github/workflows/kaggle-titanic-research.yml) executa o notebook completo com os dados oficiais e disponibiliza `submission.csv` no artefato **titanic-notebook-output**, para download e envio manual na aba **Submit Predictions**. Este fluxo não gasta submissões nem simula nota no leaderboard.
