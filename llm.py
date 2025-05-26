import os
from google import genai
from dotenv import load_dotenv


class LLM:
    def __init__(self):
        pass

    def get_api(self):
        load_dotenv()
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        return GEMINI_API_KEY

    def call_llm(self, content, api):
        client = genai.Client(api_key=api)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"""Você é especialista em escrever blogs, siga as instruções abaixo para realizar a tarefa:
                        - Escreva em Português Brasileiro
                        - O blog deve conter no máximo 500 palavras
                        - Use título, subtítulo
                        - Use sumário
                        - Use bullet points

                        INPUT: {content}
                        """,
        )

        return response.text
