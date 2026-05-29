import streamlit as st

st.set_page_config(page_title="Streamlit Hello World")

st.title("Hello from Streamlit!")
st.write("This is a simple Streamlit application.")

name = st.text_input("What's your name?")
if name:
    st.write(f"Nice to meet you, {name}!")
