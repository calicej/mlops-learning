def test_predict_positive():
    response = client.post(
        "/predict",
        json={"text": "I love it!"},
        headers={"X-API-Key": "mysecret"}
    )
    assert response.status_code == 200


def test_missing_api_key():
    response = client.post("/predict", json={"text": "No key!"})
    assert response.status_code == 401
