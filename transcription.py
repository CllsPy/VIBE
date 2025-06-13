import os
from youtube_transcript_api import YouTubeTranscriptApi

class Transcription:
    def __init__(self, path=None):
        if path is None:
            path = os.path.join(os.path.dirname(__file__), "transcript.txt")
        self.transcript_path = path

    def get_transcript_text(self, video_id):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            script = "\n".join([f"{item['text']}" for item in transcript])

            with open(self.transcript_path, "w", encoding="utf-8") as file:
                file.write(script)

            print("Transcript saved successfully!")

        except Exception as e:
            print(f"Error: {e}")
