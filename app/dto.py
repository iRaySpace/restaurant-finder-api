from pydantic import BaseModel
from typing import List


class RestaurantDto(BaseModel):
    name: str
    address: str
    operating_hours: str
    rating: float | None = None


class GeospatialResponse(BaseModel):
    total: int
    limit: int
    data: List[RestaurantDto] = []
