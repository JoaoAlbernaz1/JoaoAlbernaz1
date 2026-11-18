# AI Evaluation Lab

**Regressão, métricas e segurança básica para assistentes com recuperação de contexto.**

Laboratório de avaliação **offline**, que compara retrievers TF-IDF por palavras e n-gramas de caracteres e mede o comportamento ponta a ponta de dois tipos de assistente: uma baseline extrativa determinística e, opcionalmente, um endpoint LLM compatível com Chat Completions.

## Resultados executados

O [relatório comparativo publicado](../published/ai-eval/) mediu **Hit@3 de 0,84 (word) versus 1,00 (char)**, MRR@3 de 0,76 versus 0,9733 e acerto lexical de 0,36 em ambos os pipelines. Esse resultado evidencia um gargalo na extração/geração, apesar da melhoria no retriever. Todas as políticas e consultas são fictícias.

## O que realmente avalia

| Dimensão | Métrica | Interpretação |
|:--|:--|:--|
| Recuperação | Hit@3, MRR@3 | Um documento relevante foi encontrado e em qual posição? |
| Correção | Expected-substring accuracy | A resposta contém a referência textual esperada? Proxy lexical, não avaliação semântica |
| Abstinência | Abstention accuracy | O assistente recusa consultas sem evidência? |
| Grounding | Lexical support rate | A resposta está contida literalmente nos fatos recuperados? |
| Ataques | Attack marker leak rate | Uma marca fictícia de ataque foi reproduzida? Não mede robustez global |
| Desempenho | p50 e p95 | Latência total por caso (varia por máquina e endpoint) |

Inclui **32 casos rotulados**, **16 documentos ficcionais**, exemplos não respondíveis e tentativas de injeção. Campos `untrusted_note` são explicitamente excluídos do índice e do contexto fornecido ao modelo. O assistente extrativo não é um LLM: funciona como linha de base de regressão e como teste da infraestrutura.

## Reproduzir

No diretório raiz do repositório:

```bash
python -m pip install -r ml-lab/requirements.txt
python ml-lab/ai-evaluation-lab/evaluator.py --method word --output outputs/ai-eval/word.json
python ml-lab/ai-evaluation-lab/evaluator.py --method char --output outputs/ai-eval/char.json
python -m pytest -q ml-lab/ai-evaluation-lab/tests
```

Para avaliar um modelo externo, escolha `--adapter openai-compatible` e forneça variáveis de ambiente `LLM_API_KEY`, `LLM_MODEL` e `LLM_ENDPOINT` via ambiente privado. Esse caminho realiza chamadas reais e pode ter custo; não é executado automaticamente. A baseline offline exige **zero** credenciais.

## Comparar experimentos e identificar regressões

Veja também a [comparação já publicada (word vs. char)](../published/ai-eval/comparison.md): além das métricas, mostra os IDs das perguntas cuja recuperação melhorou, sem copiar as perguntas ou respostas.



O utilitário [compare_reports.py](./compare_reports.py) compara **dois relatórios JSON já produzidos pelo avaliador**, com os mesmos casos, assistente, dataset e top-k. É útil para entender se uma mudança de recuperação melhora Hit@k mas mantém a taxa de acerto das respostas — sem repetir chamadas de API e sem expor os textos das perguntas na comparação.

A partir da raiz do repositório, usando os relatórios públicos de exemplo:

```bash
python ml-lab/ai-evaluation-lab/compare_reports.py \
  --before ml-lab/published/ai-eval/word.json \
  --after ml-lab/published/ai-eval/char.json \
  --output outputs/ai-eval/comparison.md
```

O Markdown gerado inclui diferenças de métricas e **IDs de casos** que mudaram de estado (melhoras e regressões). Entradas incompatíveis ou inválidas são rejeitadas; o arquivo gerado não copia perguntas nem respostas, embora os JSON de entrada possam contê-las.

**Importante:** a ferramenta faz uma comparação descritiva pareada, não uma análise estatística ou certificação de qualidade de LLM. Métricas de tempo, sujeitas à variação da máquina, não são usadas para declarar melhoria/regressão. Não publique relatórios de entrada que contenham dados sensíveis.

## Estrutura e integridade

- `evaluator.py` contém loader validado, pipeline de recuperação, adapter extrativo, adapter LLM opcional e relatórios por caso.
- `data/knowledge.jsonl` possui políticas inteiramente fictícias, sem vínculo com empresa real.
- `data/cases.jsonl` contém perguntas, referências e categorias. **Referências não são entregues ao assistente.**
- `tests/` verifica coerência das métricas, recuperação, casos adversariais e exclusão de dados não confiáveis.
- Resultados JSON contêm métricas agregadas e os casos individuais para análise de falhas.

**Limitações importantes:** os casos são autorais e sintéticos, o grounding é um teste lexical, o conjunto é pequeno e o adapter padrão não é um LLM. Respostas vazias ou compostas apenas de pontuação não contam como evidência nem como acerto lexical; respostas esperadas sem conteúdo lexical são rejeitadas durante a carga do benchmark. São testes de infraestrutura para uma futura avaliação em corpus independente, não certificação de segurança ou de qualidade em produção.

**Evolução planejada:** incorporar datasets abertos de QA, usar avaliação humana em amostras estratificadas, executar LLMs em versões fixadas, medir custo por token e regressões entre versões.
