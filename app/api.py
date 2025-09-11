from fastapi import FastAPI
from app.router import api_router
from app.error.handler import register_exception_handler
from app.middleware.rate_limit_middleware import rate_limit_middleware
from app.logger import register_cw_logger


def get_api() -> FastAPI:
    api = FastAPI()
    api.middleware("http")(rate_limit_middleware)
    api.include_router(prefix="/api", router=api_router)
    register_exception_handler(api)
    register_cw_logger()
    return api
