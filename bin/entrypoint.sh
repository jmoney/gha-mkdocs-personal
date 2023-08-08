#!/bin/sh

mkdir -p ./docs
mkdir -p ./docs/img
cp /app/mkdocs.yml .
cp /app/favicon.ico ./docs/img
cp --recursive /app/hooks .

cp LICESNE ./docs/license.md

mkdocs build --clean