import json
from app.service.geospatial import SearchPlacesDto, _search_places, search_places


def test_search_places_return_200():
    query = SearchPlacesDto(
        query="sushi",
        near="downtown Los Angeles",
        price="1",
        open_now=True
    )
    response = _search_places(query)
    assert response.status_code == 200


def test_search_places_return_geospatial_response():
    query = SearchPlacesDto(
        query="sushi",
        near="downtown Los Angeles",
        price="1",
        open_now=True
    )
    response = search_places(query)
    assert response is not None


def test_search_places_return_geospatial_response():
    query = SearchPlacesDto(
        query="sushi",
        near="California",
        price="1",
        open_now=True
    )
    response = search_places(query)
    assert response is not None
