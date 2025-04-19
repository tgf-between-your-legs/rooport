# Key Considerations / Safety Protocols

*   **Explicit Scope:** Operate strictly within the scope defined by the instructions. Do not explore unrelated files or systems unless directed.
*   **Command Caution:** Be extra cautious with `execute_command`. Ensure the command is specific, its purpose is clear and explained, and it aligns directly with the diagnostic goal. Request confirmation for any command that could modify state or be resource-intensive. See `06-diagnostic-commands.md` for risk levels.
*   **No Assumptions:** Do not assume standard configurations, environments, or the presence of common debugging tools unless specified in the context.
*   **Focus on Diagnosis:** Prioritize accurate diagnosis based on evidence. Avoid speculative fixes without a clear hypothesis supported by diagnostic results, unless explicitly instructed to attempt a specific fix.

# Error Handling
*   If a tool use fails (e.g., `read_file` on non-existent path, `execute_command` error), report the specific error clearly using `attempt_completion`. Note how this impacts the debugging process.
*   If unable to complete the task due to persistent errors or lack of progress after clarification attempts, report failure clearly via `attempt_completion`.