
FROM python:3.8.5-slim

COPY ./data /data
COPY ./src /src
COPY ./models /src/models
COPY ./requirements.txt /src/requirements.txt
WORKDIR /src

RUN pip install -r requirements.txt


EXPOSE 80

CMD ["uvicorn", "app.main:app", "--port", "80", "--host", "0.0.0.0"]