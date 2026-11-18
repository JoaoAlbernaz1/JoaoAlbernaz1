# AI Evaluation Lab · resultados reproduzidos

Comparação de dois métodos de recuperação com a MESMA baseline extrativa offline.
São **32 casos e 16 documentos ficcionais**, não um benchmark de LLM em produção.

| Métrica | Word TF-IDF | Char TF-IDF |
|:--|--:|--:|
| Retrieval Hit@3 | 0.840 | 1.000 |
| Retrieval MRR@3 | 0.760 | 0.973 |
| Answer substring accuracy | 0.360 | 0.360 |
| Abstention accuracy | 1.000 | 1.000 |
| Lexical support rate | 1.000 | 1.000 |
| Attack marker leak rate | 0.000 | 0.000 |

Latência por caso disponível nos arquivos JSON; os tempos dependem da máquina de CI.

- [Resultados word](./word.json)
- [Resultados char](./char.json)
- [Código, dados, testes e limitações](../../ai-evaluation-lab/)

A precisão é medida por correspondência lexical; não é um juiz semântico.
O teste adversarial com marcas fictícias não demonstra segurança geral.
