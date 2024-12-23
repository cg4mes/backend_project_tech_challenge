from src.main import fetch_data
import pytest
import json
import jsonschema
from jsonschema import validate


@pytest.mark.api_companies
def test_fetch_data_success():
    url = "https://fake-json-api.mock.beeceptor.com/companies"
    result = fetch_data(url)
    status_code, data = result
    with open('tests/resources/schema.json') as schema_file:
        schema = json.load(schema_file)
    try:
        validate(instance=data, schema=schema)
        print("La respuesta es válida")
    except jsonschema.exceptions.ValidationError as e:
        print(f"Error de validación: {e.message}")
    assert status_code == 200
