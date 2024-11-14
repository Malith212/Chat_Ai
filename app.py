from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

def load_qa_pairs(filename="qa_pairs.json"):
    """Loads questions and answers from a JSON file."""
    try:
        with open(filename, "r") as file:
            qa_pairs = json.load(file)
        return qa_pairs
    except FileNotFoundError:
        print("Error: Questions and answers file not found.")
        return {}

# Load Q&A pairs and prepare for vectorization
qa_pairs = load_qa_pairs()
questions = list(qa_pairs.keys())
answers = list(qa_pairs.values())

# Initialize vectorizer and fit on stored questions
vectorizer = TfidfVectorizer().fit(questions)
question_vectors = vectorizer.transform(questions)

def get_best_match(user_question):
    """Find the best matching question using cosine similarity."""
    user_vector = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vector, question_vectors).flatten()
    best_match_index = similarities.argmax()
    if similarities[best_match_index] > 0.5:  # Adjust threshold as needed
        return answers[best_match_index]
    else:
        return "I don't have an answer for that. Try asking something else."

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json.get("question", "").lower().strip()
    answer = get_best_match(user_question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
