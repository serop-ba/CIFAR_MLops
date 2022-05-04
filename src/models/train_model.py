import tensorflow as tf
from data import *
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import os 

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


def train_model(data, epochs):
    """fetch the dataset and train the model
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


def evaluate_model(model, test_images, test_labels):
    """evaluate a trained model using the test data 

    Parameters
    ----------
    model : _type_
        _description_
    test_images : _type_
        _description_
    test_labels : _type_
        _description_
    """
    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
    print(f"Test loss: {test_loss} - accuracy: {test_acc}")


def save_model(path, model, version):
    """save trained model in savedModel format

    Parameters
    ----------
    path : str
        path to save the model
    model : _type_
        _description_
    version : int
        version number of the model
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

