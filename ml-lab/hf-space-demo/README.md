# Hugging Face Space · BANKING77-PTBR

Aplicativo Gradio minimalista para experimentar um **classificador NLP treinado**, com 77 classes de intenções. As margens do LinearSVC são mostradas sem interpretá-las como probabilidades.

O app baixa os pesos do [modelo existente no Hugging Face](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1) e executa inferência no Space. Nenhuma chave de API é usada em inferência. O pipeline foi serializado com `skops`.

**Código da demonstração:** [space/app.py](./space/app.py) · **publicação:** [publish_space.py](./publish_space.py).

## Qualidade

- Avaliação do dataset de pesquisa: macro-F1 0,8964.
- Auditoria sem coincidências textuais com treino: macro-F1 0,8910.
- O corpus foi traduzido e revisado por pesquisadores; não é composto por mensagens privadas em português.
- O app não mede qualidade em produção; disponibiliza uma interface demonstrativa para o modelo realmente publicado.

**Status: código pronto, Gradio Space NÃO publicado.** O Hugging Face retornou HTTP 402 na tentativa de criação: novos Spaces com Gradio/Docker usando CPU exigem plano elegível. A alternativa pública gratuita é o [dashboard estático de pesquisa](../hf-space-static/), que não oferece inferência. Esta versão em Gradio permanece como projeto executável localmente ou futuramente em infraestrutura compatível.
