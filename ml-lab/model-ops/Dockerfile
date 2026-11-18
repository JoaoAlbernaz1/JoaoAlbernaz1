FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/tmp/huggingface-cache
WORKDIR /app
COPY ml-lab/requirements.txt /app/ml-lab/requirements.txt
COPY ml-lab/model-ops/requirements-serving.txt /app/ml-lab/model-ops/requirements-serving.txt
RUN pip install --no-cache-dir -r ml-lab/model-ops/requirements-serving.txt
COPY ml-lab/model-ops/serving.py /app/serving.py
RUN useradd --system --uid 10001 --home-dir /tmp modelops
USER 10001
EXPOSE 8000
CMD ["uvicorn", "serving:app", "--host", "0.0.0.0", "--port", "8000"]
