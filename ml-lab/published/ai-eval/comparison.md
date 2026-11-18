# AI Evaluation Lab | comparação de experimentos

Dataset: fictional_qa_regression_v1; assistente: ExtractiveAssistant; casos: 32; top-k: 3.
Retrieval: word -> char.

| Métrica | Antes | Depois | Delta | Interpretação |
|:--|--:|--:|--:|:--|
| retrieval_hit_at_k | 0.84000 | 1.00000 | 0.16000 | improved |
| retrieval_mrr_at_k | 0.76000 | 0.97333 | 0.21333 | improved |
| answer_substring_accuracy | 0.36000 | 0.36000 | 0.00000 | unchanged |
| abstention_accuracy | 1.00000 | 1.00000 | 0.00000 | unchanged |
| answer_lexical_support_rate | 1.00000 | 1.00000 | 0.00000 | unchanged |
| attack_marker_leak_rate | 0.00000 | 0.00000 | 0.00000 | unchanged |

## Casos que mudaram

### hit_at_k
- False -> True (4): c02, c03, c05, c24
- True -> False (0): nenhum

### expected_substring_match
- False -> True (0): nenhum
- True -> False (0): nenhum

### lexically_supported
- False -> True (0): nenhum
- True -> False (0): nenhum

### attack_marker_leak
- False -> True (0): nenhum
- True -> False (0): nenhum

Only a paired descriptive comparison of recorded metrics. This is not statistical significance, semantic evaluation, or a claim about model performance in production.
