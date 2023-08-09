#!/bin/sh

mkdir -p ./docs
mkdir -p ./docs/img
cp /app/mkdocs.yml .
cp /app/favicon.ico ./docs/img
cp --recursive /app/hooks .
cp --recursive /app/overrides .

[ -f ./docs/index.md ] || cp /app/index.md ./docs/index.md
cp LICENSE ./docs/license.md

mkdocs build --clean