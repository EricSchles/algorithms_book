FROM python:3.6-slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 80

ENV NAME HelloWorld

ENTRYPOINT ["python", "hello_world.py"]