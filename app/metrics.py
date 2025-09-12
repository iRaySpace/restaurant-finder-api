import os
import boto3
from boto3.session import Session


_metrics = None


def get_metrics():
    global _metrics
    return _metrics


def register_cw_metrics():
    global _metrics

    cw_namespace = os.environ.get("CW_NAMESPACE")
    if not cw_namespace:
        return

    boto3_session = Session(region_name="us-east-1")
    _metrics = boto3_session.client("cloudwatch")
