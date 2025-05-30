#!/bin/sh
set -a
if [ -f .env ]; then
  . ./.env
fi
set +a
exec uvicorn astro.main:astro --host 0.0.0.0 --port ${PORT:-8000}
