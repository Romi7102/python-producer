FROM python:3.11.2

WORKDIR /app

COPY requirements.txt ./
COPY main.py ./
COPY config.yaml ./
COPY config.py ./
COPY utils.py ./

RUN pip install -r requirements.txt

CMD [ "python" , "main.py" ]