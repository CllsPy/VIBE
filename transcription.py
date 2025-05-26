import os
from youtube_transcript_api import YouTubeTranscriptApi

class Transcription:
    def __init__(self):
        # Define o caminho absoluto do arquivo transcript.txt
        self.transcript_path = os.path.join(os.getcwd(), "transcript.txt")

    def get_transcript_text(self, video_id):
        try:
            # Buscar transcrição
            transcript = YouTubeTranscriptApi.get_transcript(video_id)

            # Juntar o texto
            script = "\n".join([f"{item['text']}" for item in transcript])

            # Salvar a transcrição
            with open(self.transcript_path, "w", encoding="utf-8") as file:
                file.write(script)

            print("Transcript saved successfully!")

        except Exception as e:
            print(f"Error: {e}")
