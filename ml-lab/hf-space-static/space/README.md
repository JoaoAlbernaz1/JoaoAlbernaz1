---
title: BANKING77 PTBR · Research Dashboard
emoji: 📊
colorFrom: gray
colorTo: gray
sdk: static
app_file: index.html
license: cc-by-4.0
short_description: Pesquisa NLP com métricas auditadas.
---

# BANKING77-PTBR · relatório visual de pesquisa

Este é um **Space estático gratuito**, que explica um experimento real de classificação de 77 intenções usando dados de pesquisa revisados e reproduzíveis. Oferece uma comparação interativa de modelos, resultados de teste e uma auditoria de sobreposição de treino/teste.

**Segundo experimento incluído:** [Confidence Evaluation](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-confidence-v1) apresenta calibração com temperatura e análise de risco-cobertura usando outro modelo treinado separadamente. Valores verificados no teste oficial: ECE 0,7844 → 0,0134, cobertura 94,42% e acurácia de 91,92% entre previsões aceitas. Nenhuma dessas taxas garante desempenho em produção.

**Não executa inferência:** para acessar o pipeline de classificação real, veja o [modelo público](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1) e o [código reproduzível](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/tree/main/ml-lab/banking77-ptbr).

**Resultados medidos:** accuracy 0,8964 no teste oficial (3.080 registros), macro-F1 0,8910 no subconjunto sem linhas textualmente repetidas com o treino (2.887 registros). Os registros foram traduzidos e revisados por pesquisadores; não são mensagens privadas originais de clientes.

Dataset e créditos: [BANKING77-PTBR (Poli/USP, CC BY 4.0)](https://huggingface.co/datasets/c2d-usp/banking77-pt-br).
