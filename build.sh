#!/usr/bin/env bash

# Render build script

set -o errexit  # exit on error

echo "=== Render Build Script ==="

# Install dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

echo "✅ Build completed successfully!" 