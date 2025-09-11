resource "aws_security_group" "restaurant_finder_sg" {
  name = "restaurant-finder-sg"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "restaurant_finder_instance" {
  ami           = "ami-0b09ffb6d8b58ca91" # AL2023 us-east-1
  instance_type = "t2.micro"

  subnet_id              = var.subnet_id
  iam_instance_profile   = var.iam_instance_profile
  vpc_security_group_ids = [aws_security_group.restaurant_finder_sg.id]

  tags = {
    Name = "restaurant-finder-instance"
  }

  user_data = <<EOF
    #!/bin/bash
    sudo yum update -y
    sudo yum install -y docker
    sudo usermod -a -G docker ec2-user
    sudo service docker start
    docker ps
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${var.ecr_url}
    docker run -p 80:8000 restaurant-finder-api
EOF

}
