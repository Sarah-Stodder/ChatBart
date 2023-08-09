from ttsp import TextToSpeechPrinter
from stti import SpeechToTextInputer
import os
from dotenv import load_dotenv
import requests
import google.generativeai as palm



load_dotenv()
api_key = os.environ.get('GOOGLE_API_KEY')

palm.configure(api_key=api_key)

class ChatBot:
    def __init__(self):
        self.name = "BotFather"
        self.user_name = "User"
    
    def save_user_name(self, user_name):
        self.user_name = user_name
    
    def get_user_info(self):
        print("What is your name? ")
        name=input("")
        self.save_user_name(name)
        
    
    def get_response(self, user_input):
        response = palm.chat(messages=user_input, temperature=1)
        return response.last
    def reply_to_geeves(self, user_input):
        response = response.reply(user_input)
        return response.last
        
        
    def start_chat(self):
        print(f"Hello! I'm {self.name}")
        self.get_user_info()
        response=palm.chat(messages=f"Hello! I am {self.user_name}", temperature=1)
        print(response.last)
        while True:
            user_input = input("")
            if user_input.lower() == "quit":
                    print("Bye! It was great chatting with you!")
                    break
            response = response.reply(user_input)
            print(response.last)



#with TextToSpeechPrinter(), SpeechToTextInputer():
chatbot = ChatBot()
chatbot.start_chat()

