# Helm - with docker and minikube k8s

### Commands
- Different commands for the session
- Minikube
```
minikube start
```

#### Docker Login
```
# docker user
docker info | sed -n 's/^ Username: //p'

# docker login using password
echo $DOCPWD | docker login -u ckcft --password-stdin
```

#### kubectl commands
```
nano ~/.bashrc
alias k=kubectl
# exit - save
source ~/.bashrc

k apply -f kubeapp.yml & k apply -f svc-kubeapp.yml & k apply -f hpa.yml
```

#### Start services
```
k apply -f kubeapp.yml & k apply -f svc-kubeapp.yml & k apply -f hpa.yml
```

#### Minikube service
- To get URL for minikube
```
minikube service --url python-app-service
URL=$(minikube service --url python-app-service | head -n1)
HOSTPORT=$(printf '%s' "$URL" | sed -E 's#^https?://##')
echo "$HOSTPORT"          # e.g., 192.168.49.2:31833
echo $URL

# ---- parallel requests using curl to cluster
seq 20 | xargs -n1 -P20 -I{} sh -c '
  printf "[req %02d] " "{}"
  curl -sS "$0"
  echo
' "$URL"
```
- Expose port using socat
```
sudo apt-get update && sudo apt-get install -y socat
# in a new bash
socat TCP-LISTEN:8081,fork,reuseaddr TCP:192.168.49.2:30895
```

#### Clean up
```
k delete -f kubeapp.yml & k delete -f svc-kubeapp.yml & k delete -f hpa.yml
```
