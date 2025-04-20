# 5. Error Handling

*   Implement robust error handling in SQL/PL/pgSQL (`EXCEPTION` blocks) where appropriate.
*   Handle connection errors gracefully in application code (coordinate with backend devs).
*   Analyze errors from `psql`, `neonctl`, or Neon API calls.
*   Report tool errors or persistent blockers via `attempt_completion`.