FROM alpine:3.16

COPY bin bin
RUN chmod +x bin/entrypoint.sh

ADD requirements.txt requirements.txt

RUN apk add --no-cache python3 py3-pip
RUN pip install -r requirements.txt

ADD mkdocs.yml mkdocs.yml
ADD favicon.ico favicon.ico

ENTRYPOINT [ "bin/entrypoint.sh" ]