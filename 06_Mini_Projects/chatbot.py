import random

responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What would you like to talk about?",
    "how are you": "I'm a chatbot, so I'm always ready to assist.",
    "what is your name": "I'm a simple Python chatbot.",
    "bye": "Goodbye! Have a nice day.",
}

fallback_responses = [
    "Tell me more.",
    "That's interesting.",
    "Can you explain that further?",
    "I see. What else?",
]


def get_response(user_input: str) -> str:
    user_input = user_input.lower().strip()
    for key, response in responses.items():
        if key in user_input:
            return response
    return random.choice(fallback_responses)


def main() -> None:
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if not user_input:
            continue
        reply = get_response(user_input)
        print(f"Chatbot: {reply}")
        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    main()
