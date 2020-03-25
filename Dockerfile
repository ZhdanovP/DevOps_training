FROM python:3.5

WORKDIR /usr/src/app

EXPOSE 8000

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install django==1.11

CMD [/bin/bash]
