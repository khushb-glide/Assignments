from backend.embed import get_embedding
from backend.db import vectors_collection
from backend.similarity import cosine_similarity


THRESHOLD = 0.65
OVERFETCH = 20
TOP_K = 5


def search_vectors(query: str):
    query_embedding = get_embedding(query)

    results = []

    for doc in vectors_collection.find():
        score = cosine_similarity(query_embedding, doc["embedding"])

        results.append({
            "text": doc["text"],
            "score": score
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    results = results[:OVERFETCH]
    results = [r for r in results if r["score"] >= THRESHOLD]

    return results[:TOP_K]
