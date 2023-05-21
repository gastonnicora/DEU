# DEU

## Arranque de aplicación de manera local (en una maquina con docker instalado)

1. En una terminal de comandos dirigirse a la ubicación donde esta docker-compose.ym
   - Ejemplo (suponiendo que estamos en home y la app esta en el escritorio):
   ```
    cd .\Desktop\DEU 
   ```
2. Ejecute el siguiente comando:
   docker-compose up

## Arranque desde [Docker Playground](https://labs.play-with-docker.com)

1. Iniciar sesión
2. Crear nueva instancia ("+ ADD NEW INSTANCE")
3. En la nueva instancia ingrese el comando:
   ```
    touch docker-compose.yml
   ```
4. Copiar el siguiente texto:

  ```
    version: '3.3'

    services:
    db:
        image: gastonnicora/deu_db
        ports:
        - "3306:3306"
        restart: always
        environment:
        MYSQL_ROOT_PASSWORD: root
        MYSQL_USER: tpdeu
        MYSQL_PASSWORD: tpdeu
        MYSQL_DATABASE: tpdeu  
    api:
        image: blancofrancisco/backend_laboratorio2022
        restart: always
        links:
        - db
        ports:
        - "8080:4000"
        - "80:80"
    phpmyadmin:
        image: phpmyadmin
        restart: always
        environment:
            PMA_HOST: db
            PMA_PORT: 3306
        ports:
        - 90:80
    ```
5. Presionar el botón "editor"
6. En la ventana emergente seleccionar el archivo "docker-compose.yml"
7. Pegar el texto anteriormente seleccionado, presionar el botón "SAVE" y cerrar ventana.
8. Ejecutar el siguiente código:
    ``` 
        docker-compose up
    ```