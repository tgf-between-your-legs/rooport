# Secure Handling of Firecrawl API Key

**Security is paramount when dealing with API keys.** The Firecrawl API key (`FIRECRAWL_API_KEY`) grants access to a paid service and must be protected.

## Best Practices

1.  **NEVER Hardcode the API Key:** Do not embed the API key directly into scripts (`.py`), commands, or configuration files committed to version control (Git).
2.  **Use Environment Variables:** The recommended method is to store the API key in an environment variable on the system where the crawler runs.
    *   **Setting (Linux/macOS):** `export FIRECRAWL_API_KEY="YOUR_API_KEY_HERE"`
    *   **Setting (Windows CMD):** `set FIRECRAWL_API_KEY=YOUR_API_KEY_HERE`
    *   **Setting (Windows PowerShell):** `$env:FIRECRAWL_API_KEY="YOUR_API_KEY_HERE"`
    *   **Accessing in `curl`:** Use `$FIRECRAWL_API_KEY` (Linux/macOS/Git Bash) or `%FIRECRAWL_API_KEY%` (Windows CMD) within the `Authorization` header.
        ```bash
        # Example for Linux/macOS
        curl ... -H "Authorization: Bearer $FIRECRAWL_API_KEY" ...
        ```
    *   **Accessing in Python:**
        ```python
        import os
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("FIRECRAWL_API_KEY environment variable not set.")
        # Use api_key when initializing Firecrawl client or making requests
        ```
3.  **Configuration Files (Use with Caution):** If environment variables are not feasible, store the key in a configuration file *outside* the Git repository (e.g., add the config file path to `.gitignore`). Load the key from this file at runtime.
4.  **Secrets Management Systems:** For production environments, use dedicated secrets management tools (e.g., AWS Secrets Manager, HashiCorp Vault, Doppler).
5.  **Limit Exposure:** Only provide the API key to the specific process or command that needs it. Avoid logging the key.
6.  **Inform the User/Requester:** When preparing commands (`execute_command`), remind the user/requester that the `$FIRECRAWL_API_KEY` environment variable must be set in their execution environment. Do not ask the user for the key directly in the chat.

**Responsibility:** While the `firecrawl-specialist` mode constructs the API calls, the **user or orchestrator** is responsible for ensuring the API key is securely stored and made available to the execution environment (typically via environment variables).