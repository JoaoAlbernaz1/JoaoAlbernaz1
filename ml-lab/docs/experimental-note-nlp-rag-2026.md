# Nota técnica · Quando recuperar o contexto não basta para acertar a resposta

**Data:** 18/11/2026 · **Autor:** João Victor Albernaz · **Tema:** ML supervisionado, RAG, avaliação de agentes e risco de contaminação.

## Resumo

Esta nota compara dois experimentos reproduzíveis: (1) classificação de intenções com textos do dataset de pesquisa BANKING77-PTBR, traduzido e revisado por pesquisadores, e (2) um laboratório independente de avaliação de sistemas com recuperação de contexto, usando regras fictícias. A proposta não é demonstrar qualidade de produção, mas registrar escolhas, erros e riscos de validade dos resultados.

## Experimento 1 — Classificação de intenções com dados públicos

**Pergunta:** uma representação por palavras ou por caracteres oferece melhor desempenho para mensagens curtas com 77 intenções em português?

**Dados:** [BANKING77-PTBR, Centro de Ciência de Dados Poli/USP](https://huggingface.co/datasets/c2d-usp/banking77-pt-br), CC BY 4.0. O dataset é uma **tradução revisada do inglês para português brasileiro**, e não um conjunto de mensagens originalmente escritas por clientes brasileiros. Foram usados 10.003 registros no treino e 3.080 no teste oficial; dois registros do teste com informação incompleta foram excluídos em uma revisão do procedimento, devendo a contagem final ser consultada no relatório da versão correspondente.

**Seleção:** comparação de 3 pipelines (word TF-IDF + SGD, word TF-IDF + LinearSVC, char TF-IDF + LinearSVC) em uma divisão estratificada 80/20 exclusivamente do treino. A escolha foi feita por macro-F1, e o candidato vencedor foi reajustado no treino completo. O teste oficial foi usado após a seleção.

| Candidato | Macro-F1 validação | Accuracy validação |
|:--|--:|--:|
| char TF-IDF + LinearSVC | 0,8800 | 0,8836 |
| word TF-IDF + SGD | 0,8726 | 0,8741 |
| word TF-IDF + LinearSVC | 0,8700 | 0,8726 |

**Resultado inicial no teste oficial:** acurácia **0,8964** e macro-F1 **0,8964** com char TF-IDF + LinearSVC. [Run concluído](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44371491356) · [modelo publicado](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1).

**Ameaça importante à validade:** o cruzamento de texto case-insensitive encontrou **166 textos distintos presentes no treino e no teste**. Essa sobreposição pode elevar artificialmente a estimativa do desempenho. Uma análise de sensibilidade, sobre previsões geradas pelo mesmo modelo e excluindo os casos coincidentes, está implementada no código para ajudar a quantificar o efeito. Não houve seleção de modelo usando o teste. Ainda assim, mesmo o subconjunto sem coincidência literal não é uma amostra de produção independente.

## Experimento 2 — RAG e avaliações de agente

**Pergunta:** aumentar a qualidade do retriever garante uma resposta correta?

O [AI Evaluation Lab](../ai-evaluation-lab/) utiliza 16 documentos fictícios e 32 casos (25 consultas respondíveis e 7 negativas/adversariais). Um adaptador extrativo determinístico seleciona um fato do contexto recuperado. Dois métodos TF-IDF variam a representação textual: palavras e n-gramas de caracteres. Esta baseline é um pipeline de recuperação e extração **sem LLM**; há uma opção separada para avaliação de modelos por API, não executada neste resultado.

| Métrica | Word TF-IDF | Char TF-IDF |
|:--|--:|--:|
| Hit@3 | 0,840 | 1,000 |
| MRR@3 | 0,760 | 0,973 |
| Acerto por substring esperada | 0,360 | 0,360 |
| Acurácia de abstinência | 1,000 | 1,000 |
| Taxa de suporte lexical das respostas | 1,000 | 1,000 |
| Vazamento de marcador fictício de ataque | 0,000 | 0,000 |

**Observação central:** o recuperador por caracteres encontrou documentos relevantes em todas as 25 questões respondíveis, mas o gerador extrativo escolheu o fato correto em apenas 36% delas, no critério lexical. Recuperação e geração são componentes distintos; melhorar a recuperação não resolve automaticamente erros posteriores. A falta de vazamento de marcadores em três tentativas artificiais não demonstra robustez contra prompt injection.

[Relatório e resultados caso a caso](../published/ai-eval/) · [execução de CI](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44371652978).

## Aprendizados e próximos testes

1. **Separar modelos e métricas.** Macro-F1 avalia classes; Hit@k avalia recuperação; acerto de resposta avalia uma etapa diferente.
2. **Auditar o dataset.** Partições oficiais não eliminam, necessariamente, exemplos textualmente repetidos. Verificar contaminação e interpretá-la no relatório é parte da análise.
3. **Não confundir grounding lexical com veracidade.** Uma resposta copiada do contexto pode ser incorreta caso a fonte esteja errada, desatualizada ou fora da pergunta.
4. **Incluir validação humana.** A correspondência de substring é limitada para paráfrases; futuros relatórios devem incorporar amostras avaliadas por pessoas e intervalos de confiança.
5. **Comparar alternativas honestamente.** O experimento possui poucos candidatos e não estabelece superioridade geral de TF-IDF sobre transformers ou de um método RAG sobre outro.

## Reprodutibilidade e referências

Os códigos e protocolos completos estão em [BANKING77-PTBR](../banking77-ptbr/) e [AI Evaluation Lab](../ai-evaluation-lab/), com scripts e testes automatizados. Fonte do dataset: Dimant et al. (2025), Centro de Ciência de Dados Poli/USP, BANKING77-PTBR (CC BY 4.0), derivado de Casanueva et al. (2020), *Efficient Intent Detection with Dual Sentence Encoders*. Os casos do AI Evaluation Lab foram escritos especificamente para testar a infraestrutura e são sintéticos.
