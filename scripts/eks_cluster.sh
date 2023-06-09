#!bin/bash

eksctl create cluster --name kubeflow --version 1.22 --region us-east-1 --zones us-east-1a,us-east-1b --nodegroup-name kubeflow-nodes --node-type t2.large --nodes-min 3 --nodes-max 4 --with-oidc

kubectl patch svc istio-ingressgateway -n istio-system -p '{"spec":{"type":"LoadBalancer"}}'

kubectl get svc istio-ingressgateway -n istio-system 