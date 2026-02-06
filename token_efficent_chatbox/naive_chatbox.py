from token_counter import count_token

chat_history=[]

def fake_llm(prompt):
    return ("Naive chatbot(type 'Exit' to quit )")

while True:
    user_input=input("You: ")
    if user_input=="Exit":
        break
    chat_history.append(f"User:{user_input}")

    full_prompt="\n".join(chat_history)
    response=fake_llm(full_prompt)
    chat_history.append(f"AI:{response}")

    tokens_used=count_token(full_prompt)

    print("AI:",response)
    print("Tokens used:",tokens_used)
    print("-" * 40)
