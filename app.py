from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

def load_qa_pairs(filename="qa_pairs.json"):
    """Loads questions and answers from a JSON file."""
    try:
        with open(filename, "r") as file:
            qa_pairs = json.load(file)
        return qa_pairs
    except FileNotFoundError:
        print("Error: Questions and answers file not found.")
        return {}

qa_pairs = load_qa_pairs()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json.get("question", "").lower().strip()
    answer = qa_pairs.get(user_question, "I don't have an answer for that. Try asking something else.")
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
