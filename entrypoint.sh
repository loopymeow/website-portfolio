#!/bin/sh

# Waiting for the database to be ready
echo "Waiting for database..."
until python manage.py migrate; do
  sleep 1
done
echo "Database is ready!"

# Running migrations
echo "Running migrations..."
python3 manage.py migrate --noinput

# Collecting static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Starting Gunicorn
echo "Starting Gunicorn..."
exec gunicorn website.wsgi:application --bind 0.0.0.0:8000
