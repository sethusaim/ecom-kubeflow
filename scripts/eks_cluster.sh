#!bin/bash

eksctl create cluster --name kubeflow --version 1.23 --region us-east-1 --zones us-east-1a,us-east-1b --nodegroup-name kubeflow-nodes --node-type t2.large --nodes-min 2 --nodes-max 4 --with-oidc