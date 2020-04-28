# Before building the container, copy the model to this folder.
# gsutil -m cp -r gs://<model location> .

# docker build -t gcr.io/cool-ml-demos/model_server:latest

FROM gcr.io/cloud-automl-tables-public/model_server

ADD fraud_creditcard /models/default/0000001