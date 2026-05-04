#!/bin/bash
set -e

minikube start --nodes 3 --insecure-registry="192.168.100.10:5000"
minikube addons enable ingress
minikube addons enable metrics-server

kubectl get ns shopmicro >/dev/null 2>&1 || kubectl create namespace shopmicro

kubectl apply -f ~/shopmicro-project/k8s/

kubectl get pods -n shopmicro
kubectl get svc -n shopmicro
kubectl get ingress -n shopmicro
kubectl get hpa -n shopmicro
