FROM python:3.14.8-alpine3.24

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD pytest -v