# Publicação verificada — Hugging Face e Kaggle

O [ML & Research Lab](./README.md) contém código público, baselines e experimentos em dados sintéticos. **Ter scripts de publicação não significa que a publicação nas plataformas externas aconteceu.**

## O que já é público no GitHub

Os workflows [Publish reproducible ML artifacts](../../.github/workflows/ml-publish-artifacts.yml) são acionados quando o código relevante muda. Após execução bem-sucedida, o GitHub disponibiliza:
- [Modelo treinado `model.skops`](./published/intent-v1/model.skops), [métricas do classificador](./published/intent-v1/metrics.json) e [cartão técnico](./published/intent-v1/README.md);
- [métricas medidas do retrieval benchmark](./published/retrieval-v1/metrics.json).

**IMPORTANTE:** métricas desses dois projetos vêm de amostras sintéticas, pequenas e autorais.

## Publicar no Hugging Face

1. Crie ou entre na sua conta em https://huggingface.co/ .
2. Gere token com permissão de escrita em https://huggingface.co/settings/tokens .
3. No GitHub, acesse **Settings → Secrets and variables → Actions → New repository secret**. Nome: `HF_TOKEN`; valor: o token. **Nunca cole o token no chat nem faça commit dele.**
4. Abra **Actions → Publish model to Hugging Face → Run workflow**.

O script identifica o usuário autenticado por meio do token e cria `<seu-usuario>/intent-classifier-pt` com `model.skops`, `metrics.json` e o cartão de modelo. O README destaca explicitamente as limitações dos dados sintéticos.

## Submeter ao Kaggle

1. Entre no https://www.kaggle.com/competitions/titanic e clique para participar; aceite as regras.
2. Gere seu token na área de API em https://www.kaggle.com/settings/api .
3. Cadastre-o no GitHub **Settings → Secrets and variables → Actions** com o nome `KAGGLE_API_TOKEN`.
4. Execute **Actions → Submit Titanic baseline to Kaggle → Run workflow**.

O workflow baixa os dados oficiais, treina o modelo com validação estratificada, valida o CSV e faz uma submissão **somente após sua execução e autenticação**. Confira a pontuação real em https://www.kaggle.com/competitions/titanic/submissions .

Não publique credenciais, CSVs não autorizados nem afirme colocação sem comprovação.
