from data import get_dataset
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.image import array_to_img
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
            'dog', 'frog', 'horse', 'ship', 'truck']

def visualize_datasamples(number=25):
    """visualize number of data samples

    Parameters
    ----------
    number : int, optional
        number of datasamples to visualize, by default 25
    """
    (_, _), (test_images, test_labels) = get_dataset()


    plt.figure(figsize=(10,10))
    for i in range(number):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(test_images[i])
        plt.xlabel(class_names[test_labels[i][0]])
    plt.show()



# Plots a numpy array representing an image
def plot_array(array, label, pred=None):
  array = np.squeeze(array)
  img = array_to_img(array)
  plt.imshow(img)
  if pred is None:
    print(f"Image shows a {class_names[label]}.\n")
  else:
    print(f"Image shows a {class_names[label]}. Model predicted it was {class_names[pred]}.\n")

