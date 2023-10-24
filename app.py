#
import openai
import requests
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai_key = os.environ.get("OPENAI_API_KEY")
langchain_key = os.environ.get("LANGCHAIN_KEY")

# Define OpenAI API endpoint and parameters
openai_url = "https://api.openai.com/v1/completions"
openai_model = "text-davinci-002"
openai_prompt = "you are a good bot with step by step instructions. review the details provided and give the best instructions you can. "

# Define LangChain API endpoint and parameters
#langchain_url = "https://api.langchain.com/v1/preprocess"
#langchain_url = "https://api.openai.com/v1/completions"

# Define Streamlit app
def app():
    st.set_page_config(page_title="OpenAI GPT-3 Chatbot", page_icon=":robot_face:")
    st.title("Testing chatbot interaction")
    st.write("This is a test of the emergency broadcast chat system")
    user_input = st.text_input("Type your message below...")
    if user_input:
        # Preprocess user input using LangChain API
        langchain_data = {
            "text": openai_prompt + " " + user_input,
            "model": "gpt-3",
            "api_key": langchain_key,
        }
        langchain_response = requests.post(langchain_url, json=langchain_data)
        langchain_output = langchain_response.json()
        langchain_text = langchain_output["text"]
        # Generate response using OpenAI API
        openai_data = {
            "prompt": langchain_text,
            "max_tokens": 1024,
            "n": 1,
            "stop": None,
            "temperature": 0.5,
        }
        openai_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_key}",
        }
        openai_response = requests.post(openai_url, json=openai_data, headers=openai_headers)
        openai_output = openai_response.json()
        message = openai_output["choices"][0]["text"].strip()
        st.write("ChatBot Reply:  " + message)

# Run Streamlit app
if __name__ == "__main__":
    app()
