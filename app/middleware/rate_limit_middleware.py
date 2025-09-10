from datetime import datetime, timezone
from pydantic import BaseModel
from fastapi import Request
from app.error.exception import RateLimitExceededException


MAX_REQUESTS = 10
WINDOW_INTERVAL_SECS = 60


class RateLimitClient(BaseModel):
    window: int
    requests: int


clients = {}


async def rate_limit_middleware(request: Request, call_next):
    ip = request.client.host

    now_utc_timestamp = int(datetime.now(timezone.utc).timestamp())
    current_window = now_utc_timestamp // WINDOW_INTERVAL_SECS

    rate_limit_client = clients.get(ip)
    if not rate_limit_client or (rate_limit_client.window != current_window):
        rate_limit_client = RateLimitClient(window=current_window, requests=0)

    if rate_limit_client.requests == MAX_REQUESTS:
        raise RateLimitExceededException("Unable to requests further due to rate limit")

    rate_limit_client.requests = rate_limit_client.requests + 1
    clients[ip] = rate_limit_client

    response = await call_next(request)
    return response
