from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from generative_ai import GenAI
from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech

app = FastAPI()

genai = GenAI()
stt = SpeechToText()
tts = TextToSpeech()

@app.get('/')

def root():
    return {'message': ''}