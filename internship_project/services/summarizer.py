import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL ="https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def summarize_text(text: str) -> str:
    if not HF_TOKEN:
        return "❌ Error: Hugging Face API token not found. Please check your .env file."

    payload = {"inputs": f"Summarize: {text}"}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            data = response.json()
            # Case 1: ["generated_text"]
            if isinstance(data, list) and "generated_text" in data[0]:
                return data[0]["generated_text"]
            # Case 2: ["summary_text"]
            if isinstance(data, list) and "summary_text" in data[0]:
                return data[0]["summary_text"]
            return str(data)  # fallback (debug info)
        except Exception as e:
            return f"❌ Error parsing response: {str(e)}"
    else:
        return f"❌ API Error {response.status_code}: {response.text}"
