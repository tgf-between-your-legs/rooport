# FastAPI: Testing with `TestClient` and `pytest`

Writing automated tests for FastAPI applications.

## Core Concept

FastAPI provides a `TestClient` class (based on `httpx`) that allows you to make requests directly to your FastAPI application *without* needing a running server. This makes testing fast and efficient. It's commonly used with `pytest` for test organization and fixtures.

## Setup

1.  **Install Dependencies:**
    ```bash
    pip install pytest httpx
    ```
2.  **Test File Structure:** Organize tests in a `tests/` directory. Use filenames like `test_main.py`, `test_users.py`, etc.
3.  **Import `TestClient`:** Import `TestClient` from `fastapi.testing`.
4.  **Import your FastAPI app:** Import the `app` instance from your main application file (e.g., `from main import app`).

## Basic Test Example (`pytest`)

```python
# tests/test_main.py
from fastapi.testclient import TestClient
from main import app # Import your FastAPI app instance

# Create a TestClient instance using your app
client = TestClient(app)

def test_read_root():
    # Make a request to the "/" endpoint
    response = client.get("/")
    # Assert the status code
    assert response.status_code == 200
    # Assert the response body (JSON)
    assert response.json() == {"message": "Hello World"}

def test_read_item_success():
    response = client.get("/items/1")
    assert response.status_code == 200
    # Check specific parts of the response
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Example"
    assert "owner" in data # Check if nested object exists

def test_read_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_create_item():
    item_data = {
        "name": "New Test Item",
        "description": "A description",
        "price": 99.99,
        "tags": ["test", "new"]
    }
    response = client.post(
        "/items/",
        json=item_data # Pass request body data as json parameter
    )
    assert response.status_code == 201 # Check for 201 Created status
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["price"] == item_data["price"]
    assert "id" in data # Check if ID was assigned

def test_create_item_invalid_price():
    item_data = {"name": "Invalid Price Item", "price": -10}
    response = client.post("/items/", json=item_data)
    # FastAPI/Pydantic automatically return 422 for validation errors
    assert response.status_code == 422
    # Check the structure of the validation error response
    data = response.json()
    assert "detail" in data
    assert isinstance(data["detail"], list)
    assert data["detail"][0]["loc"] == ["body", "price"] # Field causing the error
    assert "Price must be positive" in data["detail"][0]["msg"]

# Add tests for PUT, PATCH, DELETE, authentication, etc.
```

## Running Tests

*   Run `pytest` in your terminal from the project root directory. `pytest` will automatically discover files named `test_*.py` or `*_test.py` and functions/methods prefixed with `test_`.

## Testing Asynchronous Code

*   `TestClient` uses `httpx` which supports `asyncio`.
*   If your path operations are `async def`, your tests using `TestClient` **do not** need to be `async def`. `TestClient` handles the async execution internally.

## Testing Dependencies (`Depends`)

*   **Overriding Dependencies:** FastAPI allows you to override dependencies during testing. This is crucial for mocking external services or database connections.
    *   Use `app.dependency_overrides[dependency_function] = override_function`.
    *   Define an `override_function` that returns the desired mock value or performs mock actions.
    *   Use `pytest` fixtures to manage the setup and teardown of overrides.

```python
# tests/test_users.py
import pytest
from fastapi.testclient import TestClient
from main import app, get_current_user # Import app and original dependency
from schemas import User # Import Pydantic model

# --- Mock Dependency ---
async def override_get_current_user():
    # Return a specific user for testing protected endpoints
    return User(username="testuser", email="test@example.com", full_name="Test User", disabled=False)

# --- Pytest Fixture to Apply Override ---
@pytest.fixture(scope="module", autouse=True) # Apply override for all tests in this module
def apply_dependency_override():
    # Apply the override before tests run
    app.dependency_overrides[get_current_user] = override_get_current_user
    yield # Let tests run
    # Clean up: remove the override after tests finish
    app.dependency_overrides = {}

# --- Test Client ---
client = TestClient(app)

# --- Tests ---
def test_read_users_me():
    response = client.get("/users/me")
    assert response.status_code == 200
    data = response.json()
    # Check if the data matches the overridden user
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"

def test_read_items_authenticated():
    response = client.get("/items/") # This endpoint requires authentication
    assert response.status_code == 200
    assert response.json() == [{"item_id": "Foo", "owner": "testuser"}]

# Test case for when authentication *should* fail (requires separate setup/teardown or different test module)
# def test_read_items_unauthenticated():
#     # Ensure override is NOT active for this test
#     app.dependency_overrides = {} # Temporarily clear override
#     response = client.get("/items/")
#     assert response.status_code == 401 # Expect unauthorized
#     app.dependency_overrides[get_current_user] = override_get_current_user # Restore for other tests if needed
```

## Testing WebSockets

*   `TestClient` provides a `websocket_connect()` context manager.

```python
def test_websocket():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("Hello")
        data = websocket.receive_text()
        assert data == "Message text was: Hello"
```

Writing comprehensive tests using `TestClient` and `pytest` is crucial for ensuring the reliability and correctness of your FastAPI application.

*(Refer to the official FastAPI Testing documentation: https://fastapi.tiangolo.com/tutorial/testing/)*