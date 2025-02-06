import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.database import engine
from app.transformer import transformer_function

# Setup the test database
@pytest.fixture(scope="function")
def db_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.rollback()  # Ensure a clean state

@pytest.fixture(scope="function")
def client(db_session):
    """Fixture to provide a fresh TestClient for each test"""
    return TestClient(app)

# Test: Create Payload Successfully
def test_create_payload(client):
    response = client.post("/payload", json={
        "list_1": ["first string", "second string", "third string"],
        "list_2": ["other string", "another string", "last string"]
    })
    assert response.status_code == 201
    assert "id" in response.json()

# Test: Fetch Generated Payload
def test_get_payload(client):
    post_response = client.post("/payload", json={
        "list_1": ["one", "two", "three"],
        "list_2": ["alpha", "beta", "gamma"]
    })
    payload_id = post_response.json()["id"]

    get_response = client.get(f"/payload/{payload_id}")
    assert get_response.status_code == 200

    expected_words = {"ONE", "ALPHA", "TWO", "BETA", "THREE", "GAMMA"}
    response_words = set(get_response.json()["output"].split(", "))
    assert response_words == expected_words

# Test: Cache is Working
def test_cache_reuse(client):
    data = {
        "list_1": ["cache", "test"],
        "list_2": ["reuse", "works"]
    }

    response_1 = client.post("/payload", json=data)
    response_2 = client.post("/payload", json=data)

    assert response_1.status_code == 201
    assert response_2.status_code == 201
    assert response_1.json()["id"] == response_2.json()["id"]  # Should be the same

# Test: Invalid Input Handling
def test_invalid_input(client):
    response = client.post("/payload", json={
        "list_1": ["one", "two"],
        "list_2": ["alpha"]
    })
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Value error, Lists must be of the same length"

# Test: Fetching Non-Existent Payload
def test_non_existent_payload(client):
    response = client.get("/payload/10000")
    assert response.status_code == 404  # Should be 404 instead of 422
    assert "detail" in response.json()

# Test: Transformer Function Works
def test_transformer_function():
    assert transformer_function("hello") == "HELLO"
    assert transformer_function("FastAPI") == "FASTAPI"
