from data import get_dataset
import matplotlib.pyplot as plt

def visualize_datasamples(number=25):
    """visualize number of data samples

    Parameters
    ----------
    number : int, optional
        number of datasamples to visualize, by default 25
    """
    (_, _), (test_images, test_labels) = get_dataset()
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

    plt.figure(figsize=(10,10))
    for i in range(number):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(test_images[i])
        plt.xlabel(class_names[test_labels[i][0]])
    plt.show()