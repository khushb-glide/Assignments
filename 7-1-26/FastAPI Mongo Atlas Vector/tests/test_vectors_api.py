from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_insert_vector():
    response = client.post(
        "/insert",
        json={
            "text": "ON DELETE CASCADE removes dependent rows automatically"
        }
    )
    assert response.status_code == 200
    assert response.json()["status"] == "inserted"


def test_search_vectors():
    response = client.post(
        "/search",
        json={
            "query": "Explain cascade delete in databases"
        }
    )
    assert response.status_code == 200

    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)
