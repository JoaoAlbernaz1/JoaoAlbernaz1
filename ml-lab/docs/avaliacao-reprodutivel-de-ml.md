# Avaliação reprodutível de modelos de ML: do baseline ao RAG

**Artigo técnico · João Victor Albernaz · 18 de novembro de 2026**

*Tema: metodologia aplicada para experimentos supervisionados e recuperação de informação.*

## 1. O que um experimento realmente prova?

Implementar uma arquitetura é diferente de demonstrar que ela funciona fora do conjunto conhecido. Um projeto de ML precisa tornar explícitos: hipótese, origem dos dados, licença, separação entre amostras, baseline, métricas, versões de dependências e limitações. Um número isolado de acurácia no README não é evidência suficiente.

Nos experimentos deste laboratório, os datasets são **sintéticos**, preparados para exercitar o processo técnico. Não devem ser tratados como validação de produto ou como resultados comparáveis com rankings públicos.

## 2. Baselines primeiro

Um classificador de intenção pode começar com TF-IDF e regressão logística. Esse modelo é barato, interpretável em termos de palavras e frequentemente estabelece uma referência útil. Trocar diretamente por um transformer sem baseline prejudica a comparação: não se sabe se o custo extra trouxe ganho.

Para problemas tabulares como o Titanic, é melhor começar com imputação, codificação categórica e uma baseline clara antes de recorrer a engenharia extensa de atributos.

## 3. Vazamento de dados e validação

A fronteira entre treino e teste é essencial. Aplicar imputação, seleção de atributos ou normalização usando **todo** o dataset antes de separar folds contamina a estimativa. A forma robusta é manter transformações dentro do `Pipeline`, de modo que cada fold tenha seus próprios parâmetros aprendidos.

Na classificação com classes potencialmente desiguais, uso de `StratifiedKFold` ajuda a preservar proporções nos folds. Se houver mensagens do mesmo cliente em períodos diferentes, pode ser necessário particionar por cliente ou por tempo, evitando exemplos quase idênticos no treino e teste. Validação estratificada por si só não resolve todas as fontes de vazamento.

## 4. Escolha de métricas

Para classificação multiclasse, **macro-F1** dá peso igual a cada classe e revela problemas escondidos por uma acurácia elevada numa classe majoritária. Deve ser acompanhada de matriz de confusão e métricas por classe.

Para recuperação de contexto em RAG, é útil separar a avaliação do recuperador da geração de linguagem:

- **Recall@k:** fração de documentos relevantes presentes entre os k primeiros retornados; exige referências rotuladas.
- **MRR@k:** média do inverso da posição do primeiro documento relevante, até k; privilegia trazer rapidamente ao topo ao menos uma fonte válida.
- **Latência e custo:** qualidade e tempo de recuperação devem ser medidos juntos quando a aplicação é interativa.

Um alto Recall@k não garante que um LLM gerará uma resposta verdadeira. A avaliação ponta a ponta exige também fidelidade às fontes, tratamento de abstenção e avaliação humana.

## 5. Como comparar BM25, TF-IDF e embeddings

O BM25 e o TF-IDF são baselines lexicais. Embeddings podem lidar melhor com sinônimos e equivalências semânticas, mas introduzem dependência de pesos, tokenização, memória e possíveis vieses de treinamento. Por isso, a comparação deve manter constante: corpus, consultas, julgamentos de relevância, k e política de normalização.

Se o conjunto de consultas for pequeno, diferenças numéricas podem ser instáveis. Registrar resultados por consulta ajuda a localizar casos em que um método acerta e outro falha. Significância estatística e intervalos de confiança tornam-se relevantes em estudos maiores.

## 6. Registro de experimento sugerido

| Campo | Registrar |
|:--|:--|
| Hipótese | O que se espera melhorar e por quê |
| Dados | URL/licença, versão, dimensão, filtros e composição |
| Particionamento | Seed, critérios de agrupamento, treino/validação/teste |
| Ambiente | Python, versões de bibliotecas, CPU/GPU |
| Baseline | Modelo, hiperparâmetros e custo |
| Avaliação | Métricas por classe/consulta, desvios e falhas |
| Limites | Viés, dados sintéticos, domínio, latência, privacidade |

## 7. Próximas etapas verificáveis

1. Substituir o dataset sintético de tickets por um corpus licenciado de mensagens em português, documentando sua procedência.
2. Registrar experimentos com um split fixo e um conjunto adicional fora de distribuição.
3. Expandir o benchmark de retrieval com consultas ambíguas e avaliação independente.
4. Publicar um modelo treinado e seu cartão no Hugging Face, somente após executar e revisar artefatos.
5. Submeter um CSV real ao Kaggle e registrar o link de submissão e a métrica oficial.

## Referências

- [scikit-learn: cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [scikit-learn: Pipeline](https://scikit-learn.org/stable/modules/compose.html#pipeline)
- [Hugging Face: upload files to the Hub](https://huggingface.co/docs/huggingface_hub/guides/upload)
- [Kaggle: Titanic](https://www.kaggle.com/competitions/titanic)

Este artigo é um texto técnico autoral do laboratório, **não** um artigo científico revisado por pares.
