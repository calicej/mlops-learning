from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
clf = pipeline("sentiment-analysis")

# 固定一組 API key（也可以做成環境變數）
API_KEY = "mysecret"

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input: InputText, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return clf(input.text)
