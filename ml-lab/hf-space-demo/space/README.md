---
title: BANKING77 PTBR · Intent Explorer
emoji: 🧪
colorFrom: gray
colorTo: gray
sdk: gradio
app_file: app.py
python_version: "3.11"
license: cc-by-4.0
short_description: Demonstração do classificador de 77 intenções em português brasileiro.
---

# BANKING77-PTBR · demonstração de NLP

Explore um classificador de **77 intenções financeiras em português brasileiro**.

A interface usa um **modelo real de Machine Learning** (TF-IDF por caracteres + LinearSVC), treinado e avaliado em dados públicos de pesquisa, não uma API de LLM.

**Modelo e documentação:** [BANKING77-PTBR Intent v1](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1).

**Código, treino e auditoria:** [GitHub / ML & Research Lab](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/tree/main/ml-lab/banking77-ptbr).

## Como ler os resultados

São mostradas as três classes com maiores margens do LinearSVC. **Margens não são probabilidades.** Classificações erradas, entradas fora de domínio e textos muito diferentes do corpus são possíveis.

## Avaliação

- Macro-F1 no teste oficial: **0,8964**.
- Macro-F1 excluindo 193 registros de teste com texto idêntico ao treino: **0,8910**.
- Corpus: BANKING77-PTBR, traduções revisadas do BANKING77, licença CC BY 4.0.

O corpus não contém mensagens privadas e não é um conjunto originalmente produzido em português brasileiro.

**Não use este modelo para decisões sobre contas, transferências ou produtos financeiros reais.**
