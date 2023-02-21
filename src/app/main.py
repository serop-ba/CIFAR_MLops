import tensorflow
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
from pydantic import BaseModel
import tensorflow as tf
from typing import List
from fastapi import FastAPI, File, UploadFile, HTTPException
import logging
import sys
import io

logging.config.fileConfig('./app/logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)
app = FastAPI(title="Demo of CIFAR deployment")

classes = ['airplane', 'automobile', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


class PredictionResponse(BaseModel):
    """
    prediction response of the class 
    """
    class_name: str
    class_value: str


@app.on_event("startup")
def load_model():
    # Load classifier from pickle file
    global model
    model = tf.keras.models.load_model('../model/1')


@app.get("/")
def home():
    return "Great! The API is working as expected. Check the /docs extension for making predictions on the model"


@app.get("/hello")
async def hello():
    return "Hello there"

# 
@app.post("/predict/", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...),):
    if file.content_type.startswith('image/') is False:
        raise HTTPException(
            status_code=400, detail=f'File \'{file.filename}\' is not an image.')

    try:
        contents = await file.read()
        foto = Image.open(io.BytesIO(contents)).convert('RGB')
        input = image.img_to_array(foto)
        input = np.expand_dims(input, axis=0) / 255.
        logger.info(f"input dimensions: {input.shape}")
        preds = model.predict(input)[0]
        logger.info(f"predictions shape: {preds.shape}")
        index = np.argmax(preds)
        value = preds[index]

        return{
            'class_name': classes[index],
            'class_value': str(value)
        }
    except Exception as error:

        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == '__main__':
    app.run(debug=True)
