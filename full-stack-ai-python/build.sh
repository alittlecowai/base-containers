#!/bin/bash

# Run sudo ./build.sh to build image with $IMAGE_TAG tag
# e.g. sudo ./build.sh 202602091800

set +e 

IMAGE_TAG=$1

# Build image to serve as base hardened image for full stack AI python app
docker build --pull -f Dockerfile --progress=plain -t "full-stack-ai-python:${IMAGE_TAG}" . || echo "Error building image."
