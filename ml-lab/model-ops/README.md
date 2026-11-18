# ModelOps · API de inferência + monitoramento de dados

**Uma demonstração de engenharia de ML que conecta o treinamento do modelo à operação técnica.**

Este laboratório usa o classificador real de **77 intenções BANKING77-PTBR**, [publicado no Hugging Face](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1). O projeto implementa serviço FastAPI, testes automatizados, contêiner Docker e monitoração estatística de mudança de distribuição.

## API de inferência

| Rota | Função |
|:--|:--|
| `GET /health/live` | Liveness sem rede e sem carregar o modelo |
| `GET /health/ready` | Readiness; verifica se o modelo pode ser carregado |
| `GET /model-info` | Proveniência, revisão e tipo dos scores |
| `POST /predict` | Intenção prevista, três margens maiores e *gap* entre as duas primeiras |

O pipeline é carregado **sob demanda** via Hugging Face ou `MODEL_PATH`, usando `skops` e rejeitando tipos desconhecidos. A API não registra nem armazena o conteúdo enviado pelo usuário. Entradas vazias ou maiores que 1.000 caracteres são rejeitadas.

A classificação expõe **margens do LinearSVC, que não são probabilidades**. O indicador `low_separation` usa um limite ilustrativo de 0,15, **não calibrado nem validado para decisões automáticas**. Para uma aplicação comercial seriam necessários autenticação, rate-limiting, controle de recursos, revisão de privacidade e calibragem.

## Executar localmente

A partir da raiz do repositório:

~~~bash
python -m pip install -r ml-lab/model-ops/requirements-serving.txt
uvicorn serving:app --app-dir ml-lab/model-ops --port 8000
curl http://localhost:8000/health/live
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"text":"Minha transferência ainda não chegou"}'
~~~

O primeiro `/predict` pode baixar o modelo do Hub, se `MODEL_PATH` não estiver definido.

## Docker

~~~bash
docker build -f ml-lab/model-ops/Dockerfile -t banking77-modelops .
docker run --rm -p 8000:8000 banking77-modelops
~~~

O contêiner usa Python 3.11 e usuário sem privilégios; a aplicação não configura um serviço de produção público.

## Monitoramento estatístico

`monitor.py` e `tests/test_monitor.py` comparam uma referência de textos com um conjunto de novos textos sem acessar nenhum dado privado. São reportadas as distribuições de comprimento e de intenções previstas, com PSI e divergência de Jensen-Shannon. **Drift não mede acurácia**: mesmo sem mudança de distribuição, a qualidade pode piorar.

A execução automatizada reproduz a análise com as divisões públicas oficiais do BANKING77-PTBR. O objetivo é mostrar como instrumentar e auditar mudança de distribuição; não é monitoramento de clientes reais.

## Engenharia de qualidade

Os testes cobrem contrato da API, ordenação de previsões, formato de scores, falhas de modelo, validação das entradas, métricas de drift e relatórios. Existe CI independente do laboratório e uma verificação offline comum em `ml-lab`.

**Limitações:** dataset traduzido/revisado, nenhuma execução sobre tráfego real, sem autenticação de API, margens não calibradas, sem controle de drift temporal de produção. O projeto não afirma disponibilidade SLA, medição de latência de produção ou superioridade de um modelo em outro domínio.
