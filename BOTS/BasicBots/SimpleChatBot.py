import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?", ]
    ],
    [
        r"what is your name?",
        ["I'm just a simple chatbot.", ]
    ],
    [
        r"how are you?",
        ["I'm doing well. Thank you!", ]
    ],
    [
        r"(.*) (weather|temperature) in (.*)",
        ["I'm sorry, I don't have access to real-time weather information.", ]
    ],
    [
        r"quit",
        ["Goodbye!", "It was nice talking to you. Goodbye!", ]
    ],
]


# Create a chatbot
def chatbot():
    print("Hello! I'm your chatbot. You can type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    nltk.download("punkt")  # Download NLTK data
    chatbot()

# Breakdown

# It imports the necessary libraries from NLTK.
#
# It defines a list of pattern-response pairs. Each pair consists of a regular expression pattern and a list of
#   possible responses.
#
# For example:
#
# If the user input matches the pattern "my name is (.*)", the chatbot responds with a greeting that includes the
#   name extracted from the input.
#
# If the user asks "what is your name?", the chatbot responds by stating that it's a simple chatbot. There are also
# patterns for asking about the weather and for quitting the conversation. It defines a function chatbot() that
# creates an instance of the Chat class with the defined pattern-response pairs and starts a conversation loop.
#
# Inside the if __name__ == "__main__": block, it downloads the necessary NLTK data (tokenizers) and then calls the
#   chatbot() function to start the chatbot.
