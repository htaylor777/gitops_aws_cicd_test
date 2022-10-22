# syntax=docker/dockerfile:1


FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV PORT 5000
ENV SERVER_NAME "192.168.59.103:5000"
EXPOSE 5000
COPY . .

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD [ "python3", "-m" , "flask", "run", "--host=192.168.59.103"]
