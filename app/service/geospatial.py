import os
import requests
from pydantic import BaseModel

class SearchPlacesDto(BaseModel):
    query: str
    near: str
    price: str
    open_now: bool


# - **Cuisine**
# - **Price Level**

def _search_places(query_data: SearchPlacesDto):
    query_data = {
        **query_data.model_dump(),
        "fields": "name,location,tastes,menu,rating,price,hours",
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


def search_places(query_data: SearchPlacesDto):
    pass
