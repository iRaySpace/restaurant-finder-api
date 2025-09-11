import os
import logging
import datetime
import watchtower


_logger = None


def get_logger():
    global _logger
    return _logger


def register_cw_logger():
    global _logger

    log_group_name = os.environ.get("CW_LOG_GROUP_NAME")
    if not log_group_name:
        return

    _logger = logging.getLogger("ErrorLogger")

    now = int(datetime.datetime.now().timestamp())
    handler = watchtower.CloudWatchLogHandler(
        log_group_name=log_group_name,
        log_stream_name=str(now),
    )

    _logger.addHandler(handler)
