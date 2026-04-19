import os
from dotenv import load_dotenv
load_dotenv()
def query(user_query):
    from google import genai

    api_key = os.getenv("API_KEY") 
    
    my_ai = genai.Client(api_key = api_key)

    response = my_ai.models.generate_content(
        model = "gemini-2.5-flash",
        contents = user_query 
    )
    
    return response.text

import streamlit as st
st.title("personal AI Chat")

if 'message' not in st.session_state:
    st.session_state.message = []

for i in st.session_state.message:
    with st.chat_message(i["role"]):
        st.markdown(i["msg"])    


user_input = st.chat_input("Enter Your Query")

if(user_input):
    st.session_state.message.append({
        "role" : "user",
        "msg" : user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
       with st.spinner("Thinking"):
            result = query(user_input)
            st.markdown(result)

    st.session_state.message.append({
        "role" : "assistant",
        "msg" : result
    })       