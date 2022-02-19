# docker run --name HomeWork_03 -p 8000:8000 blogapp

FROM python:3.9.9-buster
#FROM python:3.10.2-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip3 install poetry==1.1.12
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock
RUN poetry install --no-dev --no-ansi

COPY . .
EXPOSE 8000

CMD uvicorn main:app --host=0.0.0.0 --port=8000




