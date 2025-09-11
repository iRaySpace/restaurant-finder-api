#!/bin/bash
set -e

ECR_URL=$1

if [ ! $ECR_URL ]; then
    echo "ECR_URL is not set. Follow this command: ./build.sh <ecr-url>"
    exit 1
fi

poetry export --without-hashes --format=requirements.txt > requirements.txt

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ECR_URL

docker build -t restaurant-finder-api .
docker tag restaurant-finder-api:latest $ECR_URL/restaurant-finder-api:latest
docker push $ECR_URL/restaurant-finder-api:latest