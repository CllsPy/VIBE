import os
import tempfile
from youtube_transcript_api import YouTubeTranscriptApi

class Transcription:
    def __init__(self):
        temp_dir = tempfile.gettempdir()
        self.transcript_path = os.path.join(temp_dir, "transcript.txt")

    def get_transcript_text(self, video_id):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            script = "\n".join([item['text'] for item in transcript])

            with open(self.transcript_path, "w", encoding="utf-8") as file:
                file.write(script)

        except Exception as e:
            raise RuntimeError(f"Erro ao obter transcrição: {e}")

    def get_path(self):
        return self.transcript_path
