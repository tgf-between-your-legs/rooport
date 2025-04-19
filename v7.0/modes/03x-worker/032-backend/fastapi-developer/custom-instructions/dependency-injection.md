# FastAPI: Dependency Injection (`Depends`)

Using FastAPI's powerful dependency injection system to manage dependencies and share logic.

## Core Concept

Dependency Injection (DI) is a design pattern where components receive their dependencies from an external source rather than creating them internally. FastAPI implements DI via the `Depends` function (and `Annotated` type hints).

FastAPI's DI system handles:
*   **Code Reusability:** Define shared logic (e.g., getting a database session, verifying authentication, complex parameter processing) in a dependency function and reuse it across multiple path operations.
*   **Resource Management:** Dependencies using `yield` can manage setup and teardown logic (e.g., opening and closing database connections/sessions).
*   **Hierarchical Dependencies:** Dependencies can depend on other dependencies, creating a graph that FastAPI resolves automatically.
*   **Integration with Path Operations:** Dependencies can receive request data (path/query parameters, request body, headers, cookies) just like path operation functions.
*   **Automatic Documentation:** Dependencies are integrated into the OpenAPI schema.

## Defining Dependencies

A dependency is typically a function (sync or async) that FastAPI will call before executing your path operation function.

```python
from fastapi import Depends, HTTPException, status, Header
from typing import Optional, Annotated # Use Annotated for Python 3.9+

# Example Dependency 1: Simple value provider
async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

# Example Dependency 2: Getting current user (simulated)
async def get_current_user(token: Annotated[str | None, Header()] = None):
    if token == "fake-valid-token":
        return {"username": "fakeuser", "email": "user@example.com"}
    # In a real app, decode JWT or query DB based on token/session
    # raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return None # Or raise exception if auth is strictly required

# Example Dependency 3: Database Session with yield (Setup/Teardown)
# Assume get_db_session_context is an async context manager for a DB session
# from contextlib import asynccontextmanager
# @asynccontextmanager
# async def get_db_session_context():
#     db = await create_db_connection()
#     try:
#         yield db # Value yielded is injected
#     finally:
#         await db.close()

async def get_db(): # Dependency function using the context manager
    # async with get_db_session_context() as session:
    #    yield session
    # Placeholder:
    print("DB Session Opened (Simulated)")
    yield {"connection": "fake_db_connection"} # Yield the resource
    print("DB Session Closed (Simulated)")


# Type alias for dependency using Annotated (Recommended for Python 3.9+)
CommonsDep = Annotated[dict, Depends(common_parameters)]
CurrentUserDep = Annotated[Optional[dict], Depends(get_current_user)]
DbDep = Annotated[dict, Depends(get_db)] # Using dict as placeholder for session type
```

## Using Dependencies in Path Operations

*   Add a parameter to your path operation function, type hint it with `Annotated[ReturnType, Depends(dependency_function)]`.
*   FastAPI will call the `dependency_function`, inject its return value into your path operation parameter, and handle setup/teardown if `yield` is used.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(commons: CommonsDep, user: CurrentUserDep, db: DbDep):
    print("Current User:", user)
    print("DB Info:", db)
    # Use commons['q'], commons['skip'], commons['limit']
    # Use db session to query items
    return {"message": "Items fetched", "params": commons}

@app.get("/users/me")
async def read_users_me(user: CurrentUserDep):
    if not user:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    return user

# Dependencies can also be used in other dependencies
async def get_admin_user(user: CurrentUserDep):
    if not user or user.get("username") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin required")
    return user

AdminUserDep = Annotated[dict, Depends(get_admin_user)]

@app.get("/admin/dashboard")
async def admin_dashboard(admin: AdminUserDep):
    return {"message": f"Welcome Admin {admin['username']}!"}

```

## Key Concepts

*   **`Depends(dependency)`:** Marks a parameter as requiring a dependency.
*   **`Annotated[Type, Depends(dependency)]`:** The preferred syntax in modern Python/FastAPI, combining the type hint and dependency declaration.
*   **Return Value Injection:** The value returned (or yielded) by the dependency function is passed to the path operation function parameter.
*   **`yield` for Setup/Teardown:** If a dependency function uses `yield`, the code before `yield` runs before the path operation, and the code after `yield` runs after the response is sent (useful for closing DB connections, releasing resources).
*   **Caching:** FastAPI caches the result of a dependency *within the same request*. If multiple path operations or dependencies in the same request depend on the same dependency function with the same parameters, it's only called once per request.
*   **Sub-Dependencies:** Dependencies can depend on other dependencies using the same `Depends`/`Annotated` syntax. FastAPI resolves the entire dependency graph.
*   **Path/Query/Body in Dependencies:** Dependency functions can declare parameters just like path operation functions to receive path parameters, query parameters, request bodies, headers, etc.

Dependency injection is a cornerstone of FastAPI, promoting cleaner, more modular, and testable code.

*(Refer to the official FastAPI Dependency Injection documentation: https://fastapi.tiangolo.com/tutorial/dependencies/)*