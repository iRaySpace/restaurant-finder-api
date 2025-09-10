from fastapi.testclient import TestClient
from app.api import get_api


client = TestClient(get_api())


def test_ping_returns_200_pong():
    response = client.get("/api/ping")
    assert response.status_code == 200
    assert response.json()['message'] == "pong"


def test_get_execute_invalid_code_returns_401():
    response = client.get("/api/execute", params={"code": "invalidcode", "message": "random"})
    assert response.status_code == 401
    assert response.json()["error"] == "code invalidcode is invalid"
