from pydantic import BaseModel
from typing import List


class RestaurantDto(BaseModel):
    name: str
    address: str
    rating: float
    operating_hours: str


class GeospatialResponse(BaseModel):
    total: int
    limit: int
    items: List[RestaurantDto] = []
