from httpx import Response
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi.testclient import TestClient
import main

client: TestClient = TestClient(main.app)

def test_root() -> None:
    response: Response = client.get("/")
    assert response.status_code == 200
    message: str = response.json()["message"]
    assert len(message) < 40
