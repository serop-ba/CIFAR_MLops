from flask import Flask, jsonify, request, abort, render_template, send_file
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
import tensorflow as tf


app = Flask(title="Demo of CIFAR deployment")

classes = ['airplane', 'automobile', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

def predict(img):
    img = img.resize((32, 32), Image.ANTIALIAS)
    img = img.convert('RGB')
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.
    preds = model.predict(x)[0]
    return {classes[x]: float(preds[x]) for x in np.argsort(preds)[::-1][:3]}

@app.on_event("startup")
def load_clf():
    # Load classifier from pickle file
    global model 
    model = tf.keras.models.load_model('/app/models/trained_model')

@app.route("/")
def home():
    return "Great! The API is working as expected."


@app.route("/classify", methods=['POST'])
def classify():
    file = request.files['query_img']
    try:
        img = Image.open(file.stream)
    except:
        abort(400)
    return jsonify(predict(img))

if __name__ == '__main__':
    app.run(debug=True)