+++
# --- Basic Metadata ---
id = "RULE-CONTEXT-MGMT-GUIDELINES-V2"
title = "Standard: Context Management & Delegation Guidelines V2"
context_type = "rules"
scope = "Workspace-wide guidelines for managing context and delegating tasks"
target_audience = ["all"] # Applies to Coordinators and Delegates
granularity = "guideline"
status = "active"
last_updated = "2025-06-05" # Use current date
tags = ["context-management", "delegation", "guideline", "workflow", "mcp", "rules"]
related_context = [
    ".ruru/docs/concepts/context_management_strategies_v1.md", # Source whitepaper
    ".roo/rules/06-iterative-execution-policy.md",
    ".roo/rules/10-vertex-mcp-usage-guideline.md",
    ".roo/rules/11-session-management.md"
]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines proactive and reactive context management strategies."
+++

# Standard: Context Management & Delegation Guidelines V2

**Objective:** To ensure reliable task completion, prevent context window overflows, promote efficient resource utilization (including MCPs), and establish clear communication protocols between modes during complex operations. These guidelines complement the reactive checkpointing mechanism defined in Rule `06-iterative-execution-policy.md`.

## 1. Delegation Principles: Task Breakdown

*   **Mandate:** Delegators (Coordinators, Leads) **MUST** break down complex work requests into logically small, focused sub-tasks before delegating to specialist modes. This applies at all levels of delegation; for example, a Lead mode receiving a task from a Coordinator must break it down further before delegating to Specialists.
*   **Judgment over Metrics:** The breakdown **MUST** be based on a qualitative assessment of the work involved (e.g., implementing a single function, modifying a specific configuration section). Avoid relying on unreliable token/line count predictions. Focus on logical coherence and manageable units.
*   **Clarity:** Each delegated sub-task **MUST** have a clear goal and well-defined acceptance criteria (often managed via MDTM checklists).
*   **Rationale:** Smaller, focused tasks reduce context pressure on delegates, improve tracking, and minimize error impact.

## 2. Delegate Pre-Check: Context Estimation

*   **Guideline:** Upon receiving a delegated task, the delegate mode **SHOULD** perform a quick, high-level estimation of the potential context cost required. Consider task complexity, file I/O, generation length, and tool use.
*   **Action if Too Large:** If the estimation suggests the task is likely too large to be completed reliably within the delegate's own context checkpoint thresholds (e.g., likely to exceed ~40-50% usage quickly, per Rule `06`), the delegate **MUST** respond *before* starting significant work.
*   **Response:** Use the `ask_followup_question` tool to inform the delegator that the task appears too large and **MUST** request it be broken down further. The delegate MUST respond to its *immediate* delegator (e.g., a Specialist responds to the Lead, a Lead responds to the Coordinator). Provide specific breakdown suggestions if possible.
*   **Rationale:** Prevents wasted effort on tasks likely to fail due to context limits, shifting breakdown responsibility back to the delegator proactively.

## 3. Leveraging MCPs for Context Offloading

*   **Guideline:** All modes **SHOULD** actively seek opportunities to leverage Model Context Protocol (MCP) servers to manage the primary context window size.
*   **Examples:** Use MCP tools for research, validation, code analysis, or summarization instead of loading large data directly into the main context (e.g., `vertex-ai-mcp-server` tools, `repomix`).
*   **Guiding Context:** Provide sufficient guiding context within MCP tool arguments (queries, topics, URLs) for effective execution. Refer to Rule `10-vertex-mcp-usage-guideline.md` for specific guidance.
*   **Rationale:** Offloading tasks keeps the primary context focused, improving reliability.

## 4. Internal Work Unit Tracking (Optional)

*   **Guideline:** For complex processes within a single delegation, modes **MAY CONSIDER** using internal tracking markers (e.g., "Step 1/3:") in logs or intermediate `attempt_completion` messages.
*   **Rationale:** Improves progress clarity for the coordinator and user, especially if progress doesn't align perfectly with MDTM checklist items.

## 5. Relationship to Iterative Execution (Rule 06)

*   **Complementary:** These guidelines are primarily **proactive and preventative**, focusing on planning, pre-checking, and offloading to *avoid* hitting context limits.
*   **Rule 06 (Iterative Execution Policy):** Provides the **reactive mechanism** for handling situations where context usage approaches thresholds *during* execution, defining the checkpointing and handover procedure.
*   **Synergy:** Together, these proactive strategies and the reactive checkpointing of Rule 06 form a comprehensive approach to context management.

## 6. Summary / Key Takeaways

*   Proactive context management is crucial.
*   Delegators **MUST** break down tasks logically.
*   Delegates **MUST** pre-check task size and push back if too large.
*   Leverage MCPs strategically for context offloading.
*   These guidelines complement the reactive checkpointing in Rule 06.