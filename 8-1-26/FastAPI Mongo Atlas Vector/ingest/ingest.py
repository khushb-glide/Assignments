import sys
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

# project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

load_dotenv(PROJECT_ROOT / ".env")

from backend.embed import get_embedding
from backend.db import vectors_collection


CSV_PATH = PROJECT_ROOT / "data" / "data.csv"
MAX_DOCS = 500 


def main():
    if not CSV_PATH.exists():
        print(f"CSV not found at {CSV_PATH}")
        return

    df = pd.read_csv(CSV_PATH)

    if "text" not in df.columns:
        print("CSV does not contain a 'text' column")
        return

    df = df.dropna(subset=["text"])
    df = df.head(MAX_DOCS)

    inserted = 0

    for text in df["text"]:
        text = str(text).strip()
        if not text:
            continue

        embedding = get_embedding(text)

        vectors_collection.insert_one({
            "text": text,
            "embedding": embedding
        })

        inserted += 1
        print(f"Inserted {inserted}")

    print(f"Done. Inserted {inserted} documents.")


if __name__ == "__main__":
    main()
