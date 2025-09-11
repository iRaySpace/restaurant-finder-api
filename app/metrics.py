import os
import boto3


_metrics = None


def get_metrics():
    global _metrics
    return _metrics


def register_cw_metrics():
    global _metrics

    cw_namespace = os.environ.get("CW_NAMESPACE")
    if not cw_namespace:
        return

    _metrics = boto3.client("cloudwatch")
