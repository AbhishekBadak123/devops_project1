# ☁️ CloudAutoX – AWS EKS Infrastructure Automation

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestrated-326CE5?logo=kubernetes&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-Automation-EE0000?logo=ansible&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20EKS-FF9900?logo=amazonaws&logoColor=white)

---

## 📖 Overview

**CloudAutoX** is a complete DevOps project that demonstrates end-to-end infrastructure automation — from provisioning AWS EC2 instances and EKS clusters using Ansible, to containerizing a Python Flask application with Docker, and deploying it on Kubernetes. This project showcases real-world DevOps practices including Infrastructure as Code (IaC), configuration management, containerization, and container orchestration.

---

## 🏗️ Architecture

```
Developer → GitHub → Ansible Automation → AWS EC2 → Docker Build → Push to DockerHub → Kubernetes (EKS) Deployment → NodePort Service → Browser
```

### Architecture Flow

1. **Developer** pushes code to **GitHub**
2. **Ansible** automates EC2 provisioning and Docker installation
3. **Docker** builds and pushes the container image to DockerHub
4. **Kubernetes** (EKS / local k3d) deploys the application with 2 replicas
5. A **NodePort Service** exposes the application for external access

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.10 (Flask)** | Web application framework |
| **Docker** | Containerization |
| **Kubernetes (EKS / k3d)** | Container orchestration |
| **Ansible** | Configuration management & IaC |
| **AWS EC2** | Cloud compute instances |
| **AWS EKS** | Managed Kubernetes service |
| **eksctl** | EKS cluster provisioning CLI |
| **Git & GitHub** | Version control |

---

## 📁 Project Structure

```
CloudAutoX_Project/
├── app/
│   └── app.py                  # Flask web application
├── Dockerfile                  # Docker image definition
├── k8s/
│   ├── deployment.yaml         # Kubernetes Deployment (2 replicas)
│   └── service.yaml            # Kubernetes NodePort Service
├── Ansible/
│   ├── inventory               # Ansible host inventory file
│   ├── docker-install.yml      # Playbook: Install Docker on Ubuntu
│   ├── ec2-provision.yml       # Playbook: Provision AWS EC2 instance
│   └── eks-cluster.yml         # Playbook: Create AWS EKS cluster
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Ensure the following tools are installed on your system:

- **Linux VM** (Ubuntu recommended)
- [Docker](https://docs.docker.com/get-docker/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) (configured with credentials)
- [eksctl](https://eksctl.io/installation/)
- [Git](https://git-scm.com/downloads)

### Step 1: Clone the Repository

```bash
git clone https://github.com/AbhishekBadak123/devops_project1.git
cd devops_project1/CloudAutoX_Project
```

### Step 2: Provision Infrastructure with Ansible

#### a) Provision an EC2 Instance

> **Note:** Update `<AMI_ID>` in `Ansible/ec2-provision.yml` with your desired Ubuntu AMI ID.

```bash
ansible-playbook Ansible/ec2-provision.yml
```

#### b) Install Docker on the EC2 Instance

> **Note:** Update `<EC2_PUBLIC_IP>` in `Ansible/inventory` with the public IP of your EC2 instance.

```bash
ansible-playbook -i Ansible/inventory Ansible/docker-install.yml
```

#### c) Create an EKS Cluster

```bash
ansible-playbook Ansible/eks-cluster.yml
```

This creates an EKS cluster named `cloudautox-cluster` in the `ap-south-1` region with a `t2.medium` node.

### Step 3: Build & Push the Docker Image

```bash
docker build -t <your-dockerhub-username>/cloudautox:v1 .
docker push <your-dockerhub-username>/cloudautox:v1
```

> **Note:** Update the `image` field in `k8s/deployment.yaml` to match your DockerHub image name.

### Step 4: Deploy to Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Step 5: Verify the Deployment

```bash
kubectl get pods
kubectl get svc
```

### Step 6: Access the Application

**Option A – Via NodePort (if on a cloud VM):**

```
http://<NODE-IP>:32448
```

**Option B – Via Port Forward (for local/VM environments):**

```bash
kubectl port-forward --address 0.0.0.0 svc/cloudautox-service 5050:80
```

Then open in your browser:

```
http://<VM-IP>:5050
```

---

## 🐳 Application Details

The Flask application (`app/app.py`) serves a simple web page that displays:

- **Application name:** CloudAutoX Application
- **Runtime environment:** Running inside Kubernetes
- **Pod hostname:** Dynamically shows the Kubernetes pod name (useful for verifying load balancing across the 2 replicas)

---

## 📋 Kubernetes Specifications

| Resource | Details |
|---|---|
| **Deployment** | `cloudautox-app` with **2 replicas** |
| **Container Port** | `5000` (Flask) |
| **Service Type** | `NodePort` |
| **Service Port** | `80` → `5000` (target) |
| **NodePort** | `32448` |

---

## ⚠️ Challenges Encountered & Solutions

| # | Challenge | Resolution |
|---|---|---|
| 1 | Docker Image Pull Error (`InvalidImageName`) | Corrected the image name format in `deployment.yaml` |
| 2 | SSH authentication issues with EC2 | Configured proper SSH key paths in the Ansible inventory |
| 3 | Docker installation package mismatch (`apt` vs `yum`) | Used `apt` package manager for Ubuntu-based servers |
| 4 | EKS nodegroup rollback with `t2` instances | Adjusted instance types and cluster configuration |
| 5 | LoadBalancer not available in local clusters | Switched to `NodePort` service type with port-forwarding |

---

## 🎯 Skills Demonstrated

- ✅ **Infrastructure as Code (IaC)** – Ansible playbooks for EC2 & EKS provisioning
- ✅ **Configuration Management** – Automated Docker installation across servers
- ✅ **Containerization** – Dockerized Python Flask application
- ✅ **Kubernetes Orchestration** – Multi-replica deployments with service exposure
- ✅ **Cloud Automation** – End-to-end AWS infrastructure automation

---

## 📄 License

This project is open source and available for learning and reference purposes.

---

## 👤 Author

**Abhishek Badak** — [GitHub Profile](https://github.com/AbhishekBadak123)
