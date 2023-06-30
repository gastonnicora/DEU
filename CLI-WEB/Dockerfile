

FROM node:14.18-alpine as build-stage
WORKDIR /app
COPY ./CLI-WEB/package*.json ./
RUN npm install
COPY ./CLI-WEB/ .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY ./CLI-WEB/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]