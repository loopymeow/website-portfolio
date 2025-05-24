#!/bin/sh

# Waiting for the database to be ready
echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Database is ready!"

# Running migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collecting static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Starting Gunicorn
echo "Starting Gunicorn..."
exec gunicorn website.wsgi:application --bind 0.0.0.0:8000
