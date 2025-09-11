import os
from fastapi import Request
from app.metrics import get_metrics


async def cw_metric_middleware(request: Request, call_next):
    metrics = get_metrics()
    if metrics:
        metrics.put_metric_data(
            Namespace=os.environ.get("CW_NAMESPACE"),
            MetricData=[
                {
                    "MetricName": "Request",
                    "Dimensions": [
                        {
                            "Name": "InstanceId",
                            "Value": os.environ.get("INSTANCE_ID"),
                        },
                    ],
                    "Value": 1,
                    "Unit": "Count",
                }
            ]
        )
    response = await call_next(request)
    return response
