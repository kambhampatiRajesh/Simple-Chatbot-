import streamlit as st
import requests

st.title("ChatBot")

if "conversation" not in st.session_state:
    st.session_state["conversation"]= []

for con in st.session_state["conversation"]:
    st.write(con)

prompt = st.chat_input("Type Your Message")    

if prompt:
    st.session_state["conversation"].append({"role":"user","prompt":prompt})
    response = requests.post(url = "https://kambhampatirajesh.app.n8n.cloud/webhook-test/d26632f3-e12e-4d52-a624-1c88f147ef3e",json = {"prompt":prompt})
    
    if response.status_code==200:
        st.session_state["conversation"].append({"role":"ai","prompt":response.json()["output"]})
        ## st.session_state["conversation"].append(response.json()["output"])

for con in st.session_state["conversation"]:
    with st.chat_message(con["role"]):
        st.write(con["prompt"])