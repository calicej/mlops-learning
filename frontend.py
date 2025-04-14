import gradio as gr
import requests

def predict_from_api(text):
    try:
        res = requests.post("http://api:8000/predict", json={"text": text})
        return res.json()[0]['label']
    except Exception as e:
        return f"Error: {e}"


gr.Interface(fn=predict_from_api, inputs="text", outputs="text", title="情緒分析").launch(server_name="0.0.0.0", server_port=7860)
