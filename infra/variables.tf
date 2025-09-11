variable "iam_instance_profile" {
  type        = string
  description = "IAM Instance Profile with Session Manager"
}

variable "subnet_id" {
  type        = string
  description = "VPC Subnet ID with Public Access"
}

variable "ecr_url" {
  type        = string
  description = "ECR URL"
}