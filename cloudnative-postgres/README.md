# About

Cloudnative postgres image based on /chainguard/postgres:latest. Currently resolves to postgres:18.x

# Packages

Refer to https://images.chainguard.dev/directory/image/postgres/versions#/version/postgres/ce2d1984a010471142503340d670612d63ffb9f6%2F8bf21997436db657%2F2b2d07e53be811e9/packages for the base image packages.

#### Additional packages:

| Name | Version |

# Deploy

#### Pre-requisite

CNPG controller has to be installed. If not, please run:

```
helm repo add cnpg https://cloudnative-pg.github.io/charts
```

#### Build image and deploy to cluster:

```
docker build . -t cloudnative-postgres:18-barman

kubectl apply -f infra/00-namespace.yaml
kubectl apply -f infra/01-minio-secret.yaml
kubectl apply -f infra/02-minio-deployment.yaml
kubectl apply -f infra/03-minio-service.yaml
kubectl apply -f infra/04-app-secret.yaml
kubectl apply -f infra/05-cluster.yaml
kubectl apply -f infra/06-scheduled-backup.yaml
```

### Create s3 bucket in minio:

Run:

```
kubectl port-forward -n database-test svc/minio 9001:9001
```

Go to: http://localhost:9001

Create bucket named: `cnpg-test`.

# Verify

```
kubectl get pods -n database-test
kubectl get svc -n database-test
kubectl get cluster -n database-test
kubectl get backups -n database-test
```
