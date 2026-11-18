# AI Evaluation Lab

**Regressão, métricas e segurança básica para assistentes com recuperação de contexto.**

Laboratório de avaliação **offline**, que compara retrievers TF-IDF por palavras e n-gramas de caracteres e mede o comportamento ponta a ponta de dois tipos de assistente: uma baseline extrativa determinística e, opcionalmente, um endpoint LLM compatível com Chat Completions.

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

## Estrutura e integridade

- `evaluator.py` contém loader validado, pipeline de recuperação, adapter extrativo, adapter LLM opcional e relatórios por caso.
- `data/knowledge.jsonl` possui políticas inteiramente fictícias, sem vínculo com empresa real.
- `data/cases.jsonl` contém perguntas, referências e categorias. **Referências não são entregues ao assistente.**
- `tests/` verifica coerência das métricas, recuperação, casos adversariais e exclusão de dados não confiáveis.
- Resultados JSON contêm métricas agregadas e os casos individuais para análise de falhas.

**Limitações importantes:** os casos são autorais e sintéticos, o grounding é um teste lexical, o conjunto é pequeno e o adapter padrão não é um LLM. São testes de infraestrutura para uma futura avaliação em corpus independente, não certificação de segurança ou de qualidade em produção.

**Evolução planejada:** incorporar datasets abertos de QA, usar avaliação humana em amostras estratificadas, executar LLMs em versões fixadas, medir custo por token e regressões entre versões.
