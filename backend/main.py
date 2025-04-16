import os
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
clf = pipeline("sentiment-analysis")

API_KEY = os.getenv("API_KEY")  # ✅ 改用環境變數讀取

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input: InputText, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return clf(input.text)
