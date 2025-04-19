# FastAPI: Async / Await

Leveraging asynchronous operations in FastAPI for high concurrency.

## Core Concept: Asynchronous I/O

*   **Problem:** Traditional synchronous web frameworks handle one request at a time per worker process/thread. If a request involves waiting for I/O (like a database query or an external API call), the worker is blocked and cannot handle other requests.
*   **Solution (Async):** Asynchronous frameworks like FastAPI (built on Starlette and using `asyncio`) can handle multiple I/O-bound operations concurrently within a single process/thread. When an `await` is encountered for an I/O operation, the framework pauses that request's execution and switches to handle another request. Once the I/O operation completes, the framework resumes the paused request.
*   **Benefit:** Significantly increases concurrency and throughput for applications with many I/O-bound operations, using fewer resources compared to thread-based synchronous frameworks.

## Using `async def` in FastAPI

*   **Path Operations:** Declare your path operation functions with `async def` if they perform any `await` operations (e.g., calling async database drivers, async HTTP clients, `asyncio.sleep`).
    ```python
    import asyncio
    from fastapi import FastAPI

    app = FastAPI()

    # Example async database call (simulated)
    async def fetch_data_from_db(item_id: int):
        await asyncio.sleep(0.1) # Simulate DB query delay
        return {"item_id": item_id, "data": "some data"}

    @app.get("/items/{item_id}")
    async def read_item(item_id: int): # Use async def
        print(f"Fetching item {item_id}...")
        # Use await to call async functions
        data = await fetch_data_from_db(item_id)
        print(f"Finished fetching item {item_id}")
        return data
    ```
*   **Dependencies:** Dependency functions can also be `async def` and use `await`. FastAPI handles awaiting them correctly.
    ```python
    async def get_external_data():
        # Assume httpx is installed: pip install httpx
        import httpx
        async with httpx.AsyncClient() as client:
            response = await client.get("https://example.com/data")
            response.raise_for_status() # Raise exception for bad status codes
            return response.json()

    @app.get("/external-data")
    async def get_data(external_data: dict = Depends(get_external_data)):
        return {"source": "external", "data": external_data}
    ```
*   **Synchronous Code:** If you define a path operation with standard `def` (synchronous), FastAPI runs it in an external threadpool to avoid blocking the main async event loop. This allows mixing sync and async code, but `async def` is generally preferred for I/O-bound tasks for better performance. **Never call blocking I/O operations directly inside an `async def` function without `await`**.

## When to Use `async def`

*   When your path operation needs to `await` an async function (database query with an async driver, HTTP request with `httpx`, `asyncio.sleep`, etc.).
*   When interacting with WebSocket connections (`await websocket.receive_text()`, `await websocket.send_text()`).
*   When calling other async libraries.

## Common Pitfalls

*   **Mixing Sync and Async Incorrectly:** Calling a blocking synchronous function (like `time.sleep()` or a sync database call) inside an `async def` path operation *without* running it in a threadpool (e.g., using `asyncio.to_thread` in Python 3.9+) will block the entire event loop, defeating the purpose of async. FastAPI handles standard `def` functions in a threadpool automatically, but be careful with libraries called *within* an `async def`.
*   **Not Awaiting:** Forgetting to use `await` when calling an async function. This won't wait for the function to complete and will likely cause errors or unexpected behavior.
*   **Choosing Libraries:** Ensure you use async-compatible libraries for I/O operations within `async def` functions (e.g., `httpx` instead of `requests`, `asyncpg` instead of `psycopg2` sync, async SQLAlchemy/SQLModel).

FastAPI's seamless support for `async`/`await` is a key feature for building high-performance, I/O-bound APIs.

*(Refer to the official FastAPI Async documentation: https://fastapi.tiangolo.com/async/)*