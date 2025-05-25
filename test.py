from transcription import Transcription
from llm import LLM


transcription = Transcription()
transcription.get_transcript_text("zfw4yPvQ9fo")

with open("transcript.txt", "r") as file:
    file = file.read()

llm_calling = LLM()
llm_calling.call_llm(file)
