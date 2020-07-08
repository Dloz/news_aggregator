FROM python:3.6-alpine

RUN adduser -D news_aggregator
USER root

WORKDIR /home/news_aggregator

RUN apk add --no-cache --virtual .build-deps gcc musl-dev

COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN venv/bin/pip3 install -r requirements.txt
RUN venv/bin/pip3 install gunicorn

COPY app news_aggregator
COPY api.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP api.py

RUN chown -R news_aggregator:news_aggregator ./
USER news_aggregator

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]