from transcription import Transcription
from llm import LLM
import streamlit as st
import time
import sys
import os
os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
file_path = os.path.join(os.path.dirname(__file__), "transcript.txt")

st.set_page_config(
    page_title="IU2B",
    page_icon="https://cdn-icons-png.flaticon.com/512/10026/10026285.png",
    layout="centered",
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://github.com/CllsPy',
        'Report a bug': 'https://github.com/CllsPy',
        'About': 'made with ♥ by CLL'
    }
)

# copies 
home_title = "IU2B"
home_introduction = """Bem-vindo ao IU2B, onde o poder da IA generativa e a simplificidade do streamlit se encontram. 
                       Nesta plataforma você será capaz de transformar vídeos do YouTube em um blog post! """
quick_start_text = """
Olá, para usar a nossa ferramenta é bem simples:
1. Escolha um vídeo do YouTube (e.x https://www.youtube.com/watch?v=e2IbNHi4uCI)
2. Remova o video_id, depois da igualdade (e2IbNHi4uCI)
3. Cole o video_id na caixa de texto e pronto!
"""

st.markdown(
    "<style>#MainMenu{visibility:hidden;}</style>",
    unsafe_allow_html=True
)

st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)

st.markdown("""\n""")
st.markdown("#### Saudações")
st.write(home_introduction)

st.markdown("""\n""")
st.markdown("""\n""")

st.markdown("#### Quickstart")
st.info(quick_start_text)

st.markdown("""\n""")
st.markdown("""\n""")

with st.sidebar:
    st.info("made with ♥ by CLL")

with st.form('Formulário'):
    st.header("Resposta")

    tab1, tab2, tab3 = st.tabs(["📈 Video ID", "Resposta", "Texto Original"])

    with tab1: 
        id = st.text_input("Cole o ID de algum vídeo")

    submit_button = st.form_submit_button('Submit')

    file_path = os.path.join(os.getcwd(), "transcript.txt")

    with tab2: 
        if submit_button: 
             transcription = Transcription()
             transcription.get_transcript_text(id)

             with st.spinner("Loading..."):
                 time.sleep(3)
                 with open(file_path, "r", encoding="utf-8") as file:
                     file = file.read()
                     llm_calling = LLM()
                     st.markdown(llm_calling.call_llm(file))

    with tab3:
         try:
             with open(file_path, "r", encoding="utf-8") as file:
                 file = file.read()
                 st.markdown(file)
         except FileNotFoundError:
             st.warning("Nenhuma transcrição encontrada ainda.")
        
    

                
        


        
        
