# BANKING77-PTBR · ModelOps Distribution Monitoring

**Auditoria offline em dados públicos**, sem monitoramento de usuários reais.

Referência: **10003** textos do treino oficial. Comparação: **3080** textos do teste oficial.

| Estatística | Valor |
|:--|--:|
| PSI de comprimento | 0.0177 |
| Jensen-Shannon de comprimento (bits) | 0.0032 |
| Jensen-Shannon de intenções previstas (bits) | 0.0129 |

## Distribuição de comprimento de mensagens

| Caracteres | Treino | Teste |
|:--|--:|--:|
| 0-19 | 26 | 10 |
| 20-39 | 1936 | 695 |
| 40-59 | 4013 | 1262 |
| 60-89 | 2411 | 731 |
| 90-129 | 743 | 200 |
| 130-189 | 567 | 121 |
| 190-299 | 284 | 57 |
| 300+ | 23 | 4 |

## Alertas demonstrativos (não calibrados)

- Shift no comprimento (PSI ≥ 0,2): **False**.
- Shift nas intenções previstas (JSD ≥ 0,05): **False**.

Não há garantia estatística de detecção de incidentes. Os limiares são exemplos, não parâmetros validados para um sistema financeiro.

## Interpretação

PSI e Jensen-Shannon descrevem mudanças nas distribuições. Não avaliam verdade de rótulos, qualidade do atendimento, desempenho de LLMs ou erro do classificador. Comparar os splits oficiais de pesquisa NÃO equivale a monitorar produção.

- [Dados agregados por classe e métricas](./metrics.json)
- [Código de monitoramento e API](../../model-ops/)
- [Modelo NLP utilizado](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1)
- [Pesquisa e auditoria dos dados](../../docs/banking77-ptbr-results.md)

O relatório omite deliberadamente textos e previsões individuais.
