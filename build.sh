#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperadmin

python manage.py collectstatic --no-input
