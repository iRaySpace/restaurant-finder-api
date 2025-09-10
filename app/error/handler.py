import uuid
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.error.exception import InvalidCodeException


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


def register_exception_handler(api: FastAPI):
    api.add_exception_handler(InvalidCodeException, handle_invalid_code)
