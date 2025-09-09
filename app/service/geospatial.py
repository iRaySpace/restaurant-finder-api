import os
import requests
from pydantic import BaseModel


class SearchPlacesDto(BaseModel):
    query: str
    near: str
    price: str
    open_now: bool


def search_places(query_data: SearchPlacesDto):
    response = requests.get(
        "https://places-api.foursquare.com/places/search",
        params=query_data.dict(),
        headers={
            "X-Places-Api-Version": "2025-06-17",
            "Accept": "application/json",
            "Authorization": "Bearer " + os.environ.get("FOURSQUARE_SERVICE_KEY"),
        }
    )
    return response
