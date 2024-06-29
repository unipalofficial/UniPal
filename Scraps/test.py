import google.generativeai as genai
import os
import json

# Configuration
GOOGLE_API_KEY = open('../KEY/api_key.txt').read()
genai.configure(api_key=GOOGLE_API_KEY)

# Training Data Loading
data_load = open('knowledge.json', 'r', encoding='utf8')
TRAINING_DATA = json.load(data_load)

# Model Loading
model = genai.GenerativeModel('gemini-1.5-flash')

# Create A Chat
chat = model.start_chat(history=[])

# Prompt Engineering Initializer
initialize = list(json.load(open('initializer.json', 'r')).values())[0]

# Prompt Engineering
response = chat.send_message(initialize.format(TRAINING_DATA)).text.strip()
print('Unipal:', response, end='\n\n')

while(True):

    response = chat.send_message(input('You: ')).text.strip()
    print()
    # response = model.generate_content(input('You: ')).text
    print('Unipal:', response, end='\n\n')