FROM  python:3.8.16-alpine3.18


WORKDIR /app

COPY ./API/ . 

RUN pip3 --no-cache-dir install -r requirements.txt
RUN set environment="development"
CMD ["python3","run.py"]