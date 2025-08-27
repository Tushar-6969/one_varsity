import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}


def answer_question(context: str, question: str) -> str:
    payload = {"inputs": {"question": question, "context": context}}
    
    print("\n--- DEBUG INFO ---")
    print("API URL:", API_URL)
    print("Question:", question)
    print("Context snippet:", context[:200] + "..." if len(context) > 200 else context)
    print("Payload:", payload)
    print("-------------------\n")

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        print("Status Code:", response.status_code)

        # Show raw response for debugging
        try:
            print("Raw Response JSON:", json.dumps(response.json(), indent=2))
        except Exception:
            print("Raw Response Text:", response.text)

        if response.status_code == 200:
            data = response.json()

            # Debug structure of response
            if isinstance(data, dict) and "answer" in data:
                return data["answer"]
            elif isinstance(data, list) and len(data) > 0 and "answer" in data[0]:
                return data[0]["answer"]
            else:
                return f"Unexpected response format: {data}"
        else:
            return f"Error: {response.text}"

    except Exception as e:
        return f"Exception occurred: {e}"


# Example test
if __name__ == "__main__":
    ctx = "Hugging Face hosts models that can be used for natural language processing tasks such as question answering."
    q = "What tasks can Hugging Face models be used for?"
    print("Answer:", answer_question(ctx, q))
