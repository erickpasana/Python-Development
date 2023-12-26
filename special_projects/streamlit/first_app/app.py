import requests
import streamlit as st

st.title("🔥Welcome to ST!!!🔥")
st.header("Content-Type")
st.subheader("Sub-header")

#paragraph text
st.text("Lorem ipsum")
st.markdown("**Hello** *World*")

first_name = st.text_input("What's your name?")
st.write(first_name)