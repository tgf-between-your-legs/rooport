# FastAPI: Error Handling

Handling expected and unexpected errors gracefully in FastAPI applications.

## Core Concept: Returning Meaningful Error Responses

When something goes wrong during request processing, the API should return an appropriate HTTP error status code (like 4xx for client errors, 5xx for server errors) and ideally a helpful JSON body explaining the error, rather than crashing or returning a generic server error page.

FastAPI provides several mechanisms for handling errors:

1.  **`HTTPException`:** The standard way to return HTTP errors with specific status codes and details from within your path operation functions or dependencies.
2.  **Custom Exception Handlers:** Define handlers for specific exception types (including custom exceptions or Pydantic's `ValidationError`) to customize the error response format globally.
3.  **Request Validation Errors:** FastAPI automatically catches Pydantic `ValidationError` during request body/parameter validation and returns a detailed 422 Unprocessable Entity response. This can be customized.

## Using `HTTPException`

This is the most common way to handle expected errors within your application logic.

```python
from fastapi import FastAPI, HTTPException, status, Path

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        # Raise HTTPException for expected errors like 'Not Found'
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, # Use status constants
            detail=f"Item not found: {item_id}",
            headers={"X-Error-Source": "Application Logic"}, # Optional custom headers
        )
    return {"item": items[item_id]}

@app.post("/secure-data/")
async def create_secure_data(data: dict, x_token: str | None = Header(None)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"}, # Standard header for 401
        )
    # ... process data ...
    return {"message": "Secure data created", "received_data": data}

```

*   Import `HTTPException` from `fastapi`.
*   Raise it when an error condition is met.
*   Specify `status_code` (use `status` module constants like `status.HTTP_404_NOT_FOUND`).
*   Provide a `detail` message (can be a string, dict, or list) which will form the JSON response body.
*   Optionally add custom `headers`.

## Custom Exception Handlers (`@app.exception_handler`)

Use these to override FastAPI's default handling for specific exception types or to handle your own custom exceptions globally.

```python
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError # For customizing 422 errors
from pydantic import ValidationError # Can also catch Pydantic errors directly

# Define a custom exception
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

# Handler for our custom UnicornException
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT, # Custom status code
        content={"message": f"Oops! {exc.name} did something magical and broke it."},
    )

# Override the default handler for RequestValidationError (422 errors)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Log the detailed error if needed: print(exc.errors(), exc.body)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Validation Failed", "errors": exc.errors()}, # Customize response structure
    )

# Example path operation that might raise the custom exception
@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}

# Example path operation that might raise a validation error (implicitly)
from pydantic import BaseModel
class Item(BaseModel): name: str
@app.post("/items/")
async def create_item(item: Item): return item

```

*   Define a handler function (sync or async) that takes `request: Request` and `exc: YourExceptionType`.
*   Decorate it with `@app.exception_handler(YourExceptionType)`.
*   Return a `Response` object (e.g., `JSONResponse`, `PlainTextResponse`).

## Default Validation Errors (422)

When request data (body, path, query params) fails Pydantic validation, FastAPI automatically catches the `RequestValidationError` and returns a JSON response like:

```json
{
  "detail": [
    {
      "loc": ["body", "item", "price"],
      "msg": "ensure this value is greater than 0",
      "type": "value_error.number.not_gt",
      "ctx": {"limit_value": 0}
    }
    // ... other errors ...
  ]
}
```

You can customize this response format using `@app.exception_handler(RequestValidationError)` as shown above.

Use `HTTPException` for expected errors within your application logic. Use custom exception handlers for global error formatting or handling specific custom exception types. Rely on FastAPI's automatic 422 responses for input validation errors, customizing the handler only if needed.