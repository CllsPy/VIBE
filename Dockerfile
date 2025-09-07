FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "youtube2blog/main.py", "--server.port=8501", "--server.address=0.0.0.0"]

