📚 AI Study Buddy (Rule-Based Chat Assistant in Python)

This is a simple chatbot made using basic Python.
It replies to user messages based on keywords and keeps running until you type `bye`.


🎯 Objective

To create a small chat assistant using Python basics like strings, conditions, dictionaries, functions, and loops.


🧠 Concepts Used

* **Strings** → to read user input
* **If-else** → to decide replies
* **Dictionary** → to store responses
* **Functions** → to keep code organized
* **Loop** → to keep chat running



⚙️ Features

* Replies to simple user inputs
* Runs continuously until user types `bye`
* Easy to edit and add new responses
* Uses only basic Python (no libraries)



 💻 Code (chatbot.py)

```python
# Study Buddy - Simple Chatbot

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
```


▶️ How to Run

```bash
python chatbot.py
```


 💬 Sample Output

```
Hello! I am Study Buddy!
You can talk to me. Type 'bye' anytime to exit.

You: Hello
Bot: Hi, welcome. How can I help you?

You: Who are you
Bot: I am your study buddy chatbot.

You: Motivate me
Bot: Keep going. Every bug you fix makes you better.
```


🚀 Future Improvements

* Add time-based greetings
* Add voice input/output
* Connect with real AI APIs
* Save chat history in a file
