+++
id = "MCP-MGR-KB-INSTALL-REPOMIX-V1"
title = "KB: Configure repomix MCP Server (via npx)"
context_type = "knowledge_base"
scope = "Procedure for configuring the repomix MCP server"
target_audience = ["agent-mcp-manager"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-03" # Use current date
tags = ["kb", "mcp", "configure", "install", "repomix", "npx", "node"]
related_context = [
    "../agent-mcp-manager.mode.md",
    "~/.roo/mcp.json"
    ]
template_schema_doc = "~/.ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Specific configuration steps for repomix"
+++

# KB: Configure repomix MCP Server (via npx)

This procedure guides the configuration of the `repomix` MCP server. Unlike many MCP servers, `repomix` is typically executed on-demand using `npx` and configured directly within the client's `mcp.json`, rather than running as a persistent background process.

**Repository:** `https://github.com/yamadashy/repomix`
**Documentation:** `https://repomix.com`

## Procedure

1.  **Prerequisites Check:**
    *   Verify `node` is installed and meets the version requirement (>= 18.0.0):
        *   `execute_command` with `node --version`.
        *   If missing or version is too low, inform the user and stop.
    *   Verify `npm` is installed:
        *   `execute_command` with `npm --version`.
        *   If missing, inform the user and stop.

2.  **Explain Execution Method:**
    *   Inform the user that `repomix` runs via `npx`, which downloads and executes the package as needed. No separate installation step like `pip install` or `docker pull` is required for the server itself.

3.  **Update `.roo/mcp.json`:**
    *   Read the current `.roo/mcp.json` using `read_file`.
    *   Construct the new server entry for `repomix`:
        ```json
        {
          "name": "repomix",
          "command": "npx",
          "args": [
            "-y",
            "repomix",
            "--mcp"
          ],
          "cwd": null, // Not applicable for npx global execution
          "enabled": true,
          "environment": {},
          "alwaysAllow": [
            // Add expected tool names here based on repomix capabilities
            // e.g., "generate_context", "search_code" (Placeholder names)
          ],
          "notes": "Configured via agent-mcp-manager using npx method. Requires Node.js v18+.",
          "timeout": 3600 // Default timeout, adjust if needed
        }
        ```
    *   Use `apply_diff` or `search_and_replace` to add/update this entry within the `mcpServers` object in `.roo/mcp.json`. Ensure the resulting file is valid JSON. Pay attention to adding commas correctly if inserting into the middle of the list.

4.  **Report Completion:**
    *   Inform the user that `repomix` has been configured in `.roo/mcp.json`.
    *   Explain that it will be executed using `npx` when needed and requires Node.js v18+ to be available in the environment where the client (e.g., Roo Commander) runs.
    *   Mention that it communicates via stdio, not a network port.