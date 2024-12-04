#!/bin/sh
python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py shell < tools/run.py

celery -A bitly worker -l info &

python3 manage.py runserver 0.0.0.0:8000
