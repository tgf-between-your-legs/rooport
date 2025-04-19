# FastAPI: Automatic API Documentation (OpenAPI / Swagger UI / ReDoc)

Leveraging FastAPI's built-in interactive API documentation features.

## Core Concept

FastAPI automatically generates an **OpenAPI schema** for your API based on your path operations, parameters, Pydantic models, type hints, and docstrings. This schema conforms to the OpenAPI standard.

Furthermore, FastAPI automatically includes two interactive documentation UIs that use this schema:

1.  **Swagger UI:** Available by default at `/docs`. Provides a rich interface to explore endpoints, view schemas, and interactively send requests to the API.
2.  **ReDoc:** Available by default at `/redoc`. Provides an alternative, often cleaner, documentation-focused view of the API schema.

## How it Works

FastAPI inspects:

*   **Path Operations:** Decorators (`@app.get`, etc.), path parameters (`/items/{item_id}`).
*   **Parameters:** Type hints, default values, and `Query()`, `Path()`, `Header()`, `Cookie()`, `Body()` functions for query parameters, path parameters, headers, cookies, and request body fields.
*   **Pydantic Models:** Used for request bodies (`item: ItemCreate`) and response models (`response_model=ItemResponse`). Field names, types, defaults, and `Field()` descriptions are used.
*   **Type Hints:** Standard Python type hints (`int`, `str`, `bool`, `list[Item]`, `Optional[str]`).
*   **Docstrings:** The docstring of a path operation function is used as the description and summary in the OpenAPI schema.

## Enhancing Documentation

You can improve the generated documentation by providing more metadata:

*   **`FastAPI()` App Metadata:**
    *   `title`: API title.
    *   `description`: API description (supports Markdown).
    *   `version`: API version.
    *   `openapi_tags`: Define tags used for grouping path operations.
    ```python
    from fastapi import FastAPI

    tags_metadata = [
        {"name": "Users", "description": "Operations with users."},
        {"name": "Items", "description": "Manage items."},
    ]

    app = FastAPI(
        title="My Super API",
        description="This API does **amazing** things. Supports _Markdown_.",
        version="1.0.0",
        openapi_tags=tags_metadata
    )
    ```
*   **Path Operation Metadata:**
    *   `tags`: List of tags to group this operation under.
    *   `summary`: Short summary (often taken from the first line of the docstring).
    *   `description`: Longer description (supports Markdown, taken from the rest of the docstring).
    *   `response_description`: Description for the success response.
    *   `deprecated`: Mark the operation as deprecated (`True`).
    ```python
    @app.post(
        "/items/",
        response_model=ItemResponse,
        status_code=status.HTTP_201_CREATED,
        tags=["Items"], # Assign to "Items" group
        summary="Create a new item",
        response_description="The created item",
    )
    async def create_item(item: ItemCreate):
        """
        Create an item with all the information:

        - **name**: each item must have a name
        - **description**: a long description
        - **price**: required
        - **tags**: a list of tags
        """
        # ... implementation ...
        return item
    ```
*   **Parameter Metadata (`Query`, `Path`, `Header`, `Cookie`, `Body`):**
    *   Use these functions (imported from `fastapi`) as default values for parameters to add validation and documentation.
    *   Common arguments: `default`, `title`, `description`, `min_length`, `max_length`, `gt`, `le`, `regex`, `deprecated`, `examples`.
    ```python
    from fastapi import Query, Path

    @app.get("/search/")
    async def search(
        q: str | None = Query(
            default=None,
            title="Query String",
            description="The string to search for in item names.",
            min_length=3,
            deprecated=True # Example: Mark as deprecated
        ),
        limit: int = Query(default=10, le=100, description="Maximum number of results") # le = less than or equal
    ):
        # ...
        pass

    @app.get("/files/{file_path:path}") # Use :path converter for paths with /
    async def read_file(
        file_path: str = Path(..., description="The full path to the file") # ... means required
    ):
        # ...
        pass
    ```
*   **Pydantic `Field()`:** Add `title`, `description`, `examples`, validation constraints within your Pydantic models.
    ```python
    from pydantic import BaseModel, Field

    class Item(BaseModel):
        name: str = Field(..., title="Item Name", description="Name of the item", min_length=3)
        price: float = Field(..., gt=0, description="Price in USD", examples=[10.50, 99.99])
    ```

## Disabling Docs

You can disable the automatic documentation UIs by setting `docs_url=None` and `redoc_url=None` when creating the `FastAPI` instance (useful for production environments if docs shouldn't be public). You can still access the schema via `openapi_url` (default `/openapi.json`), which can also be disabled (`openapi_url=None`).

```python
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
```

By leveraging type hints, Pydantic models, and FastAPI's parameters, you get comprehensive, interactive API documentation with minimal extra effort.

*(Refer to the official FastAPI documentation tutorials on Path Parameters, Query Parameters, Body, and Metadata: https://fastapi.tiangolo.com/tutorial/)*