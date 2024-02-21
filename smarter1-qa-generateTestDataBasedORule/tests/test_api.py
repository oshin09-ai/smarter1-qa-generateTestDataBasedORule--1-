# test_api.py
import pytest
from .utils import load_excel_to_json
from .api_utils import make_api_call
import os

classification = os.getenv('CLASSIFICATION')

EXCEL_FILE_PATH = f'docs/{classification}.xlsx'
API_URL = f'https://inno-tools-6c68031f855c.herokuapp.com/classify/regulatory?api_key=c74d94c2-5e81-11ee-8c99' \
          f'-0242ac120002&skip_embeddings=true&attribute_filter={classification}'

json_objects = load_excel_to_json(EXCEL_FILE_PATH)


@pytest.mark.parametrize("json_object", json_objects, ids=lambda json_object: f"Test_UPC_{json_object['UPC']}")
def test_api_with_json_object(json_object):
    """Test making an API call with a JSON object."""
    response = make_api_call(json_object, API_URL)
    assert response.status_code == 200  # Assuming 200 is the success status code
    json_response = response.json()

    print(f"Expected value {json_object['REAL ANSWER']}, received value: {json_response[classification]}")

    # Verify specific parameters in the response
    assert json_response[classification] == json_object['REAL ANSWER'], \
        f"{classification} value mismatch"

