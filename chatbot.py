import json

def load_qa_pairs(filename="qa_pairs.json"):
    """Loads questions and answers from a JSON file."""
    try:
        with open(filename, "r") as file:
            qa_pairs = json.load(file)
        return qa_pairs
    except FileNotFoundError:
        print("Error: Questions and answers file not found.")
        return {}

def chatbot():
    # Load questions and answers from JSON file
    qa_pairs = load_qa_pairs()
    print("Hello! I am a chatbot. Ask me questions, or type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        if user_input == "quit":
            print("Chatbot: Goodbye!")
            break
        elif user_input in qa_pairs:
            print(f"Chatbot: {qa_pairs[user_input]}")
        else:
            print("Chatbot: I don't have an answer for that. Try asking something else.")

if __name__ == "__main__":
    chatbot()
