from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
clf = pipeline("sentiment-analysis")

@app.get("/")
def read_root():
    return {"msg": "Hello from FastAPI"}

@app.post("/predict")
def predict(text: str):
    return clf(text)
