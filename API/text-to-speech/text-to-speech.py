import os
from google.cloud import texttospeech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Key/text-to-speech/unipal-text-to-speech-key.json'

class textToSpeech :
    def __init__(self) :
        self.client = texttospeech.TextToSpeechClient()

    def generate(self, text) :
        synthesis_input = texttospeech.SynthesisInput(text=text)

        voice = texttospeech.VoiceSelectionParams(
            language_code="id-ID",
            name="id-ID-Standard-A",
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=1.0,
            pitch=2.0,
        )

        response = self.client.synthesize_speech(
            input=synthesis_input, 
            voice=voice, 
            audio_config=audio_config
        )

        return response.audio_content

