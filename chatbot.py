def chatbot():
    print("Hello! I am a simple chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        elif "hello" in user_input.lower():
            print("Chatbot: Hello! How can I help you today?")
        elif "how are you" in user_input.lower():
            print("Chatbot: I'm just a bunch of code, but thanks for asking!")
        else:
            print("Chatbot: Sorry, I don't understand.")

if __name__ == "__main__":
    chatbot()
