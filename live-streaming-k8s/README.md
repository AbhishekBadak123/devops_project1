LIVE STREAMING ON KUBERNETES (MINIKUBE)

RUN COMMANDS:

kubectl apply -f streaming-nginx-conf.yaml
kubectl apply -f streaming-deployment.yaml
kubectl apply -f streaming-service.yaml

OBS SETTINGS:
Server: rtmp://<MINIKUBE_IP>:31935/live
Stream Key: test

BROWSER:
http://<MINIKUBE_IP>:30080/live/test.m3u8
