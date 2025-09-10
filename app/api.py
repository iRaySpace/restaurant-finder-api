from fastapi import FastAPI
from app.router import api_router
from app.error.handler import register_exception_handler


def get_api() -> FastAPI:
    api = FastAPI()
    api.include_router(prefix="/api", router=api_router)
    register_exception_handler(api)
    return api
