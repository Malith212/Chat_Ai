def chatbot():
    # Dictionary to store questions and answers
    qa_pairs = {
        "what is your name": "I'm your friendly chatbot!",
        "how are you": "I'm a computer program, so I don't have feelings, but thanks for asking!",
        "what can you do": "I can answer some basic questions. Try asking me!",
        "who created you": "I was created by a curious mind experimenting with Python.",
        "what is python": "Python is a versatile programming language known for its simplicity and readability."
    }

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
