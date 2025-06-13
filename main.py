from transcription import Transcription
from llm import LLM
import streamlit as st
import time
import os

# Inicializa a transcrição
transcription = Transcription()
file_path = transcription.get_path()

# Configuração da página
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

# Oculta menu superior
st.markdown("<style>#MainMenu{visibility:hidden;}</style>", unsafe_allow_html=True)

# Título e introdução
st.markdown(f"""# IU2B <span style=color:#2E9BF5><font size=5>Beta</font></span>""", unsafe_allow_html=True)
st.markdown("#### Saudações")
st.write("""
Bem-vindo ao IU2B, onde o poder da IA generativa e a simplicidade do Streamlit se encontram. 
Nesta plataforma você será capaz de transformar vídeos do YouTube em um blog post!
""")

st.markdown("#### Quickstart")
st.info("""
Olá, para usar a nossa ferramenta é bem simples:
1. Escolha um vídeo do YouTube (ex: https://www.youtube.com/watch?v=e2IbNHi4uCI)
2. Copie o ID do vídeo (e2IbNHi4uCI)
3. Cole o ID na caixa de texto e pronto!
""")

# Sidebar com senha
with st.sidebar:
    st.info("made with ♥ by CLL")
    api = st.text_input("Password", type="password")
    st.markdown(
        """
        <style>
            [title="Show password text"] {
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Form principal
with st.form('Formulário'):
    st.header("Resposta")

    tab1, tab2, tab3 = st.tabs(["📈 Video ID", "Resposta", "Texto Original"])

    with tab1:
        video_id = st.text_input("Cole o ID de algum vídeo")

    submit_button = st.form_submit_button('Submit')

    with tab2:
        if submit_button:
            if not video_id:
                st.warning("Por favor, forneça um ID de vídeo.")
            else:
                try:
                    transcription.get_transcript_text(video_id)
                    with st.spinner("Carregando resposta com IA..."):
                        time.sleep(2)

                        if os.path.exists(file_path):
                            with open(file_path, "r", encoding="utf-8") as file:
                                transcript_text = file.read()
                                llm = LLM()
                                resposta = llm.call_llm(transcript_text, api)
                                st.markdown(resposta)
                        else:
                            st.warning("Transcrição não foi encontrada após a tentativa de geração.")

                except RuntimeError as e:
                    st.error(str(e))

    with tab3:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                st.write(file.read())
        else:
            st.info("Nenhuma transcrição encontrada ainda.")
