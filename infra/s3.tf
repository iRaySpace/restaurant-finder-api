resource "aws_s3_bucket" "restaurant_finder_bucket" {
    bucket = "restaurant-finder-bucket"
}

resource "aws_s3_object" "env_file" {
    bucket = aws_s3_bucket.restaurant_finder_bucket.id
    key = ".env"
    source = "../.env"
    etag = file("../.env")
}
