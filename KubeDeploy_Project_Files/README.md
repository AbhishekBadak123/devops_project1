# 🚀 KubeDeploy – Kubernetes Application Orchestration

> A hands-on DevOps project — build, containerize, and deploy a Python (Flask) web application on Kubernetes using Deployment and Service manifests.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-green?logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes&logoColor=white)

---

## 📖 Project Overview

**KubeDeploy** demonstrates the complete workflow of deploying a containerized Python Flask application to a Kubernetes cluster. The project covers building a Docker image, pushing it to Docker Hub, and orchestrating it on Kubernetes with Deployments and Services.

### What it does
- Serves a dynamic web page showing:
  - ✅ Application status
  - 🖥️ Pod hostname (demonstrating Kubernetes pod identity)
- Runs **2 replicas** for high availability
- Exposes the application via a **NodePort** service on port `30007`

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────┐
│                  Developer                       │
│           (Code + Docker Build)                  │
└──────────────┬───────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────┐
│            Docker Hub Registry                   │
│        (Container Image Storage)                 │
└──────────────┬───────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────┐
│         Kubernetes Cluster (Minikube)            │
│  ┌────────────────────────────────────────────┐  │
│  │         Deployment (2 Replicas)            │  │
│  │  ┌──────────────┐  ┌──────────────┐       │  │
│  │  │   Pod 1      │  │   Pod 2      │       │  │
│  │  │  Flask:5000  │  │  Flask:5000  │       │  │
│  │  └──────────────┘  └──────────────┘       │  │
│  └────────────────────────────────────────────┘  │
│  ┌────────────────────────────────────────────┐  │
│  │    Service (NodePort: 30007 → 5000)        │  │
│  └────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────┘
```

---

## 🧰 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.10** | Application runtime |
| **Flask** | Lightweight web framework |
| **Docker** | Containerization |
| **Kubernetes** | Container orchestration |
| **Minikube** | Local Kubernetes cluster |
| **Docker Hub** | Container image registry |

---

## 📁 Project Structure

```
KubeDeploy_Project_Files/
├── app/
│   └── app.py               # Flask application (main entry point)
├── k8s/
│   ├── deployment.yaml       # Kubernetes Deployment manifest (2 replicas)
│   └── service.yaml          # Kubernetes Service manifest (NodePort)
├── Dockerfile                # Docker build instructions
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 📄 Application Code

The Flask application (`app.py`) serves a dynamic HTML page displaying the Kubernetes pod hostname:

```python
from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>KubeDeploy Application</h1>
    <p>Running inside Kubernetes!</p>
    <p>Pod Hostname: {socket.gethostname()}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## 🐳 Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ ./app

EXPOSE 5000

CMD ["python", "app/app.py"]
```

---

## ☸️ Kubernetes Manifests

### Deployment (`k8s/deployment.yaml`)

- Creates **2 replicas** of the Flask application
- Uses the Docker Hub image `username/kube-deploy-app:v1`
- Exposes container port `5000`

### Service (`k8s/service.yaml`)

- **Type:** NodePort
- **Port mapping:** External `30007` → Service `80` → Container `5000`
- Enables external access to the application

---

## ⚙️ Prerequisites

- **Docker** installed ([Install Guide](https://docs.docker.com/get-docker/))
- **Minikube** installed ([Install Guide](https://minikube.sigs.k8s.io/docs/start/))
- **kubectl** installed ([Install Guide](https://kubernetes.io/docs/tasks/tools/))
- **Docker Hub** account (for pushing images)

---

## ▶️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AbhishekBadak123/devops_project1.git
cd devops_project1/KubeDeploy_Project_Files
```

### 2️⃣ Build the Docker Image

```bash
docker build -t kube-deploy-app .
```

### 3️⃣ Tag & Push to Docker Hub

```bash
docker tag kube-deploy-app <your-dockerhub-username>/kube-deploy-app:v1
docker push <your-dockerhub-username>/kube-deploy-app:v1
```

> **Note:** Update the `image` field in `k8s/deployment.yaml` with your Docker Hub username before deploying.

### 4️⃣ Start Minikube

```bash
minikube start
```

### 5️⃣ Deploy to Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 6️⃣ Access the Application

```bash
minikube service kube-deploy-service
```

Or manually navigate to:

```
http://<MINIKUBE_IP>:30007
```

You should see the **KubeDeploy Application** page showing the pod hostname.

---

## 🔍 Useful Commands

```bash
# Check running pods
kubectl get pods

# Check services
kubectl get svc

# View pod logs
kubectl logs -f <pod-name>

# Scale the deployment
kubectl scale deployment kube-deploy-app --replicas=4

# Describe the deployment
kubectl describe deployment kube-deploy-app

# Delete all resources
kubectl delete -f k8s/
```

---

## 🔄 Scaling & Self-Healing

Kubernetes provides **built-in scaling and self-healing**:

```bash
# Scale up to 4 replicas
kubectl scale deployment kube-deploy-app --replicas=4

# Watch pods being created
kubectl get pods -w

# Delete a pod and watch Kubernetes recreate it
kubectl delete pod <pod-name>
```

---

## 🧠 Key Learnings

- **Containerization** — Writing a Dockerfile and building images
- **Container Registry** — Tagging and pushing images to Docker Hub
- **Kubernetes Deployments** — Declarative pod management with replicas
- **Kubernetes Services** — Exposing applications using NodePort
- **Scaling** — Horizontal scaling with `kubectl scale`
- **Self-Healing** — Kubernetes automatically restarts failed pods
- **Pod Identity** — Each pod gets a unique hostname visible in the app

---

## 🛠️ DevOps Workflow Summary

```
Code → Docker Build → Docker Push → kubectl Apply → Kubernetes Cluster → Live Application
```

---

## 📌 Why This Project Matters

- ✅ Covers the **core Kubernetes deployment workflow** end-to-end
- ✅ Great for **beginners** learning Kubernetes and Docker
- ✅ Demonstrates **Deployments, Services, scaling, and self-healing**
- ✅ **Portfolio-ready** project for DevOps interviews
- ✅ Hands-on experience with **real Kubernetes concepts**

---


## 📜 License

This project is open source and available for learning purposes.

---

## 🙌 Acknowledgements

> *The best way to learn Kubernetes is by deploying real applications.*

Built with ❤️ as a hands-on DevOps learning project.

⭐ **If you find this useful, consider starring the repo!**
