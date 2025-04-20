# FastAPI: Structuring Applications with APIRouter

Organizing larger FastAPI applications by splitting path operations into multiple modules using `APIRouter`.

## Core Concept: Modular Path Operations

As an API grows, putting all path operations into a single `main.py` file becomes unmanageable. FastAPI provides `APIRouter`, a class that works like a "mini" `FastAPI` application. You can define path operations on an `APIRouter` instance in separate modules (e.g., one module for user-related endpoints, another for item-related endpoints) and then include these routers in the main `FastAPI` application.

**Benefits:**

*   **Organization:** Keeps related path operations grouped together in separate files/modules.
*   **Maintainability:** Easier to navigate and modify code for specific features.
*   **Reusability:** Routers can potentially be reused or shared.
*   **Scalability:** Better structure for larger projects with many endpoints.

## Using `APIRouter`

1.  **Create Router Files:** Create separate Python files for different sets of related endpoints (e.g., `routers/items.py`, `routers/users.py`).
2.  **Instantiate `APIRouter`:** In each router file, import and create an instance of `APIRouter`.
3.  **Define Path Operations on Router:** Use the router instance (e.g., `router.get`, `router.post`) instead of the main `app` instance to define path operations within that module.
4.  **Include Router in Main App:** In your main application file (`main.py`), import the router instances and include them in the main `FastAPI` app using `app.include_router()`.

```python
# === Router File 1: routers/items.py ===
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import schemas # Assuming schemas.py exists from previous examples
from dependencies import get_current_user # Assuming a dependency file

# Create a router instance
router = APIRouter(
    prefix="/items", # All paths in this router will start with /items
    tags=["items"], # Group endpoints under "items" tag in OpenAPI docs
    # dependencies=[Depends(get_current_user)], # Apply dependency to ALL routes in this router
    responses={404: {"description": "Item not found"}}, # Default response for 404
)

# In-memory "database" for example
fake_items_db = {"item1": {"name": "Foo"}, "item2": {"name": "Bar"}}

@router.get("/", response_model=List[schemas.ItemResponse])
async def read_items(skip: int = 0, limit: int = 10):
    # Simulate returning items based on actual data structure
    items_list = [{"id": i, **data} for i, data in enumerate(fake_items_db.values(), 1)]
    return items_list[skip : skip + limit]

@router.get("/{item_id}", response_model=schemas.ItemResponse)
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    # Simulate returning item based on actual data structure
    return {"id": hash(item_id), **fake_items_db[item_id]} # Example ID generation

@router.post("/", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: schemas.ItemCreate, current_user: dict = Depends(get_current_user)):
    # Example: Using dependency applied at router level or path operation level
    print(f"User {current_user['username']} creating item.")
    if item.name in fake_items_db: # Simulate check
         raise HTTPException(status_code=400, detail="Item name already exists")
    fake_items_db[item.name] = item.dict()
    return {"id": hash(item.name), **item.dict()}


# === Router File 2: routers/users.py ===
from fastapi import APIRouter, Depends
import schemas
from dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_current_user)], # All user routes require authentication
)

@router.get("/me", response_model=schemas.UserResponse)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    # The dependency is run again, but FastAPI might cache the result within the same request
    return current_user


# === Main Application File: main.py ===
from fastapi import FastAPI, Depends
from .routers import items, users # Import the router modules
# from .dependencies import some_global_dependency # Example global dependency

app = FastAPI(
    # dependencies=[Depends(some_global_dependency)] # Apply dependency to ALL paths in the app
)

# Include the routers
app.include_router(items.router)
app.include_router(users.router)

# You can still define path operations directly on the app
@app.get("/")
async def root():
    return {"message": "Welcome to the main application"}

```

**Key `APIRouter` Parameters:**

*   `prefix`: A path prefix to add to all routes defined in the router (e.g., `/items`).
*   `tags`: A list of strings used to group path operations in the OpenAPI documentation.
*   `dependencies`: A list of dependencies (`Depends(...)`) to apply to *all* path operations in the router.
*   `responses`: Default responses (like `404`) to add to all path operations.

Use `APIRouter` to split your FastAPI application into logical modules based on features or resources. Define path operations on router instances within these modules and include the routers in your main `FastAPI` app using `app.include_router()`. This significantly improves organization and maintainability for larger projects.