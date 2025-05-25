from youtube_transcript_api import YouTubeTranscriptApi


class Transcription:
    def __init__(self):
        pass

    def get_transcript_text(self, video_id):
        try:
            # Fetch the transcript
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            # Combine transcript lines
            script = "\n".join([f"{item['text']}" for item in transcript])
            # Save the transcript to a file
            with open("transcript.txt", "w") as file:
                file.write(script)
            print("Transcript saved successfully!")
        except Exception as e:
            print(f"Error: {e}")
