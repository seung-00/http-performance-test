FROM ubuntu:20.04

USER root

ENV DEBIAN_FRONTEND=noninteractive 

COPY ./src/server /home
WORKDIR /home

RUN apt-get update && apt-get -y install \
python3-pip \
golang \
nodejs \
python3 \
npm \
&& npm install \
&& pip3 install pymysql

EXPOSE 80
