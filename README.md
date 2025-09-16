# Video to Intelligent Blog Engine (Vibe)
![ui2b-ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/bf4e8f7d-34f8-4ffa-a451-041c13438bae)

This project is an automated pipeline that takes **YouTube videos** as input and generates **blog-style posts** as output. It combines transcription, natural language processing, and large language model capabilities (via Gemini API) to transform spoken video content into well-structured written articles.


## Project Description

The main objective of this project is to streamline content repurposing by turning long-form YouTube videos into readable, SEO-friendly blog posts. The workflow involves extracting transcripts from YouTube videos, processing the text, and leveraging the Gemini API to generate high-quality blog content.

The system is containerized with **Docker** to ensure easy setup, reproducibility, and portability.

## Steps

1. Extract video transcript from YouTube.
2. Process and clean the transcript.
3. Send the processed text to the Gemini API for blog-style generation.
4. Save the generated post into a structured format (Markdown or HTML).

## Requirements

### Languages & Tools

* **Python**: Scripting language for orchestration and processing.
* **Docker**: To containerize and run the project consistently across environments.
* **Gemini API**: Large language model API for generating high-quality blog posts.

### Python Packages

Install the following packages before running the code (if not using Docker):

```python
pytube
requests
python-dotenv
```

## Launch

### Using Docker

1. Clone the repository.
2. Build the Docker image:

   ```bash
   docker build -t yt2blog .
   ```
3. Run the container:

   ```bash
   docker run -it --env-file .env yt2blog
   ```

### Without Docker
1. Clone the repository.
2. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your **Gemini API key**.
4. Run the Python script:

   ```bash
   python main.py --url <YOUTUBE_VIDEO_URL>
   ```

## License
This project is licensed under the MIT License.

## Acknowledgements
* YouTube Data and Transcript APIs.
* Gemini API for natural language generation.
* Docker for simplifying deployment.
