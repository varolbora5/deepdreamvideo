FROM python:3.9.15-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt update; apt install -y libgl1 \
libglib2.0-0 libsm6 libxrender1 libxext6

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]
