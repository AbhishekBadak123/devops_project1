
# KubeDeploy – Kubernetes Application Orchestration

This project demonstrates how to deploy a containerized Python Flask application
to Kubernetes using Deployment and Service manifests.

## Steps

1. Build Docker image
2. Push image to Docker Hub
3. Apply Kubernetes deployment
4. Expose application using service
5. Manage pods and scale application

## Run Commands

docker build -t kube-deploy-app .
docker tag kube-deploy-app username/kube-deploy-app:v1
docker push username/kube-deploy-app:v1

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods
kubectl get svc
