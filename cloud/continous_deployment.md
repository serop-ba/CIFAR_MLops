# User Guid

1. create a new service account with the following roles:
    a. Cloud Build Service Account
    b. Cloud Run Admin
    c. Cloud Run Service Agent
    d. Storage Admin
    
2. view the email adress of the created service using the following:
```
gcloud iam service-accounts list --project PROJECT_ID
```

3. create keys files for the service account using the following by replacing EMAIL-ADDRESS with the service email address:
 
```
gcloud iam service-accounts keys create ./keys.json --iam-account EMAIL-ADDRESS
```
4. add keys.json to gitignore

5. authenticate the service locally using 
```
gcloud auth activate-service-account --key-file=keys.json
```
6. create an app on google cloud run manually following the instructions from [google.md](google.md).

7. add the secretes specified in .github/workflows/main.yaml
8. the workflow will be triggered once a commit message contains to deploy is pushed.