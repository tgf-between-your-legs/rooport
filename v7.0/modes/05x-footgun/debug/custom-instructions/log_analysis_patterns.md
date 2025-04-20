# Log Analysis Patterns

This document lists common patterns and keywords to look for when analyzing logs, intended to help formulate specific search instructions for `footgun-debug`.

## Common Error Keywords

Instruct `footgun-debug` to search logs (`search_files` on `.logs/`) for keywords like:

*   `ERROR`
*   `FATAL`
*   `Exception`
*   `Traceback`
*   `panic`
*   `failed`
*   `timeout`
*   `denied`
*   `unauthorized`
*   `invalid`
*   `null pointer` / `nil pointer`
*   `segmentation fault` / `segfault`
*   `connection refused`
*   `not found` / `404`
*   `server error` / `500`

## Contextual Patterns

Consider instructing searches based on context:

*   **Transaction/Request IDs:** Search for specific IDs provided in the error report (e.g., `search_files` for `request_id="xyz123"`).
*   **User IDs:** Search for actions related to a specific user ID experiencing the issue.
*   **Timestamps:** Search for log entries within a specific time window around when the error occurred (e.g., using `grep` via `execute_command` if precise time matching is needed and `search_files` regex is insufficient).
*   **Specific Components/Modules:** Search for log entries originating from a suspected component (e.g., `[AuthService]`, `module=payment_processor`).
*   **Sequence of Events:** Instruct the mode to read log sections before and after an error to understand the sequence leading up to it.

## Success/Informational Patterns (for comparison)

Sometimes understanding normal operation helps identify deviations:

*   `INFO`
*   `DEBUG` (if enabled)
*   `success`
*   `completed`
*   `request processed`
*   `connection established`

*(Adapt this list based on the specific logging formats and common issues within the project. Provide `footgun-debug` with precise patterns and file targets.)*