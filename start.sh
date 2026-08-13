#!/usr/bin/env bash
set -e
echo "Starting Replit deployment script..."
# create venv if missing
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec gunicorn backend.wsgi:application --bind 0.0.0.0:8000
