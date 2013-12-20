#!/bin/sh

set -e

rm -rf venv || true
virtualenv-2.7 --distribute venv
. venv/bin/activate
pip install -r perfmon/requirements.txt

