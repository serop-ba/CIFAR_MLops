# FROM node:12-alpine as builder
# COPY ./ui /ui
# WORKDIR /ui
# RUN npm ci
# RUN npm run build

FROM frolvlad/alpine-miniconda3:python3.7
COPY ./src /app
COPY ./models /app/models
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app


# COPY --from=builder /ui/build ./build
RUN pip install -r requirements.txt
# RUN bash ./ui_cd.sh

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]