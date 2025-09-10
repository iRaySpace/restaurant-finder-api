from pydantic import BaseModel
from typing import List


class SearchPlacesDto(BaseModel):
    query: str
    near: str
    min_price: str
    max_price: str
    open_now: bool


class RestaurantDto(BaseModel):
    name: str
    cuisine: str
    address: str
    operating_hours: str
    rating: float | None = None
    price_level: int | None = None


class GeospatialResponse(BaseModel):
    total: int
    limit: int
    data: List[RestaurantDto] = []
