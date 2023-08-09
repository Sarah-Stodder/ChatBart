import google.generativeai as palm
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('GOOGLE_API_KEY')



print('Configuring')
palm.configure(api_key=api_key)
print('Configuring')


############################################################  CHAT  #########################################################################################

# def chitchat():
#     first=input("Hello!")
#     response=palm.chat(messages=first, temperature=1)
#     print(response.last)
#     while True:
#         user_input = input("")
#         if user_input.lower() == "quit":
#                 print("Bye! It was great chatting with you!")
#                 break
#         response = response.reply(user_input)
#         print(response.last)

# print(chitchat())

############################################################  Prompt  #########################################################################################

# models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
# model = models[0].name


# prompt = input("Hello! how can i help you")
# completion = palm.generate_text(
#     model=model,
#     prompt=prompt,
#     temperature=1,
#     # The maximum length of the response
#     max_output_tokens=800,
# )

# print(completion.result)