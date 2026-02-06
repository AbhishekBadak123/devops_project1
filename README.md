
# Kubernetes Multi-Tier & Live Streaming Project

This repository contains **two real-world Kubernetes projects** built from scratch using Minikube.  
Both projects focus on **practical DevOps learning**, real debugging, and production-like behavior.

---

## 🚀 Projects Included

### 1️⃣ Multi-Tier Web Application (E‑commerce style)
A classic **3-tier architecture** deployed on Kubernetes.

**Architecture**
```
Frontend (Nginx)
   |
Backend (API)
   |
MySQL Database (Persistent Storage)
```

**Components**
- Frontend: Nginx + HTML
- Backend: Application server
- Database: MySQL with PVC
- Secrets: Kubernetes Secrets for DB credentials

---

### 2️⃣ Live Streaming Platform (YouTube‑like)
A **real-time video streaming system** using Kubernetes.

**Architecture**
```
OBS Studio
   |
RTMP (1935)
   |
NGINX‑RTMP (Kubernetes Pod)
   |
HLS (.m3u8 + .ts)
   |
Browser / VLC Player
```

---

## 🧰 Technologies Used

- Kubernetes
- Minikube
- Docker
- NGINX & NGINX‑RTMP
- MySQL
- OBS Studio
- RTMP & HLS
- YAML (Kubernetes manifests)

---

## 📁 Repository Structure

```
.
├── frontend-configmap.yaml
├── frontend-deployment.yaml
├── frontend-service.yaml
├── backend-configmap.yaml
├── backend-deployment.yaml
├── backend-service.yaml
├── mysql-deployment.yaml
├── mysql-service.yaml
├── mysql-pvc.yaml
├── mysql-secret.yaml
├── streaming-nginx-conf.yaml
├── streaming-deployment.yaml
├── streaming-service.yaml
└── README.md
```

---

## ⚙️ Prerequisites

- Windows / Linux / macOS
- Minikube installed
- kubectl installed
- VirtualBox (or supported Minikube driver)
- OBS Studio (for streaming project)

---

## ▶️ Start Minikube

```bash
minikube start --driver=virtualbox --no-vtx-check
```

---

## ▶️ Deploy Multi‑Tier Application

```bash
kubectl apply -f mysql-secret.yaml
kubectl apply -f mysql-pvc.yaml
kubectl apply -f mysql-deployment.yaml
kubectl apply -f mysql-service.yaml

kubectl apply -f backend-configmap.yaml
kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-service.yaml

kubectl apply -f frontend-configmap.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f frontend-service.yaml
```

Access frontend:
```bash
minikube service frontend-service
```

---

## ▶️ Deploy Live Streaming Platform

```bash
kubectl apply -f streaming-nginx-conf.yaml
kubectl apply -f streaming-deployment.yaml
kubectl apply -f streaming-service.yaml
```

---

## 🎥 OBS Configuration

- Service: Custom
- Server:
```
rtmp://<MINIKUBE_IP>:31935/live
```
- Stream Key:
```
test
```

---

## 🌐 Watch Live Stream

```
http://<MINIKUBE_IP>:30080/live/test.m3u8
```

Use VLC or an HLS‑enabled browser/player.

---

## 🔍 How to Verify

```bash
kubectl get pods
kubectl logs -f <streaming-pod-name>
kubectl exec -it <streaming-pod-name> -- ls /tmp/hls/live
```

Expected files:
```
test.m3u8
test0.ts
test1.ts
```

---

## 🧠 Key Learnings

- Kubernetes is declarative
- Controllers recreate pods automatically
- Container filesystems can be read‑only
- Correct use of ConfigMaps & volumes is critical
- Debugging CrashLoopBackOff requires log analysis
- Real DevOps learning comes from breaking & fixing systems

---

## 📌 Why This Project Matters

- Real‑world DevOps use cases
- Not a copy‑paste tutorial
- Covers networking, storage, secrets & streaming
- Portfolio & interview‑ready
- Demonstrates persistence and problem‑solving

---

## 🙌 Final Note

This project involved **significant debugging and hands‑on effort**.  
If you are learning Kubernetes — build something real, face errors, and fix them.

⭐ If you find this useful, consider starring the repo!
