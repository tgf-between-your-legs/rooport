+++
id = "KB-LOOKUP-ROO-COMMANDER"
title = "KB Lookup Rule: Roo Commander"
context_type = "rules"
scope = "Mode-specific knowledge base access"
target_audience = ["roo-commander"]
granularity = "ruleset"
status = "active"
last_updated = "2025-04-20" # Updated date
tags = ["kb-lookup", "roo-commander", "knowledge-base"]

# --- KB Lookup Specific Fields ---
target_mode_slug = "roo-commander"
kb_directory = ".modes/roo-commander/kb" # Points to the KB directory
+++

# Knowledge Base Lookup Rule: roo-commander

This rule instructs the AI assistant operating in `roo-commander` mode to consult the specified knowledge base directory (`kb_directory`) when it needs specific, detailed information, guidelines, or context relevant to this mode's operation (e.g., detailed workflow steps, specific procedures, large reference lists).

**Purpose:** To leverage curated knowledge specific to the `roo-commander` mode efficiently, keeping the main prompt context focused while allowing access to detailed information on demand.

**Procedure:**

1.  **Identify Need:** When encountering a query or task requiring detailed knowledge about `roo-commander`'s domain, specific procedures, workflows, or constraints not covered by core operational principles.
2.  **Consult KB:** Use the `read_file` tool to access the relevant document within the `.modes/roo-commander/kb/` directory. Use the KB README (`.modes/roo-commander/kb/README.md`) to identify the correct document if unsure.
3.  **Synthesize & Apply:** Integrate the retrieved information into the response or task execution.
4.  **Cite (If Applicable):** If directly quoting or relying heavily on a specific KB document, mention the source file.

This rule prioritizes using the dedicated KB for detailed, situational information, complementing the core principles loaded automatically.