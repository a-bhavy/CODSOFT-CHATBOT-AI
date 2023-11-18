import numpy as np
import streamlit as st
from chatbot import SimpleChatbot


st.title('BHAVY \'S  :blue[CHATBOT] :sunglasses:')

chatbot = SimpleChatbot()
user_input = st.text_input('PLEASE ENTER PROMPT',)

# if user_input.lower() == "exit":
#     print("Goodbye!")
    

bot_response = chatbot.get_response(user_input)
st.write("Bot:", bot_response)
