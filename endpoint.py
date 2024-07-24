from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

from API.generative_ai import GenAI
from API.speech_to_text import SpeechToText
from API.text_to_speech import TextToSpeech
app = FastAPI()

class userMessage(BaseModel):
    message: str

genai = GenAI()
genai.initialize()
stt = SpeechToText()
tts = TextToSpeech()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate")
async def generate(user_Request: Request):
    formData = await user_Request.form()
    user_message = userMessage(**formData)
    data = user_message.message
    generated_text = genai.send_message(data)
    response = re.sub(r'[^a-zA-Z0-9 ,?!\.\n-]+', '', generated_text).strip()
    return {"generated_text": response}