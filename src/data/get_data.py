# -*- coding: utf-8 -*-
from pkgutil import get_data
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def get_dataset():
    """Downloads the dataset and normalize it 
    """
    (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
    assert train_images.shape == (50000, 32, 32, 3)
    assert test_images.shape == (10000, 32, 32, 3)
    assert train_labels.shape == (50000, 1)
    assert test_labels.shape == (10000, 1)

    train_images, test_images = train_images / 255.0, test_images / 255.0
    return (train_images, train_labels), (test_images, test_labels)

def save_test_images(data, number: int=12):
    """save a number of test images for testing the API

    Parameters
    ----------
    number : int
        number of test images to save
    """
    (_, _), (test_images, test_labels) = data
    for i in range(number):
        if not os.path.exists(os.path.join('data/test', str(test_labels[i][0]))):
            os.mkdir( os.path.join('data/test', str(test_labels[i][0])))


        plt.imsave(os.path.join(f'data/test/{test_labels[i][0]}', f'im_{i}.PNG'),test_images[i])


if __name__ == '__main__':
    get_dataset()
