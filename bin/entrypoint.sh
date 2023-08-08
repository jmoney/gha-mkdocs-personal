#!/bin/sh

mkdir ./docs/img
cp /app/mkdocs.yml .
cp /app/favicon.ico ./docs/img
cp --recursive /app/hooks .
mkdocs build --clean