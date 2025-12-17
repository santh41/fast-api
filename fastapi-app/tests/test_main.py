from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}

def test_create_item():
    payload = {
        "id": 1,
        "name": "Laptop",
        "price": 55000,
        "in_stock": True
    }
    response = client.post("/items", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"
