#1

FROM python:3.7

#2

RUN pip install Flask gunicorn

#3

COPY src/ /app
WORKDIR /app

#4

ENV PORT 8080

#5

