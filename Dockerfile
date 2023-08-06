FROM alpine:3.16

COPY bin ${GITHUB_WORKSPACE}
RUN chmod +x bin/entrypoint.sh

ADD requirements.txt ${GITHUB_WORKSPACE}/requirements.txt

RUN apk add --no-cache python3 py3-pip
RUN pip install -r ${GITHUB_WORKSPACE}/requirements.txt

ADD mkdocs.yml ${GITHUB_WORKSPACE}/mkdocs.yml
ADD favicon.ico ${GITHUB_WORKSPACE}/favicon.ico

ENTRYPOINT [ "entrypoint.sh" ]