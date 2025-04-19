# 05: Error Handling

*   **Error Handling Note:** If file saving (`write_to_file`) or logging (`apply_diff`) fail, analyze the error. Log the failure to the task log (`.tasks/[TaskID].md`) using `apply_diff` if possible, and report the issue in your `attempt_completion` message to the `design-lead`, potentially indicating a 🧱 BLOCKER.