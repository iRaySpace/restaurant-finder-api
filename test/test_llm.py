from app.service.llm import parse_to_json


def test_parse_to_json_returns_search_places_dto():
    response = parse_to_json("Find me a cheap sushi restaurant in downtown Los Angeles that's open now and has at least a 4-star rating.")
    assert response.query == "sushi restaurant"
    assert response.near == "downtown Los Angeles"
    assert response.price == "1"
    assert response.open_now == True
