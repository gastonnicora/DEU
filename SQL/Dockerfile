FROM mariadb
WORKDIR /app

COPY . /app 
COPY ./app/script/ /docker-entrypoint-initdb.d/

