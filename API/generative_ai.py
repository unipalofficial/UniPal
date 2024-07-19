import google.generativeai as genai
import os
import json

class GenAI():

    def send_message(self, msg:str):
        return self._chat.send_message(msg).text.strip() # Return message

    def initialize(self):
        genai.configure(api_key=open(os.getcwd() + '/Key/gemini/API_key.txt').read())
        train_data = json.load(open(os.getcwd() + '/knowledge_clean.json', 'r', encoding='utf8'))
        self._model = genai.GenerativeModel('gemini-1.5-flash')
        self._chat = self._model.start_chat(history=[])
        return self._chat.send_message(list(json.load(open(os.getcwd() + '/initializer.json', 'r')).values())[0].format(train_data)).text.strip() # Return first response message