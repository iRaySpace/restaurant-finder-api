#!/bin/bash
(cd infra && terraform apply -auto-approve -target=aws_ecr_repository.restaurant_finder_api_repo)