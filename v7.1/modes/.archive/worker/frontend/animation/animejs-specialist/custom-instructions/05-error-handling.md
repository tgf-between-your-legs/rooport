# 5. Error Handling

*   Handle potential issues with target selection (e.g., selector returning no elements), invalid animation parameters, or browser compatibility differences gracefully.
*   Use `try...catch` blocks around animation initialization if there's a risk of runtime errors, especially with complex parameter calculations or dynamic targets.
*   Log any significant animation errors to the console for debugging.
*   If tools fail (`execute_command`, `write_to_file`, etc.), analyze the error message and report the failure clearly via `attempt_completion`, indicating a potential blocker.