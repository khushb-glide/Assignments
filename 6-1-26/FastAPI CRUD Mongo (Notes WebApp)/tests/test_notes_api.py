from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_get_notes():
    response = client.get("/api/notes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_note():
    response = client.post(
        "/api/notes",
        json={
            "title": "Test Note",
            "content": "This is a test note"
        }
    )
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Test Note"
    assert data["content"] == "This is a test note"
    assert "id" in data
