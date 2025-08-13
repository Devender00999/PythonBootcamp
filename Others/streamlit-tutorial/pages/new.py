import streamlit as st

st.title("📄 Second Page")
st.write("Welcome to Page 2!")

name = st.text_input("What's your name?")
if name:
    st.success(f"Hello, {name}!")