import os
import requests
from pydantic import BaseModel
from app.mapper import map_geospatial_response
from app.dto import GeospatialResponse


class SearchPlacesDto(BaseModel):
    query: str
    near: str
    price: str
    open_now: bool

# - **Cuisine**
# - **Price Level**


FSQ_CATEGORY_IDS = [
    "4d4b7105d754a06374d81259", # Restaurant
]

def _search_places(query_data: SearchPlacesDto):
    query_data = {
        **query_data.model_dump(),
        "fields": "name,location,tastes,menu,rating,price,hours",
        "fsq_category_ids": FSQ_CATEGORY_IDS,
    }
    response = requests.get(
        "https://places-api.foursquare.com/places/search",
        params=query_data,
        headers={
            "X-Places-Api-Version": "2025-06-17",
            "Accept": "application/json",
            "Authorization": "Bearer " + os.environ.get("FOURSQUARE_SERVICE_KEY"),
        }
    )
    return response


def search_places(query_data: SearchPlacesDto) -> GeospatialResponse:
    return map_geospatial_response(_search_places(query_data))
