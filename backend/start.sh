#! /bin/bash

# Wait for the DB to start
./wait-for-it.sh postgres:5432


python manage.py migrate --noinput

python manage.py runserver 0.0.0.0:80