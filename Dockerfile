FROM python:3.10.12-slim

WORKDIR /app

COPY src ./src
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "src/producer.py"]