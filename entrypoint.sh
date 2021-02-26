#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

# running with guicorn
# gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000

gunicorn portfolio.wsgi:application --bind 0.0.0.0:$PORT config.wsgi