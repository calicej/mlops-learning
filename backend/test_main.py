from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_positive():
    response = client.post(
        "/predict",
        json={"text": "I love it!"},
        headers={"X-API-Key": "mysecret"}  # ✅ 注意這裡大小寫
    )
    assert response.status_code == 200
    assert response.json()[0]["label"] == "POSITIVE"

def test_missing_api_key():
    response = client.post(
        "/predict",
        json={"text": "No key!"}
    )
    assert response.status_code == 401
