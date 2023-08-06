FROM alpine:3.16

COPY bin /app/bin
RUN chmod +x /app/bin/entrypoint.sh

ADD requirements.txt /app/requirements.txt

RUN apk add --no-cache python3 py3-pip
RUN pip install -r /app/requirements.txt

ENTRYPOINT [ "/app/bin/entrypoint.sh" ]