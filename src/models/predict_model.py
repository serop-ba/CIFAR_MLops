from sklearn.semi_supervised import LabelSpreading
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
from ..visualization import *


def get_test_data():
    """get the test data saved in data/test

    Returns
    -------
    data_imgs: np.ndarray
        test images
    labels: np.ndarray
        test labels
    """

    # Normalize pixel values
    test_datagen = ImageDataGenerator(rescale=1./255)

    # Point to the directory with the test images
    val_gen_no_shuffle = test_datagen.flow_from_directory(
        './data/test',
        target_size=(32, 32),
        batch_size=3,
        class_mode='binary',
        shuffle=True)

    # Print the label that is assigned to each class
    print(f"labels for each class in the test generator are: {val_gen_no_shuffle.class_indices}")
    # Get a batch of 32 images along with their true label
    data_imgs, labels = next(val_gen_no_shuffle)

    # Check shapes
    print(f"data_imgs has shape: {data_imgs.shape}")
    print(f"labels has shape: {labels.shape}")
    return data_imgs, labels

    
def serve_model(model_path:str, model_name:str, model_version: str):
    """_summary_

    Parameters
    ----------
    model_path : str
        model path
    model_name : str
        model version
    """
    # Define an env variable with the path to where the model is saved
    os.environ["MODEL_DIR"] = model_path
    import json
    data_imgs, labels = get_test_data()
    # Convert numpy array to list
    data_imgs_list = data_imgs.tolist()

    # Create JSON to use in the request
    import requests
    data = json.dumps({"instances": data_imgs_list})

    # Define headers with content-type set to json
    headers = {"content-type": "application/json"}

    # Capture the response by making a request to the appropiate URL with the appropiate parameters
    json_response = requests.post(f'http://localhost:8501/v1/models/{model_name}/versions/{model_version}:predict', data=data, headers=headers)

    # Parse the predictions out of the response
    predictions = json.loads(json_response.text)['predictions']

    # Print shape of predictions
    print(f"predictions has shape: {np.asarray(predictions).shape}")

        # Compute argmax
    preds = np.argmax(predictions, axis=1)

    # Print shape of predictions
    print(f"preds has shape: {preds.shape}")

    for i in range(10):
        plot_array(data_imgs[i], labels[i], preds[i])



