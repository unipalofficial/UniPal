import io
from google.oauth2 import service_account
from google.cloud import speech

client_file = 'Key/speech-to-text/unipal-speech-to-text-key.json'
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

# Make class to encapsulate the speech-to-text process

class SpeechToText :
    def __init__(self) :
        self.client = speech.SpeechClient(credentials=credentials)

    def recognize(self, audio_file) :
        with io.open(audio_file, 'rb') as audio:
            content = audio.read()
            audio = speech.RecognitionAudio(content=content)
            
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code='id-ID',
            model='latest_short',
            enable_automatic_punctuation=True,
            enable_word_time_offsets=True,
            enable_word_confidence=True,
        )

        response = self.client.recognize(config=config, audio=audio)
        return response

# Try to recognize speech from audio
def test() :
    stt = SpeechToText()
    response = stt.recognize('Cache/output.wav')

    for result in response.results:
        alternative = result.alternatives
        print('Transcript: {}'.format(alternative[0].transcript))
        print('Confidence: {}'.format(alternative[0].confidence))
        print('Word Time Offsets:')
        for word_info in alternative[0].words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            print('\t{}s - {}s: {}'.format(start_time.total_seconds(), end_time.total_seconds(), word))
            
    # Output:
    # Transcript: Halo nama saya Unipal Saya adalah asisten virtual yang akan membantu Anda dalam belajar

test()