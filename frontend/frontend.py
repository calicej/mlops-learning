import gradio as gr
import requests

def predict_from_api(text):
    try:
        print(f"Sending to API: {text}")
        res = requests.post(
            "http://nginx/api/predict",
            json={"text": text},
            headers={"x-api-key": "mysecret"}  # ⭐️ 這一定要有
        )
        print(f"Status: {res.status_code}, Body: {res.text}")
        return res.json()[0]['label']
    except Exception as e:
        return f"Error: {e}"

gr.Interface(
    fn=predict_from_api,
    inputs="text",
    outputs="text",
    title="Sentiment Analysis",
).launch(
    server_name="0.0.0.0",
    server_port=7860,
    root_path="/ui"
)
