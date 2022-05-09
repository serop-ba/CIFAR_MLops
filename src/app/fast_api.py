from flask import Flask, jsonify, request, abort, render_template, send_file
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
import tensorflow as tf
from fastapi import FastAPI


app = FastApi(title="Demo of CIFAR deployment")

classes = ['airplane', 'automobile', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

@app.on_event("startup")
def load_model():
    # Load classifier from pickle file
    global model 
    model = tf.keras.models.load_model('/app/models/1')

@app.get("/")
def home():
    return "Great! The API is working as expected."


@app.post("/predict")
def predict(img):

    img = img.resize((32, 32), Image.ANTIALIAS)
    img = img.convert('RGB')
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.
    preds = model.predict(x)[0]
    return {classes[x]: float(preds[x]) for x in np.argsort(preds)[::-1][:3]}

if __name__ == '__main__':
    app.run(debug=True)