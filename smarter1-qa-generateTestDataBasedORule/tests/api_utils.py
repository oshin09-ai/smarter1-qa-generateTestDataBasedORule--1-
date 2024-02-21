# api_utils.py

import requests
import json


def make_api_call(json_object, api_url):
    # Extract the stringified JSON from the 'JSON_Output' key
    json_output_str = json_object['JSON_Output']

    # Parse the stringified JSON to get an actual Python dictionary
    json_output_dict = json.loads(json_output_str)

    # Extract the 'content' key from the parsed dictionary, which is your actual request body
    actual_request_body = json_output_dict['content']

    # Assuming the 'content' is also in JSON format and needs to be sent as a JSON payload
    # If 'content' is a stringified JSON, parse it to a dict
    # If it's already the format you need, adjust accordingly
    request_body_to_send = json.loads(actual_request_body)

    print(f"Making API call to {api_url} with data: {request_body_to_send}")

    # Make the API POST request with the correct request body
    response = requests.post(api_url, json=request_body_to_send)

    print(f"Response body received: {response.json()}")

    return response
