
FROM python:3.8.5-slim

COPY ./data /data
COPY ./src /src
COPY ./model /model
COPY ./requirements.txt /src/requirements.txt
WORKDIR /src

RUN pip install -r requirements.txt
RUN pip install gunicorn

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app.main:app  QEWW