import os
from openai import OpenAI
from app.service.geospatial import SearchPlacesDto


client = OpenAI()


def parse_to_json(message: str) -> SearchPlacesDto:
    with client.responses.stream(
        model="gpt-4o",
        input=[
            {"role": "system", "content": "Extract entities from the input text. For the price, use the following criteria: '1' (most affordable) to '4' (most expensive)."},
            {"role": "user", "content": message},
        ],
        text_format=SearchPlacesDto
    ) as stream:
        final_response = stream.get_final_response()
        parsed_model = final_response.output[0].model_dump().get('content')[0].get('parsed')
        return SearchPlacesDto.model_validate(parsed_model)