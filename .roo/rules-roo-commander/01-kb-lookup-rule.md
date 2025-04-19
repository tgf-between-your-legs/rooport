+++
id = "KB-LOOKUP-ROO-COMMANDER"
title = "KB Lookup Rule: Roo Commander"
context_type = "rules"
scope = "Mode-specific knowledge base access"
target_audience = ["roo-commander"]
granularity = "ruleset"
status = "active"
last_updated = "2025-04-18"
# version = ""
# related_context = []
tags = ["kb-lookup", "roo-commander", "knowledge-base"]
# relevance = ""

# --- KB Lookup Specific Fields ---
target_mode_slug = "roo-commander"
kb_directory = ".modes/roo-commander/kb"
+++

# Knowledge Base Lookup Rule: roo-commander

This rule instructs the AI assistant operating in `roo-commander` mode to consult the specified knowledge base directory (`kb_directory`) when it needs specific information, guidelines, or context relevant to this mode's operation.

**Purpose:** To ensure the assistant leverages curated knowledge specific to its role and tasks, improving accuracy, consistency, and adherence to established practices for the `roo-commander` mode.

**Procedure:**

1.  **Identify Need:** When encountering a query or task requiring specialized knowledge about `roo-commander`'s domain, principles, workflows, or constraints.
2.  **Consult KB:** Access and search the contents of the `.modes/roo-commander/kb` directory.
3.  **Synthesize & Apply:** Integrate the retrieved information into the response or task execution.
4.  **Cite (If Applicable):** If directly quoting or relying heavily on a specific KB document, mention the source.

This rule prioritizes the use of the dedicated KB over general knowledge for mode-specific inquiries.