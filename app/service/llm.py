import os
from openai import OpenAI
from app.service.geospatial import SearchPlacesDto


client = OpenAI()


def parse_to_json(message: str) -> SearchPlacesDto:
    with client.responses.stream(
        model="gpt-4o",
        input=[
            {"role": "system", "content": "Extract entities from the input text. For the name, you can remove the 'restaurant' term, it is already given we are searching for restaurant. For the price (min and max), use the following criteria: '1' (Cheap), '2' (Moderate), '3' (Expensive), '4' (Very Expensive). The max price is always higher than min price (e.g. min price 1, max price 2)"},
            {"role": "user", "content": message},
        ],
        text_format=SearchPlacesDto
    ) as stream:
        final_response = stream.get_final_response()
        parsed_model = final_response.output[0].model_dump().get('content')[0].get('parsed')
        return SearchPlacesDto.model_validate(parsed_model)