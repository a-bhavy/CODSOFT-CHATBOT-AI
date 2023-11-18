import nltk
from nltk.tokenize import word_tokenize
import numpy as np
import streamlit as st



class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "name me your admin ":"BHAVY",
            "hello"              : "Hi there How can I help you today?",
            "wassup"             : "I'm very good, thanks for asking! WBU you",
            "bye"                : "Bye Have a great day.",
            "what is your name"  : "I'm a simple chatbot made by Bhavy. My name is Alloh",
            "tell me a bad joke" : "Why don't scientists have sense Because they make up everything!",
            "who created you"    : "I was created by a programmer who's new to programming.",
            "tell me a joke"     : "Why don't scientists trust atoms? Because they make up everything!",
            "default"            : "I'm not sure how to respond to that. Can you ask me something else?",
            "tell me a good joke": "blahhh",
           
        }

    

    def preprocess_input(self, user_input):
        tokens = word_tokenize(user_input.lower())
        tokens = [token for token in tokens if token.isalnum()]
        return tokens
        
    def get_response(self, user_input):
        tokens = self.preprocess_input(user_input)

        # Initialize variables to keep track of the best score and responses
        # best_score = 0
        len_rule_tokens = []
        responses = []
        count = 0
        ratio = 0
        result = []
        # Iterate through rule-response pairs
        for rule, response in self.responses.items():
            rule_tokens = self.preprocess_input(rule)
            #st.write(rule_tokens)
            score = sum(token in tokens for token in rule_tokens)
            ratio = score/len(rule_tokens)
            #   print(score)
            if ratio == 1:
                count +=1
                len_rule_tokens.append(len(rule_tokens))
                responses.append(response)
                # print("count" , count)
                # print(best_responses) 

        if count == 0 and user_input :
            st.write("please enter more rules to get an accurate response. Hope this helps")
            st.write("BOT SHOWING POSIBLE OUTCOMES")
            for rule, response in self.responses.items():
                rule_tokens = self.preprocess_input(rule)
                #st.write(rule_tokens)
                score = sum(token in tokens for token in rule_tokens)
                ratio = score/len(rule_tokens)
                #   print(score)
                if ratio >= 0 :
                    len_rule_tokens.append(len(rule_tokens))
                    responses.append(response)
            if ratio == 0:
                responses.append(self.responses["default"])    
            result = responses[:3]
        elif len_rule_tokens :
            result = responses[np.argmax(len_rule_tokens)]    
        #st.write(len_rule_tokens)
        #st.write(responses)
        # st.write(np.argmax(len_rule_tokens)))
        # Randomly choose one of the best responses if there are multiple with the same score
        return result


    
