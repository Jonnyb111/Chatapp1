### This is a streamlit app I am building to use openai keys in order to create a web application interface. The future desire is to be able to container the application to a webhosted LLM. This in turn will allow you to have a chat bot you can container and deploy for the mass to utilize. 
---------------------------
### To run this right now its based really simply off of current streamlit code. you will need to create a env, install the requirements and then you can launch it via streamlit.
'streamlit run app.py'
---------------------------
### App1 - chatbot, uses local host to interact with the chat via web browser (streamlit).
'UI: http://localhost:8501'
---------------------------
### Future: I will upload the missing Docker file template to container the env to an image. I Currently need to remove my api keys and process the env details in a different way in order to allow for apikey changes dynamically by updating the needful.txt file.
---------------------------
