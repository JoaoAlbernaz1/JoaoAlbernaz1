# Hugging Face Space · BANKING77-PTBR

Aplicativo Gradio minimalista para experimentar um **classificador NLP treinado**, com 77 classes de intenções. As margens do LinearSVC são mostradas sem interpretá-las como probabilidades.

O app baixa os pesos do [modelo existente no Hugging Face](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1) e executa inferência no Space. Nenhuma chave de API é usada em inferência. O pipeline foi serializado com `skops`.

**Código da demonstração:** [space/app.py](./space/app.py) · **publicação:** [publish_space.py](./publish_space.py).

## Qualidade

- Avaliação do dataset de pesquisa: macro-F1 0,8964.
- Auditoria sem coincidências textuais com treino: macro-F1 0,8910.
- O corpus foi traduzido e revisado por pesquisadores; não é composto por mensagens privadas em português.
- O app não mede qualidade em produção; disponibiliza uma interface demonstrativa para o modelo realmente publicado.

A disponibilidade pública depende do status do build do Hugging Face Spaces; apenas o workflow de publicação bem-sucedido comprova upload, não necessariamente que o app já esteja funcional.
