
# CloudAutoX – AWS EKS Infrastructure Automation

## Overview
CloudAutoX demonstrates a DevOps pipeline that automates infrastructure provisioning,
containerization, and Kubernetes deployment using Ansible, Docker, and Kubernetes.

## Architecture
Developer → GitHub → Ansible Automation → EC2 DevOps Node → Docker Image → Kubernetes Deployment → Service → Browser

## Technologies
AWS EC2
Ansible
Docker
Kubernetes (EKS / local k3d)
GitHub
Linux

## Project Structure
CloudAutoX
 ├── app/
 │    └── app.py
 ├── Dockerfile
 ├── k8s/
 │    ├── deployment.yaml
 │    └── service.yaml
 └── Ansible/
      ├── inventory
      ├── docker-install.yml
      ├── ec2-provision.yml
      └── eks-cluster.yml

## Deployment Steps

### Build Docker Image
docker build -t <dockerhub-username>/cloudautox:v1 .
docker push <dockerhub-username>/cloudautox:v1

### Deploy to Kubernetes
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

### Verify
kubectl get pods
kubectl get svc

### Port Forward (for VM environments)
kubectl port-forward --address 0.0.0.0 svc/cloudautox-service 5050:80

Open in browser:
http://<VM-IP>:5050

## Challenges Encountered
1. Docker Image Pull Error (InvalidImageName)
2. SSH authentication issues with EC2
3. Docker installation package mismatch (apt vs yum)
4. EKS nodegroup rollback with t2 instances
5. LoadBalancer not available in local clusters

## Requirements
Linux VM
Docker
kubectl
Ansible
AWS CLI
eksctl
Git

## Skills Demonstrated
Infrastructure as Code
Configuration Management
Containerization
Kubernetes Orchestration
Cloud Automation
