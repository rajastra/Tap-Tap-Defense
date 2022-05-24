FROM python:3.6

COPY game_assets /game_assets
COPY main.py .
COPY classes.py .
COPY settings.py .

RUN pip3 install pygame

CMD ["python", "/main.py"]