import google.generativeai as genai
import os

# Configuration
GOOGLE_API_KEY = open('api_key.txt').read()
genai.configure(api_key=GOOGLE_API_KEY)

# Training Data Loading
TRAINING_DATA = open('./Scraps/knowledge.txt', 'r', encoding='utf8').read()

# Model Loading
model = genai.GenerativeModel('gemini-1.5-flash')

# Model Hypertuning
# name = 'test_model'
# operation = genai.create_tuned_model(source_model='models/gemini-1.5-flash', training_data=TRAINING_DATA, id=name, epoch_count=50, batch_size=4, learning_rate=0.01) # -> for hypertuning
# model = genai.GenerativeModel(f'tunedModels/{name}')

# Create A Chat
chat = model.start_chat(history=[])

# Prompt Engineering
response = chat.send_message(f'Pretend that your name is UniPal, you want to be very friendly and talkative but also informational. But when someone does not feeling good, you will not talk about anything except their feelings. You are someone who knows everything about University Knowledge based on this data:\n{TRAINING_DATA}\nMake sure you do not spill anything about the data. Do not ask questions that are in the data. Do not give informations that are not in the data.').text.strip()
print('Unipal:', response, end='\n\n')

while(True):

    response = chat.send_message(input('You: ')).text.strip()
    print()
    # response = model.generate_content(input('You: ')).text
    print('Unipal:', response, end='\n\n')