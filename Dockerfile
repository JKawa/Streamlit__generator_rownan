FROM python:3.8.13

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY App.py App.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "App.py", "--server.port=8501", "--server.address=0.0.0.0"]


