FROM ubuntu:20.04

USER root

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update
RUN apt-get -y install golang
RUN apt-get -y install nodejs
RUN apt-get -y install python3
COPY ./src/server /home

EXPOSE 80
