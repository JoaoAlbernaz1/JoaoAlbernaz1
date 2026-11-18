"""Benchmark offline BM25 vs TF-IDF; embeddings opcionais sem gerar respostas."""
from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).parent


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)


def bm25_scores(docs: list[str], query: str, k1: float = 1.5, b: float = 0.75) -> np.ndarray:
    tokens = [tokenize(d) for d in docs]
    query_tokens = tokenize(query)
    if not docs:
        return np.array([], dtype=float)
    lengths = [len(t) for t in tokens]
    avgdl = max(sum(lengths) / len(docs), 1)
    df = Counter(token for document in tokens for token in set(document))
    scores = np.zeros(len(docs), dtype=float)
    for i, document in enumerate(tokens):
        freqs = Counter(document)
        for term in query_tokens:
            if term not in freqs:
                continue
            idf = math.log(1 + (len(docs) - df[term] + 0.5) / (df[term] + 0.5))
            scores[i] += idf * freqs[term] * (k1 + 1) / (
                freqs[term] + k1 * (1 - b + b * lengths[i] / avgdl)
            )
    return scores


def tfidf_matrix_scores(docs: list[str], queries: list[str]) -> np.ndarray:
    vectorizer = TfidfVectorizer(strip_accents="unicode", ngram_range=(1, 2))
    document_vectors = vectorizer.fit_transform(docs)
    query_vectors = vectorizer.transform(queries)
    return cosine_similarity(query_vectors, document_vectors)


def retrieval_metrics(ranked_ids: list[str], relevant_ids: set[str], k: int) -> dict[str, float]:
    if not relevant_ids:
        raise ValueError("Cada consulta precisa ter pelo menos um documento relevante")
    top = ranked_ids[:k]
    matched = len(set(top) & relevant_ids)
    reciprocal_rank = next((1.0 / (i + 1) for i, doc_id in enumerate(top) if doc_id in relevant_ids), 0.0)
    return {f"recall@{k}": matched / len(relevant_ids), f"mrr@{k}": reciprocal_rank}


def aggregate(score_matrix: np.ndarray, documents: list[dict], queries: list[dict]) -> dict:
    results = []
    for idx, query in enumerate(queries):
        ordered = sorted(
            range(len(documents)),
            key=lambda j: (-float(score_matrix[idx, j]), documents[j]["id"]),
        )
        ranked = [documents[i]["id"] for i in ordered]
        relevant = set(query["relevant_ids"])
        r1 = retrieval_metrics(ranked, relevant, 1)
        r3 = retrieval_metrics(ranked, relevant, 3)
        results.append({"query_id": query["id"], "top3": ranked[:3], **r1, **r3})
    means = {metric: float(np.mean([row[metric] for row in results])) for metric in ("recall@1", "recall@3", "mrr@3")}
    return {"mean_metrics": means, "per_query": results}


def run(with_embeddings: bool = False) -> dict:
    documents = read_jsonl(ROOT / "data" / "documents.jsonl")
    queries = read_jsonl(ROOT / "data" / "queries.jsonl")
    ids = {d["id"] for d in documents}
    if len(ids) != len(documents):
        raise ValueError("IDs duplicados em documentos")
    for query in queries:
        if not set(query["relevant_ids"]) <= ids or not query["relevant_ids"]:
            raise ValueError(f"Qrels inválidos para {query['id']}")
    docs_text = [d["text"] for d in documents]
    queries_text = [q["text"] for q in queries]
    lexical = np.vstack([bm25_scores(docs_text, text) for text in queries_text])
    matrices = {"bm25": lexical, "tfidf": tfidf_matrix_scores(docs_text, queries_text)}
    if with_embeddings:
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
        doc_embeddings = model.encode(docs_text, normalize_embeddings=True)
        query_embeddings = model.encode(queries_text, normalize_embeddings=True)
        matrices["multilingual_embeddings"] = np.asarray(query_embeddings) @ np.asarray(doc_embeddings).T
    return {
        "dataset": "synthetic_pt_retrieval_v1",
        "documents": len(documents),
        "queries": len(queries),
        "limitations": "Small author-created corpus and manual relevance annotations; not a public benchmark.",
        "methods": {key: aggregate(matrix, documents, queries) for key, matrix in matrices.items()},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--with-embeddings", action="store_true")
    parser.add_argument("--output", type=Path, default=Path("outputs/retrieval.json"))
    args = parser.parse_args()
    results = run(with_embeddings=args.with_embeddings)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({name: data["mean_metrics"] for name, data in results["methods"].items()}, indent=2))


if __name__ == "__main__":
    main()
