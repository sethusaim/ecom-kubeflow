#!bin/bash

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 566373416292.dkr.ecr.us-east-1.amazonaws.com

docker build -t 566373416292.dkr.ecr.us-east-1.amazonaws.com/ecom_model_training:latest ecom/model_training/

docker push 566373416292.dkr.ecr.us-east-1.amazonaws.com/ecom_model_training:latest
