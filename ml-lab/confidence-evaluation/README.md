# Confidence Evaluation · Calibração e classificação seletiva

Um estudo em ML aplicado à decisão de **quando o modelo deve se abster de responder**. Experimento distinto do classificador principal BANKING77-PTBR: esse novo estimador é treinado em apenas 80% do treino oficial, usando os outros 20% somente para ajuste da temperatura e escolha do limiar.

**Protocolo:** classe prevista por TF-IDF de caracteres + LinearSVC; escala de temperatura ajustada para minimizar NLL exclusivamente na divisão de calibração; e avaliação no teste oficial independente com ECE em dez faixas, NLL, Brier multiclass, macro-F1, acurácia e risk–coverage.

O limiar de abstenção é calculado na divisão de calibração usando limite inferior de Wilson como critério ilustrativo. Ele não é calibrado em ambiente operacional e não garante o nível de precisão alvo.

**Dados:** [BANKING77-PTBR](https://huggingface.co/datasets/c2d-usp/banking77-pt-br), traduções revistas por pesquisadores da Poli/USP, CC BY 4.0; nenhum dado real de atendimento privado. Há textos repetidos entre treino e teste; a auditoria pós-hoc com exclusão de correspondências exatas é registrada separadamente.

## Reproduzir

    python -m pip install -r ml-lab/requirements.txt
    python -m pytest -q ml-lab/confidence-evaluation/tests
    python ml-lab/confidence-evaluation/confidence.py --output-dir outputs/confidence-evaluation

O experimento não exige GPU ou serviços de inferência pagos. Saídas: model.skops, calibration.json, metrics.json e README.md gerado com números medidos. O workflow de CI publica os artefatos em um novo repositório de modelo Hugging Face. Nenhuma métrica é declarada antes da execução.

**Limitações:** o softmax de margens de SVM não é, por si só, uma probabilidade confiável; a escala por temperatura exige validação externa. O conjunto de calibração é reutilizado para escolher o limiar, o que pode produzir otimismo. A amostra é traduzida, de domínio financeiro, e não demonstra desempenho em produção. O modelo com 80% dos dados não deve ser apresentado como melhoria direta de accuracy em relação ao modelo v1 treinado em todo o treino.

[Modelo anterior](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1) · [ModelOps e monitoramento](../model-ops/) · [Laboratório principal](../).
