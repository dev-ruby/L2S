#!/bin/sh

redis-server &

exec uvicorn src:app --host 0.0.0.0 --port 8000