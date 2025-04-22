# backend/test_main.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_positive():
    response = client.post(
        "/predict",
        json={"text": "I love it!"},
        headers={"x-api-key": "mysecret"}
    )
    assert response.status_code == 200
    assert response.json()[0]["label"] == "POSITIVE"

def test_missing_api_key():
    response = client.post("/predict", json={"text": "No key!"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid API Key"
