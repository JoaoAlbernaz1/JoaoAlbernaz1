# Classificador de intenções · NLP em português

**Problema.** Classificar mensagens curtas de suporte em cinco intenções: pagamento, acesso, cancelamento, entrega e suporte técnico.

**Abordagem.** Baseline supervisionada com `TfidfVectorizer` (unigramas + bigramas) e `LogisticRegression` dentro de um pipeline. `train.py` separa holdout estratificado, usa 3 folds *somente* no conjunto de treino, ajusta modelo final e calcula macro-F1, accuracy, matriz de confusão e relatório por classe.

### Executar a partir de `ml-lab/`

```bash
pip install -r requirements.txt
python nlp-intent-classifier/train.py --output-dir outputs/intent
python nlp-intent-classifier/predict.py --model outputs/intent/model.skops "Nao consigo entrar na minha conta"
pytest -q
```

Artefatos: `model.skops` e `metrics.json` em `outputs/intent/`. A exportação com `skops` evita usar pickle como formato padrão; **ainda assim, não carregue artefatos de origem desconhecida**.

### Dados e limitações

O arquivo `data/tickets.csv` contém **60 exemplos sintéticos escritos especificamente para demonstrar o pipeline**. Eles não representam interações reais nem um dataset de benchmark independente. Métricas obtidas nele **não permitem inferir generalização em produção**. Antes de qualquer deployment: obter dataset público com licença adequada, aumentar diversidade, tratar desbalanceamento, separar temporalmente e realizar avaliação humana.

### Publicar no Hugging Face

Depois do treino, configure um token com permissão de escrita e rode:

```bash
export HF_TOKEN="..."  # use o gerenciador de segredos; não faça commit
python nlp-intent-classifier/publish_hf.py --artifact-dir outputs/intent --repo-id SEU_USUARIO/intent-classifier-pt
```

O script cria o repositório de modelo e envia os arquivos, com **model card** informando natureza sintética dos dados e limitações. A publicação não ocorre automaticamente nem está sendo alegada neste README.

### Extensões de pesquisa

Comparar com LinearSVC, calibrar confiança para encaminhamento humano e avaliar robustez em textos com erros de digitação e mudanças de domínio.
