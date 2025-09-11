provider "aws" {
  region = "us-east-1"
}

resource "aws_ecr_repository" "restaurant_finder_api_repo" {
  name                 = "restaurant-finder-api"
  image_tag_mutability = "MUTABLE"
}
