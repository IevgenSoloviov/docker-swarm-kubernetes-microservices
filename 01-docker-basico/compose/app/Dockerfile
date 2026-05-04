FROM php:8.2-fpm-alpine

RUN apk add --no-cache bash \
    && docker-php-ext-install pdo pdo_mysql

RUN addgroup -g 1000 appgroup && adduser -G appgroup -u 1000 -D appuser
WORKDIR /var/www/html

COPY ./src/ /var/www/html

RUN chown -R appuser:appgroup /var/www/html
USER appuser
