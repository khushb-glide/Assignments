import os
import requests

OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL = os.getenv("EMBED_MODEL")

def get_embedding(text: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": text
        }
    )
    response.raise_for_status()
    return response.json()["embedding"]
