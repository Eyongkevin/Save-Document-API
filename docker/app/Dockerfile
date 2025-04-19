FROM alpine:latest AS compile-image 

RUN apk add --update python3

RUN mkdir -p /opt/code
WORKDIR /opt/code 

RUN apk add python3-dev build-base gcc linux-headers

RUN python3 -m venv /opt/.venv 

ENV PATH="/opt/.venv/bin:$PATH"

RUN pip3 install --upgrade pip 

RUN pip3 install uwsgi==2.0.29

COPY requirements /opt/requirements
RUN pip3 install -r /opt/requirements/dev.txt



FROM alpine:latest AS runtime-image

LABEL maintainer="Eyong Kevin Enowanyo <tonyparkerkenz@gmail.com>"
LABEL description="This image provisions a uwsgi server that runs our flask app"

RUN apk add --update python3 curl && \
        rm -rf /var/cache/apk/*

RUN mkdir -p /opt/uwsgi 
COPY docker/app/uwsgi.ini /opt/uwsgi/
COPY docker/app/start_server.sh /opt/uwsgi/

RUN addgroup -S uwsgi && adduser -H -D -S uwsgi
USER uwsgi

COPY --chown=uwsgi:uwsgi --from=compile-image /opt/.venv /opt/.venv

ENV PATH="/opt/.venv/bin:$PATH"

COPY --chown=uwsgi:uwsgi src/ /opt/code/src
COPY --chown=uwsgi:uwsgi tests/ /opt/code/tests
COPY --chown=uwsgi:uwsgi wsgi.py /opt/code/

WORKDIR /opt/code

EXPOSE 5000

ENTRYPOINT [ "/bin/sh" ]

CMD ["/opt/uwsgi/start_server.sh"]
