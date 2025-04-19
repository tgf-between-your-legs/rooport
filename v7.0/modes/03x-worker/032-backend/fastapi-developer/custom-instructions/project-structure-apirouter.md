# FastAPI: Project Structure & `APIRouter`

Organizing larger FastAPI applications using `APIRouter`.

## Problem: Single File Limitations

For very small APIs, defining all path operations in a single `main.py` might be sufficient. However, as the application grows, this becomes unmanageable.

## Solution: `APIRouter`

FastAPI provides `APIRouter`, which works like a mini `FastAPI` application. It allows you to group related path operations together, typically within separate Python modules (files). You can then include these routers in your main `FastAPI` application instance.

**Benefits:**
*   **Modularity:** Keeps related endpoints together (e.g., all user-related endpoints in `users.py`, all item-related endpoints in `items.py`).
*   **Organization:** Improves code readability and maintainability.
*   **Reusability:** Routers can potentially be reused or shared.
*   **Prefixing & Tagging:** Routers can have a common URL prefix (e.g., `/users`) and tags applied to all their path operations.

## Implementation Steps

1.  **Create Router Files:** Create separate Python files for different logical sections of your API (e.g., `routers/users.py`, `routers/items.py`).
2.  **Instantiate `APIRouter`:** In each router file, import and create an instance of `APIRouter`.
3.  **Define Path Operations on Router:** Use the router instance decorator (`@router.get`, `@router.post`, etc.) instead of the main app instance (`@app.get`).
4.  **Include Router in Main App:** In your main application file (`main.py`), import the router instances and include them in the main `FastAPI` app using `app.include_router()`.

**Example Structure:**

```
your_project/
├── main.py             # Main FastAPI app instance
├── schemas.py          # Pydantic models
├── crud.py             # Database interaction functions (optional)
├── dependencies.py     # Dependency functions (optional)
└── routers/
    ├── __init__.py
    ├── items.py        # Router for item-related endpoints
    └── users.py        # Router for user-related endpoints
```

**Example: `routers/items.py`**

```python
# routers/items.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Annotated
from .. import schemas, crud # Assuming schemas/crud are in parent dir
from ..dependencies import SessionDep, get_current_active_user # Assuming dependencies exist

# Create a router instance
router = APIRouter(
    prefix="/items", # All routes in this router will start with /items
    tags=["Items"], # Group endpoints under "Items" tag in docs
    # dependencies=[Depends(get_current_active_user)], # Apply dependency to ALL routes in this router
    responses={404: {"description": "Not found"}}, # Default response for this router
)

@router.get("/", response_model=List[schemas.ItemResponse])
async def read_items(
    db: SessionDep,
    skip: int = 0,
    limit: int = 100,
    # current_user: schemas.User = Depends(get_current_active_user) # Or apply per-route
):
    # items = crud.get_items(db=db, skip=skip, limit=limit)
    # return items
    return [] # Placeholder

@router.get("/{item_id}", response_model=schemas.ItemResponse)
async def read_item(item_id: int, db: SessionDep):
    # db_item = crud.get_item(db=db, item_id=item_id)
    # if db_item is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    # return db_item
    # Placeholder:
    if item_id == 1:
         return schemas.ItemResponse(id=1, name="Example", price=10.0, owner={"id": 1, "username": "test", "email": "test@example.com"}, created_at=datetime.now())
    raise HTTPException(status_code=404, detail="Item not found")


@router.post("/", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item_for_user(
    item: schemas.ItemCreate,
    db: SessionDep,
    current_user: Annotated[schemas.User, Depends(get_current_active_user)] # Require auth here
):
    # return crud.create_user_item(db=db, item=item, user_id=current_user.id) # Assuming user ID needed
    # Placeholder:
    return schemas.ItemResponse(id=1, owner=current_user, created_at=datetime.now(), **item.model_dump())

# ... other item-related endpoints (PUT, DELETE, etc.) ...
```

**Example: `main.py`**

```python
# main.py
from fastapi import FastAPI
from .routers import items, users # Import routers

app = FastAPI(title="My Structured API")

# Include the routers
app.include_router(users.router)
app.include_router(items.router)

# You can still define global path operations here if needed
@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

```

## `include_router` Options

*   **`prefix`:** Add a URL prefix to all routes defined in the included router (e.g., `prefix="/api/v1"`).
*   **`tags`:** Add tags to all routes in the included router for documentation grouping.
*   **`dependencies`:** Apply dependencies to all routes in the included router.
*   **`responses`:** Define default responses for status codes for all routes in the router.

Using `APIRouter` is the standard way to structure FastAPI applications beyond a few endpoints, promoting better organization and maintainability.

*(Refer to the official FastAPI Bigger Applications documentation: https://fastapi.tiangolo.com/tutorial/bigger-applications/)*