import urllib.parse
from fastapi import APIRouter
from app.helper import encode_str
from app.error.exception import InvalidCodeException
from app.service.llm import parse_to_json
from app.service.geospatial import search_places
from app.dto import GeospatialResponse


api_router = APIRouter()


@api_router.get("/ping")
async def get_ping():
    return {"message": "pong"}


@api_router.get("/execute")
async def get_execute(code: str, message: str) -> GeospatialResponse:
    if code != "pioneerdevai":
        raise InvalidCodeException(f"code {code} is invalid")
    message = encode_str(message)
    llm_response = parse_to_json(message)
    return search_places(llm_response)

