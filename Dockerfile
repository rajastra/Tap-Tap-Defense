# Dockerfile, Image, Container
FROM python:3.6

WORKDIR /Users/Christian/Documents/GitHub/Tap-Tap-Defense/game_assets
COPY game_assets ./

WORKDIR /Users/Christian/Documents/GitHub/Tap-Tap-Defense
ADD main.py .
ADD settings.py .
ADD classes.py .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python", "./main.py" ]