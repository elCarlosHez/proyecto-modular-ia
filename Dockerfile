FROM python:3.10-slim
EXPOSE 5000/tcp
WORKDIR /app
COPY requirements.txt .
COPY model.pkl .
RUN pip install -r requirements.txt
COPY app.py .