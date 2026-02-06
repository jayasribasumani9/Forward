import json
import random

with open("token_efficent_chatbox/intents.json","r")as file:
    data=json.load(file)


print("🤖 Bot: Hello! I'm an AI chatbot. Type 'bye' to exit.")

user_input=input().lower()

found=False
for intent in data["intents"]:
    if user_input in intent["patterns"]:
        print("Bot: ",random.choice(intent["responses"]))
        found=True
        break

if not found:
    print("Bot:Im still learning!")