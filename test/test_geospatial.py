from app.service.geospatial import SearchPlacesDto, search_places


def test_search_places_return_200():
    query = SearchPlacesDto(
        query="sushi",
        near="downtown Los Angeles",
        price="1",
        open_now=True
    )
    response = search_places(query)
    assert response.status_code == 200

