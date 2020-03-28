FROM python:3.6

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt

ARG LOGIN
ENV LOGIN $LOGIN

ARG PASSWORD
ENV PASSWORD $PASSWORD

RUN apt update \
    && pip3 install -r requirements.txt

COPY ./ /app

CMD  pytest
