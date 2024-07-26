import requests
import os

class ELTextToSpeech:
    def generate(self, message):
        CHUNK_SIZE = 1024
        url = "https://api.elevenlabs.io/v1/text-to-speech/OKanSStS6li6xyU1WdXa"

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": open(os.getcwd() + '/Key/el-text-to-speech/el-text-to-speech.txt', 'r').read()
        }

        data = {
            "text": message,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }

        response = requests.post(url, json=data, headers=headers)
        if (response.ok):
            with open('output.mp3', 'wb') as f:
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)