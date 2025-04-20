# FastAPI: Middleware

Adding custom logic to process requests before they reach path operations and responses before they are sent to the client.

## Core Concept: Intercepting Requests & Responses

Middleware in FastAPI (and other ASGI frameworks like Starlette) are functions or classes that sit between the web server and your path operation functions. They allow you to execute code globally for every incoming request and/or outgoing response.

**Use Cases:**

*   **Authentication/Authorization:** Checking credentials or permissions for specific routes or the entire application.
*   **Logging:** Recording details about each request and response.
*   **Performance Monitoring:** Measuring request processing time.
*   **Adding Headers:** Injecting common headers (like `X-Request-ID` or security headers) into responses.
*   **Request Modification:** Modifying the incoming request object before it reaches the path operation (use with caution).
*   **Response Modification:** Modifying the outgoing response object (use with caution).
*   **Error Handling:** Catching specific exceptions globally and modifying the response (though `@app.exception_handler` is often preferred for this).
*   **CORS:** Handling Cross-Origin Resource Sharing headers (FastAPI provides built-in `CORSMiddleware`).
*   **GZip Compression:** Compressing responses (FastAPI provides built-in `GZipMiddleware`).

## Creating Custom Middleware

Middleware can be implemented as simple functions decorated with `@app.middleware("http")` or as classes conforming to the ASGI middleware interface.

**1. Using the `@app.middleware("http")` Decorator (Simpler):**

This is suitable for middleware that needs to process both the request and the response.

```python
import time
from fastapi import FastAPI, Request
from starlette.responses import Response # Import Response from starlette

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    Calculates the time taken to process a request and adds it
    as a custom 'X-Process-Time' header to the response.
    """
    start_time = time.time()
    # Process the request by calling the next middleware or path operation
    response: Response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"Request {request.url.path} processed in {process_time:.4f} secs")
    return response

@app.get("/")
async def main():
    # Simulate some work
    await asyncio.sleep(0.1)
    return {"message": "Hello World"}

```

*   Define an `async` function that accepts `request: Request` and `call_next`.
*   `request`: The incoming request object.
*   `call_next`: An awaitable function that takes the `request` object. You **must** `await call_next(request)` to pass the request to the next middleware or path operation and get the response.
*   Code *before* `await call_next(request)` processes the incoming request.
*   Code *after* `await call_next(request)` processes the outgoing response.
*   The function must return the `response` object.

**2. ASGI Middleware Class (More Complex/Flexible):**

For more complex scenarios or reusable middleware components, you can create a class following the ASGI standard.

```python
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseCall
from starlette.requests import Request
from starlette.responses import Response
import time

class ProcessTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseCall) -> Response:
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        print(f"Request {request.url.path} processed in {process_time:.4f} secs (Class)")
        return response

app = FastAPI()

# Add middleware using app.add_middleware()
app.add_middleware(ProcessTimeMiddleware)

@app.get("/")
async def main():
    await asyncio.sleep(0.1)
    return {"message": "Hello World"}

```

*   Inherit from `starlette.middleware.base.BaseHTTPMiddleware`.
*   Implement the `async def dispatch(self, request, call_next)` method.
*   The logic is similar to the decorator approach: code before `await call_next(request)` handles the request, code after handles the response.
*   Add the middleware class to the application using `app.add_middleware(YourMiddlewareClass, **options)`.

## Built-in Middleware

FastAPI includes (via Starlette) several useful middleware classes:

*   **`CORSMiddleware`:** Handles CORS headers.
    ```python
    from fastapi.middleware.cors import CORSMiddleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], # Or specific origins: ["http://localhost:3000"]
        allow_credentials=True,
        allow_methods=["*"], # Or specific methods: ["GET", "POST"]
        allow_headers=["*"], # Or specific headers
    )
    ```
*   **`GZipMiddleware`:** Compresses responses for clients that support it.
    ```python
    from fastapi.middleware.gzip import GZipMiddleware
    app.add_middleware(GZipMiddleware, minimum_size=1000) # Only compress responses > 1000 bytes
    ```
*   **`HTTPSRedirectMiddleware`:** Redirects HTTP requests to HTTPS (requires server/proxy handling SSL termination).
*   **`TrustedHostMiddleware`:** Validates the `Host` header against allowed hosts.

## Order Matters

Middleware is processed in the order it is added. The request goes through them sequentially before hitting the path operation, and the response goes back through them in reverse order.

```
Request -> Middleware 1 -> Middleware 2 -> Path Operation -> Middleware 2 -> Middleware 1 -> Response
```

Middleware provides a powerful way to add cross-cutting concerns to your FastAPI application. Use the `@app.middleware("http")` decorator for simpler cases or implement ASGI classes for more complex or reusable components. Leverage built-in middleware for common tasks like CORS and GZip.