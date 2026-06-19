import streamlit as st

from src.classifier import classify_persona
from src.generator import generate_response
from src.escalator import should_escalate

st.title("Persona Support Agent")

query = st.text_area("Enter your query")

if st.button("Submit"):

    persona = classify_persona(query)

    if should_escalate(query):
        st.error("Escalation Required")
    else:
        response = generate_response(persona, query)

        st.write("### Persona")
        st.write(persona)

        st.write("### Response")
        st.write(response)
