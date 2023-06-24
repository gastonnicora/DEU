FROM  python:3.8.16-alpine3.18


WORKDIR /app

COPY . /app 

RUN pip3 --no-cache-dir install -r ./API/requirements.txt

CMD ["python3","./API/run.py"]