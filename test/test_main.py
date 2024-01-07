import pytest
import requests

URL = "http://localhost:9000/"

def test_root():
    response = requests.get(URL)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}