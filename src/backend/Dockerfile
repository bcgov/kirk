FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1
ENV LANG C.UTF-8

WORKDIR /api
COPY . /api/

# apk update
RUN apk add --no-cache curl py3-psycopg2 libpq postgresql-client

RUN apk add --virtual build-dependencies --no-cache  pkgconfig  openssl-dev postgresql-libs  make gcc libffi-dev  musl-dev postgresql-dev  \
    && python3 -m pip install -r /api/requirements.txt \
    && apk del build-dependencies

ENV PYTHONPATH='/usr/local/lib/python3.8/site-packages:/usr/lib/python3.8:/usr/lib/python3.8/site-packages'
