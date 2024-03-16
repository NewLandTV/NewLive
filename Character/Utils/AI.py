# Imports
import openai
import os

from dotenv import load_dotenv

# Set API key
load_dotenv()

openai.api_key = os.environ.get("OPEN_AI_API_KEY")

# Variables
messages = []

# Functions
def Request(message):
    messages.append({ "role": "user", "content": message })

    completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = messages)
    response = completion.choices[0].message.content

    messages.append({ "role": "user", "content": response })

    return response