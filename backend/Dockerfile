FROM python:3.12-slim

WORKDIR /workspace/

COPY ./src /workspace/src
COPY ./main.py /workspace/

RUN pip install fastapi --no-cache-dir
RUN pip install uvicorn[standard] --no-cache-dir
RUN pip install pydantic --no-cache-dir
RUN pip install sqlalchemy --no-cache-dir

CMD uvicorn main:app --host 0.0.0.0 --port 8000