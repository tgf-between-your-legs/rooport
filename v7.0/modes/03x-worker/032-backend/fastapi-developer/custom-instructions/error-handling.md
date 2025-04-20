# FastAPI: Error Handling

Handling errors gracefully and providing informative responses in FastAPI.

## Core Concept

FastAPI provides several mechanisms for handling errors that occur during request processing:

*   **Automatic Validation Errors:** Pydantic model validation failures automatically trigger HTTP `422 Unprocessable Entity` responses with detailed error information.
*   **`HTTPException`:** A standard way to return HTTP error responses with specific status codes and details from within your path operations or dependencies.
*   **Custom Exception Handlers:** Define handlers for specific exception types (including `HTTPException` or custom exceptions) to customize the error response format or perform additional actions (like logging).

## Automatic 422 Errors (Pydantic Validation)

*   When request data (body, path/query parameters mapped to Pydantic models) fails validation against the defined model types or constraints, FastAPI automatically catches the `RequestValidationError` and returns a JSON response with status code `422`.
*   The response body contains a `detail` field, which is a list of objects, each describing a specific validation error (location, message, type).

```json
// Example 422 Response Body
{
  "detail": [
    {
      "loc": [ // Location of the error
        "body", // In the request body
        "item", // Field name
        "price" // Nested field name (if applicable)
      ],
      "msg": "Input should be greater than 0", // Human-readable message
      "type": "greater_than" // Pydantic error type
    },
    {
      "loc": [ "query", "limit" ], // Error in query parameter
      "msg": "Input should be less than or equal to 100",
      "type": "less_than_equal"
    }
  ]
}
```

## `HTTPException`

*   Use `HTTPException` to manually trigger standard HTTP error responses from your code.
*   **Import:** `from fastapi import HTTPException`
*   **Usage:** `raise HTTPException(status_code=..., detail=..., headers=...)`
    *   `status_code` (Required): The HTTP status code (e.g., `404`, `403`, `400`). Use `fastapi.status` for standard codes (e.g., `status.HTTP_404_NOT_FOUND`).
    *   `detail` (Optional): Any JSON-serializable value (string, dict, list) providing details about the error.
    *   `headers` (Optional): Dictionary of custom headers to include in the response (e.g., `{"WWW-Authenticate": "Bearer"}` for 401 errors).

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID '{item_id}' not found",
            headers={"X-Error-Source": "Item Lookup"}, # Custom header
        )
    return {"item": items[item_id]}

# Example in a dependency
async def verify_admin(is_admin: bool = False): # Simplified check
    if not is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
```

## Custom Exception Handlers (`@app.exception_handler`)

*   Use decorators to register functions that handle specific exception types raised during request processing.
*   Allows you to customize the response format, log errors, or perform other actions when a particular error occurs.
*   Handlers receive the `request: Request` and the `exc: Exception` instance.
*   They should return a `Response` object (e.g., `JSONResponse`).

```python
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError # Import Pydantic validation error
from pydantic import BaseModel

# Example Custom Exception
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

# Handler for our custom UnicornException
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418, # I'm a teapot ;)
        content={"message": f"Oops! {exc.name} did something magical. But it's an error."},
    )

# Handler to override the default 422 validation error format
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_details = []
    for error in exc.errors():
        field = " -> ".join(map(str, error["loc"])) # Join location path
        error_details.append({"field": field, "message": error["msg"]})
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, # Change status code if desired
        content={"error_code": "VALIDATION_FAILED", "errors": error_details},
    )

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    if item.name == "unicorn":
        raise UnicornException(name=item.name) # Raise custom exception
    return item

@app.get("/test-validation")
async def test_validation(price: int): # Expects int, will fail if string passed
    return {"price": price}

```

**Order:** Exception handlers are checked from specific to general. If you have handlers for both `Exception` and a specific subclass like `UnicornException`, the `UnicornException` handler will be called first if that specific exception is raised.

Use `HTTPException` for standard HTTP errors within your logic, and custom exception handlers for global error formatting or handling specific custom exceptions.

*(Refer to the official FastAPI Error Handling documentation: https://fastapi.tiangolo.com/tutorial/handling-errors/)*