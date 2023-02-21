CIFAR_Mlops
==============================

A machine learning pipeline that applies best practices of MLops on classification task using the benchmark dataset CIFAR10. This project serves as a basic tutorial for maintaining and developing a machine learning pipeline from data acquisition to model monitoring from scratch

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   └── test            <- Test data for testing the API   
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── get_data.py
    │   │
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions and deployment
    │   │   ├── deploy_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

# User Guide

Serving deep learning model thorugh API.

### Installation

Used **fastapi, tensorflow** mainly to create this project. You can use requirements.txt to install appropriate package version. First, create a virtual environment before installing any packages.
```
pip install -r requirements.txt
```
>Note: The model was trained on Google Colab with GPU support.

### About Project 

The idea behind this project is to serve a model's predictions throught an api which can then be attached to a frontend webframe for visualizing the results or uploading the input data. To do this, i used FastApi, which is very light and Flask like framework and written in python.

CIFAR10 dataset was used in this project. 

The project was designed in such a way that anyone can clone/download and run the projcet without any tweaking.

### How to run the app

After installing necessary packages,run the main.py to train a model and to donwload a test set. AFter that you can start the server using the following command to run the app from project root directory:

```
uvicorn app.main:app --port 5000
```
Then, visit **http://127.0.0.1:5000/docs** from your browser. You will be able to see swagger, which is a built in UI interface that let's you test the functions you just wrote in fastapi. From there you can upload an image through *predict* endpoint and get a json response with the prediction output. Here you add click on try it yourself and upload a test image from the test directory and get the model's response.

Use *--reload* argument if you want to change code and see the effect immediately.

>To Run the Test Cases Use *pytest* command from project root directory.

### How to run the app with docker

Make sure you are in the project root directory and you have **started docker, trained a model and have downloaded the test data**. Then create docker image using the following command.

```
docker build -t fastapi-demo .
```
After the image is successfully built, run the following commands to run the container.

```
docker run -p 5000:80 fastapi-demo
```
And visit **http://127.0.0.1:5000/docs** from your browser. You will be able to see swagger. From there you can upload an image through *predict* endpoint and then you will get a json response.

### Model Training and Performance

Model performance wasn't the main focus of this project. So, I didn't try much to improve the model performance.

All the files related to training can be found in the *deep_learning_model/training* folder.

### Personal Feedback About The Project
- More work on making the project modular is needed.


>NOTE: Please, raise issue if you find an area where it needs some improvement.

### Future Plan

This projects isn't upto the production standard at all. I will be updating this periodically.

Though I have plan to work on the following improvements:

- [ ] CI/CD pipeline
- [ ] Adding experiments tracking
- [ ] Adding model versioning
- [ ] Adding Kubeflow pipeline 
- [ ] Deploying using kubernetes
- [ ] deploying the project on GCP
- [ ] Add tracking tools for the project
