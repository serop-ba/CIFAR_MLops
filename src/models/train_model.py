import tensorflow as tf
from ..data import *
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import tensorflow.keras as keras
import os 
import numpy as np

def get_untrained_model():
    """Get the model to train

    Returns
    -------
    model: 
        untrained_model
    """
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10))

    model.summary()

    return model


def train_model(data:tuple, epochs:int):
    """Train a model on the data for the specified epochs

    Parameters
    ----------
    data : tuple
        data to train the model
    epochs : int
        number of epochs

    Returns
    -------
    model: tf.keras.models.Sequential
        trained model
    """
    (train_images, train_labels), (test_images, test_labels) = data
    model = get_untrained_model()
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

    history = model.fit(train_images, train_labels, epochs=epochs, 
                        validation_data=(test_images, test_labels))
    print(history)
    return model


def evaluate_model(model:tf.keras.models.Sequential, test_images:np.ndarray, test_labels:np.ndarray):
    """Evaluate a trained model using the test dat

    Parameters
    ----------
    model : tf.keras.models.Sequential
        trained model
    test_images : np.ndarray
        test images
    test_labels : np.ndarray
        labels of trained images
    """
    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
    print(f"Test loss: {test_loss} - accuracy: {test_acc}")


def save_model(path:str, model:tf.keras.models.Sequential, version: str):
    """save trained model in savedModel format

    Parameters
    ----------
    path : str
        path to save the model 
    model : tf.keras.models.Sequential
        trained model 
    version : str
        version of the trained model
    """

    export_path = os.path.join(path, str(version))
    print('export_path = {}\n'.format(export_path))

    tf.keras.models.save_model(
        model,
        export_path,
        overwrite=True,
        include_optimizer=True,
        save_format=None,
        signatures=None,
        options=None
    )
    print('\nSaved model successfully')

