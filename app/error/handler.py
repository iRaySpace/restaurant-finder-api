import uuid
import traceback
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.error.exception import InvalidCodeException, RateLimitExceededException
from app.logger import get_logger


class ErrorResponse(BaseModel):
    error_id: str
    code: str
    error: str


def handle_invalid_code(_: Request, ex: InvalidCodeException):
    status_code = 401
    error = ErrorResponse(
        error_id=str(uuid.uuid4()),
        error=ex.message,
        code=type(ex).__name__,
    )
    _log_exception(status_code, error)
    return JSONResponse(
        status_code=status_code,
        content=error.model_dump(),
    )

# HAX: This couldn't be called when a middleware is raised but...
# handle_general gets called
def handle_rate_limit_exceeded(_: Request, ex: RateLimitExceededException):
    status_code = 429
    error = ErrorResponse(
        error_id=str(uuid.uuid4()),
        error=ex.message,
        code=type(ex).__name__,
    )
    _log_exception(status_code, error)
    return JSONResponse(
        status_code=status_code,
        content=error.model_dump(),
    )


def handle_general(_: Request, ex: Exception):
    if isinstance(ex, RateLimitExceededException):
        return handle_rate_limit_exceeded(_, ex)

    # For the most very general error
    status_code = 500
    error = ErrorResponse(
        error_id=str(uuid.uuid4()),
        error=ex.message,
        code=type(ex).__name__,
    )
    _log_exception(status_code, error)
    return JSONResponse(
        status_code=status_code,
        content=error.model_dump(),
    )


def register_exception_handler(api: FastAPI):
    api.add_exception_handler(Exception, handle_general)
    api.add_exception_handler(InvalidCodeException, handle_invalid_code)


def _log_exception(status_code: int, error: ErrorResponse):
    logger = get_logger()
    logger.error({
        **error.model_dump(),
        "status_code": status_code,
    })
