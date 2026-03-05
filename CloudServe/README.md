# ☁️ CloudServe: Python Application Delivery Pipeline

> A hands-on DevOps project — build, containerize, and deploy a Python (Flask) web application on AWS EC2 using Docker.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-green?logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazonwebservices&logoColor=white)

---

## 🚀 Project Overview

**CloudServe** is a simple yet complete DevOps project that demonstrates how application development, containerization, and cloud deployment work together in a real-world workflow.

A Python Flask web application is built, containerized using Docker, and deployed on an **AWS EC2** instance running Linux — covering the core stages of a modern application delivery pipeline.

### What it does
- Serves a dynamic web page showing:
  - ✅ Application status
  - 🖥️ Container hostname
  - 🕐 Current server timestamp

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────┐
│                  Developer                       │
│            (Code + Git Push)                     │
└──────────────┬───────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────┐
│              GitHub Repository                   │
│         (Source Code Management)                  │
└──────────────┬───────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────┐
│          Docker (Containerization)               │
│   ┌────────────────────────────────────────┐     │
│   │  Python 3.10-slim Base Image           │     │
│   │  Flask Application (Port 5000)         │     │
│   │  Dependencies (requirements.txt)       │     │
│   └────────────────────────────────────────┘     │
└──────────────┬───────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────┐
│           AWS EC2 Instance (Linux)               │
│       Docker Container Running on Port 5000      │
│              ↕ Public IP Access                  │
└──────────────────────────────────────────────────┘
```

---

## 🧰 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.10** | Application runtime |
| **Flask** | Lightweight web framework |
| **Docker** | Containerization |
| **Git & GitHub** | Version control & source code management |
| **AWS EC2** | Cloud deployment (Linux instance) |

---

## 📁 Project Structure

```
CloudServe/
└── app/
    ├── app.py              # Flask application (main entry point)
    ├── Dockerfile.txt       # Docker build instructions
    └── requirements.txt     # Python dependencies
```

---

## 📄 Application Code

The Flask application (`app.py`) serves a dynamic HTML page:

```python
from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>CloudServe Application</h1>
    <p>Containerized Python Application Running Successfully!</p>
    <p>Hostname: {socket.gethostname()}</p>
    <p>Time: {datetime.datetime.now()}</p>
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

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

EXPOSE 5000

CMD ["python", "app/app.py"]
```

---

## ⚙️ Prerequisites

- **AWS Account** with an EC2 instance (Amazon Linux / Ubuntu)
- **Docker** installed on the EC2 instance
- **Git** installed on the EC2 instance
- **Security Group** configured to allow inbound traffic on port `5000`

---

## ▶️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AbhishekBadak123/devops_project1.git
cd devops_project1/CloudServe
```

### 2️⃣ Build the Docker Image

```bash
docker build -t cloudserve-app -f app/Dockerfile.txt .
```

### 3️⃣ Run the Docker Container

```bash
docker run -d -p 5000:5000 --name cloudserve cloudserve-app
```

### 4️⃣ Access the Application

Open your browser and navigate to:

```
http://<EC2_PUBLIC_IP>:5000
```

You should see the **CloudServe Application** page with the container hostname and current timestamp.

---

## 🔍 Useful Docker Commands

```bash
# Check running containers
docker ps

# View container logs
docker logs cloudserve

# Stop the container
docker stop cloudserve

# Remove the container
docker rm cloudserve

# Remove the image
docker rmi cloudserve-app
```

---

## 🚀 Deployment on AWS EC2

### Step 1: Launch an EC2 Instance
- AMI: Amazon Linux 2 / Ubuntu
- Instance Type: `t2.micro` (free tier eligible)
- Security Group: Allow SSH (22) and Custom TCP (5000)

### Step 2: Connect via SSH

```bash
ssh -i your-key.pem ec2-user@<EC2_PUBLIC_IP>
```

### Step 3: Install Docker

```bash
# Amazon Linux 2
sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
```

### Step 4: Clone & Deploy

```bash
git clone https://github.com/AbhishekBadak123/devops_project1.git
cd devops_project1/CloudServe
docker build -t cloudserve-app -f app/Dockerfile.txt .
docker run -d -p 5000:5000 --name cloudserve cloudserve-app
```

---

## 🧠 Key Learnings

- **Application Development** — Building a simple web app with Flask
- **Version Control** — Managing source code with Git & GitHub
- **Containerization** — Writing a Dockerfile and building images
- **Cloud Deployment** — Deploying containers on AWS EC2
- **Networking** — Exposing container ports and configuring security groups
- **DevOps Workflow** — Understanding the end-to-end application delivery pipeline

---

## 🛠️ DevOps Workflow Summary

```
Code → Git Push → Docker Build → Docker Run → AWS EC2 → Live Application
```

---

## 📌 Why This Project Matters

- ✅ Covers the **core DevOps pipeline** from code to deployment
- ✅ Great for **beginners** learning Docker and AWS
- ✅ Demonstrates **practical, hands-on** DevOps skills
- ✅ **Portfolio-ready** project for interviews
- ✅ Moves from **theory to practical learning**

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📜 License

This project is open source and available for learning purposes.

---

## 🙌 Acknowledgements

> *Always good to move from theory to practical learning.*

Built with ❤️ as a hands-on DevOps learning project.

⭐ **If you find this useful, consider starring the repo!**

---

**#DevOps #Docker #AWS #Python #Flask #CloudComputing #LearningByDoing**