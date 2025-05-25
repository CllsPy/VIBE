from transcription import Transcription
from llm import LLM
import streamlit as st

with st.form("YouTube"):
    st.title("YOUTUBE VIDEO TO BLOG")
    st.write("Inside the form")
    id = st.text_input("Youtube ID_VIDEO")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:

        transcription = Transcription()
        transcription.get_transcript_text(id)

        with open('transcript.txt', 'r') as file:
            file = file.read()
        
        llm_calling = LLM()
        st.markdown(llm_calling.call_llm(file))

