---
language: pt
license: cc-by-4.0
tags:
- model-calibration
- selective-prediction
- intent-classification
- reproducible-research
datasets:
- c2d-usp/banking77-pt-br
---

# BANKING77-PTBR · Confidence Evaluation

**Modelo novo**, treinado em 8002 textos (80% do treino oficial). Outros 2001 textos do treino oficial foram reservados para calibração. O teste independente tem 3080 textos.

- Acurácia no teste: **0.8870**.
- Macro-F1 no teste: **0.8869**.
- Temperatura ajustada apenas na calibração: **0.1945**.

| Avaliação no teste oficial | T=1 (softmax cru) | Temperatura calibrada |
|:--|--:|--:|
| NLL | 2.4561 | 0.4423 |
| ECE em 10 bins | 0.7844 | 0.0134 |
| Brier multiclass (soma) | 0.8248 | 0.1654 |

## Abstenção seletiva

O limiar é definido na **divisão de calibração**, nunca no teste. Um limite inferior Wilson de 90% para precisão foi usado como alvo de demonstração, não como garantia.

- Limiar: **0.4240**.
- Cobertura de calibração: **94.6%**.
- Cobertura de teste: **94.4%**.
- Acurácia apenas nas previsões aceitas no teste: **0.9192**.

A escolha de temperatura e de limiar usa o mesmo split de calibração, então esse método **não estabelece desempenho confiável em produção**. Foram identificadas 193 linhas de teste com texto idêntico a alguma linha do treino oficial.

## Artefatos e transparência

- model.skops: estimador distinto do modelo original.
- calibration.json: temperatura, ordem das classes e limiar de pesquisa.
- metrics.json: relatórios completos, cobertura, NLL, ECE, Brier, risco.
- Código reproduzível: https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/tree/main/ml-lab/confidence-evaluation

Dataset: BANKING77-PTBR, traduções do inglês revisadas por pesquisadores, CC BY 4.0 (Dimant et al., Poli/USP, 2025). Não usar para decisões financeiras reais.
