import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

## gemini initialization
#initialize the dotenv to load the environment variables
load_dotenv()

#configure the API key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')


st.title("SWAP IS SEXY")
st.markdown("-----------------------------------------------------")

## initializing the message history
if "messages" not in st.session_state:
    st.session_state.messages = []

## initializing the chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


## display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


## context for the model
context = """YYou are a customer service bot for a ride sharing application. 
Answer the user's question in a helpful and informative way. Do not entertain 
questions outside the scope of the ride sharing app. If the question is vague, 
ask for clarification. If further assistance is needed, suggest connecting to a human representative. history:{history}"""


## get user input
if prompt := st.chat_input("say something nice"):
    # displaying the user message in teh caht message container
    with st.chat_message("user"):
        st.markdown(prompt)
        if prompt:
                # Append the user's message to the chat history
            st.session_state['chat_history'].append({'role': 'me ', 'content': prompt})

            # Format the history for the model
            history = '\n'.join([f"{message['role']}: {message['content']}" for message in st.session_state['chat_history']])

            # Add the history to the context
            full_context = context.format(history=history)

            # Generate the model's response
            response = model.generate_content(full_context)

            # Append the model's response to the chat history
            st.session_state['chat_history'].append({'role': 'assistant', 'content': response.text})

            # Append the model's response to the message history
            st.session_state.messages.append({'role': 'user', 'content': prompt})


    # displaying the response in the chat message container
    with st.chat_message("assistant"):
        st.markdown(response.text)

    # add assistant response to the message history
    st.session_state.messages.append({'role': 'assistant', 'content': response.text})


