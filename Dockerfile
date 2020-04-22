FROM python:3.7-alpine
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=manage.py
ENV FLASK_ENV=development