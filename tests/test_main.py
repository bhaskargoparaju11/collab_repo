"""Unit tests for the FastAPI application."""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint response."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Bhaskar I have  made changes!"}
