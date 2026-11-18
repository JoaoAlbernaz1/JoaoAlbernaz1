# BANKING77-PTBR · Robustness & Metamorphic Tests

Modelo publicado avaliado em **3080 mensagens do teste oficial** do dataset de pesquisa BANKING77-PTBR.

**Baseline sem alterações:** accuracy **0.8964** · macro-F1 **0.8964**.

| Perturbação | Macro-F1 | Variação F1 | Troca de previsão | Textos alterados |
|:--|--:|--:|--:|--:|
| Remover acentos | 0.8964 | +0.0000 | 0.0% | 84.5% |
| Caixa alta + espaços | 0.8964 | +0.0000 | 0.0% | 100.0% |
| Transposição de letras | 0.8502 | -0.0462 | 9.4% | 99.9% |

## O que esse experimento mostra

As transformações são determinísticas. Remoção de acentos e caixa alta/espaçamento testam invariâncias esperadas da vetorização TF-IDF. A troca de duas letras testa sensibilidade a um erro de digitação simulado e **pode alterar o sentido da frase**.

O estudo é uma avaliação pontual, não uma garantia de robustez adversarial. Não são usados dados de usuários reais nem rótulos ocultos do Kaggle.

- [Métricas completas](./robustness.json)
- [Código das transformações](../../model-ops/robustness.py)
- [Modelo publicado](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1)
