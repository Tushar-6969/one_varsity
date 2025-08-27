from flask import Flask, request, render_template
from services.summarizer import summarize_text
from services.qa import answer_question
from services.learning_path import suggest_learning_path

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    task = request.form.get("task")

    if task == "summarize":
        text = request.form.get("text", "").strip()
        if not text:
            result = "❌ Please enter some text to summarize."
        else:
            result = summarize_text(text)

    elif task == "qa":
        context = request.form.get("context", "")
        question = request.form.get("question", "")

        if not context.strip() or not question.strip():
            result = "❌ Please provide both context and a question for Q&A."
        else:
            result = answer_question(context.strip(), question.strip())

    elif task == "learn":
        topic = request.form.get("topic", "").strip()
        if not topic:
            result = "❌ Please enter a topic for the learning path."
        else:
            result = suggest_learning_path(topic)

    else:
        result = "❌ Invalid Task Selected"

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
