
# User Guide
This tutorial shows the ways to replicate the deployment of this FastApi on Google cloud. 

I'm going to use google cloud sdk docker image since it is an easier way to use the google cloud commands.

Start by pulling the docker image 

```
docker pull google/cloud-sdk:latest
```

You can verify the install using:

```
docker run -ti  google/cloud-sdk:latest gcloud version
```

To authenticate into your google cloud account use the following: 

```
gcloud auth login --no-browser
```
After that post the entire output into another terminal outside the container and authenticate using the instructions.

You can mount your current directory and create a docker container from your image using the following. Replace pwd with the directory path if you are on windows or use it in powershell: 
```
docker run -it --rm -v $(pwd):/work -w /work --entrypoint /bin/bash google/cloud-sdk:latest
```

You need to create a project if you haven't already. 


```
gcloud projects create CIFARMlops
gcloud config set project CIFARMlops
```

you can get the id of the current project using the following 
```
gcloud config get-value project
```

then you can send build the container the google build service  using:

```
gcloud builds submit --tag gcr.io/{MY-PROJECT-ID}/first_test
```
You can test your build before deployment locally using the following command
```
PORT=8080 && docker run -p 9090:${PORT} -3 PORT=${PORT} gcr.io/{MY-PROJECT-ID}/first_test
```

You can deploy the container using docker build using the following command:

```
gcloud run deploy --image gcr.io/{MY-PROJECT-ID}/first_test
```

You can then test the server using a REST API service such as Postman or Insomnia. 

For postman you can send a file using the post request by chosing form-data then then file as parameter with the file name in the value.

You can check my deployed server on google using the following link: 

https://first-test-noi376kdgq-uc.a.run.app/docs

