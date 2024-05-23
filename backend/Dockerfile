FROM python:3.12-slim

WORKDIR /workspace/

COPY ./src /workspace/src

RUN pip install fastapi --no-cache-dir
RUN pip install uvicorn[standard] --no-cache-dir
RUN pip install pydantic --no-cache-dir
RUN pip install sqlalchemy --no-cache-dir
RUN pip install fastapi-limiter --no-cache-dir

RUN apt-get update
RUN apt-get install redis-server -y

COPY redis-server.sh /workspace/
RUN chmod +x /workspace/redis-server.sh

ENTRYPOINT ["/workspace/redis-server.sh"]