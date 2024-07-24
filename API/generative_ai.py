import google.generativeai as genai
import os
import json

class GenAI():

    def send_message(self, msg:str):
        return self._chat.send_message(msg).text.strip() # Return message

    def initialize(self):
        genai.configure(api_key=open(os.getcwd() + '/Key/gemini/API_key.txt').read())
        get_data = json.load(open(os.getcwd() + '/knowledge_clean.json', 'r', encoding='utf8'))
        train_data = []
        train_data.append(get_data[:int(.5*len(get_data))])
        train_data.append(get_data[int(.5*len(get_data)):]) # Initialize train data
        self._model = genai.GenerativeModel('gemini-1.5-flash')
        self._chat = self._model.start_chat(history=[])
        for i in range(2):
            data = json.load(open(os.getcwd() + '/initializer.json', 'r'))[i]
            for key in data.keys():
                print(self._chat.send_message(data[key].format(train_data[i])).text.strip())