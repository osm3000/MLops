FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
RUN make install
EXPOSE 8501
# ENTRYPOINT ["streamlit","run"]
# CMD ["streamlit", "run", "main.py"]
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
# ENTRYPOINT ["make", "run"]