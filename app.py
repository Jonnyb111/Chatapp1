import streamlit as st
import openai
import requests
import openai_secret_manager

# Read OpenAI API key from needful.txt
with open("needful.txt") as f:
    openai_key = f.read().strip()

# Define OpenAI API endpoint and parameters
openai_url = "https://api.openai.com/v1/completions"
openai_model = "text-davinci-002"
openai_prompt = "Hello, how are you?"

# Define Langchain api and params
langchain_url = "https://api.langchain.com/v1/preprocess"
langchain_key = openai_secret_manager.get_secret("langchain")["api_key"]

# Define Streamlit app
def app():
    st.set_page_config(page_title="OpenAI GPT-3 Chatbot", page_icon=":robot_face:")
    st.title("Testing chatbot interaction")
    st.write("This is a test of the emergency broadcast chat system")
    user_input = st.text_input("Type your message below...")
    if user_input:
        # Preprocess user input using LangChain API
        langchain_data = {
            "text": user_input,
            "model": "gpt-3.5",
            "api_key": langchain_key,
        }
        langchain_response = requests.post(langchain_url, json=langchain_data)
        langchain_output = langchain_response.json()
        print(langchain_output)  # Print contents of langchain_output dictionary
        langchain_text = langchain_output["text"]
        # Generate response using OpenAI API
        openai_data = {
            "prompt": openai_prompt + " " + langchain_text,
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
