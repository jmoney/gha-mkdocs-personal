#!/bin/sh

mkdir ./docs/img
cp /app/mkdocs.yml .
cp /app/favicon.ico ./docs/img
mkdocs build --clean