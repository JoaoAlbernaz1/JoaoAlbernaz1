"""Minimal live demo: pretrained NLP classifier from its published Hub repository."""
from functools import lru_cache

import gradio as gr
import numpy as np
from huggingface_hub import hf_hub_download
import skops.io as sio

MODEL_REPO = "JOAOOALBERNAZ/banking77-ptbr-intent-v1"


@lru_cache(maxsize=1)
def load_model():
    file_path = hf_hub_download(
        repo_id=MODEL_REPO, repo_type="model", filename="model.skops"
    )
    # Do not automatically trust types declared by an untrusted file.
    # This model uses scikit-learn Pipeline, TfidfVectorizer and LinearSVC.
    # skops safely loads supported estimators by default.
    return sio.load(file_path, trusted=[])


def predict(text):
    question = (text or "").strip()
    if not question:
        return "Digite uma frase para classificar.", []
    if len(question) > 1000:
        return "Limite de 1.000 caracteres.", []
    model = load_model()
    predicted = str(model.predict([question])[0])
    labels = model.named_steps["clf"].classes_
    margins = np.asarray(model.decision_function([question])).reshape(-1)
    top = np.argsort(margins)[-3:][::-1]
    rows = [[str(labels[int(i)]), round(float(margins[int(i)]), 4)] for i in top]
    return "Intenção prevista: " + predicted.replace("_", " "), rows


with gr.Blocks(theme=gr.themes.Monochrome(), title="BANKING77 PTBR | Intent Explorer") as demo:
    gr.Markdown(
        "# BANKING77-PTBR\n"
        "Classificação de intenções em português • **77 classes** • "
        "**TF-IDF + LinearSVC**\n\n"
        "Experimento de pesquisa, não uma ferramenta de atendimento financeiro."
    )
    inp = gr.Textbox(
        label="Mensagem para classificar",
        lines=3,
        max_lines=6,
        placeholder="Ex.: Minha transferência ainda não chegou. Como posso acompanhar?"
    )
    go = gr.Button("Classificar")
    main = gr.Textbox(label="Resultado", interactive=False)
    scores = gr.Dataframe(headers=["Intenção", "Margem (não é probabilidade)"], interactive=False)
    go.click(fn=predict, inputs=inp, outputs=[main, scores])
    inp.submit(fn=predict, inputs=inp, outputs=[main, scores])
    gr.Examples(
        examples=[
            ["Não recebi meu cartão novo. Onde posso acompanhar a entrega?"],
            ["Quero consultar a taxa aplicada à minha compra internacional."],
            ["Uma transferência saiu da conta, mas não chegou ao destinatário."],
        ],
        inputs=inp,
    )
    gr.Markdown(
        "**Avaliação:** macro-F1 0,8964 no teste oficial; 0,8910 na auditoria sem textos duplicados. "
        "Margens de decisão não estão calibradas como probabilidades. "
        "O corpus é traduzido/revisado e pode não generalizar para mensagens reais."
    )
    gr.Markdown(
        "[Modelo no Hugging Face](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1)"
        " · [Código e metodologia](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/tree/main/ml-lab/banking77-ptbr)"
    )


if __name__ == "__main__":
    demo.launch()
