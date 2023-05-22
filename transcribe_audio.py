import openai
import os
import load_dotenv from dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio(file_name):
    with open(file_name, "rb") as audio_file:
        response = openai.Whisper.transcribe(audio_file.read())
    return response['text']
