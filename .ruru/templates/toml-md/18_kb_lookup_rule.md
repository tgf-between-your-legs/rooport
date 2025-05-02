+++
id = "KB-LOOKUP-RULE-TEMPLATE"
title = "KB Lookup Rule Template"
context_type = "rules"
scope = "Mode-specific knowledge base access"
target_audience = ["{{mode_slug}}"]
granularity = "rule"
status = "active"
last_updated = "{{current_date}}" # Placeholder for dynamic date
# version = ""
# related_context = []
tags = ["kb-lookup", "knowledge-base", "rule", "template"]
# relevance = ""
# target_mode_slug = "{{mode_slug}}" # Removed as per instruction
kb_directory = ".ruru/modes/{{mode_slug}}/kb/"
+++

# Knowledge Base (KB) Lookup Rule

**Applies To:** `{{mode_slug}}` mode

**Rule:**

Before attempting a task, **ALWAYS** consult the dedicated Knowledge Base (KB) directory for this mode located at:

`{{kb_directory}}`

**Procedure:**

1.  **Identify Keywords:** Determine the key concepts, tools, or procedures relevant to the current task.
2.  **Scan KB:**
    *   a. **Read `README.md`:** Always start by reading the `{{kb_directory}}README.md` for an overview and structure guidance.
    *   b. **List Contents:** Identify relevant files and subdirectories within `{{kb_directory}}`.
    *   c. **Prioritize Top-Level:** Review relevant top-level `.md` files first.
    *   d. **Explore Subdirectories:** If keywords, task context, or the `README.md` suggest relevance, explore pertinent subdirectories. Look for `README.md` or index files within them.
    *   e. **Review Content:** Read the content of potentially relevant files identified.
3.  **Apply Knowledge:** Integrate relevant information from the KB into your task execution plan and response.
4.  **If KB is Empty/Insufficient:** If the KB doesn't contain relevant information, proceed using your core capabilities and general knowledge, but note the potential knowledge gap.

**Rationale:** This ensures the mode leverages specialized, curated knowledge for consistent and effective operation, even if the KB is currently sparse or empty. Adhering to this rule promotes maintainability and allows for future knowledge expansion.