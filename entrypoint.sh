#!/bin/bash
# Entrypoint script for Django application in Docker

set -e

echo "Starting EcommerceFinal application..."

# Wait for database to be ready
echo "Waiting for database to be ready..."
until python manage.py shell -c "import django; django.setup(); from django.db import connection; connection.ensure_connection()" 2>/dev/null; do
  echo "Database unavailable, waiting..."
  sleep 3
done

echo "Database is ready!"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create cache table (if using database cache)
echo "Creating cache table..."
python manage.py createcachetable || true

echo "Starting Django application with Gunicorn..."

# Start Gunicorn
exec gunicorn \
  --bind 0.0.0.0:8000 \
  --workers 4 \
  --worker-class sync \
  --worker-tmp-dir /dev/shm \
  --timeout 120 \
  --access-logfile - \
  --error-logfile - \
  --log-level info \
  EcommerceFinal.wsgi:application
