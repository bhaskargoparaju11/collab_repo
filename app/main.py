"""Main FastAPI application."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Handle root GET request."""
    return {"message": "Hello, Bhaskar I have made changes!"}
