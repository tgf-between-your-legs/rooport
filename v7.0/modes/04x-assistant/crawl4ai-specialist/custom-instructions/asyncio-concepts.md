# Python AsyncIO Concepts for Crawl4AI

This document provides a brief overview of `asyncio` concepts relevant to using the `crawl4ai` library.

## Core Ideas

*   **Asynchronous Programming:** Allows multiple tasks (like network requests) to run concurrently without blocking the main thread. Instead of waiting for one task to finish, the program can switch to another task that's ready to run.
*   **`async` / `await`:** Keywords used to define and manage asynchronous operations.
    *   `async def function_name():` Defines an asynchronous function (a coroutine).
    *   `await expression`: Pauses the execution of the current coroutine, allowing the event loop to run other tasks, until the `await`ed expression (usually another coroutine or an awaitable object) completes.
*   **Event Loop:** The core of `asyncio`. It manages and distributes the execution of different asynchronous tasks. `crawl4ai` manages its own event loop internally when you call `crawler.run()`.
*   **Coroutines:** Special functions defined with `async def`. When called, they return a coroutine object, which doesn't execute immediately but can be run by the event loop (often via `await`).
*   **Concurrency vs. Parallelism:** `asyncio` provides concurrency (multiple tasks making progress over time on a single thread) by switching between tasks during I/O waits. It does *not* typically provide true parallelism (multiple tasks running simultaneously on multiple CPU cores), although libraries can sometimes bridge this gap.

## Relevance to `crawl4ai`

*   `crawl4ai.AsyncWebCrawler` is built on `asyncio`.
*   The `crawler.run()` method handles the event loop and manages the concurrent execution of web requests, browser interactions, and filtering.
*   Understanding `async`/`await` is helpful if you need to write custom processing logic *around* the `crawler.run()` call or integrate it into a larger `asyncio` application, but often not strictly necessary just to configure and run the crawler itself.
*   The `concurrency` option in `CrawlerOptions` controls how many crawling tasks `crawl4ai` attempts to run concurrently using `asyncio`.

*(Consult the official Python `asyncio` documentation for a full understanding.)*