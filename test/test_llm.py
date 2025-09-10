from app.service.llm import parse_to_json


def test_parse_to_json_returns_search_places_dto():
    response = parse_to_json("Find me a cheap sushi restaurant in downtown Los Angeles that's open now and has at least a 4-star rating.")
    assert response.query == "sushi"
    assert response.near == "downtown Los Angeles"
    assert response.min_price == "1"
    assert response.max_price == "2"
    assert response.open_now == True


def test_parse_to_json_california_returns_search_places_dto():
    response = parse_to_json("Find me a ramen restaurant moderately priced in California that's open now and has at least a 4-star rating.")
    assert response.query == "ramen"
    assert response.near == "California"
    assert response.min_price == "2"
    assert response.max_price == "3"
    assert response.open_now == True
