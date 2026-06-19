import streamlit as st

st.title("Persona Support Agent")

user_input = st.text_area("Enter your query")

if st.button("Submit"):
    st.write("Response will appear here")
