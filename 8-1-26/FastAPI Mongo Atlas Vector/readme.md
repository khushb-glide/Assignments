# 🔍 Vector Search Web App

A semantic search application that demonstrates **vector embeddings and similarity search** using FastAPI, MongoDB, and Ollama.
The app allows users to **insert text as vectors** and **search by meaning** using cosine similarity with overfetching and thresholding.

This project focuses on **vector-based retrieval**, not chatbot generation.

---

# 🚀 Features

* **Insert Mode**: Convert text into vector embeddings using Ollama and store them in MongoDB
* **Search Mode**: Perform semantic search using cosine similarity with overfetch and similarity threshold
* **Stable Retrieval**: Query and document text are normalized before embedding for consistent results
* **Meaning-based Retrieval**: Finds related content even when keywords don’t exactly match
* **Clean Web UI**: Simple HTML/CSS/JS interface for inserting and searching text
* **Environment-based Config**: No hardcoded URLs or secrets
* **Automated Testing**: API tests using pytest and FastAPI TestClient

---

# 🧠 How It Works

1. Text is normalized and sent to the backend
2. Ollama generates an embedding vector
3. Vectors are stored in MongoDB
4. Search queries are embedded using the same pipeline
5. Cosine similarity is computed against stored vectors
6. Results are overfetched, filtered by a similarity threshold, and top matches are returned

This is a **retrieval-only semantic search system**, forming the basis for RAG-style applications.

---

# 🛠️ Tech Stack

* **Backend**: FastAPI (Python)
* **Database**: MongoDB (local)
* **Embeddings**: Ollama (`nomic-embed-text`)
* **Frontend**: HTML, CSS, Vanilla JavaScript
* **Server**: Uvicorn (ASGI)
* **Testing**: Pytest & HTTPX

---

# ⚙️ Setup & Installation

## 1. Prerequisites

* Python 3.10+
* MongoDB running locally
* Ollama installed

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

---

## 2. Configure Environment

Create a `.env` file in the project root:

```
MONGO_URI=mongodb://localhost:27017
OLLAMA_URL=http://localhost:11434/api/embeddings
EMBED_MODEL=nomic-embed-text
```

---

## 3. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 4. Run the Application

From the project root:

```bash
uvicorn backend.main:app --reload
```

Open the UI at:

```
http://127.0.0.1:8000/
```

---

# 📊 Dataset Ingestion

The vector database is populated using a text dataset stored in the `data` folder.
A one-time ingestion script reads the dataset, generates embeddings, and inserts them into MongoDB using the same embedding pipeline as the API.

* Dataset location: `data/data.csv`
* Text column used for embedding: `text`
* Ingestion script: `ingest/ingest.py`

To ingest the dataset, run the following command from the project root:

```bash
python ingest/ingest.py
```

The dataset file is included in the repository. A public link to the dataset source can also be provided here:

* Dataset source: <DATASET_LINK>

---

# 🧪 Testing

Run API tests from the project root:

```bash
pytest
```

The tests validate:

* API availability
* Vector insertion
* Search response structure

---

# 📌 Notes

* This project uses **Top-K (K=5)** semantic search with overfetching and a similarity threshold
* No deep learning models are trained
* Embeddings are used only for **semantic similarity**, not answer generation
