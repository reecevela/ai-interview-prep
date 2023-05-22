import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(messages : list):
    response = openai.ChatCompletion.create(
      model="gpt4",
      messages=messages
    )
    
    return response['choices'][0]['message']['content']
