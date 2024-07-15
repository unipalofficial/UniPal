from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from API.generative_ai import GenAI
from API.speech_to_text import SpeechToText
from API.text_to_speech import TextToSpeech
app = FastAPI()

genai = GenAI()
stt = SpeechToText()
tts = TextToSpeech()

@app.get('/')

def root():
    return {'message': ''}