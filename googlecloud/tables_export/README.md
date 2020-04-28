# AutoML Tables: Export and test your model on Kubernetes

This guide walks you through the process of exporting and testing your model from AutoML Tables on a Kubernetes cluster.\
The goal here is to demonstrate who to use an exported model from AutoML and a simple script to make request to it.

High level architecture of this tutorial:

![architecture](https://github.com/leiterenato/ml-samples/blob/master/googlecloud/tables_export/diagrams/architecture.png "Architecture")

ps.: For this example I create a model with the Creditcard dataset from Kaggle. (https://www.kaggle.com/mlg-ulb/creditcardfraud)

## Export the models from AutoML Tables

![export model](https://github.com/leiterenato/ml-samples/blob/master/googlecloud/tables_export/diagrams/export.png "Export Model")

After exporting the model, copy to your working machine and change the name of your folder to remove the timestamp (avoid naming problems).\
Example from documentation:
https://cloud.google.com/automl-tables/docs/model-export#run-server

> gsutil -m cp -r gs://{path the exported model} .
    
Change the last name to remove the timestamp (not supported by the Docker container).
    
> mv model-export/tbl/tf_saved_model-<model-name>-<export-timestamp> model-export/tbl/<new-dir-name>

Remember the path to your model, it will be used to copy to a docker image.

## Prepare the Container for model serving

From this repo, go to folder 'container_serving' and change the Dockerfile with the path to your model.

Dockerfile:
> FROM gcr.io/cloud-automl-tables-public/model_server\
> ADD {path to your model} /models/default/0000001

Build and push your image:
> docker build -t gcr.io/{your project}/model_server:latest .

> docker push gcr.io/{your project}/model_server:latest

(you can push the images to a local registry as well.)

Note that you must have the necessary permissions to push the image.

Run to check if everything is OK:
> docker run gcr.io/cool-ml-demos/model_server:latest
    
(optional) Make local predictions with the following curl command. First you need to create a file request.json.

> curl -X POST --data @/tmp/request.json http://localhost:8080/predict

## Prepare the Payload for request

Schema of a payload:
```
{ "instances": [ { "column_name_1": value, "column_name_2": value, … } , … ] }
```

In the file container_requester/local_request.py I fixed the request to simplify the example.

Example in my case (Fraud Creditcard example):
```{
    "instances": 
        [
            {
                "8496745483987845120":1,
                "282179763664060416":1,
                "2155677208650186752":1,
                "5614441722470727680":1,
                "9073206236291268608":1,
                "7920284731684421632":1,
                "4461520217863880704":1,
                "714525327891628032":1,
                "2443907584801898496":1,
                "1290986080195051520":1,
                "7055593603229286400":1,
                "3596829089408745472":1,
                "5902672098622439424":1,
                "8208515107836133376":1,
                "5326211346319015936":1,
                "3020368337105321984":1,
                "7632054355532709888":1,
                "1867446832498475008":1,
                "8784975860139556864":1,
                "4173289841712168960":1,
                "6479132850925862912":1,
                "2732137960953610240":1,
                "426294951739916288":1,
                "5037980970167304192":1,
                "7343823979380998144":1,
                "1579216456346763264":1,
                "3885059465560457216":1,
                "6190902474774151168":1,
                "1002755704043339776":1,
                "3308598713257033728":1
            }
        ]
}
```

## Prepare Kubernetes

First you need to create a Kubernetes cluster or use an existing cluster.\
Understing the files in folder kubernetes/:

> kubernetes/model_deployment.yaml

Please chenge the path to your image
```
      containers:
        - name: model
          image: {path to your image}
          ports:
            - name: http
              containerPort: 8080
```

> kubernetes/model_service.yaml

This is a L4 (TCP) load balancer, but you can build more sofisticated architecture with Ingress.

> kubernetes/requester_deploy.yaml

Change the URL to your model.
Get this value from the services deployed.
```
...
          env:
            - name: URL
              value: "http://35.230.177.138:8080/predict"
          ports:
            - name: http
              containerPort: 8080
```

For each .yaml file, execute:
> kubectl apply -f {file_name}

After the model and requester are deployed, your can increase the number of nodes in your cluster, the number of PODs in your serving and requester.