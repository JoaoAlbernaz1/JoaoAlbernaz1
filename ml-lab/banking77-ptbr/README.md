# BANKING77-PTBR · classificação de intenção com dados de pesquisa

Modelo NLP em **77 categorias de intenções bancárias em português brasileiro**, treinado sobre o conjunto público [BANKING77-PTBR](https://huggingface.co/datasets/c2d-usp/banking77-pt-br), do Centro de Ciência de Dados da Poli/USP (CC BY 4.0).

## Hipótese e protocolo

Três baselines clássicas, TF-IDF de palavras + SGD, TF-IDF de palavras + LinearSVC e TF-IDF de caracteres + LinearSVC, são comparadas por **macro-F1 em 20% estratificados do treino oficial**. O vencedor é reajustado nos 100% do treino oficial. O teste oficial independente é acessado **somente depois** da seleção do modelo.

A implementação mede macro-F1, accuracy, weighted-F1, métricas por classe, confusões comuns e repetições entre treino/teste. Os modelos são serializados com skops e publicados com um cartão gerado a partir das métricas verdadeiras da execução.

## Reproduzir

~~~bash
python -m pip install -r ml-lab/requirements.txt
python ml-lab/banking77-ptbr/train.py --output-dir outputs/banking77-ptbr
python -m pytest -q ml-lab/banking77-ptbr/tests
~~~

O download é feito diretamente do dataset público, fixado na revisão 85f51c4. Registros com texto ou rótulo ausente são excluídos do treino/teste, com contagens no relatório. Nenhum serviço de IA pago é necessário para o treino.

## Resultado inicial auditável

A execução [GitHub Actions #44371491356](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44371491356) terminou com sucesso e publicou o [modelo no Hugging Face](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1). No teste oficial: **accuracy 0,8964, macro-F1 0,8964, weighted-F1 0,8964**. Melhor baseline: **char TF-IDF + LinearSVC**; três alternativas foram comparadas somente no treino. A auditoria inicial identificou **166 textos distintos compartilhados entre treino e teste**, limitação relevante para interpretação do score. A execução posterior incluiu uma métrica de sensibilidade excluindo essas correspondências, sem selecionar novamente o modelo.

## Auditoria de resultados

[Resultado detalhado, comparações e auditoria de sobreposição entre treino e teste](../docs/banking77-ptbr-results.md). O teste oficial apresentou macro-F1 de **0,8964**; excluindo os **193 registros de teste com texto idêntico a algum texto do treino** (casefold), o macro-F1 foi **0,8910** em 2.887 exemplos. Essa comparação é pós-hoc e não foi utilizada para escolher modelos.

## Limitações

Este corpus é **tradução para português, revisada por pesquisadores**, não conversas de clientes brasileiros originalmente escritas em português. O benchmark não garante qualidade em produção, generalização para outras empresas ou robustez contra ataques.

**Créditos:** Dimant et al. (2025), BANKING77-PTBR (Poli/USP); Casanueva et al. (2020), BANKING77 original.
