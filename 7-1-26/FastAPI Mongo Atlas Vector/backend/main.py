from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from pydantic import BaseModel

from backend.embed import get_embedding
from backend.db import vectors_collection
from backend.similarity import cosine_similarity



app = FastAPI()

# Serve frontend folder as /static
app.mount("/static", StaticFiles(directory="frontend"), name="static")


class InsertRequest(BaseModel):
    text: str


class SearchRequest(BaseModel):
    query: str


@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/ui", response_class=HTMLResponse)
def ui():
    return Path("frontend/vectors.html").read_text()


@app.post("/insert")
def insert_document(req: InsertRequest):
    embedding = get_embedding(req.text)
    vectors_collection.insert_one({
        "text": req.text,
        "embedding": embedding
    })
    return {"status": "inserted"}


@app.post("/search")
def search(req: SearchRequest):
    query_embedding = get_embedding(req.query)

    results = []
    for doc in vectors_collection.find():
        score = cosine_similarity(query_embedding, doc["embedding"])
        results.append({
            "text": doc["text"],
            "score": score
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return {"results": results[:5]}
