import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi.testclient import TestClient
import main

client = TestClient(main.app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    message = response.json()["message"]
    assert len(message) < 40
