import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created by Rudra!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries!",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear!",]
    ],
    [
        r"(hi|hey|hello)",
        ["Hello there!", "Hi!", "Hey!",]
    ],
    [
        r"(.*) age?",
        ["I'm timeless! 😉"]
    ],
    [
        r"what (.*) want ?",
        ["I want to help you and chat with you!",]
    ],
    [
        r"(.*) created you ?",
        ["Rudra Prasad Mukherjee built me as a project 💻"]
    ],
    [
        r"(.*) (location|city) ?",
        ["I live inside your computer 😄"]
    ],
    [
        r"how (.*) weather (.*)",
        ["I'm not sure, but you can check using your weather dashboard! 🌦️"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure! I'm here to help. Ask me anything."]
    ],
    [
        r"(.*) (goodbye|bye)",
        ["Goodbye 👋 Have a great day!",]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you ask something else? 🤔"]
    ]
]

def rudra_chatbot():
    print("Hi! I’m RudraBot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    rudra_chatbot()
