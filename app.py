import streamlit as st
import openai

# Read OpenAI API key from needful.txt
with open("needful.txt") as f:
    openai_key = f.read().strip()

# Define OpenAI API endpoint and parameters
openai_url = "https://api.openai.com/v1/completions"
openai_model = "text-davinci-002"
openai_prompt = "Hello, how are you?"

# Define Streamlit app
def app():
    st.set_page_config(page_title="OpenAI GPT-3 Chatbot", page_icon=":robot_face:")
    st.title("Testing chatbot interaction")
    st.write("This is a test of the emergency broadcast chat system")
    user_input = st.text_input("Type your message below...")
    if user_input:
        # Generate response using OpenAI API
        response = openai.Completion.create(
            engine=openai_model,
            prompt=openai_prompt + " " + user_input,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = response.choices[0].text.strip()
        st.write("ChatBot Reply:  " + message)

# Run Streamlit app
if __name__ == "__main__":
    app()
