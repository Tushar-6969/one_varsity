import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def suggest_learning_path(topic: str) -> str:
    if not HF_TOKEN:
        return "❌ Error: Hugging Face API token not found. Please check your .env file."

    prompt = f"Create a clear, structured learning path for the topic: {topic}. Include beginner, intermediate, and advanced steps."
    payload = {"inputs": prompt}

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and "summary_text" in data[0]:
                return data[0]["summary_text"]
            return str(data)  # fallback debug info
        else:
            return f"❌ API Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"❌ Request failed: {str(e)}"

# Example usage:
if __name__ == "__main__":
    topic = "AI and Machine Learning"
    print(suggest_learning_path(topic))
