# AI Study Buddy - Simple Chatbot

def get_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi, welcome. How can I help you?",
        "how are you": "I am fine. Thanks for asking.",
        "who are you": "I am your study buddy chatbot.",
        "motivate me": "Keep going. Every bug you fix makes you better.",
        "happy": "Good to hear that!",
        "functions kya hote hain": "Chapter 12 parho :)"
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "Sorry, I did not understand that."


def chat():
    print("Hello! I am Study Buddy!")
    print("You can talk to me. Type 'bye' anytime to exit.\n")

    while True:
        user = input("You: ")

        if user.lower() == "bye":
            print("Bot: Goodbye! Happy studying.")
            break

        reply = get_response(user)
        print("Bot:", reply)


chat()