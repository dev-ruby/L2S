FROM python:3.12-slim

WORKDIR /workspace/

COPY ./src/requirements.txt /workspace/src/
RUN pip install --no-cache-dir -r /workspace/src/requirements.txt

RUN apt-get update && \
    apt-get install -y redis-server && \
    rm -rf /var/lib/apt/lists/*

COPY ./src /workspace/src

COPY redis-server.sh /workspace/
RUN chmod +x /workspace/redis-server.sh

ENTRYPOINT ["/workspace/redis-server.sh"]
