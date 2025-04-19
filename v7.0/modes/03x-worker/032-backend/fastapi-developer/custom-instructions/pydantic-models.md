# FastAPI: Pydantic Models for Validation & Serialization

Using Pydantic's `BaseModel` with Python type hints for data validation, serialization, and documentation in FastAPI.

## Core Concept

Pydantic is a data validation and settings management library using Python type annotations. FastAPI leverages Pydantic models (`BaseModel`) extensively to:

1.  **Declare Request Bodies:** Define the expected structure and types of incoming JSON data.
2.  **Validate Data:** Automatically validate incoming request data against the model's type hints and validators. Returns structured validation errors if checks fail.
3.  **Serialize Response Data:** Define the structure and types of outgoing JSON data using `response_model`. Pydantic handles converting your return data (e.g., ORM objects, dictionaries) into the specified JSON structure.
4.  **Generate OpenAPI Schema:** FastAPI uses Pydantic models to automatically generate the JSON Schema definitions within the OpenAPI documentation (`/docs`, `/redoc`).

## Defining Models (`BaseModel`)

*   Import `BaseModel` from `pydantic`.
*   Define a class inheriting from `BaseModel`.
*   Declare fields using standard Python type hints (`str`, `int`, `float`, `bool`, `list[T]`, `dict[K, V]`, `datetime`, etc.).
*   Provide default values if needed.
*   Use `Optional[T]` or `T | None` for optional fields (defaulting to `None` or using `Field(default=None)`).

```python
# schemas.py (or models.py, depending on convention)
from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import List, Optional
from datetime import datetime

class ItemBase(BaseModel):
    name: str = Field(..., min_length=3, description="The name of the item") # ... means required
    description: Optional[str] = Field(default=None, description="Optional item description")
    price: float = Field(..., gt=0, description="Price must be positive") # gt = greater than
    tags: List[str] = [] # List of strings, defaults to empty list

class ItemCreate(ItemBase):
    # Inherits fields from ItemBase
    pass # No additional fields needed for creation in this example

class ItemUpdate(BaseModel):
    # All fields optional for partial updates (PATCH)
    name: Optional[str] = Field(default=None, min_length=3)
    description: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    tags: Optional[List[str]] = None

class User(BaseModel):
    id: int
    username: str
    email: EmailStr # Pydantic provides specific types like EmailStr
    website: Optional[HttpUrl] = None # And HttpUrl

class ItemResponse(ItemBase):
    id: int
    owner: User # Nested Pydantic model
    created_at: datetime

    # Pydantic V2: Use model_config = ConfigDict(...)
    # Pydantic V1: Use class Config: orm_mode = True
    model_config = {
        "from_attributes": True # Allow creating model from ORM object attributes
    }
    # class Config: # Pydantic V1 syntax
    #     orm_mode = True
```

## Using Models in Path Operations

*   **Request Body:** Type hint a path operation parameter with your Pydantic model. FastAPI automatically reads the request body as JSON, validates it, and provides the parsed Pydantic model instance.
*   **Response Model:** Use the `response_model` parameter in the path operation decorator (`@app.post(...)`) to specify the Pydantic model for the response. FastAPI filters the return value to match the model and serializes it.
*   **Query/Path Parameters:** Can also use Pydantic models for complex query parameters using `Depends`.

```python
# main.py
from fastapi import FastAPI, HTTPException, Depends, status
from typing import List, Annotated # Use Annotated for Depends in newer Python/FastAPI
from .schemas import ItemCreate, ItemResponse, ItemUpdate # Import models
# Assume db_session dependency and crud functions exist
# from .dependencies import get_db_session
# from . import crud

app = FastAPI()

# Dependency for database session (example)
# SessionDep = Annotated[Session, Depends(get_db_session)]

@app.post(
    "/items/",
    response_model=ItemResponse, # Define the response shape
    status_code=status.HTTP_201_CREATED # Set default success status code
)
async def create_item(
    item_in: ItemCreate, # Request body validated against ItemCreate model
    # db: SessionDep # Example dependency injection
):
    # 'item_in' is now a validated Pydantic model instance
    # db_item = crud.create_item(db=db, item=item_in)
    # FastAPI will serialize db_item according to ItemResponse model
    # return db_item
    # Placeholder response:
    return ItemResponse(id=1, owner={"id": 1, "username": "test", "email": "test@example.com"}, created_at=datetime.now(), **item_in.model_dump())


@app.get("/items/", response_model=List[ItemResponse])
async def read_items(skip: int = 0, limit: int = 100):
    # items = crud.get_items(db=db, skip=skip, limit=limit)
    # return items
    # Placeholder:
    return []

@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int):
    # db_item = crud.get_item(db=db, item_id=item_id)
    # if db_item is None:
    #     raise HTTPException(status_code=404, detail="Item not found")
    # return db_item
    # Placeholder:
    if item_id == 1:
         return ItemResponse(id=1, name="Example", price=10.0, owner={"id": 1, "username": "test", "email": "test@example.com"}, created_at=datetime.now())
    raise HTTPException(status_code=404, detail="Item not found")

@app.patch("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item_update: ItemUpdate):
    # item_update contains only fields provided in PATCH request body
    # update_data = item_update.model_dump(exclude_unset=True) # Get only provided fields
    # updated_item = crud.update_item(db=db, item_id=item_id, update_data=update_data)
    # if updated_item is None:
    #     raise HTTPException(status_code=404, detail="Item not found")
    # return updated_item
    # Placeholder:
    if item_id == 1:
        # Simulate update
        base_data = {"id":1, "name":"Example", "price":10.0, "owner":{"id": 1, "username": "test", "email": "test@example.com"}, "created_at":datetime.now()}
        update_data = item_update.model_dump(exclude_unset=True)
        base_data.update(update_data)
        return ItemResponse(**base_data)
    raise HTTPException(status_code=404, detail="Item not found")

```

Pydantic models are fundamental to FastAPI, providing data validation, serialization, and documentation with minimal code.

*(Refer to the official FastAPI documentation on Pydantic Models: https://fastapi.tiangolo.com/tutorial/body/ and Response Model: https://fastapi.tiangolo.com/tutorial/response-model/)*