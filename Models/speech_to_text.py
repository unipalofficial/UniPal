import io
from google.oauth2 import service_account
from google.cloud import speech
import os

client_file = '/KEY/speech-to-text/unipal-speech-to-text-key.json'
credentials = service_account.Credentials.from_service_account_file(os.getcwd() + client_file)
client = speech.SpeechClient(credentials=credentials)

# Make class to encapsulate the speech-to-text process

class SpeechToText():
    def __init__(self) :
        self.client = speech.SpeechClient(credentials=credentials)

    def recognize(self, audio_file) :
        with io.open(audio_file, 'rb') as audio:
            content = audio.read()
            audio = speech.RecognitionAudio(content=content)
            
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code='id-ID',
            enable_automatic_punctuation=True,
            enable_word_time_offsets=True,
            enable_word_confidence=True,
        )

        response = self.client.recognize(config=config, audio=audio)
        return response
