from backend.embed import get_embedding
from backend.db import vectors_collection
from backend.similarity import cosine_similarity


THRESHOLD = 0.65
OVERFETCH = 20
TOP_K = 5


def search_vectors(query: str):
    query_embedding = get_embedding(query)
    results = []

    # Get all docs from MongoDB
    all_docs = list(vectors_collection.find())
    print(f"DEBUG: Found {len(all_docs)} total documents in DB")

    for doc in all_docs:
        score = cosine_similarity(query_embedding, doc["embedding"])
        results.append({
            "text": doc["text"],
            "score": score
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    
    # Filter by threshold
    filtered_results = [r for r in results if r["score"] >= THRESHOLD]
    print(f"DEBUG: {len(filtered_results)} results met the {THRESHOLD} threshold")

    return {
        "results": filtered_results[:TOP_K]
    }