FROM python:3.11-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app app

CMD ["python", "app/app.py"]