# Kubernetes Prometheus Monitoring Stack

A complete Prometheus monitoring solution for Kubernetes clusters using **k3d**, featuring automated service discovery and node-level metrics collection.

---

## 🚀 Project Overview

This repository provides a **clean, minimal, and production-aligned Prometheus monitoring stack** for Kubernetes clusters.  
It is ideal for **learning, local labs, DevOps practice, and portfolio projects**.

The stack includes:
- Prometheus server
- Node Exporter
- Kubernetes-native service discovery
- Secure RBAC configuration
- External access via NodePort

---

## 🏗 Architecture

Prometheus scrapes metrics from:
- Kubernetes pods (via service discovery)
- Node Exporter (system-level metrics)

Prometheus UI is exposed using a NodePort service.

---

## 📦 Components

| Component | Description |
|---------|-------------|
| Prometheus | Metrics collection and querying |
| Node Exporter | Node-level CPU, memory, disk, network metrics |
| RBAC | Secure access to Kubernetes API |
| ConfigMap | Prometheus scrape configuration |
| NodePort | External access to Prometheus UI |

---

## 🧰 Prerequisites

- Docker
- k3d
- kubectl
- Basic Kubernetes knowledge

---

## ⚙️ Setup Instructions

### 1️⃣ Create k3d Cluster

```bash
k3d cluster create observability \
  --agents 1 \
  -p "30090:30090@loadbalancer"
```

Verify:
```bash
kubectl get nodes
```

---

### 2️⃣ Deploy Monitoring Stack

```bash
kubectl create namespace monitoring

kubectl apply -f prometheus-rbac.yaml
kubectl apply -f prometheus-config.yaml
kubectl apply -f prometheus-deployment.yaml
kubectl apply -f prometheus-service.yaml
kubectl apply -f node-exporter-pod.yaml
```

---

### 3️⃣ Verify Deployment

```bash
kubectl get pods -n monitoring
```

Check Node Exporter metrics:
```bash
kubectl exec -it node-exporter-pod -n monitoring -- wget -qO- http://localhost:9100/metrics
```

---

### 4️⃣ Access Prometheus UI

Open in browser:
```
http://localhost:30090
```

---

## 📊 Sample PromQL Queries

```promql
up
node_cpu_seconds_total
node_memory_MemAvailable_bytes
```

---

## 🔧 Customization

### Change Scrape Interval
Edit `prometheus-config.yaml`:
```yaml
global:
  scrape_interval: 15s
```

### Add New Targets
```yaml
- job_name: "my-app"
  static_configs:
    - targets: ["app:8080"]
```

---

## 🛡 Security Notes

- RBAC follows least-privilege principle
- No persistent storage (ephemeral metrics)
- Designed for labs and learning

---

## 🏭 Production Recommendations

- Use PersistentVolume for Prometheus
- Deploy Node Exporter as DaemonSet
- Add Alertmanager
- Enable TLS
- Apply resource limits
- Use Helm for lifecycle management

---

## 🧹 Cleanup

```bash
kubectl delete namespace monitoring
k3d cluster delete observability
```

---

## 📜 License

MIT License

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

**Built for Kubernetes & DevOps learning**