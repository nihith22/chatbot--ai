import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



#load the pretrained hugging face model
chatbot = pipeline("question-answering",model="deepset/bert-base-cased-squad2")



#define healthcare-specific response logic
def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "please consult doctor for accurate advice"
    elif "appointment" in user_input:
        return "would you like to schedule appointment with the doctor?"
    elif "medication" in user_input:
        return "It is important to take prescribed medicines regularly.If you have any concerns, consult your doctor"
    else:
        response = chatbot(user_input,max_length = 500,num_return_sequences=1)
        return response[0]['generated_text']            
    
    
#streamlit web app interface
def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?", "")
    if st.button("submit"):
        if user_input:
            st.write("user:",user_input)
            response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant:", response)
    else:
         st.write("please enter a query.")

if __name__=="__main__":
    main()               

