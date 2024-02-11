FROM python:3.11.2

WORKDIR /app

COPY requirements.txt ./
COPY main.py ./

RUN apt update
RUN apt install inetutils-ping
RUN pip install -r requirements.txt

CMD [ "python" , "main.py" ]