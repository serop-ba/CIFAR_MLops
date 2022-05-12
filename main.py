from src.models import *
from src.data import get_dataset, save_test_images

if __name__ == "__main__":
    # download the dataset
    data = get_dataset()
    # save the test images into data/test
    save_test_images(data)
    # train for 10 epochs
    model = train_model(data, 10)
    # save the trained model
    save_model('models', model, '1')



