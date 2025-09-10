from app.dto import RestaurantDto, GeospatialResponse


def map_geospatial_response(response_data: dict) -> GeospatialResponse:
    results = response_data.json().get("results", [])
    return GeospatialResponse(
        limit=10,
        total=len(results),
        data=list(map(lambda result: _map_result(result), results)),
    )


def _map_result(data: dict) -> RestaurantDto:
    return RestaurantDto(
        name=data.get("name"),
        address=data.get("location").get("formatted_address"),
        operating_hours=data.get("hours").get("display"),
        rating=data.get("rating"),
    )
