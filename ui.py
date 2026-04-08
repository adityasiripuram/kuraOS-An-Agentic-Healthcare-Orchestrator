import streamlit as st
import requests

st.title("Med-AI Appointment Portal")

user_input = st.text_input("How can I help you today?")
if st.button("Send to Agent"):
    # This calls your FastAPI backend
    response = requests.post(f"http://localhost:8080/ask?prompt={user_input}")
    st.write(response.json()["output"])
