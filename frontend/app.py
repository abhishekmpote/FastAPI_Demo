import streamlit as st
import requests

backend_url = "http://127.0.0.1:8000" 

st.title("FastAPI and Streamlit Integration")

st.header("Hello Endpoint")

if st.button("call get api"):
    response = requests.get(f"{backend_url}/hello")
    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("Failed to call the hello endpoint.")

st.header("Create User Endpoint")
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, step=1)

if st.button("Create User"):
    if name and age:
        user_data = {"name": name, "age": age}
        response = requests.post(f"{backend_url}/great_user", json=user_data)
        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error("Failed to create user.")
    else:
        st.warning("Please provide both name and age.")
