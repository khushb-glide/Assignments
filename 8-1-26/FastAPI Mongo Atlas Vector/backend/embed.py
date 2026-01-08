import os
import requests

OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL = os.getenv("EMBED_MODEL")


def normalize(text: str) -> str:
    return (
        text.strip()
            .lower()
            .replace("?", "")
            .replace(".", "")
    )


def get_embedding(text: str):
    text = normalize(text)

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": text
        }
    )
    response.raise_for_status()
    return response.json()["embedding"]
