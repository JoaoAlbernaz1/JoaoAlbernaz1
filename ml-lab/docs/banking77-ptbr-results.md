# BANKING77-PTBR · avaliação reproduzida e auditoria de sobreposição

**Experimento executado em 18/11/2026.**

**Objetivo:** avaliar como três baselines clássicas de NLP classificam 77 intenções bancárias em português brasileiro. A análise utiliza o dataset público [BANKING77-PTBR](https://huggingface.co/datasets/c2d-usp/banking77-pt-br), traduzido e revisado por pesquisadores, com licença CC BY 4.0.

**Demonstração visual:** [dashboard de pesquisa publicado no Hugging Face](https://huggingface.co/spaces/JOAOOALBERNAZ/banking77-ptbr-research), com comparação interativa de modelos e auditoria. O Space é estático e não executa inferência do modelo.

**Evidências:** [treino e publicação reproduzidos no GitHub Actions](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44372375897) · [modelo e métricas publicados no Hugging Face](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1).

## Protocolo e seleção

- **Divisão oficial:** 10.003 registros de treino e 3.080 de teste após exclusão de **2 linhas incompletas do teste**. São 77 classes.
- **Escolha de modelo:** split estratificado de 80/20 apenas dentro do treino oficial, seed 42. O conjunto de teste não participou da escolha.
- **Candidatos:** TF-IDF de palavras com SGD, TF-IDF de palavras com LinearSVC e TF-IDF de caracteres com LinearSVC.
- **Ajuste final:** candidato de maior macro-F1 de validação, reajustado no treino completo.
- **Teste oficial:** calculado após a escolha. A auditoria de sobreposição foi adicionada depois, como análise de sensibilidade, **sem retreinar ou reescolher o modelo**.

| Baseline | Macro-F1 validação | Accuracy validação |
|:--|--:|--:|
| TF-IDF caracteres + LinearSVC | **0,8800** | **0,8836** |
| TF-IDF palavras + SGD | 0,8726 | 0,8741 |
| TF-IDF palavras + LinearSVC | 0,8700 | 0,8726 |

## Resultado de teste

| Medida | Teste oficial completo | Teste sem texto idêntico ao treino |
|:--|--:|--:|
| Exemplos | 3.080 | 2.887 |
| Accuracy | **0,8964** | **0,8916** |
| Macro-F1 | **0,8964** | **0,8910** |
| Weighted-F1 | **0,8964** | **0,8916** |

### Por que a auditoria de sobreposição importa?

O cruzamento *casefold* encontrou **166 textos distintos que aparecem tanto no treino quanto no teste**, correspondentes a **193 linhas de teste**, que foram excluídas apenas da análise de sensibilidade. Esses valores medem coisas diferentes: textos únicos em comum versus registros excluídos.

A acurácia diminui de 89,64% para 89,16% quando as 193 linhas de teste com texto igual a um texto de treino são desconsideradas. Esse resultado **não prova** ausência de contaminação: paráfrases e amostras quase duplicadas ainda podem existir. É uma auditoria *post-hoc*, e não um novo conjunto independente.

A avaliação oficial preserva a métrica do benchmark original para comparabilidade. A auditoria complementa a interpretação com uma estimativa mais conservadora. Nenhum dado de teste foi utilizado na seleção dos três candidatos.

## Limitações

1. O corpus é uma tradução revisada por pesquisadores; **não representa diretamente mensagens originalmente escritas por clientes brasileiros**.
2. O domínio é atendimento financeiro, não delivery nem um sistema real do iFood.
3. Textos repetidos e variações quase idênticas podem inflar o score.
4. Os modelos não foram avaliados sob mudança temporal, drift, viés ou ataques adversariais.
5. Esta é uma avaliação clássica supervisionada de intenções, não treinamento de um LLM generativo.

## Reprodução

No repositório:

```bash
python -m pip install -r ml-lab/requirements.txt
python ml-lab/banking77-ptbr/train.py --output-dir outputs/banking77-ptbr
python -m pytest -q ml-lab/banking77-ptbr/tests
```

O script gera `metrics.json`, `README.md` e `model.skops`; os mesmos valores auditados estão no artefato do [GitHub Actions](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44372375897) e no [Hugging Face](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1). O código documenta pré-processamento, divisão dos dados e critérios de avaliação.

**Fontes:** Dimant et al. (2025), *BANKING77-PTBR: conjunto de dados do domínio financeiro traduzido para o português brasileiro* (CC BY 4.0), Centro de Ciência de Dados Poli/USP; Casanueva et al. (2020), *Efficient Intent Detection with Dual Sentence Encoders*.
