AI Microservices Web App

Project Overview

This project implements modular AI microservices for text summarization, question answering, and dynamic learning path suggestion. It uses Flask as the backend REST API server with a Bootstrap-based frontend UI for user interaction.

AI models are accessed via the Hugging Face Inference API, providing easy integration with open-source transformer models such as facebook/bart-large-cnn and deepset/roberta-base-squad2.

Features

Text Summarization: Summarizes input text using the BART large CNN model.

Question and Answering: Answers user questions based on provided context using RoBERTa SQuAD2.

Learning Path Suggestion: Generates structured, multi-level learning paths on given topics using BART summarization.

Clean and responsive Bootstrap UI with dynamic form fields based on selected service.

Clear error handling for missing inputs.

Modular Python service architecture for each AI function.

Easily extendable to integrate other open-source LLMs or local models with tools like Flowise or LangChain.

Project Structure

/
├── app.py # Flask app entry and routing
├── services/
│ ├── summarizer.py # Summarization service
│ ├── qa.py # Question answering service
│ └── learning_path.py # Learning path suggestion service
├── templates/
│ ├── index.html # Main input form with task selectors
│ └── result.html # Result display page
├── static/
│ └── css/ # Bootstrap and custom styles
├── .env # Environment variables containing API token
├── requirements.txt # Python dependencies
└── README.md # This file

Setup Instructions

Prerequisites

Python 3.8+

A Hugging Face account with an API token for inference usage
(Get one from huggingface.co/settings/tokens)

Installation

Clone the repository:

git clone https://github.com/yourusername/ai-microservices-webapp.git
cd ai-microservices-webapp

Create and activate a Python virtual environment:

python -m venv env
source env/bin/activate # On Windows: .\env\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Create a .env file in the root folder and add your Hugging Face API token:

HF_TOKEN=your_hugging_face_api_token_here

Run the App

python app.py

Open your browser and navigate to http://127.0.0.1:5000 to use the web interface.

Usage

Select the desired AI microservice task: Summarization, Q&A, or Learning Path.

Provide the necessary inputs in the displayed fields.

Submit the form to get AI-generated results.

Errors are shown clearly if required inputs are missing.

API Endpoints

GET / — Render main form page.

POST /result — Accepts form data with the selected task and inputs; returns processed results.

Technologies Used

Python 3.8+

Flask — Lightweight Python web framework

Hugging Face Transformers & Inference API — Access to open-source AI models

Bootstrap 5 — Responsive UI styling

dotenv — Environment variable management

Future Improvements

Integrate Flowise or LangChain for custom local LLM usage.

Add dedicated REST API endpoints for each microservice.

Expand frontend UI with React/Vue for richer experience.

Add authentication for secured API access.

Include unit and integration tests.

License

This project is licensed under the MIT License.

Author

Tushar — aspiring AI/ML developer

Thank you 