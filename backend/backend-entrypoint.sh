#!/bin/sh

set -e

echo "Starting Uvicorn server..."
poetry run pytest -v -s --disable-warnings tests/
exec poetry run uvicorn app.main:app --host "$BACKEND_HOST" --port "$BACKEND_PORT"
