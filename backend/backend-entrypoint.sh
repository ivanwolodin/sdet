#!/bin/sh

set -e

echo "Starting Uvicorn server..."
exec poetry run uvicorn app.main:app --host "$BACKEND_HOST" --port "$BACKEND_PORT"
