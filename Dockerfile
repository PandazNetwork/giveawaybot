FROM python:3.9-slim-buster
RUN apt-get update -y && apt-get upgrade -y
RUN pip3 install -U pip
COPY . /GiveAwayBot
WORKDIR /GiveAwayBot
RUN chmod 777 /GiveAwayBot
RUN pip3 install --no-cache-dir -U -r requirements.txt
RUN gunicorn app:app & python3 main.py
