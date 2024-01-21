#!/usr/bin/env bash

pip install  virtualenv

python3 -m venv venv

source venv/bin/activate

pip install -r req.txt

python3 manage.py runserver