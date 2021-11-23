FROM python:3.9
LABEL maintainer="nikita31416@yandex.ru"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
EXPOSE 5050
VOLUME /app/models
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]