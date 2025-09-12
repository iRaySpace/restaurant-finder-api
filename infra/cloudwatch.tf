resource "aws_cloudwatch_log_group" "restaurant_finder_log_group" {
  name              = "/staging/restaurant-finder"
  retention_in_days = 5
}

resource "aws_cloudwatch_dashboard" "restaurant_finder_dashboard" {
  dashboard_name = "RestaurantFinder"
  dashboard_body = jsonencode({
    "widgets" : [
      {
        "x" : 0,
        "y" : 0,
        "width" : 12,
        "height" : 12,
        "type" : "metric",
        "properties" : {
          "title" : "CPU Utilization",
          "region" : "us-east-1"
          "period" : 60,
          "metrics" : [
            ["AWS/EC2", "CPUUtilization", "InstanceId", aws_instance.restaurant_finder_instance.id]
          ]
        }
      },
      {
        "x" : 12,
        "y" : 0,
        "width" : 12,
        "height" : 12,
        "type" : "metric",
        "properties" : {
          "title" : "Network In",
          "region" : "us-east-1"
          "period" : 60,
          "metrics" : [
            ["AWS/EC2", "NetworkIn", "InstanceId", aws_instance.restaurant_finder_instance.id]
          ]
        }
      },
      {
        "x" : 0,
        "y" : 12,
        "width" : 12,
        "height" : 12,
        "type" : "metric",
        "properties" : {
          "title" : "Total Requests",
          "region" : "us-east-1"
          "period" : 60,
          "metrics" : [
            ["RestaurantFinderAPI", "Request", "InstanceId", aws_instance.restaurant_finder_instance.id]
          ]
        }
      }
    ]
  })
}