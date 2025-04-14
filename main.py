from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
clf = pipeline("sentiment-analysis")

class InputText(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"msg": "Hello from FastAPI"}

@app.post("/predict")
def predict(input: InputText):
    return clf(input.text)
