FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get install -y libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev

RUN apt-get update
RUN apt-get install -qqy x11-apps

RUN pip3 install pygame

WORKDIR /app

ADD . .

ENV NAME World


CMD ["python3", "main.py", "-w", "-d"]
