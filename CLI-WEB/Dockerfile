FROM node:9.11.1-alpine



# hacer la carpeta 'app' el directorio de trabajo actual
WORKDIR /app

# copiar los archivos y carpetas del proyecto al directorio de trabajo actual (es decir, la carpeta 'app')
COPY . ./app

# instalar dependencias del proyecto
RUN npm install ./CLI-WEB/package.json

# instalar un simple servidor http para servir nuestro contenido estático
RUN npm install  http-server

# construir aplicación para producción minificada
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]