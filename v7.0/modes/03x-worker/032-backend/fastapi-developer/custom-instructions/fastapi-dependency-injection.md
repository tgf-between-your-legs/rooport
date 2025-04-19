# FastAPI: Dependency Injection System (`Depends`)

Using FastAPI's dependency injection for managing dependencies, sharing logic, and improving code structure.

## Core Concept: Injecting Dependencies into Path Operations

FastAPI includes a powerful yet simple dependency injection system based on the `Depends` function. It allows you to declare dependencies (which are typically functions, but can also be classes) that your path operation functions require. FastAPI takes care of executing these dependencies and "injecting" their results into your path operation function as arguments.

**Benefits:**

*   **Code Reusability:** Share common logic (e.g., getting the current user, database session management, complex parameter validation) across multiple path operations without repeating code.
*   **Separation of Concerns:** Keep path operation functions focused on their core business logic by moving dependency setup/retrieval elsewhere.
*   **Testability:** Dependencies can be easily overridden during testing, allowing you to inject mocks or test doubles.
*   **Automatic Documentation:** Dependencies are integrated into the OpenAPI schema, showing how endpoints rely on shared components.
*   **Hierarchical Dependencies:** Dependencies can depend on other dependencies, creating a graph that FastAPI resolves automatically.

## Defining Dependencies

A dependency is typically a function (sync or async) that can receive parameters just like a path operation function (from path, query, body, etc., including other dependencies).

```python
from fastapi import Depends, FastAPI, HTTPException, status, Header
from typing import Optional
from typing_extensions import Annotated # Preferred for Python 3.9+

app = FastAPI()

# --- Simple Dependency Function ---
async def common_parameters(
    q: Optional[str] = None,
    skip: int = 0,
    limit: int = 100
):
    """Shared logic for common query parameters."""
    return {"q": q, "skip": skip, "limit": limit}

# --- Dependency with Sub-dependencies ---
async def get_current_user(token: Annotated[str | None, Header()] = None):
    """Dependency to get the current user based on a token (simplified)."""
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    # In a real app, decode token, fetch user from DB
    if token != "fake-valid-token":
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return {"username": "testuser", "email": "test@example.com", "id": 1}

# --- Dependency using 'yield' (for setup/teardown) ---
# Example: Database Session Management
async def get_db_session():
    """Dependency yielding a database session."""
    # db = SessionLocal() # Create session (e.g., SQLAlchemy)
    db = {"connection": "fake_db_connection"} # Simulate session
    try:
        print("DB Session Opened")
        yield db # Provide the session to the path operation
    finally:
        # db.close() # Close session after response is sent
        print("DB Session Closed")

# --- Dependency Class ---
# Less common, but possible. FastAPI calls the class instance.
class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

# --- Using Dependencies in Path Operations ---

@app.get("/items/")
# Inject the result of common_parameters into the 'commons' argument
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return {"message": "Reading items", "params": commons}

@app.get("/users/me")
# Inject the result of get_current_user into the 'current_user' argument
async def read_current_user(current_user: Annotated[dict, Depends(get_current_user)]):
    # This endpoint now requires a valid token via the Header
    return current_user

@app.post("/items/db")
# Inject the result of get_db_session into the 'db' argument
async def create_item_db(item_name: str, db: Annotated[dict, Depends(get_db_session)]):
    print(f"Using DB session: {db}")
    # ... use db session to save item ...
    return {"message": f"Item '{item_name}' created using {db['connection']}"}

# Using a dependency class instance
# @app.get("/search/")
# async def search(params: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
#     # Access params.q, params.skip, params.limit
#     return {"query": params.q, "skip": params.skip, "limit": params.limit}

# Older syntax (without Annotated)
# async def read_items_old(commons: dict = Depends(common_parameters)): ...
# async def read_current_user_old(current_user: dict = Depends(get_current_user)): ...
# async def create_item_db_old(item_name: str, db: dict = Depends(get_db_session)): ...
```

**Key Points:**

*   Use `Depends(dependency_function)` as the default value for the parameter where you want the result injected.
*   Using `typing.Annotated` (`Annotated[ReturnType, Depends(dependency_function)]`) is the recommended modern syntax (Python 3.9+).
*   Dependencies can receive parameters from the request (path, query, body, headers, cookies) just like path operations.
*   Dependencies can depend on other dependencies. FastAPI resolves the graph.
*   Use `yield` within a dependency function (or an `async` generator) to perform setup actions before yielding the resource and teardown actions after the path operation finishes (e.g., opening/closing database connections/sessions).
*   FastAPI caches the result of a dependency *within the same request*. If multiple dependencies or the path operation itself depend on the *same* dependency function with the *same* parameters, it's only executed once per request.

Dependency injection is a core feature for writing clean, reusable, and testable code in FastAPI. Use it to handle authentication, database sessions, complex parameter processing, and other shared logic.