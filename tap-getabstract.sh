#!/bin/sh

# This simple script allows you to test your tap from any directory, while still taking
# advantage of the poetry-managed virtual environment.
# Adapted from: https://github.com/python-poetry/poetry/issues/2179#issuecomment-668815276

unset VIRTUAL_ENV

STARTDIR=$(pwd)
TOML_DIR=$(dirname "$0")

cd "$TOML_DIR" || exit
"/Users/giovanni/Library/Application Support/pypoetry/venv/bin/poetry" install 1>&2
"/Users/giovanni/Library/Application Support/pypoetry/venv/bin/poetry" run tap-getabstract $*
