import os
from openai import OpenAI

# OpenAI API key
api_key = 'your-openai-api-key-here'

client = OpenAI(
  api_key=api_key,
)

# Define the messages for the chat
messages = [
        {"role": "system", "content": "You are a helpful assistant."}
        ]

def get_chatCompletion(messages):
    completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages)
    return completion.choices[0].message.content


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        messages.append({"role": "user", "content": user_input})
        response = get_chatCompletion(messages)
        messages.append({"role": "assistant", "content": response})
        print(response)
