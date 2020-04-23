FROM python:3.7-alpine
WORKDIR /web
COPY requirements.txt /web
RUN pip install -r requirements.txt
ENV FLASK_APP=manage.py
ENV FLASK_ENV=development