import uuid
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.error.exception import InvalidCodeException, RateLimitExceededException


class ErrorResponse(BaseModel):
    error_id: str
    code: str
    error: str


def handle_invalid_code(_: Request, ex: InvalidCodeException):
    return JSONResponse(
        status_code=401,
        content=ErrorResponse(
            error_id=str(uuid.uuid4()),
            error=ex.message,
            code=type(ex).__name__,
        ).model_dump()
    )

# HAX: This couldn't be called when a middleware is raised but...
# handle_general gets called
def handle_rate_limit_exceeded(_: Request, ex: RateLimitExceededException):
    return JSONResponse(
        status_code=429,
        content=ErrorResponse(
            error_id=str(uuid.uuid4()),
            error=ex.message,
            code=type(ex).__name__,
        ).model_dump()
    )


def handle_general(_: Request, ex: Exception):
    if isinstance(ex, RateLimitExceededException):
        return handle_rate_limit_exceeded(_, ex)

    # For the most very general error
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error_id=str(uuid.uuid4()),
            error=ex.message,
            code=type(ex).__name__,
        ).model_dump()
    )


def register_exception_handler(api: FastAPI):
    api.add_exception_handler(Exception, handle_general)
    api.add_exception_handler(InvalidCodeException, handle_invalid_code)

