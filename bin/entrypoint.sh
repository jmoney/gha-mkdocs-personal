#!/bin/sh

mkdir ./docs/img
cp /app/mkdocs.yml .
cp /app/favicon.ico ./docs/img
cp /app/inject_git_repo.py .
mkdocs build --clean