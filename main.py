from src.models import *
from src.data import get_dataset, save_test_images

if __name__ == "__main__":
    data = get_dataset()
    save_test_images(data)
    model = train_model(data, 10) 
    evaluate_model(model, data[1][0], data[1])[1]
    save_model('models', model, '1.0.0')
    serve_model('models', 'cifar_classifier')




