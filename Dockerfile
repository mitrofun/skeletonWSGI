FROM alpine:3.8

COPY . /opt/app

RUN apk update && apk add --update --no-cache --progress \
    make \
    python3 \
    git \
    ca-certificates \
    bash bash-completion \
    && update-ca-certificates 2>/dev/null || true \
    && apk add --no-cache --virtual=.build-dependencies \
    python3-dev \
    build-base \
    supervisor \
    nginx \
    linux-headers \
    pcre-dev \
    && pip3 install --upgrade pip setuptools \
    && pip3 install --no-cache-dir -r /opt/app/requirements/dev.txt


COPY deploy/nginx.conf /etc/nginx/nginx.conf
COPY deploy/nginx-site.conf /etc/nginx/conf.d/default.conf
COPY deploy/supervisord.conf /etc/supervisord.conf

WORKDIR /opt/app

EXPOSE 80

CMD ["/usr/bin/supervisord"]