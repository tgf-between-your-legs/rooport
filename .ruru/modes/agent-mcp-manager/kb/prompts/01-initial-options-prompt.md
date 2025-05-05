+++
# --- Basic Metadata ---
id = "AGENT-MCP-MANAGER-KB-PROMPT-INITIAL-OPTIONS-V1"
title = "MCP Manager Agent: KB Prompt - Initial Options"
context_type = "kb"
scope = "Defines the initial <ask_followup_question> prompt for the MCP Manager Agent"
target_audience = ["agent-mcp-manager"]
granularity = "content"
status = "active"
last_updated = "2025-05-05" # Use current date
tags = ["kb", "prompt", "mcp", "initialization", "options", "agent-mcp-manager"]
related_context = [
    ".roo/rules-agent-mcp-manager/01-initialization-rule.md"
]
template_schema_doc = ".ruru/templates/toml-md/18_kb_article.README.md" # Assuming a generic KB template schema
relevance = "High: Contains the core initial prompt content"
+++

# KB Prompt: Initial Options for MCP Manager Agent

This file contains the standard initial prompt presented by the `agent-mcp-manager` mode using the `<ask_followup_question>` tool, as referenced in rule `AGENT-MCP-MANAGER-RULE-INIT-V1`.

```xml
 <ask_followup_question>
  <question>Welcome to the MCP Manager Agent! What would you like to do?</question>
  <follow_up>
    <suggest>🔌 Install Vertex AI Server</suggest> <!-- Option 1 -->
    <suggest>🌐 Install Custom Server from Github URL (Placeholder)</suggest> <!-- Option 3 -->
    <suggest>📚 Install Other MCP Servers...</suggest> <!-- Option 4 (New) -->
    <suggest>🗑️ Remove an existing MCP Server</suggest> <!-- Option 5 -->
    <suggest>🔄 Check for MCP Server Updates (Placeholder)</suggest> <!-- Option 6 -->
    <suggest>❌ Cancel</suggest> <!-- Option 7 -->
  </follow_up>
 </ask_followup_question>