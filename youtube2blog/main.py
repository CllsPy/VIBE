from transcription import Transcription
from llm import LLM
import streamlit as st

st.set_page_config(
    page_title="IU2B",
    page_icon="https://cdn-icons-png.flaticon.com/512/10026/10026285.png"
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
st.markdown(quick_start_text)

st.markdown("""\n""")
st.markdown("""\n""")

id = st.text_input("Cole o ID de algum vídeo")
transcription = Transcription()
transcription.get_transcript_text(id)

with open("transcript.txt", "r") as file:
    file = file.read()
    llm_calling = LLM()
    st.markdown(llm_calling.call_llm(file))
