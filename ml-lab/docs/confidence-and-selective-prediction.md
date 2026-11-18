# A confiança de um modelo é confiável? Calibração e classificação seletiva

**Estudo reproduzível | 18/11/2026 | João Victor Albernaz**

## Pergunta técnica

Quando um modelo de classificação atribui uma categoria a uma mensagem, a força de seu score equivale à chance real de ele estar correto? E como medir o custo de deixar o modelo responder automaticamente, em vez de encaminhar casos incertos para revisão?

O [Confidence Evaluation](../confidence-evaluation/) foi criado para investigar as duas perguntas com um classificador de **77 intenções financeiras em português brasileiro**, usando o corpus público BANKING77-PTBR (Poli/USP, CC BY 4.0). O dataset contém traduções do inglês revisadas por pesquisadores e não corresponde a mensagens originalmente escritas por clientes brasileiros.

## Experimento e prevenção de vazamento

O modelo é uma **nova instância de TF-IDF por caracteres (n-gramas 3 a 5) + LinearSVC**, treinada em 8.002 linhas de 10.003 registros do treino oficial (80%). As 2.001 linhas restantes do mesmo treino são reservadas para calibrar a temperatura e escolher uma regra de abstenção. Os 3.080 exemplos do teste oficial permanecem fora dessas escolhas.

O modelo anterior do portfólio usa **todo o treino oficial**, portanto a redução de acurácia do novo experimento não prova que a calibração piora a classificação. Os modelos foram treinados em tamanhos de dados diferentes.

As margens produzidas por uma SVM linear **não são probabilidades**. O experimento converte os vetores de margens em distribuições via softmax com temperatura positiva. Um otimizador ajusta a temperatura **apenas na divisão de calibração**, minimizando negative log-likelihood (NLL). A temperatura final foi **0,1945**.

## Avaliação independente no teste oficial

| Métrica | Softmax direto, T=1 | Softmax calibrado, T=0,1945 |
|:--|--:|--:|
| Negative log-likelihood | 2,4561 | **0,4423** |
| Expected calibration error (10 bins) | 0,7844 | **0,0134** |
| Brier multiclass, soma sobre classes | 0,8248 | **0,1654** |

**Acurácia do novo modelo:** 0,8870. **Macro-F1:** 0,8869. Escalar as margens por uma temperatura positiva não muda a classe com maior score; o experimento mede principalmente a qualidade dos scores associados a essas classes.

O ECE depende de como as probabilidades são agrupadas em faixas, e um ECE baixo não garante acurácia, robustez ou boa calibração em subgrupos específicos.

## Política de abstenção e risk–coverage

A calibração usa o maior score probabilístico por mensagem como confiança estimada. Uma política ilustrativa seleciona o menor limiar que mantém, **na própria divisão de calibração**, um limite inferior de Wilson de pelo menos 90% para a proporção de acertos dos exemplos aceitos, respeitando um número mínimo de amostras.

**Limiar selecionado na calibração:** 0,4240.

No teste oficial independente, esse limiar aceitou **2.908 dos 3.080 exemplos**: cobertura **94,42%**, acurácia entre os aceitos **91,92%** e risco de erro **8,08%**. Os restantes **172 exemplos foram rejeitados** para encaminhamento hipotético à revisão humana. Não houve seleção de limiar usando resultados do teste.

| Parcela de exemplos com maior confiança, apenas para diagnóstico | Acurácia nas previsões aceitas |
|:--|--:|
| 25% | 99,74% |
| 50% | 99,55% |
| 75% | 97,75% |
| 100% | 88,70% |

Essa tabela usa o teste **somente para visualização retrospectiva da curva risco-cobertura**. Não serve para escolher uma nova política.

**Limitação fundamental:** tanto a temperatura quanto o limiar foram ajustados nos mesmos 2.001 exemplos de calibração. O limite Wilson de calibração **não é uma garantia estatística independente** da precisão no teste nem na produção. Um experimento mais forte reservaria um terceiro conjunto para selecionar a política, além de avaliar mudança de domínio e rótulos desbalanceados.

## Auditoria de sobreposição e limitações

Foram identificadas **193 linhas no teste com texto exatamente igual (ignorando maiúsculas/minúsculas) a pelo menos um registro do treino oficial**. A auditoria sem essas coincidências resultou em acurácia de **88,19%** no subconjunto de 2.887 exemplos; essa análise é pós-hoc e não elimina paráfrases quase idênticas.

Não foram avaliadas mensagens privadas, tráfego real, falsos positivos de alto custo, erros de linguagem regional, desvio temporal, confiança de classes raras ou calibração por segmentos. A política não está implantada em um serviço comercial.

## Evidências verificáveis

- [Código, documentação e testes offline](../confidence-evaluation/).
- [Relatório JSON e cartão do experimento](../published/confidence-evaluation/).
- [Modelo efetivamente publicado no Hugging Face](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-confidence-v1).
- [GitHub Actions: teste, treino, publicação de modelo e resultados](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44389602707).
- [Estudo anterior: robustez, drift e inferência](../model-ops/) e [auditoria do benchmark](./banking77-ptbr-results.md).

**Conclusão:** previsões confiantes não são necessariamente previsões corretas. Para que um sistema de IA possa recusar respostas difíceis, é preciso separar **treinamento**, **calibração**, **seleção de política** e **avaliação independente**, sempre acompanhando risco e cobertura.
