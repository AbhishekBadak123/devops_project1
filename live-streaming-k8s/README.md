🚀 Project Overview

This project implements a multi-tier live streaming architecture where:
OBS Studio sends a live stream using RTMP
NGINX-RTMP ingests and processes the stream
The stream is converted to HLS (.m3u8 + .ts) format
Viewers can watch the stream via a browser or video player
Everything runs inside Kubernetes (Minikube)


🧰 Technologies Used
Kubernetes
Minikube
NGINX-RTMP
OBS Studio
RTMP & HLS Streaming
Docker Containers
YAML (Kubernetes Manifests)

live-streaming-k8s/
│
├── streaming-nginx-conf.yaml     # NGINX RTMP & HLS configuration (ConfigMap)
├── streaming-deployment.yaml     # Streaming server deployment
├── streaming-service.yaml        # NodePort service for RTMP & HTTP
├── README.md                     # Project documentation

▶️ Setup & Deployment Steps
1️⃣ Start Minikube
minikube start --driver=virtualbox --no-vtx-check

2️⃣ Deploy Kubernetes Resources
kubectl apply -f streaming-nginx-conf.yaml
kubectl apply -f streaming-deployment.yaml
kubectl apply -f streaming-service.yaml

3️⃣ Verify Pod Status
kubectl get pods
Expected:
streaming-server   1/1   Running

4️⃣ Get Minikube IP
minikube ip
Example:
192.168.59.101

🎥 OBS Studio Configuration

Settings → Stream
Service: Custom
Server:rtmp://<MINIKUBE_IP>:31935/live
Stream Key:test


Click Start Streaming

🌐 Watch the Live Stream
Option 1: VLC Player

Media → Open Network Stream

http://<MINIKUBE_IP>:30080/live/test.m3u8

Option 2: Browser (HLS compatible)
http://<MINIKUBE_IP>:30080/live/test.m3u8

🔍 How to Verify It’s Working
Check RTMP connection logs
kubectl logs -f streaming-server-<pod-name>


Expected:
connect: app='live'
publish: name='test'

Check HLS file generation
kubectl exec -it streaming-server-<pod-name> -- ls /tmp/hls/live

Expected:
test.m3u8
test0.ts
test1.ts
