from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_unix_to_utc():
    response = client.get("/api/to-utc", params={"unix": 1715774400})
    assert response.status_code == 200
    assert "utc" in response.json()
    assert "unix" in response.json()


def test_valid_utc_to_unix():
    response = client.get("/api/to-unix", params={"utc": "2024-05-15T12:00:00Z"})
    assert response.status_code == 200
    assert response.json()["unix"] == 1715774400


def test_invalid_utc():
    response = client.get("/api/to-unix", params={"utc": "invalid-date"})
    assert response.status_code == 400
    assert "Invalid UTC" in response.json()["detail"]


def test_invalid_unix():
    response = client.get("/api/to-utc", params={"unix": "not-a-number"})
    assert response.status_code == 422  # FastAPI catches type mismatch before our code
