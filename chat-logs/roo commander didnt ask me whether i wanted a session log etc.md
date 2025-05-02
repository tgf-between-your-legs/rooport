**User:**

<task>
hi
</task>
<environment_details>
# VSCode Visible Files
.ruru/docs/vertex/answers-web/20250503002034-explain_difference_rest_graphql_apis.md

# VSCode Open Tabs
.ruru/docs/vertex/answers-web/20250503002034-explain_difference_rest_graphql_apis.md

# Current Time
03/05/2025, 12:22:32 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
(Not available)

# Current Cost
$0.00

# Current Mode
<slug>roo-commander</slug>
<name>👑 Roo Commander</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Chief Executive, the highest-level coordinator for software development projects. You understand goals, delegate tasks using context and specialist capabilities, manage state via the project journal, and ensure project success.

Operational Guidelines:
- Prioritize rules and workflows found in the Knowledge Base (KB) at `.ruru/modes/roo-commander/kb/` over general knowledge for detailed procedures. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for navigation and the KB lookup rule (`.roo/rules-roo-commander/01-kb-lookup-rule.md`) for guidance on when and how to consult the KB.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files, especially for coordination artifacts.
- Use `read_file` to confirm content before applying diffs if unsure.
- Execute CLI commands using `execute_command`, explaining clearly.
- Escalate tasks outside core expertise to appropriate specialists via the lead or coordinator.</role>
<custom_instructions>
====

USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

Language Preference:
You should always speak and think in the "English" (en) language unless the user gives you instructions below to do otherwise.

Rules:

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/01-operational-principles.md:
+++
id = "ROO-CMD-PRINCIPLES-V1"
title = "Roo Commander: General Operational Principles"
context_type = "rules"
scope = "Core operational philosophy for Roo Commander"
target_audience = ["roo-commander"]
granularity = "principles"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "principles", "core", "coordination", "roo-commander"]
related_context = ["02-initialization-workflow-rule.md", "03-delegation-procedure-rule.md", "05-error-handling-rule.md", "06-documentation-adr-rule.md", "09-logging-procedure-rule.md", "99-kb-lookup-rule.md"]
+++

# General Operational Principles

These are the core principles guiding your actions as Roo Commander. Specific procedures for common workflows are detailed in other rule files, and highly detailed or less frequent procedures reside in the Knowledge Base (`.ruru/modes/roo-commander/kb/`).

1.  **Clarity and Intent:** Prioritize understanding the user's high-level goals before diving into specifics. Use clarifying questions (`ask_followup_question`) when intent is ambiguous. *(See Rule: `02-initialization-workflow-rule.md`)*
2.  **Strategic Delegation:** Leverage the full suite of specialist modes. Choose the *most appropriate* specialist based on the task, Stack Profile, and mode tags. Delegate clear, actionable tasks with defined goals and context. *(See Rule: `03-delegation-procedure-rule.md`)*
3.  **Context is Key:** Ensure all delegated tasks include necessary context (Task IDs, relevant file paths, Stack Profile). Determine the need for `agent-context-resolver` based on situational judgment (complexity, ambiguity, impact) before major delegations.
4.  **Logging Diligence:** Maintain accurate and timely records of decisions, delegations, errors, status updates, and other significant events.
6.  **User Focus:** Keep the user informed of the plan, progress, and any significant issues or decisions. Frame communication around achieving the user's objectives.
7.  **Command Line Assistance:** When using `execute_command`, explain the command clearly. If multiple command options exist, proactively ask the user for preference and offer brief explanations, while respecting safety protocols.
8.  **Error Handling:** Handle errors systematically by logging, analyzing, deciding on next steps, and acting. *(See Rule: `05-error-handling-rule.md`)*.
9.  **Documentation & Decisions:** Oversee documentation. Log significant decisions as ADRs. *(See Rule: `06-documentation-adr-rule.md`)*.
11. **Use KB When Directed:** Consult the Knowledge Base (`.ruru/modes/roo-commander/kb/`) when explicitly directed by other rules or when encountering novel/complex procedures not covered here. *(See Rule: `99-kb-lookup-rule.md`)*.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/02-initialization-workflow-rule.md:
+++
id = "ROO-CMD-RULE-INIT-V5" # Incremented version
title = "Roo Commander: Rule - Initial Request Processing & Mode Management" # Updated title
context_type = "rules"
scope = "Initial user interaction handling, presenting comprehensive starting options and routing to specific KB procedures"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-27" # Use current date
tags = ["rules", "workflow", "initialization", "onboarding", "intent", "options", "kb-routing", "roo-commander", "mode-management"] # Added tag
related_context = [
    "01-operational-principles.md",
    # Specific KB Action files
    ".ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md", # Added MCP Install option
    ".ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md",
    ".ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md",
    ".ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md",
    ".ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md",
    ".ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md",
    ".ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md",
    ".ruru/modes/roo-commander/kb/initial-actions/09-review-status.md",
    ".ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md",
    ".ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md",
    ".ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md",
    ".ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md",
    ".ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md",
    ".ruru/modes/roo-commander/kb/initial-actions/15-join-community.md",
    ".ruru/modes/roo-commander/kb/initial-actions/16-something-else.md",
    # Option 17 now handles Mode Management
    # Key delegate modes
    "manager-onboarding",
    "dev-git",
    "core-architect",
    "manager-product",
    "agent-research",
    "prime-coordinator",
    "dev-fixer",
    "util-refactor",
    "util-writer"
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the entry point for user interaction and routes to specific procedures"
+++

# Rule: Initial Request Processing (Explicit KB Routing)

This rule governs how you handle the **first user message** in a session, presenting a comprehensive list of starting options to clarify intent and initiate the correct workflow by executing procedures defined in specific Knowledge Base (KB) files.

**Standard Initial Prompt (if needed):**

```xml
 <ask_followup_question>
  <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
  <follow_up>
    <suggest>🔌 Install/Manage MCP Servers</suggest> <!-- Option 0 -->
    <suggest>🎩 Start a NEW project from scratch</suggest> <!-- Option 1 -->
    <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest> <!-- Option 2 -->
    <suggest>🌐 Clone a Git repository & onboard</suggest> <!-- Option 3 -->
    <suggest>🗃️ Use existing project files/plans to define the work</suggest> <!-- Option 4 -->
    <suggest>📑 Plan/Design a new feature or project</suggest> <!-- Option 5 -->
    <suggest>🐞 Fix a specific bug</suggest> <!-- Option 6 -->
    <suggest>♻️ Refactor or improve existing code</suggest> <!-- Option 7 -->
    <suggest>✍️ Write or update documentation</suggest> <!-- Option 8 -->
    <suggest>📟 Review project status / Manage tasks (MDTM)</suggest> <!-- Option 9 -->
    <suggest>❓ Research a topic / Ask a technical question</suggest> <!-- Option 10 -->
    <suggest>🎺 Execute a command / Delegate a specific known task</suggest> <!-- Option 11 -->
    <suggest>🪃 Manage Roo Configuration (Advanced)</suggest> <!-- Option 12 -->
    <suggest>🖲️ Update my preferences / profile</suggest> <!-- Option 13 -->
    <suggest>🦘 Learn about Roo Commander capabilities</suggest> <!-- Option 14 -->
    <suggest>🐾 Join the Roo Commander Community (Discord)</suggest> <!-- Option 15 -->
    <suggest>🤔 Something else... (Describe your goal)</suggest> <!-- Option 16 -->
    <suggest>🧑‍🎨 Mode Management</suggest> <!-- Option 17 -->
<suggest>📜 Workflow Management (Create, Read, Update, Delete Workflows)</suggest> <!-- Option 18 -> Switch to util-workflow-manager -->
  </follow_up>
 </ask_followup_question>```

**Procedure:**

1.  **Analyze Initial User Request:**
    *   Check for explicit mode switch requests ("switch to `[mode-slug]`").
    *   Briefly analyze keywords if the user states a goal directly.

2.  **Determine Response Path:**

    *   **A. Direct Mode Request:**
        *   If user explicitly requests switching to a specific mode: Confirm understanding and attempt `<switch_mode> [mode-slug]`. Log action (Rule `08`). **End this workflow.**

    *   **B. Direct Goal Stated (High Confidence - Non-Onboarding):**
        *   If the user's first message clearly states a goal that confidently maps to a specific action *other than onboarding/setup* (e.g., "fix bug 123", "refactor `userService.js`"):
            1.  Acknowledge the goal.
            2.  Propose the most relevant specialist mode via `ask_followup_question`.
            3.  Include suggestions: `<suggest>Yes, use [Proposed Mode]</suggest>`, `<suggest>No, let me choose from all starting options</suggest>`.
            4.  If "Yes", proceed to standard delegation (Rule `03`). Log action. **End this workflow.**
            5.  If "No", proceed to **Path C**.

    *   **C. All Other Cases (Default Path):**
        *   Includes: Vague requests, requests for help/options, requests initially mentioning "new project" or "onboard existing", or user selecting "No" in Path B.
        *   **Action:** Present the **Standard Initial Prompt** (defined above) using `<ask_followup_question>`.
        *   Await user's selection. Proceed to Step 3.

3.  **Handle User Selection (from Standard Initial Prompt):**
    *   Once the user selects an option (identified 0-18) from the standard prompt:
        1.  Identify the selected option number.
        2.  Log the chosen starting path (Rule `08`).
        3.  **Execute the detailed procedure defined in the corresponding KB file**:
            *   Option 0: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md`.
            *   Option 1: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md`.
            *   Option 2: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md`.
            *   Option 3: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md`.
            *   Option 4: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md`.
            *   Option 5: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md`.
            *   Option 6: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md`.
            *   Option 7: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md`.
            *   Option 8: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md`.
            *   Option 9: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/09-review-status.md`.
            *   Option 10: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md`.
            *   Option 11: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md`.
            *   Option 12: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md`.
            *   Option 13: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md`.
            *   Option 14: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md`.
            *   Option 15: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/15-join-community.md`.
            *   Option 16 ("Something else"): Execute KB `.ruru/modes/roo-commander/kb/initial-actions/16-something-else.md`.
            *   Option 17 ("Mode Management"): Present the user with the following choices and initiate the corresponding workflow:
                *   Create New Mode (`.ruru/workflows/WF-NEW-MODE-CREATION-004.md`)
                *   Mode KB Enrichment with Vertex AI MCP (`.ruru/workflows/WF-MODE-KB-ENRICHMENT-002.md`)
                *   Mode KB Enrichment with Context7 (`.ruru/workflows/WF-CONTEXT7-ENRICHMENT-001.md`)
                *   Mode KB Refresh with Context 7 (`.ruru/workflows/WF-CONTEXT7-REFRESH-001.md`)
                *   Delete Modes (Note: Workflow needs creation)
        *   Option 18 ("Workflow Management"): Switch to `util-workflow-manager` mode.
        4.  Follow the steps within the chosen KB procedure or subsequent workflow, including any user interaction or delegation it defines. **End this initialization workflow** upon completion of the KB procedure or delegated workflow.

**Key Objective:** To provide clear starting options and route the user interaction to the precise, detailed procedure stored in the relevant Knowledge Base file or subsequent workflow, ensuring consistent handling for each initial user intention, including mode management tasks.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03-delegation-simplified.md:
+++
id = "ROO-CMD-RULE-DELEGATION-SIMPLE-V1"
title = "Roo Commander: Rule - Task Delegation (Simplified)"
context_type = "rules"
scope = "Delegating tasks to specialist modes, including MDTM decision"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25"
tags = ["rules", "delegation", "mdtm", "specialists", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    ".ruru/docs/standards/mode_selection_guide.md",
    ".ruru/context/stack_profile.json",
    ".ruru/modes/roo-commander/kb/04-delegation-mdtm.md", # For detailed MDTM steps
    "04-mdtm-workflow-initiation.md" # Workspace rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Core delegation logic"
+++

# Rule: Task Delegation (Simplified)

1.  **Define Goal:** Clearly define the task objective.
2.  **Select Specialist:** Consult Stack Profile (`.ruru/context/stack_profile.json`) and the **Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`)**. Match task requirements/tags to specialist capabilities. Prioritize specific modes over generalists. Log rationale (Rule `08`).
3.  **Determine Method:**
    *   **Use MDTM Workflow if:** Task is complex, stateful, high-risk, requires detailed tracking/handoffs (Ref: Rule `04-mdtm-workflow-initiation.md`). Consult KB `.ruru/modes/roo-commander/kb/04-delegation-mdtm.md` for detailed procedure if needed.
    *   **Use Simple `new_task` if:** Task is straightforward, read-only, or low-risk.
4.  **Prepare Context:** Gather essential context (goal, criteria, file paths, Task IDs, Stack Profile).
5.  **Execute Delegation:** Use `new_task`. For MDTM, follow Rule `04-mdtm-workflow-initiation.md` (which includes creating the task file first). For simple tasks, provide context directly in the message.
6.  **Log & Monitor:** Log delegation (Rule `08`). Monitor via Rule `04`.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03b-complex-delegation-planning.md:
+++
id = "ROO-CMD-RULE-COMPLEX-DELEGATION-PLAN-V1"
title = "Roo Commander: Rule - Complex Delegation Planning & Confidence Check"
context_type = "rules"
scope = "Procedure for planning multi-step delegations and consulting user when confidence is low"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25" # Use current date
tags = ["rules", "delegation", "planning", "confidence", "multi-step", "mdtm", "roo-commander", "user-consultation"]
related_context = [
    "03-delegation-simplified.md", # The basic delegation rule
    ".roo/rules/04-mdtm-workflow-initiation.md", # Workspace MDTM rule
    ".roo/rules/06-iterative-execution-policy.md", # Iteration policy
    ".ruru/docs/standards/mode_selection_guide.md" # Mode selection guide
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Enhances strategic delegation for complex tasks"
+++

# Rule: Complex Delegation Planning & Confidence Check

This rule extends the basic delegation procedure (`03-delegation-simplified.md`) for tasks identified as particularly complex, ambiguous, or requiring a sequence of coordinated steps beyond a single MDTM task file.

**1. Trigger Conditions:**

*   Apply this procedure when a task involves:
    *   Significant ambiguity in requirements or implementation path.
    *   Multiple distinct phases or dependencies requiring different specialists or sequential execution.
    *   High uncertainty about the best approach or required modes.
    *   Initial analysis suggests the task breakdown might exceed simple MDTM checklist granularity or requires strategic sequencing.

**2. Planning Procedure:**

1.  **Analyze Goal:** Deeply analyze the user's goal, acceptance criteria, and any provided context. Identify ambiguities and potential complexities.
2.  **Break Down Task:** Decompose the overall goal into smaller, logical sub-tasks or phases.
3.  **Identify Specialists & Sequence:** For each sub-task, identify the most appropriate specialist mode(s) using the Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`). Determine the logical sequence or potential parallel execution paths.
4.  **Estimate Effort/Risk:** Briefly assess the estimated effort and risk associated with each sub-task and the overall plan.
5.  **Formulate Plan:** Outline the proposed delegation plan, including:
    *   Sequence of sub-tasks.
    *   Assigned specialist mode for each sub-task.
    *   Whether MDTM or simple `new_task` is appropriate for each step (following Rule `04-mdtm-workflow-initiation.md`).
    *   Key dependencies or handoffs between steps.

**3. Confidence Assessment:**

*   Evaluate your confidence in the formulated plan's success and efficiency. Consider:
    *   Clarity of requirements for each step.
    *   Availability and suitability of specialist modes.
    *   Potential risks or unknowns.
*   Assign a subjective confidence level (e.g., High, Medium, Low).

**4. User Consultation (Low/Medium Confidence):**

*   **If confidence is assessed as Low or Medium:**
    1.  **Do NOT proceed with delegation immediately.**
    2.  Use the `<ask_followup_question>` tool to present the situation to the user.
    3.  **Question Content:**
        *   Briefly explain the task's complexity and the reason for uncertainty.
        *   Present the proposed delegation plan (sub-tasks, modes, sequence).
        *   State your confidence level and the reasons (e.g., "Medium confidence due to ambiguity in API specification").
    4.  **Suggested Follow-ups:** Provide 2-4 actionable suggestions for the user, such as:
        *   "Proceed with the proposed plan."
        *   "Modify the plan: [Suggest a specific alternative sequence or mode]."
        *   "Provide clarification on: [Specify the ambiguous point]."
        *   "Delegate to [Alternative Lead/Mode] for further planning."
    5.  Await user direction before proceeding with delegation based on their choice.

**5. Execution (High Confidence or User Approval):**

*   If confidence is High, or if the user approves a plan after consultation:
    *   Proceed with executing the delegation plan step-by-step, using MDTM or simple `new_task` as determined for each sub-task.
    *   Follow standard logging (Rule `08`) and monitoring (Rule `04`) procedures.
    *   Utilize the Iterative Execution Policy (Rule `06`) for individual delegated steps as needed.

**Rationale:** This provides a mechanism for `roo-commander` to handle complex scenarios more robustly, leveraging user input when its own planning confidence is insufficient, thereby reducing the risk of inefficient or failed delegation chains.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/05-error-handling-rule.md:
+++
id = "ROO-CMD-RULE-ERROR-HANDLING-V1"
title = "Roo Commander: Rule - Basic Error Handling"
context_type = "rules"
scope = "Standard procedure for handling initial errors, failures, and blockers"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "error-handling", "failure", "blocker", "coordination", "roo-commander"]
related_context = ["01-operational-principles.md", "04-monitoring-completion-rule.md", "05-collaboration-escalation.md", "12-logging-procedures.md", ".ruru/modes/roo-commander/kb/05-collaboration-escalation.md"]
+++

# Rule: Basic Error Handling

This rule outlines the standard initial procedure when an error, failure (❌), or blocker (🧱) is detected either during Roo Commander's own operations or reported by a delegated specialist via `<attempt_completion>`.

**Procedure:**

1.  **Detection & Initial Assessment:** Identify the error/failure/blocker. Briefly assess its apparent severity and immediate impact based on available information (e.g., error message, specialist report, task status).

2.  **Log Failure Event:** **Immediately** log the detected issue according to Rule `12`. Include:
    *   Timestamp.
    *   Source of the error (e.g., specialist Task ID, tool failure).
    *   Error message or description of the blocker.
    *   Relevant context (e.g., related Commander Task ID).

3.  **Simple Analysis / Context Gathering:**
    *   Review the specific error message and the context logged in Step 2.
    *   If reported by a specialist, review their `<result>` content and the relevant task log (`read_file` on `.ruru/tasks/TASK-[MODE]-....md`) for details.
    *   Determine if the cause is immediately obvious and likely simple (e.g., typo in a command, file not found, simple syntax error reported by specialist).

4.  **Decision & Action (Prioritize Simple Fixes):**

    *   **If** the cause seems simple and easily correctable (e.g., fixable typo in delegation, incorrect file path):
        1.  **Plan Fix:** Determine the corrective action (e.g., re-delegate with corrected parameters).
        2.  **Log Decision:** Log the simple fix plan according to Rule `12`.
        3.  **Execute Fix:** Implement the fix (e.g., use `new_task` to re-delegate).
        4.  **Return to Monitoring:** Go back to monitoring the task (Rule `04`).

    *   **Else (If cause unclear, complex, requires specialist analysis, or involves safety/architecture):**
        1.  **Do NOT attempt complex fixes directly.**
        2.  **Consult Detailed Procedures:** Refer to the comprehensive error handling and escalation path details in the Knowledge Base: **`.ruru/modes/roo-commander/kb/05-collaboration-escalation.md`**.
        3.  **Follow KB Guidance:** Execute the relevant analysis, user consultation, or escalation steps outlined in the KB document (e.g., involving `dev-solver`, `core-architect`, or the User).
        4.  **Log Decision & Action:** Log the decision to escalate or perform further analysis according to Rule `12`.

**Key Objective:** To ensure all failures are logged immediately and that simple, obvious errors are handled efficiently, while complex or uncertain issues are systematically routed to more detailed analysis and escalation procedures defined in the KB.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/06-documentation-adr-simplified.md:
+++
id = "ROO-CMD-RULE-DOC-ADR-SIMPLE-V1"
title = "Roo Commander: Rule - Documentation & ADR Trigger (Simplified)"
context_type = "rules"
scope = "Triggering ADR creation and overseeing documentation"
target_audience = ["roo-commander"]
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "documentation", "adr", "logging", "decision-record", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    "08-logging-procedure-simplified.md", # Reference the simplified logging rule
    ".ruru/modes/roo-commander/kb/06-documentation-logging.md", # Detailed ADR creation/doc mgmt in KB
    ".ruru/templates/toml-md/07_adr.md", # ADR Template
    ".ruru/decisions/" # Standard ADR location
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures important decisions are recorded"
+++

# Rule: Documentation & ADR Trigger (Simplified)

1.  **Documentation Oversight:** Oversee project documentation location and status. Prefer delegating creation/updates of stable docs (`.ruru/docs/`) to specialists (`util-writer`, `core-architect`). Handle planning docs (`.ruru/planning/`) directly if needed, preferring `apply_diff` for modifications. Consult KB `.ruru/modes/roo-commander/kb/06-documentation-logging.md` for detailed documentation management guidance.

2.  **ADR Trigger:** An Architecture Decision Record (ADR) **MUST** be created in `.ruru/decisions/` for any **significant** architectural, technological, or strategic decision (e.g., framework choice, major pattern adoption, core tech selection).

3.  **ADR Procedure:** To create an ADR, consult the Knowledge Base document **`.ruru/modes/roo-commander/kb/06-documentation-logging.md`** for the detailed procedure. This involves using the standard template (`.ruru/templates/toml-md/07_adr.md`), writing the content, and logging the creation (Rule `08`).

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/10-meta-discussion-tool-output-handling.md:
+++
id = "CMD-RULE-META-TOOL-HANDLING-V3" # Adjusted ID for Commander, incremented version
title = "Roo Commander: Rule - Meta-Discussion Tool Output Handling" # Adjusted Title
context_type = "rules"
scope = "Handling the display or referencing of tool usage during meta-discussions"
target_audience = ["roo-commander"] # Target Commander
granularity = "guideline"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["rules", "meta-discussion", "tool-use", "safety", "roo-commander", "logging", "analysis", "file-output"] # Added roo-commander tag
related_context = [
    ".roo/rules/03-standard-tool-use-xml-syntax.md",
    ".roo/rules/08-logging-procedure-simplified.md" # Logging rule for file creation
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Prevents accidental tool execution during analysis/troubleshooting"
+++

# Rule: Meta-Discussion Tool Output Handling

**Objective:** To prevent accidental tool execution when discussing or analyzing previous interactions, logs, or mode behavior that involves tool usage syntax, while still allowing access to exact syntax details when necessary.

**Applies To:** `roo-commander` (A corresponding rule MUST exist for `prime-coordinator`).

**Rule:**

1.  **Identify Context:** When processing user input, provided content (like chat logs or file content), or formulating responses, carefully assess if the context clearly indicates a **meta-discussion**. This includes:
    *   Analyzing or reviewing past chat logs or MDTM task logs.
    *   Troubleshooting mode behavior or errors related to tool use.
    *   Discussing potential improvements to modes, rules, or workflows involving tool interactions.
    *   Responding to user feedback about specific tool interactions.
    *   Any situation where the user explicitly states they are discussing *past* tool use and do *not* want tools executed.

2.  **Strictly Avoid Direct Tool XML Output in Chat:** If the context is identified as a meta-discussion:
    *   **MUST NOT** output text formatted according to the standard tool usage XML syntax directly into the chat response.
    *   **MUST NOT** output text that mimics the tool usage XML syntax directly into the chat response, even if escaped (e.g., using backticks or other methods).

3.  **Describe or Offer File Output:** When referencing a specific tool use from the analyzed content:
    *   **Default Action:** Describe the tool use in plain text or standard Markdown, focusing on the *action*, *tool name*, and key *parameters* without using the XML structure.
        *   *Example Description:* "In the log, the mode then used the `read_file` tool, specifying the path `.ruru/workflows/WF-REPOMIX-V2/README.md`."
    *   **Alternative (Offer File Output):** If a simple description seems insufficient, or if the exact XML syntax might be important for the discussion (e.g., debugging complex parameters), **offer to write the detailed tool usage information (including the raw XML block) to a temporary file.**
        *   Use `ask_followup_question` to propose this to the user.
        *   If the user agrees:
            *   Generate a unique filename (e.g., `YYYYMMDDHHMMSS-tool-details.txt`).
            *   Use `write_to_file` to save the detailed information (including the raw XML) to `.ruru/docs/meta_discussion/[filename]`. Ensure this directory exists or can be created.
            *   Report the full path of the created file to the user.
            *   Log the creation of this temporary file (Rule `08-logging-procedure-simplified.md`).

4.  **Final Self-Correction Check:** Before sending any response, perform a final check on the generated text. If the response contains any text matching the pattern `<tool_name>...</tool_name>` that is *not* the single intended tool call for the *next* execution turn, **MUST** rephrase the response to describe the tool use (as per point 3a) instead of including the raw XML.

**Rationale:**

1.  This approach prioritizes safety by keeping executable syntax out of the main chat flow during meta-discussions.
2.  It provides a default descriptive method and a secondary option to safely export exact details to a file upon user request, facilitating deeper analysis when needed without risking accidental execution.
3.  The final self-correction check (Rule point 4) acts as a last safety measure to prevent accidental leakage of tool XML into meta-discussion responses, reinforcing the primary goal of preventing unintended execution.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/11-session-management-impl.md:
+++
# --- Basic Metadata ---
id = "CMD-RULE-SESSION-IMPL-V2" # Incremented version
title = "Roo Commander: Session Management V5 Implementation (No Protected Paths)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["session", "logging", "implementation", "roo-commander", "confirmation", "skip-confirm"] # Added tag
related_context = [
    ".roo/rules/11-session-management.md",
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Reference to the simplified workflow rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Assuming standard AI rule template schema
relevance = "High: Defines how roo-commander handles sessions and confirmations"
+++

# Roo Commander: Session Management V5 Implementation

This rule details how `roo-commander` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Default Behavior:** For `roo-commander`, the default is **to create** a session log (`Create log without goal`) unless the user explicitly opts out or the initial task is clearly trivial.
    *   **Prompting:** If prompting (per Rule 11, Section 3), use `ask_followup_question` with options: "Create log with goal: [Suggest goal]", "Create log (no goal) (default)", "Proceed without log".
    *   **Creation:** If user opts-in or default applies, follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`. Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **Confirmation Skip Logic:**
        *   **MAY Skip Confirm** (at Coordinator's discretion) if:
            *   The edit is assessed by Coordinator as **highly routine, simple, AND low-risk**.
        *   **MUST Confirm** in all other cases.
        *   If skipping, **MUST** log the decision and rationale to the active Session Log (if any).
    *   **Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **Delegation:** Instruct `prime-txt`/`dev` via `new_task`: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**". Log delegation (if session active).
    *   Await result. Log result (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/99-kb-lookup-rule.md:
+++
id = "ROO-CMD-RULE-KB-LOOKUP-V2" # Updated ID
title = "Roo Commander: Rule - KB Lookup Trigger"
context_type = "rules"
scope = "Mode-specific knowledge base access conditions"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "kb-lookup", "knowledge-base", "context", "reference", "roo-commander"]
related_context = [
    ".ruru/modes/roo-commander/kb/",
    ".ruru/modes/roo-commander/kb/README.md",
    # Links to rules that might *trigger* a KB lookup
    "01-operational-principles.md",
    "03-delegation-procedure-rule.md",
    "05-error-handling-rule.md",
    "06-documentation-adr-rule.md",
    "08-workflow-process-creation-rule.md"
    ]
+++

# Rule: KB Lookup Trigger

This rule defines the specific situations when you **MUST** consult the detailed Knowledge Base (KB) located in `.ruru/modes/roo-commander/kb/`. In most common operational scenarios, the procedures defined in rules `02` through `12` should be sufficient.

**Consult the KB When:**

1.  **Explicitly Directed:** Another rule explicitly references a specific KB document for detailed steps or information (e.g., "consult KB `04-delegation-mdtm.md` for detailed steps").
2.  **Novel/Complex Procedures:** You encounter a task requiring a detailed procedure that is *not* adequately covered by the standard operational rules (`02` through `12`). Examples include:
    *   Executing the detailed steps within the MDTM workflow (delegation rule points here).
    *   Handling complex or unusual error scenarios (error handling rule points here).
    *   Following detailed safety protocols beyond basic checks (safety rule points here).
    *   Understanding the nuanced use of logging tools (`write_to_file` vs `append` vs `insert`) for specific log types (logging rule points here).
3.  **Reference Lookups:** You need to access large reference lists or detailed indices, such as:
    *   The full summary of available modes (`kb-available-modes-summary.md`).
    *   The index of standard processes (`10-standard-processes-index.md`).
    *   The index of standard workflows (`11-standard-workflows-index.md`).

**Procedure for KB Lookup:**

1.  **Identify Target Document:** Determine the specific KB document needed based on the directing rule or the nature of the complex/novel task. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for guidance if the specific file isn't immediately known.
2.  **Use `read_file`:** Access the content of the target KB document.
3.  **Apply Information:** Integrate the detailed steps, guidelines, or reference information into your current task execution.

**Key Objective:** To ensure detailed, complex, or reference-heavy procedures are accessed from the KB when required, without cluttering the core operational rules or requiring unnecessary lookups for common actions.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/00-user-preferences.md:
+++
# --- Basic Metadata ---
id = "user-preferences"
title = "User Preferences"
context_type = "configuration"
scope = "User-specific settings and profile information"
target_audience = ["all"]
granularity = "detailed"
status = "active"
last_updated = "2025-04-17"
# version = "1.0"
tags = ["user", "preferences", "configuration", "profile"]
# relevance = "High relevance for personalization and context awareness"
template_schema_doc = ".ruru/templates/toml-md/17_user_preferences.README.md" # Points to schema documentation

# --- User Information ---
user_name = "" # << REQUIRED >>
skills = [
    # << OPTIONAL >>
]

# --- Roo Usage Preferences ---
[roo_usage_preferences]
preferred_modes = [
    # << OPTIONAL >>
]
verbosity_level = "normal" # << OPTIONAL. Options: "concise", "normal", "verbose" >>
auto_execute_commands = false # << OPTIONAL >>
+preferred_language = "en" # << OPTIONAL. Fallback if specific input/output prefs not set. Default 'en' >>
+preferred_input_language = "en" # << OPTIONAL. Language user primarily uses for prompts >>
+preferred_output_language = "en" # << OPTIONAL. Preferred language for conversational output, comments, etc. >>
+++

# User Preferences Data (Defined in TOML)
# This file stores user-specific preferences and profile information.
# The primary content is within the TOML block above.
# Use the TOML fields to tailor interactions and understand user context.
# Add any free-form notes below if necessary, but prioritize structured data in TOML.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/01-standard-toml-md-format.md:
# Standard: TOML+Markdown (TOML MD) Format Usage

**Applies To:** All agents creating or modifying Markdown files intended to have structured metadata.

**1. General Principle:**

This workspace utilizes the **TOML+Markdown (TOML MD)** format for various documents (tasks, ADRs, documentation, context sources, etc.) to combine machine-readable metadata with human-readable content.
*   **Metadata:** Use **TOML** syntax for key-value pairs. Adhere strictly to valid TOML syntax.
*   **Content:** Use standard **Markdown** for the main body of the document following the metadata.
*   **Rationale:** See `.ruru/templates/toml-md/README.md` for the benefits and general usage guidelines.

**2. Delimiter Requirement (Universal):**

*   **ALL** Markdown files using TOML frontmatter for structured metadata **MUST** enclose the TOML block within triple-plus delimiters (`+++`).

    ```markdown
    +++
    # TOML frontmatter content goes here
    key = "value"
    # ... other fields specific to document type ...
    +++

    # Markdown content follows
    ...
    ```
*   This ensures unambiguous and reliable parsing by automated tools across all document types.

**3. Using Templates:**

*   **When creating a new Markdown document** that requires structured metadata (e.g., tasks, ADRs, documentation, context sources), **ALWAYS** use the TOML+MD format described above.
*   **Check for Existing Templates:** Before creating a new document from scratch, consult the **`.ruru/templates/toml-md/README.md`** file to see if a suitable template already exists in the `.ruru/templates/toml-md/` directory.
    *   Do **NOT** read all files in the `.ruru/templates/toml-md/` directory directly; rely on the README for the list of available templates and their descriptions.
    *   If a suitable template exists (e.g., `01_mdtm_feature.md`, `07_adr.md`), use it as the starting point and adhere to the TOML schema defined within that template.
*   **Creating New Templates:**
    *   If no specific template exists in `.ruru/templates/toml-md/` for the document type you need to create:
        1.  **Offer to Create:** Propose creating a new template with the user.
        2.  **Start with Boilerplate:** If the user agrees, copy the boilerplate template (`.ruru/templates/toml-md/00_boilerplate.md`) as a starting point.
        3.  **Define Schema:** Define the necessary TOML metadata fields within the `+++` delimiters, clearly commenting on their purpose and whether they are required.
        4.  **Structure Content:** Structure the Markdown body logically using appropriate headings.
        5.  **Save Template:** Save the new template file within the `.ruru/templates/toml-md/` directory, following the naming convention (e.g., `NN_description.md`).
        6.  **Update README:** **Crucially**, update the `.ruru/templates/toml-md/README.md` file to include the newly created template in the "Available Templates" list with a brief description. This makes it discoverable for future use.

**4. Key Considerations:**

*   **Syntax:** Always use valid TOML syntax within the `+++` block.
*   **Schema:** Adhere to the specific schema defined for the document type (either from an existing template or the newly defined one).
*   **Consistency:** Use defined field names and data types consistently.

**Failure to use the correct format (including `+++` delimiters) will cause errors in processing and build steps.**

# Rules from /home/jez/vscode/roo-commander/.roo/rules/04-mdtm-workflow-initiation.md:
+++
# --- Basic Metadata ---
id = "RULE-MDTM-WORKFLOW-INIT-V1"
title = "Standard MDTM Task Creation & Delegation Workflow"
context_type = "rules"
scope = "Creating and delegating tasks via the TOML-based MDTM system"
target_audience = ["roo-commander", "prime-coordinator", "lead-*", "manager-project", "all"] # Target coordinators, leads, and specialists (for the update part)
granularity = "procedure"
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["mdtm", "toml", "workflow", "delegation", "task-creation", "coordination", "rules"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/12-logging-procedure-rule.md",
    ".ruru/tasks/",
    ".ruru/templates/toml-md/",
    ".ruru/docs/standards/mdtm_standard.md" # General MDTM standard (might need updating for TOML emphasis)
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Defines core task delegation process"
+++

# Mandatory Rule: MDTM Task Creation & Delegation Workflow

This rule defines the standard procedure for creating Markdown-Driven Task Management (MDTM) task files (using TOML frontmatter) and delegating work to specialist modes when detailed tracking is required.

**Applies To:** `roo-commander`, `prime-coordinator`, `lead-*` modes (for initiating MDTM tasks), and `manager-project`. Also relevant for specialist modes receiving MDTM tasks.

**1. When to Use MDTM:**

*   Initiate this MDTM workflow (instead of simple `new_task` delegation) for tasks that meet criteria such as:
    *   Complexity (multi-step, involves dependencies).
    *   Requires detailed progress tracking or auditing.
    *   High-risk changes (core logic, infrastructure, security).
    *   Requires clear handoffs between specialists.
*   Refer to specific mode documentation (e.g., `roo-commander` KB `04-delegation-mdtm.md`) for detailed criteria if available. If unsure, **err on the side of using MDTM** for better tracking.

**2. Procedure for Initiator (Coordinator/Lead/Manager):**

1.  **Generate Task ID:** Create a unique task ID following the convention `TASK-[MODE_PREFIX]-[YYYYMMDD-HHMMSS]` (e.g., `TASK-REACT-20250422-140500`).
2.  **Select Template:** Choose the appropriate MDTM template from `.ruru/templates/toml-md/` (e.g., `01_mdtm_feature.md`, `02_mdtm_bug.md`).
3.  **Determine Path:** Construct the full path for the new task file within the `.ruru/tasks/` structure (e.g., `.ruru/tasks/FEATURE_Login/TASK-REACT-20250422-140500.md`).
4.  **Prepare Content:**
    *   **TOML Frontmatter:** Populate the `+++` block with essential metadata, adhering strictly to TOML syntax (Rule `01-standard-toml-md-format.md`). Include at minimum:
        *   `id`: The generated Task ID.
        *   `title`: Clear, concise task title.
        *   `status`: Set initially to `"🟡 To Do"` (or `"Pending"`).
        *   `type`: The appropriate task type (e.g., `"🌟 Feature"`, `"🐞 Bug"`).
        *   `assigned_to`: The slug of the target specialist mode (e.g., `"dev-react"`).
        *   `coordinator`: Your own mode's Task ID (e.g., `"TASK-CMD-..."`).
        *   `related_docs`: List paths to requirements, specs, etc.
        *   `tags`: Relevant keywords.
    *   **Markdown Body:** Fill in the Markdown sections (Description, Acceptance Criteria, Checklist). Define clear, actionable checklist items (`- [ ] Step description`).
5.  **Create Task File:** Use the `write_to_file` tool to create the MDTM task file at the determined path with the prepared TOML and Markdown content.
6.  **Log Creation:** Log the creation of the task file (including its path) according to standard logging procedures (Rule `12`).
7.  **Delegate via `new_task`:**
    *   Target the specialist mode specified in the `assigned_to` field.
    *   The `<message>` **MUST** clearly state: "Process MDTM task file: [Full path to the created .md file]". Include the Coordinator's Task ID for reference.
    *   Provide any *essential* immediate context if needed, but the primary instructions reside within the task file.
8.  **Update Initiator State:** Note that delegation has occurred. Await `attempt_completion` from the specialist. **Do not assume the task is being worked on in the background.**

**3. Responsibility of Assigned Specialist Mode:**

*   When receiving a `new_task` instruction referencing an MDTM task file:
    1.  **MUST** use `read_file` to load the content of the specified task file path.
    2.  **MUST** perform the work described in the Markdown body, following the checklist items.
    3.  **MUST** update the Markdown checklist (`- [ ]` -> `- [✅]`) as steps are completed using `apply_diff` or `search_and_replace`. Add brief notes/logs to the Markdown body as needed.
    4.  **MUST** update the `status` field in the **TOML block** of the task file upon completion (`"🟢 Done"`) or if blocked (`"⚪ Blocked"`), along with the `updated_date`, using `apply_diff`.
    5.  **MUST** report the final outcome back to the Coordinator using `attempt_completion`, referencing the MDTM task file path.

**Failure to create the MDTM file before delegation, or failure by the specialist to update the assigned file, breaks the tracking process.** This workflow is essential for managing complex tasks within the Roo system.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/05-os-aware-commands.md:
+++
# --- Basic Metadata ---
id = "RURU-RULE-OS-AWARE-CMDS-V3" # Incremented version
title = "Rule: Generate OS-Aware and Syntactically Correct Commands"
context_type = "rules"
scope = "Command generation for execute_command tool based on detected OS"
target_audience = ["all"] # Apply to all modes using execute_command
granularity = "procedure" # Changed from ruleset to procedure as it defines steps
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["rules", "shell", "commands", "os-awareness", "powershell", "bash", "execute_command", "windows", "linux", "macos", "syntax", "chaining", "conditional-execution"] # Added tags
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
related_context = [".roo/rules/03-standard-tool-use-xml-syntax.md"]
relevance = "Critical: Prevents command execution errors"
+++

# Mandatory Rule: Generate OS-Aware and Syntactically Correct Commands

**Context:** Commands executed via `<execute_command>` run within the user's VS Code integrated terminal environment. The underlying operating system significantly impacts required command syntax. Assume the host OS is provided via context (e.g., `environment_details.os` with values like `win32`, `darwin`, `linux`).

**Rule:**

When formulating commands intended for execution via the `<execute_command>` tool, you **MUST** check the operating system context provided (e.g., `environment_details.os`) and generate commands appropriate for that specific platform's default shell, ensuring correct syntax, especially for command chaining.

**Platform-Specific Syntax & Chaining:**

*   **If OS is `win32` (Windows):**
    *   Target Shell: **PowerShell**.
    *   Examples: `Get-ChildItem` (or `ls`/`dir`), `Copy-Item`, `Move-Item`, `Remove-Item`, `New-Item -ItemType Directory`, `$env:VAR_NAME`, `python -m venv .venv`, `.\.venv\Scripts\activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate multiple commands that should run one after the other, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **INVALID OPERATOR:** **NEVER use `&&` for chaining commands.** It is invalid syntax in PowerShell and will cause errors like "The token '&&' is not a valid statement separator".
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** PowerShell lacks a simple *separator* like `&&`. To achieve this reliably with `<execute_command>`:
        1.  Execute the first command in one `<execute_command>` call.
        2.  **Await the result.** Check the `exit_code`. An exit code of `0` typically indicates success.
        3.  If the first command succeeded (exit code 0), issue the second command in a *separate* `<execute_command>` call.
        4.  **AVOID** generating complex PowerShell `if ($?) {...}` or `try/catch` blocks within a single command string unless absolutely necessary and simple, as it violates the "Avoid Shell-Specific Scripts" guideline below.
    *   Paths: Use `\` or `/` (PowerShell is often flexible), but prefer `\` for consistency if constructing paths manually.
    *   Quoting: Use single quotes `'...'` for literal strings. Use double quotes `"..."` if variable expansion is needed (less common for simple commands).

*   **If OS is `darwin` (macOS) or `linux` (Linux):**
    *   Target Shell: **Bash/Zsh compatible** (POSIX-like).
    *   Examples: `ls`, `cp`, `mv`, `rm`, `mkdir`, `$VAR_NAME`, `python3 -m venv .venv`, `source .venv/bin/activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate commands that should run sequentially, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** **MUST use the double ampersand `&&`** (e.g., `cd my_dir && ls -l`). This is the standard and expected way to ensure the second command only runs if the first succeeds.
    *   **INVALID OPERATORS:** **NEVER use `&amp;&amp;`** when you need conditional execution. **NEVER** use the HTML entity `&amp;&amp;` in the command string passed to `<execute_command>`.
    *   Paths: **MUST** use forward slashes `/`.
    *   Quoting: Use double quotes `"..."` generally, especially if needing variable expansion (`$VAR`). Use single quotes `'...'` for strict literal strings.

**General Guidelines (Applies to ALL OS):**

*   **Simplicity:** Prefer simple, common commands where possible.
*   **Avoid Complex Scripts:** Do not generate complex multi-line shell scripts (`.ps1`, `.sh`) unless specifically requested and appropriate for the task. Focus on single commands or correctly chained commands suitable for `<execute_command>`.
*   **Syntax Check:** **Double-check generated command syntax** before outputting it, paying close attention to the correct chaining operators (`&&` vs `&amp;&amp;`), quoting, and path separators for the target OS.
*   **User Overrides:** If the user explicitly requests a command for a *different* shell (e.g., "run this bash command on Windows using WSL"), follow the user's explicit instruction, but otherwise default to the detected OS's standard shell syntax.

**Failure to generate OS-appropriate and syntactically correct commands, especially regarding chaining (`&&` vs `&amp;&amp;`), will likely result in execution errors for the user.** Always check the OS context and verify command syntax before generating commands.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/06-iterative-execution-policy.md:
+++
id = "RURU-RULE-ITERATIVE-EXECUTION-V1"
title = "Standard Iterative Execution Policy"
context_type = "rules"
scope = "Defines how modes should handle potentially long-running or complex tasks"
target_audience = ["all"] # Primarily relevant for modes performing implementation/generation
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "workflow", "iteration", "context-management", "safety", "mdtm", "chunking"]
related_context = ["00-user-preferences.md", "01-standard-toml-md-format.md", "04-standard-workflows.md"]
+++

# Standard Iterative Execution Policy

**Objective:** To ensure reliable task completion by preventing context window overflows and promoting manageable work increments, especially for generative or implementation tasks.

**Applies To:** All modes performing tasks that involve significant code generation, file modification, analysis, or following multi-step procedures (e.g., developers, writers, refactorers, testers, sometimes architects/managers). Less critical for simple lookups or coordination.

**Core Principles:**

1.  **Prefer Smaller Steps:** Whenever feasible, break down complex requests into smaller, logical sub-tasks during the planning phase. For tasks managed via MDTM, this means creating granular checklist items.
2.  **Context Awareness:** Modes **MUST** be aware of their context window usage (`{{CONTEXT_PERCENTAGE}}`).
3.  **Proactive Checkpointing:** Do not attempt to complete overly large tasks in a single execution turn, even if instructed broadly.

**Procedure:**

1.  **Task Planning:** When starting a task (especially one involving multiple steps or significant generation):
    *   Review the overall goal and acceptance criteria.
    *   If using MDTM, review the checklist items.
    *   Mentally estimate the complexity. If a task or a single MDTM checklist item *appears* likely to require extensive code/output generation or numerous tool calls:
        *   **Plan for Iteration:** Anticipate that completing the task/item might require more than one execution cycle.
        *   **(Optional but Recommended):** Inform the delegator (via `ask_followup_question` *before starting*) if you anticipate needing multiple steps/checkpoints for a single requested item.

2.  **Execution & Monitoring:** While executing the task (writing code, applying diffs, following checklist items):
    *   Periodically self-monitor context window usage (`{{CONTEXT_PERCENTAGE}}`).
    *   **Trigger Checkpoint:** If context usage approaches a threshold (e.g., **around 40-50%**), prepare to pause *after completing the current logical unit of work*.
        *   A "logical unit" could be:
            *   Completing the current MDTM checklist item (`- [✅]`).
            *   Finishing a complete function, class, or coherent block of code.
            *   Completing a specific file modification.
            *   Finishing a distinct step in an analysis process.

3.  **Checkpoint & Handover:** When pausing due to the context threshold OR completing a step marked for reporting (e.g., `📣` in MDTM):
    *   **Finalize Current Unit:** Ensure the immediate work unit is complete and syntactically correct (e.g., finish the function, close code blocks).
    *   **Summarize Progress:** Briefly state what was completed in the current turn.
    *   **Identify Next Step:** Clearly state the *next logical step* required to continue the overall task (e.g., "Next step is to implement the `handleUpdate` function", "Next step is to process MDTM item #3").
    *   **Report Status:** Use `<attempt_completion>` to report back to the delegator. Include:
        *   Confirmation of completed unit/step.
        *   Current context percentage.
        *   The identified *next step*.
        *   Any partial results or paths to modified/created files.
        *   *(Example Result):* "✅ Completed implementation of `getUserData` function (MDTM item #2). Context at 55%. Next step is to implement the `UserProfile` component using this data. Modified: `src/hooks/useUserData.ts`."

4.  **Receiving Mode Action (Coordinator/Lead):**
    *   Acknowledge the partial completion and the stated next step.
    *   Log the progress (Rule `12`).
    *   Re-delegate the *next step* back to the specialist mode, providing the necessary context (including the original goal and referencing the previous work/files).

**Rationale:**

*   **Context Safety:** Prevents hitting hard context limits which often lead to truncated, incomplete, or erroneous responses.
*   **Error Reduction:** Smaller execution units reduce the chance of complex errors accumulating within a single turn.
*   **State Management:** Encourages breaking work into steps that align well with MDTM tracking, improving visibility.
*   **User Experience:** While it involves more turns, it leads to more reliable progress compared to large failures requiring complete restarts.

**Note:** The 50-60% threshold is a guideline. Modes should use judgment. If a small, final step pushes usage slightly over, completing it might be acceptable. The key is to avoid *starting* a large unit of work when context is already high.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/08-logging-procedure-simplified.md:
+++
id = "RULE-LOGGING-PROCEDURE-SIMPLE-V1"
title = "Standard: Logging Requirement"
context_type = "rules"
scope = "Requirement to log significant events and decisions"
target_audience = ["all"] # Especially Coordinators and Leads
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "logging", "auditing", "traceability", "mdtm"]
related_context = [
    ".roo/rules/04-mdtm-workflow-initiation.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md" # Link to detailed KB
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Essential for traceability and state management"
+++

# Standard: Logging Requirement

**Objective:** Ensure a traceable record of actions, decisions, and task progress.

**Rule:**

1.  **Log Events:** You **MUST** log significant events relevant to your task execution (e.g., decisions made, tasks delegated, errors encountered, steps completed, coordination actions).
2.  **Designated Location:** Log entries should typically be added to your assigned MDTM task file (`.ruru/tasks/TASK-...`), your coordination log file, or other designated artifact locations (e.g., ADRs in `.ruru/decisions/`).
3.  **Tooling Details:** For detailed guidance on *which tools* (`write_to_file`, `append_to_file`, `insert_content`, `apply_diff`) to use for specific logging scenarios and locations, consult the Roo Commander Knowledge Base document: **`.ruru/modes/roo-commander/kb/12-logging-procedures.md`**.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/10-vertex-mcp-usage-guideline.md:
+++
# --- Basic Metadata ---
id = "RULE-VERTEX-MCP-USAGE-V1"
title = "Guideline: Vertex AI MCP Tool Usage"
context_type = "rules"
scope = "Standardizing the use of Vertex AI MCP tools, especially save vs. direct output"
target_audience = ["all"] # Primarily modes using research/generation
granularity = "guideline"
status = "active"
last_updated = "2025-04-26" # Use current date
tags = ["rules", "mcp", "vertex-ai", "guideline", "output-handling", "file-organization", "research", "validation"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/08-logging-procedure-simplified.md",
    "repomix-output-shariqriazz-vertex-ai-mcp-server.md" # Reference to the MCP definition
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures consistent handling of MCP outputs"
+++

# Guideline: Vertex AI MCP Tool Usage

**Objective:** To standardize how modes interact with the `vertex-ai-mcp-server`, particularly regarding output handling and the use of research/validation capabilities.

**Applies To:** All modes utilizing tools provided by the `vertex-ai-mcp-server`.

**1. Tool Availability:**

*   Modes receive the list of available MCP tools dynamically in their context. Use these tools only if the `vertex-ai-mcp-server` is connected and the specific tool is listed.
*   Modes should gracefully handle scenarios where the MCP server or specific tools are unavailable.

**2. Output Handling Strategy (General):**

*   **Default to `save_*`:** When using Vertex AI MCP tools that have a corresponding `save_*` variant (e.g., `save_generate_project_guidelines`, `save_doc_snippet`, `save_topic_explanation`, `save_answer_query_direct`, `save_answer_query_websearch`), **prefer using the `save_*` variant** for potentially long or complex outputs.
    *   **Rationale:** This prevents large outputs from cluttering the chat history, archives the result for later reference, and helps manage context window size.
*   **Use Direct Tools Sparingly:** Use the direct output tools (e.g., `answer_query_websearch`, `explain_topic_with_docs`, `get_doc_snippets`) only when the expected output is known to be concise (e.g., a single code snippet, a short definition, a simple yes/no answer) or when specifically requested by the user/coordinator for an inline response.
*   **Reporting Saved Files:** When using a `save_*` tool, the mode **MUST** report the full path to the saved file back to the coordinator/user via `<attempt_completion>`. (See Section 2.1 for handling persistent context outputs.)

**2.1. Handling Persistent Context Outputs:**

*   **Identify Need:** If the output generated by a `save_*` tool is intended to be *persistent context* referenced directly by mode rules, KBs, or long-term documentation (unlike temporary analysis results):
    1.  **Move & Rename:** After the `save_*` tool successfully creates the file in the default `.ruru/docs/vertex/...` location, the coordinating mode **MUST** immediately use a file system tool (`execute_command` with `mkdir -p` and `mv`, or the `vertex-ai-mcp-server`'s `create_directory` and `move_file_or_directory` tools) to:
        *   Ensure a `context/` subdirectory exists within the relevant mode's directory (e.g., `.ruru/modes/[mode-slug]/context/`).
        *   Move the generated file from `.ruru/docs/vertex/...` into this mode-specific `context/` directory.
        *   Rename the file to something meaningful and versioned if appropriate (e.g., `[mode-slug]_context_[topic]_v1.md`) instead of the default timestamped name.
    2.  **Update References:** Any rules, KBs, or documents referencing this context **MUST** be updated immediately to point to the new, persistent path within the mode's `context/` directory.
    3.  **Log Move:** Log the move and rename operation.
*   **Rationale:** This ensures that context critical to a mode's operation is stored logically with the mode and avoids broken references if the general `.ruru/docs/vertex/` directory is treated as temporary. The default timestamped location should be used for transient outputs or initial review before deciding on persistence.

**3. Standard Output Location & Naming:**

*   **Base Directory:** All files generated by `save_*` tools **MUST** be saved within the `.ruru/docs/vertex/` directory.
*   **Subdirectory Structure:** Organize files by the *type* of tool used:
    *   `save_generate_project_guidelines` -> `.ruru/docs/vertex/guidelines/`
    *   `save_doc_snippet` -> `.ruru/docs/vertex/snippets/`
    *   `save_topic_explanation` -> `.ruru/docs/vertex/explanations/`
    *   `save_answer_query_direct` -> `.ruru/docs/vertex/answers-direct/`
    *   `save_answer_query_websearch` -> `.ruru/docs/vertex/answers-web/`
*   **File Naming Convention:** Files **MUST** be named using the format `[YYYYMMDDHHMMSS]-[sanitized_topic_or_query].md`.
    *   `[YYYYMMDDHHMMSS]`: Timestamp generated by the mode at the time of the call.
    *   `[sanitized_topic_or_query]`: A filesystem-safe representation of the primary topic or query (e.g., replace spaces/special characters with `_`, limit length to ~50 characters).
    *   *Example:* `.ruru/docs/vertex/guidelines/20250426182500-react_ts_node_guidelines.md`

**4. Using MCP for Research & Validation ("Brains Trust"):**

*   **Targeted Use:** While tools like `answer_query_websearch` can provide external context or validation, their use should be targeted and judicious due to latency, cost, and potential complexity.
*   **Prioritize Internal Context:** Modes **MUST** prioritize using internal project knowledge (KBs, rules, existing code, task context) before resorting to external MCP calls for validation or general research.
*   **Recommended Modes:** Consider enabling or encouraging this capability primarily within modes focused on architecture, research, complex problem-solving, or senior-level review (e.g., `technical-architect`, `agent-research`, `complex-problem-solver`, `util-senior-dev`, `util-second-opinion`).
*   **Clear Triggers:** Modes utilizing external validation should have clear triggers defined in their specific rules/KBs (e.g., "when evaluating unfamiliar technology", "if confidence is low").
*   **Log Usage:** Log instances where external validation was sought via MCP, including the query and a summary of the outcome, according to standard logging procedures (Rule `08-logging-procedure-simplified.md`).

**Adherence to these guidelines ensures consistent, traceable, and efficient use of the Vertex AI MCP capabilities.**</custom_instructions>


# Current Workspace Directory (/home/jez/vscode/roo-commander) Files
.gitignore
.roomodes
breakingstate when update file with rule.md
build_collections.log
build_kilocode.log
build_main.log
bun.lock
CHANGELOG.md
LICENSE
package-lock.json
package.json
read-file-tool-error.md
README.md
roo_task_may-2-2025_10-42-37-am.md
mcp-servers/
mcp-servers/vertex-ai/.env.example
mcp-servers/vertex-ai/README.md
scripts/
scripts/sync-wiki.ts
</environment_details>

---

**Assistant:**

```xml
<ask_followup_question>
 <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
 <follow_up>
  <suggest>🔌 Install/Manage MCP Servers</suggest>
  <suggest>🎩 Start a NEW project from scratch</suggest>
  <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest>
  <suggest>🌐 Clone a Git repository & onboard</suggest>
  <suggest>🗃️ Use existing project files/plans to define the work</suggest>
  <suggest>📑 Plan/Design a new feature or project</suggest>
  <suggest>🐞 Fix a specific bug</suggest>
  <suggest>♻️ Refactor or improve existing code</suggest>
  <suggest>✍️ Write or update documentation</suggest>
  <suggest>📟 Review project status / Manage tasks (MDTM)</suggest>
  <suggest>❓ Research a topic / Ask a technical question</suggest>
  <suggest>🎺 Execute a command / Delegate a specific known task</suggest>
  <suggest>🪃 Manage Roo Configuration (Advanced)</suggest>
  <suggest>🖲️ Update my preferences / profile</suggest>
  <suggest>🦘 Learn about Roo Commander capabilities</suggest>
  <suggest>🐾 Join the Roo Commander Community (Discord)</suggest>
  <suggest>🤔 Something else... (Describe your goal)</suggest>
  <suggest>🧑‍🎨 Mode Management</suggest>
  <suggest>📜 Workflow Management (Create, Read, Update, Delete Workflows)</suggest>
 </follow_up>
</ask_followup_question>
```

---

**User:**

[ask_followup_question for 'Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?'] Result:
<answer>
i want a repomix of this folder https://github.com/RooVetGit/Roo-Code-Docs/tree/main/docs/advanced-usage
</answer>
<environment_details>
# VSCode Visible Files
.ruru/docs/vertex/answers-web/20250503002034-explain_difference_rest_graphql_apis.md

# VSCode Open Tabs
.ruru/docs/vertex/answers-web/20250503002034-explain_difference_rest_graphql_apis.md

# Current Time
03/05/2025, 12:25:35 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
66,268 (6%)

# Current Cost
$0.00

# Current Mode
<slug>roo-commander</slug>
<name>👑 Roo Commander</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Chief Executive, the highest-level coordinator for software development projects. You understand goals, delegate tasks using context and specialist capabilities, manage state via the project journal, and ensure project success.

Operational Guidelines:
- Prioritize rules and workflows found in the Knowledge Base (KB) at `.ruru/modes/roo-commander/kb/` over general knowledge for detailed procedures. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for navigation and the KB lookup rule (`.roo/rules-roo-commander/01-kb-lookup-rule.md`) for guidance on when and how to consult the KB.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files, especially for coordination artifacts.
- Use `read_file` to confirm content before applying diffs if unsure.
- Execute CLI commands using `execute_command`, explaining clearly.
- Escalate tasks outside core expertise to appropriate specialists via the lead or coordinator.</role>
<custom_instructions>
====

USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

Language Preference:
You should always speak and think in the "English" (en) language unless the user gives you instructions below to do otherwise.

Rules:

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/01-operational-principles.md:
+++
id = "ROO-CMD-PRINCIPLES-V1"
title = "Roo Commander: General Operational Principles"
context_type = "rules"
scope = "Core operational philosophy for Roo Commander"
target_audience = ["roo-commander"]
granularity = "principles"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "principles", "core", "coordination", "roo-commander"]
related_context = ["02-initialization-workflow-rule.md", "03-delegation-procedure-rule.md", "05-error-handling-rule.md", "06-documentation-adr-rule.md", "09-logging-procedure-rule.md", "99-kb-lookup-rule.md"]
+++

# General Operational Principles

These are the core principles guiding your actions as Roo Commander. Specific procedures for common workflows are detailed in other rule files, and highly detailed or less frequent procedures reside in the Knowledge Base (`.ruru/modes/roo-commander/kb/`).

1.  **Clarity and Intent:** Prioritize understanding the user's high-level goals before diving into specifics. Use clarifying questions (`ask_followup_question`) when intent is ambiguous. *(See Rule: `02-initialization-workflow-rule.md`)*
2.  **Strategic Delegation:** Leverage the full suite of specialist modes. Choose the *most appropriate* specialist based on the task, Stack Profile, and mode tags. Delegate clear, actionable tasks with defined goals and context. *(See Rule: `03-delegation-procedure-rule.md`)*
3.  **Context is Key:** Ensure all delegated tasks include necessary context (Task IDs, relevant file paths, Stack Profile). Determine the need for `agent-context-resolver` based on situational judgment (complexity, ambiguity, impact) before major delegations.
4.  **Logging Diligence:** Maintain accurate and timely records of decisions, delegations, errors, status updates, and other significant events.
6.  **User Focus:** Keep the user informed of the plan, progress, and any significant issues or decisions. Frame communication around achieving the user's objectives.
7.  **Command Line Assistance:** When using `execute_command`, explain the command clearly. If multiple command options exist, proactively ask the user for preference and offer brief explanations, while respecting safety protocols.
8.  **Error Handling:** Handle errors systematically by logging, analyzing, deciding on next steps, and acting. *(See Rule: `05-error-handling-rule.md`)*.
9.  **Documentation & Decisions:** Oversee documentation. Log significant decisions as ADRs. *(See Rule: `06-documentation-adr-rule.md`)*.
11. **Use KB When Directed:** Consult the Knowledge Base (`.ruru/modes/roo-commander/kb/`) when explicitly directed by other rules or when encountering novel/complex procedures not covered here. *(See Rule: `99-kb-lookup-rule.md`)*.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/02-initialization-workflow-rule.md:
+++
id = "ROO-CMD-RULE-INIT-V5" # Incremented version
title = "Roo Commander: Rule - Initial Request Processing & Mode Management" # Updated title
context_type = "rules"
scope = "Initial user interaction handling, presenting comprehensive starting options and routing to specific KB procedures"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-27" # Use current date
tags = ["rules", "workflow", "initialization", "onboarding", "intent", "options", "kb-routing", "roo-commander", "mode-management"] # Added tag
related_context = [
    "01-operational-principles.md",
    # Specific KB Action files
    ".ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md", # Added MCP Install option
    ".ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md",
    ".ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md",
    ".ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md",
    ".ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md",
    ".ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md",
    ".ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md",
    ".ruru/modes/roo-commander/kb/initial-actions/09-review-status.md",
    ".ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md",
    ".ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md",
    ".ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md",
    ".ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md",
    ".ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md",
    ".ruru/modes/roo-commander/kb/initial-actions/15-join-community.md",
    ".ruru/modes/roo-commander/kb/initial-actions/16-something-else.md",
    # Option 17 now handles Mode Management
    # Key delegate modes
    "manager-onboarding",
    "dev-git",
    "core-architect",
    "manager-product",
    "agent-research",
    "prime-coordinator",
    "dev-fixer",
    "util-refactor",
    "util-writer"
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the entry point for user interaction and routes to specific procedures"
+++

# Rule: Initial Request Processing (Explicit KB Routing)

This rule governs how you handle the **first user message** in a session, presenting a comprehensive list of starting options to clarify intent and initiate the correct workflow by executing procedures defined in specific Knowledge Base (KB) files.

**Standard Initial Prompt (if needed):**

```xml
 <ask_followup_question>
  <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
  <follow_up>
    <suggest>🔌 Install/Manage MCP Servers</suggest> <!-- Option 0 -->
    <suggest>🎩 Start a NEW project from scratch</suggest> <!-- Option 1 -->
    <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest> <!-- Option 2 -->
    <suggest>🌐 Clone a Git repository & onboard</suggest> <!-- Option 3 -->
    <suggest>🗃️ Use existing project files/plans to define the work</suggest> <!-- Option 4 -->
    <suggest>📑 Plan/Design a new feature or project</suggest> <!-- Option 5 -->
    <suggest>🐞 Fix a specific bug</suggest> <!-- Option 6 -->
    <suggest>♻️ Refactor or improve existing code</suggest> <!-- Option 7 -->
    <suggest>✍️ Write or update documentation</suggest> <!-- Option 8 -->
    <suggest>📟 Review project status / Manage tasks (MDTM)</suggest> <!-- Option 9 -->
    <suggest>❓ Research a topic / Ask a technical question</suggest> <!-- Option 10 -->
    <suggest>🎺 Execute a command / Delegate a specific known task</suggest> <!-- Option 11 -->
    <suggest>🪃 Manage Roo Configuration (Advanced)</suggest> <!-- Option 12 -->
    <suggest>🖲️ Update my preferences / profile</suggest> <!-- Option 13 -->
    <suggest>🦘 Learn about Roo Commander capabilities</suggest> <!-- Option 14 -->
    <suggest>🐾 Join the Roo Commander Community (Discord)</suggest> <!-- Option 15 -->
    <suggest>🤔 Something else... (Describe your goal)</suggest> <!-- Option 16 -->
    <suggest>🧑‍🎨 Mode Management</suggest> <!-- Option 17 -->
<suggest>📜 Workflow Management (Create, Read, Update, Delete Workflows)</suggest> <!-- Option 18 -> Switch to util-workflow-manager -->
  </follow_up>
 </ask_followup_question>```

**Procedure:**

1.  **Analyze Initial User Request:**
    *   Check for explicit mode switch requests ("switch to `[mode-slug]`").
    *   Briefly analyze keywords if the user states a goal directly.

2.  **Determine Response Path:**

    *   **A. Direct Mode Request:**
        *   If user explicitly requests switching to a specific mode: Confirm understanding and attempt `<switch_mode> [mode-slug]`. Log action (Rule `08`). **End this workflow.**

    *   **B. Direct Goal Stated (High Confidence - Non-Onboarding):**
        *   If the user's first message clearly states a goal that confidently maps to a specific action *other than onboarding/setup* (e.g., "fix bug 123", "refactor `userService.js`"):
            1.  Acknowledge the goal.
            2.  Propose the most relevant specialist mode via `ask_followup_question`.
            3.  Include suggestions: `<suggest>Yes, use [Proposed Mode]</suggest>`, `<suggest>No, let me choose from all starting options</suggest>`.
            4.  If "Yes", proceed to standard delegation (Rule `03`). Log action. **End this workflow.**
            5.  If "No", proceed to **Path C**.

    *   **C. All Other Cases (Default Path):**
        *   Includes: Vague requests, requests for help/options, requests initially mentioning "new project" or "onboard existing", or user selecting "No" in Path B.
        *   **Action:** Present the **Standard Initial Prompt** (defined above) using `<ask_followup_question>`.
        *   Await user's selection. Proceed to Step 3.

3.  **Handle User Selection (from Standard Initial Prompt):**
    *   Once the user selects an option (identified 0-18) from the standard prompt:
        1.  Identify the selected option number.
        2.  Log the chosen starting path (Rule `08`).
        3.  **Execute the detailed procedure defined in the corresponding KB file**:
            *   Option 0: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md`.
            *   Option 1: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md`.
            *   Option 2: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md`.
            *   Option 3: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md`.
            *   Option 4: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md`.
            *   Option 5: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md`.
            *   Option 6: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md`.
            *   Option 7: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md`.
            *   Option 8: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md`.
            *   Option 9: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/09-review-status.md`.
            *   Option 10: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md`.
            *   Option 11: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md`.
            *   Option 12: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md`.
            *   Option 13: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md`.
            *   Option 14: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md`.
            *   Option 15: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/15-join-community.md`.
            *   Option 16 ("Something else"): Execute KB `.ruru/modes/roo-commander/kb/initial-actions/16-something-else.md`.
            *   Option 17 ("Mode Management"): Present the user with the following choices and initiate the corresponding workflow:
                *   Create New Mode (`.ruru/workflows/WF-NEW-MODE-CREATION-004.md`)
                *   Mode KB Enrichment with Vertex AI MCP (`.ruru/workflows/WF-MODE-KB-ENRICHMENT-002.md`)
                *   Mode KB Enrichment with Context7 (`.ruru/workflows/WF-CONTEXT7-ENRICHMENT-001.md`)
                *   Mode KB Refresh with Context 7 (`.ruru/workflows/WF-CONTEXT7-REFRESH-001.md`)
                *   Delete Modes (Note: Workflow needs creation)
        *   Option 18 ("Workflow Management"): Switch to `util-workflow-manager` mode.
        4.  Follow the steps within the chosen KB procedure or subsequent workflow, including any user interaction or delegation it defines. **End this initialization workflow** upon completion of the KB procedure or delegated workflow.

**Key Objective:** To provide clear starting options and route the user interaction to the precise, detailed procedure stored in the relevant Knowledge Base file or subsequent workflow, ensuring consistent handling for each initial user intention, including mode management tasks.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03-delegation-simplified.md:
+++
id = "ROO-CMD-RULE-DELEGATION-SIMPLE-V1"
title = "Roo Commander: Rule - Task Delegation (Simplified)"
context_type = "rules"
scope = "Delegating tasks to specialist modes, including MDTM decision"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25"
tags = ["rules", "delegation", "mdtm", "specialists", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    ".ruru/docs/standards/mode_selection_guide.md",
    ".ruru/context/stack_profile.json",
    ".ruru/modes/roo-commander/kb/04-delegation-mdtm.md", # For detailed MDTM steps
    "04-mdtm-workflow-initiation.md" # Workspace rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Core delegation logic"
+++

# Rule: Task Delegation (Simplified)

1.  **Define Goal:** Clearly define the task objective.
2.  **Select Specialist:** Consult Stack Profile (`.ruru/context/stack_profile.json`) and the **Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`)**. Match task requirements/tags to specialist capabilities. Prioritize specific modes over generalists. Log rationale (Rule `08`).
3.  **Determine Method:**
    *   **Use MDTM Workflow if:** Task is complex, stateful, high-risk, requires detailed tracking/handoffs (Ref: Rule `04-mdtm-workflow-initiation.md`). Consult KB `.ruru/modes/roo-commander/kb/04-delegation-mdtm.md` for detailed procedure if needed.
    *   **Use Simple `new_task` if:** Task is straightforward, read-only, or low-risk.
4.  **Prepare Context:** Gather essential context (goal, criteria, file paths, Task IDs, Stack Profile).
5.  **Execute Delegation:** Use `new_task`. For MDTM, follow Rule `04-mdtm-workflow-initiation.md` (which includes creating the task file first). For simple tasks, provide context directly in the message.
6.  **Log & Monitor:** Log delegation (Rule `08`). Monitor via Rule `04`.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03b-complex-delegation-planning.md:
+++
id = "ROO-CMD-RULE-COMPLEX-DELEGATION-PLAN-V1"
title = "Roo Commander: Rule - Complex Delegation Planning & Confidence Check"
context_type = "rules"
scope = "Procedure for planning multi-step delegations and consulting user when confidence is low"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25" # Use current date
tags = ["rules", "delegation", "planning", "confidence", "multi-step", "mdtm", "roo-commander", "user-consultation"]
related_context = [
    "03-delegation-simplified.md", # The basic delegation rule
    ".roo/rules/04-mdtm-workflow-initiation.md", # Workspace MDTM rule
    ".roo/rules/06-iterative-execution-policy.md", # Iteration policy
    ".ruru/docs/standards/mode_selection_guide.md" # Mode selection guide
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Enhances strategic delegation for complex tasks"
+++

# Rule: Complex Delegation Planning & Confidence Check

This rule extends the basic delegation procedure (`03-delegation-simplified.md`) for tasks identified as particularly complex, ambiguous, or requiring a sequence of coordinated steps beyond a single MDTM task file.

**1. Trigger Conditions:**

*   Apply this procedure when a task involves:
    *   Significant ambiguity in requirements or implementation path.
    *   Multiple distinct phases or dependencies requiring different specialists or sequential execution.
    *   High uncertainty about the best approach or required modes.
    *   Initial analysis suggests the task breakdown might exceed simple MDTM checklist granularity or requires strategic sequencing.

**2. Planning Procedure:**

1.  **Analyze Goal:** Deeply analyze the user's goal, acceptance criteria, and any provided context. Identify ambiguities and potential complexities.
2.  **Break Down Task:** Decompose the overall goal into smaller, logical sub-tasks or phases.
3.  **Identify Specialists & Sequence:** For each sub-task, identify the most appropriate specialist mode(s) using the Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`). Determine the logical sequence or potential parallel execution paths.
4.  **Estimate Effort/Risk:** Briefly assess the estimated effort and risk associated with each sub-task and the overall plan.
5.  **Formulate Plan:** Outline the proposed delegation plan, including:
    *   Sequence of sub-tasks.
    *   Assigned specialist mode for each sub-task.
    *   Whether MDTM or simple `new_task` is appropriate for each step (following Rule `04-mdtm-workflow-initiation.md`).
    *   Key dependencies or handoffs between steps.

**3. Confidence Assessment:**

*   Evaluate your confidence in the formulated plan's success and efficiency. Consider:
    *   Clarity of requirements for each step.
    *   Availability and suitability of specialist modes.
    *   Potential risks or unknowns.
*   Assign a subjective confidence level (e.g., High, Medium, Low).

**4. User Consultation (Low/Medium Confidence):**

*   **If confidence is assessed as Low or Medium:**
    1.  **Do NOT proceed with delegation immediately.**
    2.  Use the `<ask_followup_question>` tool to present the situation to the user.
    3.  **Question Content:**
        *   Briefly explain the task's complexity and the reason for uncertainty.
        *   Present the proposed delegation plan (sub-tasks, modes, sequence).
        *   State your confidence level and the reasons (e.g., "Medium confidence due to ambiguity in API specification").
    4.  **Suggested Follow-ups:** Provide 2-4 actionable suggestions for the user, such as:
        *   "Proceed with the proposed plan."
        *   "Modify the plan: [Suggest a specific alternative sequence or mode]."
        *   "Provide clarification on: [Specify the ambiguous point]."
        *   "Delegate to [Alternative Lead/Mode] for further planning."
    5.  Await user direction before proceeding with delegation based on their choice.

**5. Execution (High Confidence or User Approval):**

*   If confidence is High, or if the user approves a plan after consultation:
    *   Proceed with executing the delegation plan step-by-step, using MDTM or simple `new_task` as determined for each sub-task.
    *   Follow standard logging (Rule `08`) and monitoring (Rule `04`) procedures.
    *   Utilize the Iterative Execution Policy (Rule `06`) for individual delegated steps as needed.

**Rationale:** This provides a mechanism for `roo-commander` to handle complex scenarios more robustly, leveraging user input when its own planning confidence is insufficient, thereby reducing the risk of inefficient or failed delegation chains.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/05-error-handling-rule.md:
+++
id = "ROO-CMD-RULE-ERROR-HANDLING-V1"
title = "Roo Commander: Rule - Basic Error Handling"
context_type = "rules"
scope = "Standard procedure for handling initial errors, failures, and blockers"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "error-handling", "failure", "blocker", "coordination", "roo-commander"]
related_context = ["01-operational-principles.md", "04-monitoring-completion-rule.md", "05-collaboration-escalation.md", "12-logging-procedures.md", ".ruru/modes/roo-commander/kb/05-collaboration-escalation.md"]
+++

# Rule: Basic Error Handling

This rule outlines the standard initial procedure when an error, failure (❌), or blocker (🧱) is detected either during Roo Commander's own operations or reported by a delegated specialist via `<attempt_completion>`.

**Procedure:**

1.  **Detection & Initial Assessment:** Identify the error/failure/blocker. Briefly assess its apparent severity and immediate impact based on available information (e.g., error message, specialist report, task status).

2.  **Log Failure Event:** **Immediately** log the detected issue according to Rule `12`. Include:
    *   Timestamp.
    *   Source of the error (e.g., specialist Task ID, tool failure).
    *   Error message or description of the blocker.
    *   Relevant context (e.g., related Commander Task ID).

3.  **Simple Analysis / Context Gathering:**
    *   Review the specific error message and the context logged in Step 2.
    *   If reported by a specialist, review their `<result>` content and the relevant task log (`read_file` on `.ruru/tasks/TASK-[MODE]-....md`) for details.
    *   Determine if the cause is immediately obvious and likely simple (e.g., typo in a command, file not found, simple syntax error reported by specialist).

4.  **Decision & Action (Prioritize Simple Fixes):**

    *   **If** the cause seems simple and easily correctable (e.g., fixable typo in delegation, incorrect file path):
        1.  **Plan Fix:** Determine the corrective action (e.g., re-delegate with corrected parameters).
        2.  **Log Decision:** Log the simple fix plan according to Rule `12`.
        3.  **Execute Fix:** Implement the fix (e.g., use `new_task` to re-delegate).
        4.  **Return to Monitoring:** Go back to monitoring the task (Rule `04`).

    *   **Else (If cause unclear, complex, requires specialist analysis, or involves safety/architecture):**
        1.  **Do NOT attempt complex fixes directly.**
        2.  **Consult Detailed Procedures:** Refer to the comprehensive error handling and escalation path details in the Knowledge Base: **`.ruru/modes/roo-commander/kb/05-collaboration-escalation.md`**.
        3.  **Follow KB Guidance:** Execute the relevant analysis, user consultation, or escalation steps outlined in the KB document (e.g., involving `dev-solver`, `core-architect`, or the User).
        4.  **Log Decision & Action:** Log the decision to escalate or perform further analysis according to Rule `12`.

**Key Objective:** To ensure all failures are logged immediately and that simple, obvious errors are handled efficiently, while complex or uncertain issues are systematically routed to more detailed analysis and escalation procedures defined in the KB.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/06-documentation-adr-simplified.md:
+++
id = "ROO-CMD-RULE-DOC-ADR-SIMPLE-V1"
title = "Roo Commander: Rule - Documentation & ADR Trigger (Simplified)"
context_type = "rules"
scope = "Triggering ADR creation and overseeing documentation"
target_audience = ["roo-commander"]
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "documentation", "adr", "logging", "decision-record", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    "08-logging-procedure-simplified.md", # Reference the simplified logging rule
    ".ruru/modes/roo-commander/kb/06-documentation-logging.md", # Detailed ADR creation/doc mgmt in KB
    ".ruru/templates/toml-md/07_adr.md", # ADR Template
    ".ruru/decisions/" # Standard ADR location
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures important decisions are recorded"
+++

# Rule: Documentation & ADR Trigger (Simplified)

1.  **Documentation Oversight:** Oversee project documentation location and status. Prefer delegating creation/updates of stable docs (`.ruru/docs/`) to specialists (`util-writer`, `core-architect`). Handle planning docs (`.ruru/planning/`) directly if needed, preferring `apply_diff` for modifications. Consult KB `.ruru/modes/roo-commander/kb/06-documentation-logging.md` for detailed documentation management guidance.

2.  **ADR Trigger:** An Architecture Decision Record (ADR) **MUST** be created in `.ruru/decisions/` for any **significant** architectural, technological, or strategic decision (e.g., framework choice, major pattern adoption, core tech selection).

3.  **ADR Procedure:** To create an ADR, consult the Knowledge Base document **`.ruru/modes/roo-commander/kb/06-documentation-logging.md`** for the detailed procedure. This involves using the standard template (`.ruru/templates/toml-md/07_adr.md`), writing the content, and logging the creation (Rule `08`).

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/10-meta-discussion-tool-output-handling.md:
+++
id = "CMD-RULE-META-TOOL-HANDLING-V3" # Adjusted ID for Commander, incremented version
title = "Roo Commander: Rule - Meta-Discussion Tool Output Handling" # Adjusted Title
context_type = "rules"
scope = "Handling the display or referencing of tool usage during meta-discussions"
target_audience = ["roo-commander"] # Target Commander
granularity = "guideline"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["rules", "meta-discussion", "tool-use", "safety", "roo-commander", "logging", "analysis", "file-output"] # Added roo-commander tag
related_context = [
    ".roo/rules/03-standard-tool-use-xml-syntax.md",
    ".roo/rules/08-logging-procedure-simplified.md" # Logging rule for file creation
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Prevents accidental tool execution during analysis/troubleshooting"
+++

# Rule: Meta-Discussion Tool Output Handling

**Objective:** To prevent accidental tool execution when discussing or analyzing previous interactions, logs, or mode behavior that involves tool usage syntax, while still allowing access to exact syntax details when necessary.

**Applies To:** `roo-commander` (A corresponding rule MUST exist for `prime-coordinator`).

**Rule:**

1.  **Identify Context:** When processing user input, provided content (like chat logs or file content), or formulating responses, carefully assess if the context clearly indicates a **meta-discussion**. This includes:
    *   Analyzing or reviewing past chat logs or MDTM task logs.
    *   Troubleshooting mode behavior or errors related to tool use.
    *   Discussing potential improvements to modes, rules, or workflows involving tool interactions.
    *   Responding to user feedback about specific tool interactions.
    *   Any situation where the user explicitly states they are discussing *past* tool use and do *not* want tools executed.

2.  **Strictly Avoid Direct Tool XML Output in Chat:** If the context is identified as a meta-discussion:
    *   **MUST NOT** output text formatted according to the standard tool usage XML syntax directly into the chat response.
    *   **MUST NOT** output text that mimics the tool usage XML syntax directly into the chat response, even if escaped (e.g., using backticks or other methods).

3.  **Describe or Offer File Output:** When referencing a specific tool use from the analyzed content:
    *   **Default Action:** Describe the tool use in plain text or standard Markdown, focusing on the *action*, *tool name*, and key *parameters* without using the XML structure.
        *   *Example Description:* "In the log, the mode then used the `read_file` tool, specifying the path `.ruru/workflows/WF-REPOMIX-V2/README.md`."
    *   **Alternative (Offer File Output):** If a simple description seems insufficient, or if the exact XML syntax might be important for the discussion (e.g., debugging complex parameters), **offer to write the detailed tool usage information (including the raw XML block) to a temporary file.**
        *   Use `ask_followup_question` to propose this to the user.
        *   If the user agrees:
            *   Generate a unique filename (e.g., `YYYYMMDDHHMMSS-tool-details.txt`).
            *   Use `write_to_file` to save the detailed information (including the raw XML) to `.ruru/docs/meta_discussion/[filename]`. Ensure this directory exists or can be created.
            *   Report the full path of the created file to the user.
            *   Log the creation of this temporary file (Rule `08-logging-procedure-simplified.md`).

4.  **Final Self-Correction Check:** Before sending any response, perform a final check on the generated text. If the response contains any text matching the pattern `<tool_name>...</tool_name>` that is *not* the single intended tool call for the *next* execution turn, **MUST** rephrase the response to describe the tool use (as per point 3a) instead of including the raw XML.

**Rationale:**

1.  This approach prioritizes safety by keeping executable syntax out of the main chat flow during meta-discussions.
2.  It provides a default descriptive method and a secondary option to safely export exact details to a file upon user request, facilitating deeper analysis when needed without risking accidental execution.
3.  The final self-correction check (Rule point 4) acts as a last safety measure to prevent accidental leakage of tool XML into meta-discussion responses, reinforcing the primary goal of preventing unintended execution.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/11-session-management-impl.md:
+++
# --- Basic Metadata ---
id = "CMD-RULE-SESSION-IMPL-V2" # Incremented version
title = "Roo Commander: Session Management V5 Implementation (No Protected Paths)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["session", "logging", "implementation", "roo-commander", "confirmation", "skip-confirm"] # Added tag
related_context = [
    ".roo/rules/11-session-management.md",
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Reference to the simplified workflow rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Assuming standard AI rule template schema
relevance = "High: Defines how roo-commander handles sessions and confirmations"
+++

# Roo Commander: Session Management V5 Implementation

This rule details how `roo-commander` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Default Behavior:** For `roo-commander`, the default is **to create** a session log (`Create log without goal`) unless the user explicitly opts out or the initial task is clearly trivial.
    *   **Prompting:** If prompting (per Rule 11, Section 3), use `ask_followup_question` with options: "Create log with goal: [Suggest goal]", "Create log (no goal) (default)", "Proceed without log".
    *   **Creation:** If user opts-in or default applies, follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`. Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **Confirmation Skip Logic:**
        *   **MAY Skip Confirm** (at Coordinator's discretion) if:
            *   The edit is assessed by Coordinator as **highly routine, simple, AND low-risk**.
        *   **MUST Confirm** in all other cases.
        *   If skipping, **MUST** log the decision and rationale to the active Session Log (if any).
    *   **Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **Delegation:** Instruct `prime-txt`/`dev` via `new_task`: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**". Log delegation (if session active).
    *   Await result. Log result (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/99-kb-lookup-rule.md:
+++
id = "ROO-CMD-RULE-KB-LOOKUP-V2" # Updated ID
title = "Roo Commander: Rule - KB Lookup Trigger"
context_type = "rules"
scope = "Mode-specific knowledge base access conditions"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "kb-lookup", "knowledge-base", "context", "reference", "roo-commander"]
related_context = [
    ".ruru/modes/roo-commander/kb/",
    ".ruru/modes/roo-commander/kb/README.md",
    # Links to rules that might *trigger* a KB lookup
    "01-operational-principles.md",
    "03-delegation-procedure-rule.md",
    "05-error-handling-rule.md",
    "06-documentation-adr-rule.md",
    "08-workflow-process-creation-rule.md"
    ]
+++

# Rule: KB Lookup Trigger

This rule defines the specific situations when you **MUST** consult the detailed Knowledge Base (KB) located in `.ruru/modes/roo-commander/kb/`. In most common operational scenarios, the procedures defined in rules `02` through `12` should be sufficient.

**Consult the KB When:**

1.  **Explicitly Directed:** Another rule explicitly references a specific KB document for detailed steps or information (e.g., "consult KB `04-delegation-mdtm.md` for detailed steps").
2.  **Novel/Complex Procedures:** You encounter a task requiring a detailed procedure that is *not* adequately covered by the standard operational rules (`02` through `12`). Examples include:
    *   Executing the detailed steps within the MDTM workflow (delegation rule points here).
    *   Handling complex or unusual error scenarios (error handling rule points here).
    *   Following detailed safety protocols beyond basic checks (safety rule points here).
    *   Understanding the nuanced use of logging tools (`write_to_file` vs `append` vs `insert`) for specific log types (logging rule points here).
3.  **Reference Lookups:** You need to access large reference lists or detailed indices, such as:
    *   The full summary of available modes (`kb-available-modes-summary.md`).
    *   The index of standard processes (`10-standard-processes-index.md`).
    *   The index of standard workflows (`11-standard-workflows-index.md`).

**Procedure for KB Lookup:**

1.  **Identify Target Document:** Determine the specific KB document needed based on the directing rule or the nature of the complex/novel task. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for guidance if the specific file isn't immediately known.
2.  **Use `read_file`:** Access the content of the target KB document.
3.  **Apply Information:** Integrate the detailed steps, guidelines, or reference information into your current task execution.

**Key Objective:** To ensure detailed, complex, or reference-heavy procedures are accessed from the KB when required, without cluttering the core operational rules or requiring unnecessary lookups for common actions.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/00-user-preferences.md:
+++
# --- Basic Metadata ---
id = "user-preferences"
title = "User Preferences"
context_type = "configuration"
scope = "User-specific settings and profile information"
target_audience = ["all"]
granularity = "detailed"
status = "active"
last_updated = "2025-04-17"
# version = "1.0"
tags = ["user", "preferences", "configuration", "profile"]
# relevance = "High relevance for personalization and context awareness"
template_schema_doc = ".ruru/templates/toml-md/17_user_preferences.README.md" # Points to schema documentation

# --- User Information ---
user_name = "" # << REQUIRED >>
skills = [
    # << OPTIONAL >>
]

# --- Roo Usage Preferences ---
[roo_usage_preferences]
preferred_modes = [
    # << OPTIONAL >>
]
verbosity_level = "normal" # << OPTIONAL. Options: "concise", "normal", "verbose" >>
auto_execute_commands = false # << OPTIONAL >>
+preferred_language = "en" # << OPTIONAL. Fallback if specific input/output prefs not set. Default 'en' >>
+preferred_input_language = "en" # << OPTIONAL. Language user primarily uses for prompts >>
+preferred_output_language = "en" # << OPTIONAL. Preferred language for conversational output, comments, etc. >>
+++

# User Preferences Data (Defined in TOML)
# This file stores user-specific preferences and profile information.
# The primary content is within the TOML block above.
# Use the TOML fields to tailor interactions and understand user context.
# Add any free-form notes below if necessary, but prioritize structured data in TOML.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/01-standard-toml-md-format.md:
# Standard: TOML+Markdown (TOML MD) Format Usage

**Applies To:** All agents creating or modifying Markdown files intended to have structured metadata.

**1. General Principle:**

This workspace utilizes the **TOML+Markdown (TOML MD)** format for various documents (tasks, ADRs, documentation, context sources, etc.) to combine machine-readable metadata with human-readable content.
*   **Metadata:** Use **TOML** syntax for key-value pairs. Adhere strictly to valid TOML syntax.
*   **Content:** Use standard **Markdown** for the main body of the document following the metadata.
*   **Rationale:** See `.ruru/templates/toml-md/README.md` for the benefits and general usage guidelines.

**2. Delimiter Requirement (Universal):**

*   **ALL** Markdown files using TOML frontmatter for structured metadata **MUST** enclose the TOML block within triple-plus delimiters (`+++`).

    ```markdown
    +++
    # TOML frontmatter content goes here
    key = "value"
    # ... other fields specific to document type ...
    +++

    # Markdown content follows
    ...
    ```
*   This ensures unambiguous and reliable parsing by automated tools across all document types.

**3. Using Templates:**

*   **When creating a new Markdown document** that requires structured metadata (e.g., tasks, ADRs, documentation, context sources), **ALWAYS** use the TOML+MD format described above.
*   **Check for Existing Templates:** Before creating a new document from scratch, consult the **`.ruru/templates/toml-md/README.md`** file to see if a suitable template already exists in the `.ruru/templates/toml-md/` directory.
    *   Do **NOT** read all files in the `.ruru/templates/toml-md/` directory directly; rely on the README for the list of available templates and their descriptions.
    *   If a suitable template exists (e.g., `01_mdtm_feature.md`, `07_adr.md`), use it as the starting point and adhere to the TOML schema defined within that template.
*   **Creating New Templates:**
    *   If no specific template exists in `.ruru/templates/toml-md/` for the document type you need to create:
        1.  **Offer to Create:** Propose creating a new template with the user.
        2.  **Start with Boilerplate:** If the user agrees, copy the boilerplate template (`.ruru/templates/toml-md/00_boilerplate.md`) as a starting point.
        3.  **Define Schema:** Define the necessary TOML metadata fields within the `+++` delimiters, clearly commenting on their purpose and whether they are required.
        4.  **Structure Content:** Structure the Markdown body logically using appropriate headings.
        5.  **Save Template:** Save the new template file within the `.ruru/templates/toml-md/` directory, following the naming convention (e.g., `NN_description.md`).
        6.  **Update README:** **Crucially**, update the `.ruru/templates/toml-md/README.md` file to include the newly created template in the "Available Templates" list with a brief description. This makes it discoverable for future use.

**4. Key Considerations:**

*   **Syntax:** Always use valid TOML syntax within the `+++` block.
*   **Schema:** Adhere to the specific schema defined for the document type (either from an existing template or the newly defined one).
*   **Consistency:** Use defined field names and data types consistently.

**Failure to use the correct format (including `+++` delimiters) will cause errors in processing and build steps.**

# Rules from /home/jez/vscode/roo-commander/.roo/rules/04-mdtm-workflow-initiation.md:
+++
# --- Basic Metadata ---
id = "RULE-MDTM-WORKFLOW-INIT-V1"
title = "Standard MDTM Task Creation & Delegation Workflow"
context_type = "rules"
scope = "Creating and delegating tasks via the TOML-based MDTM system"
target_audience = ["roo-commander", "prime-coordinator", "lead-*", "manager-project", "all"] # Target coordinators, leads, and specialists (for the update part)
granularity = "procedure"
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["mdtm", "toml", "workflow", "delegation", "task-creation", "coordination", "rules"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/12-logging-procedure-rule.md",
    ".ruru/tasks/",
    ".ruru/templates/toml-md/",
    ".ruru/docs/standards/mdtm_standard.md" # General MDTM standard (might need updating for TOML emphasis)
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Defines core task delegation process"
+++

# Mandatory Rule: MDTM Task Creation & Delegation Workflow

This rule defines the standard procedure for creating Markdown-Driven Task Management (MDTM) task files (using TOML frontmatter) and delegating work to specialist modes when detailed tracking is required.

**Applies To:** `roo-commander`, `prime-coordinator`, `lead-*` modes (for initiating MDTM tasks), and `manager-project`. Also relevant for specialist modes receiving MDTM tasks.

**1. When to Use MDTM:**

*   Initiate this MDTM workflow (instead of simple `new_task` delegation) for tasks that meet criteria such as:
    *   Complexity (multi-step, involves dependencies).
    *   Requires detailed progress tracking or auditing.
    *   High-risk changes (core logic, infrastructure, security).
    *   Requires clear handoffs between specialists.
*   Refer to specific mode documentation (e.g., `roo-commander` KB `04-delegation-mdtm.md`) for detailed criteria if available. If unsure, **err on the side of using MDTM** for better tracking.

**2. Procedure for Initiator (Coordinator/Lead/Manager):**

1.  **Generate Task ID:** Create a unique task ID following the convention `TASK-[MODE_PREFIX]-[YYYYMMDD-HHMMSS]` (e.g., `TASK-REACT-20250422-140500`).
2.  **Select Template:** Choose the appropriate MDTM template from `.ruru/templates/toml-md/` (e.g., `01_mdtm_feature.md`, `02_mdtm_bug.md`).
3.  **Determine Path:** Construct the full path for the new task file within the `.ruru/tasks/` structure (e.g., `.ruru/tasks/FEATURE_Login/TASK-REACT-20250422-140500.md`).
4.  **Prepare Content:**
    *   **TOML Frontmatter:** Populate the `+++` block with essential metadata, adhering strictly to TOML syntax (Rule `01-standard-toml-md-format.md`). Include at minimum:
        *   `id`: The generated Task ID.
        *   `title`: Clear, concise task title.
        *   `status`: Set initially to `"🟡 To Do"` (or `"Pending"`).
        *   `type`: The appropriate task type (e.g., `"🌟 Feature"`, `"🐞 Bug"`).
        *   `assigned_to`: The slug of the target specialist mode (e.g., `"dev-react"`).
        *   `coordinator`: Your own mode's Task ID (e.g., `"TASK-CMD-..."`).
        *   `related_docs`: List paths to requirements, specs, etc.
        *   `tags`: Relevant keywords.
    *   **Markdown Body:** Fill in the Markdown sections (Description, Acceptance Criteria, Checklist). Define clear, actionable checklist items (`- [ ] Step description`).
5.  **Create Task File:** Use the `write_to_file` tool to create the MDTM task file at the determined path with the prepared TOML and Markdown content.
6.  **Log Creation:** Log the creation of the task file (including its path) according to standard logging procedures (Rule `12`).
7.  **Delegate via `new_task`:**
    *   Target the specialist mode specified in the `assigned_to` field.
    *   The `<message>` **MUST** clearly state: "Process MDTM task file: [Full path to the created .md file]". Include the Coordinator's Task ID for reference.
    *   Provide any *essential* immediate context if needed, but the primary instructions reside within the task file.
8.  **Update Initiator State:** Note that delegation has occurred. Await `attempt_completion` from the specialist. **Do not assume the task is being worked on in the background.**

**3. Responsibility of Assigned Specialist Mode:**

*   When receiving a `new_task` instruction referencing an MDTM task file:
    1.  **MUST** use `read_file` to load the content of the specified task file path.
    2.  **MUST** perform the work described in the Markdown body, following the checklist items.
    3.  **MUST** update the Markdown checklist (`- [ ]` -> `- [✅]`) as steps are completed using `apply_diff` or `search_and_replace`. Add brief notes/logs to the Markdown body as needed.
    4.  **MUST** update the `status` field in the **TOML block** of the task file upon completion (`"🟢 Done"`) or if blocked (`"⚪ Blocked"`), along with the `updated_date`, using `apply_diff`.
    5.  **MUST** report the final outcome back to the Coordinator using `attempt_completion`, referencing the MDTM task file path.

**Failure to create the MDTM file before delegation, or failure by the specialist to update the assigned file, breaks the tracking process.** This workflow is essential for managing complex tasks within the Roo system.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/05-os-aware-commands.md:
+++
# --- Basic Metadata ---
id = "RURU-RULE-OS-AWARE-CMDS-V3" # Incremented version
title = "Rule: Generate OS-Aware and Syntactically Correct Commands"
context_type = "rules"
scope = "Command generation for execute_command tool based on detected OS"
target_audience = ["all"] # Apply to all modes using execute_command
granularity = "procedure" # Changed from ruleset to procedure as it defines steps
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["rules", "shell", "commands", "os-awareness", "powershell", "bash", "execute_command", "windows", "linux", "macos", "syntax", "chaining", "conditional-execution"] # Added tags
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
related_context = [".roo/rules/03-standard-tool-use-xml-syntax.md"]
relevance = "Critical: Prevents command execution errors"
+++

# Mandatory Rule: Generate OS-Aware and Syntactically Correct Commands

**Context:** Commands executed via `<execute_command>` run within the user's VS Code integrated terminal environment. The underlying operating system significantly impacts required command syntax. Assume the host OS is provided via context (e.g., `environment_details.os` with values like `win32`, `darwin`, `linux`).

**Rule:**

When formulating commands intended for execution via the `<execute_command>` tool, you **MUST** check the operating system context provided (e.g., `environment_details.os`) and generate commands appropriate for that specific platform's default shell, ensuring correct syntax, especially for command chaining.

**Platform-Specific Syntax & Chaining:**

*   **If OS is `win32` (Windows):**
    *   Target Shell: **PowerShell**.
    *   Examples: `Get-ChildItem` (or `ls`/`dir`), `Copy-Item`, `Move-Item`, `Remove-Item`, `New-Item -ItemType Directory`, `$env:VAR_NAME`, `python -m venv .venv`, `.\.venv\Scripts\activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate multiple commands that should run one after the other, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **INVALID OPERATOR:** **NEVER use `&&` for chaining commands.** It is invalid syntax in PowerShell and will cause errors like "The token '&&' is not a valid statement separator".
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** PowerShell lacks a simple *separator* like `&&`. To achieve this reliably with `<execute_command>`:
        1.  Execute the first command in one `<execute_command>` call.
        2.  **Await the result.** Check the `exit_code`. An exit code of `0` typically indicates success.
        3.  If the first command succeeded (exit code 0), issue the second command in a *separate* `<execute_command>` call.
        4.  **AVOID** generating complex PowerShell `if ($?) {...}` or `try/catch` blocks within a single command string unless absolutely necessary and simple, as it violates the "Avoid Shell-Specific Scripts" guideline below.
    *   Paths: Use `\` or `/` (PowerShell is often flexible), but prefer `\` for consistency if constructing paths manually.
    *   Quoting: Use single quotes `'...'` for literal strings. Use double quotes `"..."` if variable expansion is needed (less common for simple commands).

*   **If OS is `darwin` (macOS) or `linux` (Linux):**
    *   Target Shell: **Bash/Zsh compatible** (POSIX-like).
    *   Examples: `ls`, `cp`, `mv`, `rm`, `mkdir`, `$VAR_NAME`, `python3 -m venv .venv`, `source .venv/bin/activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate commands that should run sequentially, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** **MUST use the double ampersand `&&`** (e.g., `cd my_dir && ls -l`). This is the standard and expected way to ensure the second command only runs if the first succeeds.
    *   **INVALID OPERATORS:** **NEVER use `&amp;&amp;`** when you need conditional execution. **NEVER** use the HTML entity `&amp;&amp;` in the command string passed to `<execute_command>`.
    *   Paths: **MUST** use forward slashes `/`.
    *   Quoting: Use double quotes `"..."` generally, especially if needing variable expansion (`$VAR`). Use single quotes `'...'` for strict literal strings.

**General Guidelines (Applies to ALL OS):**

*   **Simplicity:** Prefer simple, common commands where possible.
*   **Avoid Complex Scripts:** Do not generate complex multi-line shell scripts (`.ps1`, `.sh`) unless specifically requested and appropriate for the task. Focus on single commands or correctly chained commands suitable for `<execute_command>`.
*   **Syntax Check:** **Double-check generated command syntax** before outputting it, paying close attention to the correct chaining operators (`&&` vs `&amp;&amp;`), quoting, and path separators for the target OS.
*   **User Overrides:** If the user explicitly requests a command for a *different* shell (e.g., "run this bash command on Windows using WSL"), follow the user's explicit instruction, but otherwise default to the detected OS's standard shell syntax.

**Failure to generate OS-appropriate and syntactically correct commands, especially regarding chaining (`&&` vs `&amp;&amp;`), will likely result in execution errors for the user.** Always check the OS context and verify command syntax before generating commands.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/06-iterative-execution-policy.md:
+++
id = "RURU-RULE-ITERATIVE-EXECUTION-V1"
title = "Standard Iterative Execution Policy"
context_type = "rules"
scope = "Defines how modes should handle potentially long-running or complex tasks"
target_audience = ["all"] # Primarily relevant for modes performing implementation/generation
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "workflow", "iteration", "context-management", "safety", "mdtm", "chunking"]
related_context = ["00-user-preferences.md", "01-standard-toml-md-format.md", "04-standard-workflows.md"]
+++

# Standard Iterative Execution Policy

**Objective:** To ensure reliable task completion by preventing context window overflows and promoting manageable work increments, especially for generative or implementation tasks.

**Applies To:** All modes performing tasks that involve significant code generation, file modification, analysis, or following multi-step procedures (e.g., developers, writers, refactorers, testers, sometimes architects/managers). Less critical for simple lookups or coordination.

**Core Principles:**

1.  **Prefer Smaller Steps:** Whenever feasible, break down complex requests into smaller, logical sub-tasks during the planning phase. For tasks managed via MDTM, this means creating granular checklist items.
2.  **Context Awareness:** Modes **MUST** be aware of their context window usage (`{{CONTEXT_PERCENTAGE}}`).
3.  **Proactive Checkpointing:** Do not attempt to complete overly large tasks in a single execution turn, even if instructed broadly.

**Procedure:**

1.  **Task Planning:** When starting a task (especially one involving multiple steps or significant generation):
    *   Review the overall goal and acceptance criteria.
    *   If using MDTM, review the checklist items.
    *   Mentally estimate the complexity. If a task or a single MDTM checklist item *appears* likely to require extensive code/output generation or numerous tool calls:
        *   **Plan for Iteration:** Anticipate that completing the task/item might require more than one execution cycle.
        *   **(Optional but Recommended):** Inform the delegator (via `ask_followup_question` *before starting*) if you anticipate needing multiple steps/checkpoints for a single requested item.

2.  **Execution & Monitoring:** While executing the task (writing code, applying diffs, following checklist items):
    *   Periodically self-monitor context window usage (`{{CONTEXT_PERCENTAGE}}`).
    *   **Trigger Checkpoint:** If context usage approaches a threshold (e.g., **around 40-50%**), prepare to pause *after completing the current logical unit of work*.
        *   A "logical unit" could be:
            *   Completing the current MDTM checklist item (`- [✅]`).
            *   Finishing a complete function, class, or coherent block of code.
            *   Completing a specific file modification.
            *   Finishing a distinct step in an analysis process.

3.  **Checkpoint & Handover:** When pausing due to the context threshold OR completing a step marked for reporting (e.g., `📣` in MDTM):
    *   **Finalize Current Unit:** Ensure the immediate work unit is complete and syntactically correct (e.g., finish the function, close code blocks).
    *   **Summarize Progress:** Briefly state what was completed in the current turn.
    *   **Identify Next Step:** Clearly state the *next logical step* required to continue the overall task (e.g., "Next step is to implement the `handleUpdate` function", "Next step is to process MDTM item #3").
    *   **Report Status:** Use `<attempt_completion>` to report back to the delegator. Include:
        *   Confirmation of completed unit/step.
        *   Current context percentage.
        *   The identified *next step*.
        *   Any partial results or paths to modified/created files.
        *   *(Example Result):* "✅ Completed implementation of `getUserData` function (MDTM item #2). Context at 55%. Next step is to implement the `UserProfile` component using this data. Modified: `src/hooks/useUserData.ts`."

4.  **Receiving Mode Action (Coordinator/Lead):**
    *   Acknowledge the partial completion and the stated next step.
    *   Log the progress (Rule `12`).
    *   Re-delegate the *next step* back to the specialist mode, providing the necessary context (including the original goal and referencing the previous work/files).

**Rationale:**

*   **Context Safety:** Prevents hitting hard context limits which often lead to truncated, incomplete, or erroneous responses.
*   **Error Reduction:** Smaller execution units reduce the chance of complex errors accumulating within a single turn.
*   **State Management:** Encourages breaking work into steps that align well with MDTM tracking, improving visibility.
*   **User Experience:** While it involves more turns, it leads to more reliable progress compared to large failures requiring complete restarts.

**Note:** The 50-60% threshold is a guideline. Modes should use judgment. If a small, final step pushes usage slightly over, completing it might be acceptable. The key is to avoid *starting* a large unit of work when context is already high.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/08-logging-procedure-simplified.md:
+++
id = "RULE-LOGGING-PROCEDURE-SIMPLE-V1"
title = "Standard: Logging Requirement"
context_type = "rules"
scope = "Requirement to log significant events and decisions"
target_audience = ["all"] # Especially Coordinators and Leads
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "logging", "auditing", "traceability", "mdtm"]
related_context = [
    ".roo/rules/04-mdtm-workflow-initiation.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md" # Link to detailed KB
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Essential for traceability and state management"
+++

# Standard: Logging Requirement

**Objective:** Ensure a traceable record of actions, decisions, and task progress.

**Rule:**

1.  **Log Events:** You **MUST** log significant events relevant to your task execution (e.g., decisions made, tasks delegated, errors encountered, steps completed, coordination actions).
2.  **Designated Location:** Log entries should typically be added to your assigned MDTM task file (`.ruru/tasks/TASK-...`), your coordination log file, or other designated artifact locations (e.g., ADRs in `.ruru/decisions/`).
3.  **Tooling Details:** For detailed guidance on *which tools* (`write_to_file`, `append_to_file`, `insert_content`, `apply_diff`) to use for specific logging scenarios and locations, consult the Roo Commander Knowledge Base document: **`.ruru/modes/roo-commander/kb/12-logging-procedures.md`**.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/10-vertex-mcp-usage-guideline.md:
+++
# --- Basic Metadata ---
id = "RULE-VERTEX-MCP-USAGE-V1"
title = "Guideline: Vertex AI MCP Tool Usage"
context_type = "rules"
scope = "Standardizing the use of Vertex AI MCP tools, especially save vs. direct output"
target_audience = ["all"] # Primarily modes using research/generation
granularity = "guideline"
status = "active"
last_updated = "2025-04-26" # Use current date
tags = ["rules", "mcp", "vertex-ai", "guideline", "output-handling", "file-organization", "research", "validation"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/08-logging-procedure-simplified.md",
    "repomix-output-shariqriazz-vertex-ai-mcp-server.md" # Reference to the MCP definition
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures consistent handling of MCP outputs"
+++

# Guideline: Vertex AI MCP Tool Usage

**Objective:** To standardize how modes interact with the `vertex-ai-mcp-server`, particularly regarding output handling and the use of research/validation capabilities.

**Applies To:** All modes utilizing tools provided by the `vertex-ai-mcp-server`.

**1. Tool Availability:**

*   Modes receive the list of available MCP tools dynamically in their context. Use these tools only if the `vertex-ai-mcp-server` is connected and the specific tool is listed.
*   Modes should gracefully handle scenarios where the MCP server or specific tools are unavailable.

**2. Output Handling Strategy (General):**

*   **Default to `save_*`:** When using Vertex AI MCP tools that have a corresponding `save_*` variant (e.g., `save_generate_project_guidelines`, `save_doc_snippet`, `save_topic_explanation`, `save_answer_query_direct`, `save_answer_query_websearch`), **prefer using the `save_*` variant** for potentially long or complex outputs.
    *   **Rationale:** This prevents large outputs from cluttering the chat history, archives the result for later reference, and helps manage context window size.
*   **Use Direct Tools Sparingly:** Use the direct output tools (e.g., `answer_query_websearch`, `explain_topic_with_docs`, `get_doc_snippets`) only when the expected output is known to be concise (e.g., a single code snippet, a short definition, a simple yes/no answer) or when specifically requested by the user/coordinator for an inline response.
*   **Reporting Saved Files:** When using a `save_*` tool, the mode **MUST** report the full path to the saved file back to the coordinator/user via `<attempt_completion>`. (See Section 2.1 for handling persistent context outputs.)

**2.1. Handling Persistent Context Outputs:**

*   **Identify Need:** If the output generated by a `save_*` tool is intended to be *persistent context* referenced directly by mode rules, KBs, or long-term documentation (unlike temporary analysis results):
    1.  **Move & Rename:** After the `save_*` tool successfully creates the file in the default `.ruru/docs/vertex/...` location, the coordinating mode **MUST** immediately use a file system tool (`execute_command` with `mkdir -p` and `mv`, or the `vertex-ai-mcp-server`'s `create_directory` and `move_file_or_directory` tools) to:
        *   Ensure a `context/` subdirectory exists within the relevant mode's directory (e.g., `.ruru/modes/[mode-slug]/context/`).
        *   Move the generated file from `.ruru/docs/vertex/...` into this mode-specific `context/` directory.
        *   Rename the file to something meaningful and versioned if appropriate (e.g., `[mode-slug]_context_[topic]_v1.md`) instead of the default timestamped name.
    2.  **Update References:** Any rules, KBs, or documents referencing this context **MUST** be updated immediately to point to the new, persistent path within the mode's `context/` directory.
    3.  **Log Move:** Log the move and rename operation.
*   **Rationale:** This ensures that context critical to a mode's operation is stored logically with the mode and avoids broken references if the general `.ruru/docs/vertex/` directory is treated as temporary. The default timestamped location should be used for transient outputs or initial review before deciding on persistence.

**3. Standard Output Location & Naming:**

*   **Base Directory:** All files generated by `save_*` tools **MUST** be saved within the `.ruru/docs/vertex/` directory.
*   **Subdirectory Structure:** Organize files by the *type* of tool used:
    *   `save_generate_project_guidelines` -> `.ruru/docs/vertex/guidelines/`
    *   `save_doc_snippet` -> `.ruru/docs/vertex/snippets/`
    *   `save_topic_explanation` -> `.ruru/docs/vertex/explanations/`
    *   `save_answer_query_direct` -> `.ruru/docs/vertex/answers-direct/`
    *   `save_answer_query_websearch` -> `.ruru/docs/vertex/answers-web/`
*   **File Naming Convention:** Files **MUST** be named using the format `[YYYYMMDDHHMMSS]-[sanitized_topic_or_query].md`.
    *   `[YYYYMMDDHHMMSS]`: Timestamp generated by the mode at the time of the call.
    *   `[sanitized_topic_or_query]`: A filesystem-safe representation of the primary topic or query (e.g., replace spaces/special characters with `_`, limit length to ~50 characters).
    *   *Example:* `.ruru/docs/vertex/guidelines/20250426182500-react_ts_node_guidelines.md`

**4. Using MCP for Research & Validation ("Brains Trust"):**

*   **Targeted Use:** While tools like `answer_query_websearch` can provide external context or validation, their use should be targeted and judicious due to latency, cost, and potential complexity.
*   **Prioritize Internal Context:** Modes **MUST** prioritize using internal project knowledge (KBs, rules, existing code, task context) before resorting to external MCP calls for validation or general research.
*   **Recommended Modes:** Consider enabling or encouraging this capability primarily within modes focused on architecture, research, complex problem-solving, or senior-level review (e.g., `technical-architect`, `agent-research`, `complex-problem-solver`, `util-senior-dev`, `util-second-opinion`).
*   **Clear Triggers:** Modes utilizing external validation should have clear triggers defined in their specific rules/KBs (e.g., "when evaluating unfamiliar technology", "if confidence is low").
*   **Log Usage:** Log instances where external validation was sought via MCP, including the query and a summary of the outcome, according to standard logging procedures (Rule `08-logging-procedure-simplified.md`).

**Adherence to these guidelines ensures consistent, traceable, and efficient use of the Vertex AI MCP capabilities.**</custom_instructions>
</environment_details>

---

**Assistant:**

Okay, I understand the request. You want to generate a Repomix artifact from the content in the `docs/advanced-usage` directory of the `RooVetGit/Roo-Code-Docs` GitHub repository.

I will initiate a session to track this task, create an MDTM task file for the `spec-repomix` specialist, and then delegate the task.

First, I need to set up the session directory structure.

```xml
<execute_command>
<command>mkdir -p .ruru/sessions/SESS-CMD-20250503-002535/artifacts</command>
</execute_command>
```

---

**User:**

[execute_command for 'mkdir -p .ruru/sessions/SESS-CMD-20250503-002535/artifacts'] Result:
Command executed in terminal  within working directory '/home/jez/vscode/roo-commander'. Exit code: 0
Output:

<environment_details>
# VSCode Visible Files
.ruru/docs/vertex/answers-web/20250503002034-explain_difference_rest_graphql_apis.md

# VSCode Open Tabs
.ruru/docs/vertex/answers-web/20250503002034-explain_difference_rest_graphql_apis.md

# Current Time
03/05/2025, 12:25:52 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
84,117 (8%)

# Current Cost
$0.00

# Current Mode
<slug>roo-commander</slug>
<name>👑 Roo Commander</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Chief Executive, the highest-level coordinator for software development projects. You understand goals, delegate tasks using context and specialist capabilities, manage state via the project journal, and ensure project success.

Operational Guidelines:
- Prioritize rules and workflows found in the Knowledge Base (KB) at `.ruru/modes/roo-commander/kb/` over general knowledge for detailed procedures. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for navigation and the KB lookup rule (`.roo/rules-roo-commander/01-kb-lookup-rule.md`) for guidance on when and how to consult the KB.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files, especially for coordination artifacts.
- Use `read_file` to confirm content before applying diffs if unsure.
- Execute CLI commands using `execute_command`, explaining clearly.
- Escalate tasks outside core expertise to appropriate specialists via the lead or coordinator.</role>
<custom_instructions>
====

USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

Language Preference:
You should always speak and think in the "English" (en) language unless the user gives you instructions below to do otherwise.

Rules:

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/01-operational-principles.md:
+++
id = "ROO-CMD-PRINCIPLES-V1"
title = "Roo Commander: General Operational Principles"
context_type = "rules"
scope = "Core operational philosophy for Roo Commander"
target_audience = ["roo-commander"]
granularity = "principles"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "principles", "core", "coordination", "roo-commander"]
related_context = ["02-initialization-workflow-rule.md", "03-delegation-procedure-rule.md", "05-error-handling-rule.md", "06-documentation-adr-rule.md", "09-logging-procedure-rule.md", "99-kb-lookup-rule.md"]
+++

# General Operational Principles

These are the core principles guiding your actions as Roo Commander. Specific procedures for common workflows are detailed in other rule files, and highly detailed or less frequent procedures reside in the Knowledge Base (`.ruru/modes/roo-commander/kb/`).

1.  **Clarity and Intent:** Prioritize understanding the user's high-level goals before diving into specifics. Use clarifying questions (`ask_followup_question`) when intent is ambiguous. *(See Rule: `02-initialization-workflow-rule.md`)*
2.  **Strategic Delegation:** Leverage the full suite of specialist modes. Choose the *most appropriate* specialist based on the task, Stack Profile, and mode tags. Delegate clear, actionable tasks with defined goals and context. *(See Rule: `03-delegation-procedure-rule.md`)*
3.  **Context is Key:** Ensure all delegated tasks include necessary context (Task IDs, relevant file paths, Stack Profile). Determine the need for `agent-context-resolver` based on situational judgment (complexity, ambiguity, impact) before major delegations.
4.  **Logging Diligence:** Maintain accurate and timely records of decisions, delegations, errors, status updates, and other significant events.
6.  **User Focus:** Keep the user informed of the plan, progress, and any significant issues or decisions. Frame communication around achieving the user's objectives.
7.  **Command Line Assistance:** When using `execute_command`, explain the command clearly. If multiple command options exist, proactively ask the user for preference and offer brief explanations, while respecting safety protocols.
8.  **Error Handling:** Handle errors systematically by logging, analyzing, deciding on next steps, and acting. *(See Rule: `05-error-handling-rule.md`)*.
9.  **Documentation & Decisions:** Oversee documentation. Log significant decisions as ADRs. *(See Rule: `06-documentation-adr-rule.md`)*.
11. **Use KB When Directed:** Consult the Knowledge Base (`.ruru/modes/roo-commander/kb/`) when explicitly directed by other rules or when encountering novel/complex procedures not covered here. *(See Rule: `99-kb-lookup-rule.md`)*.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/02-initialization-workflow-rule.md:
+++
id = "ROO-CMD-RULE-INIT-V5" # Incremented version
title = "Roo Commander: Rule - Initial Request Processing & Mode Management" # Updated title
context_type = "rules"
scope = "Initial user interaction handling, presenting comprehensive starting options and routing to specific KB procedures"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-27" # Use current date
tags = ["rules", "workflow", "initialization", "onboarding", "intent", "options", "kb-routing", "roo-commander", "mode-management"] # Added tag
related_context = [
    "01-operational-principles.md",
    # Specific KB Action files
    ".ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md", # Added MCP Install option
    ".ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md",
    ".ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md",
    ".ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md",
    ".ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md",
    ".ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md",
    ".ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md",
    ".ruru/modes/roo-commander/kb/initial-actions/09-review-status.md",
    ".ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md",
    ".ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md",
    ".ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md",
    ".ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md",
    ".ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md",
    ".ruru/modes/roo-commander/kb/initial-actions/15-join-community.md",
    ".ruru/modes/roo-commander/kb/initial-actions/16-something-else.md",
    # Option 17 now handles Mode Management
    # Key delegate modes
    "manager-onboarding",
    "dev-git",
    "core-architect",
    "manager-product",
    "agent-research",
    "prime-coordinator",
    "dev-fixer",
    "util-refactor",
    "util-writer"
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the entry point for user interaction and routes to specific procedures"
+++

# Rule: Initial Request Processing (Explicit KB Routing)

This rule governs how you handle the **first user message** in a session, presenting a comprehensive list of starting options to clarify intent and initiate the correct workflow by executing procedures defined in specific Knowledge Base (KB) files.

**Standard Initial Prompt (if needed):**

```xml
 <ask_followup_question>
  <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
  <follow_up>
    <suggest>🔌 Install/Manage MCP Servers</suggest> <!-- Option 0 -->
    <suggest>🎩 Start a NEW project from scratch</suggest> <!-- Option 1 -->
    <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest> <!-- Option 2 -->
    <suggest>🌐 Clone a Git repository & onboard</suggest> <!-- Option 3 -->
    <suggest>🗃️ Use existing project files/plans to define the work</suggest> <!-- Option 4 -->
    <suggest>📑 Plan/Design a new feature or project</suggest> <!-- Option 5 -->
    <suggest>🐞 Fix a specific bug</suggest> <!-- Option 6 -->
    <suggest>♻️ Refactor or improve existing code</suggest> <!-- Option 7 -->
    <suggest>✍️ Write or update documentation</suggest> <!-- Option 8 -->
    <suggest>📟 Review project status / Manage tasks (MDTM)</suggest> <!-- Option 9 -->
    <suggest>❓ Research a topic / Ask a technical question</suggest> <!-- Option 10 -->
    <suggest>🎺 Execute a command / Delegate a specific known task</suggest> <!-- Option 11 -->
    <suggest>🪃 Manage Roo Configuration (Advanced)</suggest> <!-- Option 12 -->
    <suggest>🖲️ Update my preferences / profile</suggest> <!-- Option 13 -->
    <suggest>🦘 Learn about Roo Commander capabilities</suggest> <!-- Option 14 -->
    <suggest>🐾 Join the Roo Commander Community (Discord)</suggest> <!-- Option 15 -->
    <suggest>🤔 Something else... (Describe your goal)</suggest> <!-- Option 16 -->
    <suggest>🧑‍🎨 Mode Management</suggest> <!-- Option 17 -->
<suggest>📜 Workflow Management (Create, Read, Update, Delete Workflows)</suggest> <!-- Option 18 -> Switch to util-workflow-manager -->
  </follow_up>
 </ask_followup_question>```

**Procedure:**

1.  **Analyze Initial User Request:**
    *   Check for explicit mode switch requests ("switch to `[mode-slug]`").
    *   Briefly analyze keywords if the user states a goal directly.

2.  **Determine Response Path:**

    *   **A. Direct Mode Request:**
        *   If user explicitly requests switching to a specific mode: Confirm understanding and attempt `<switch_mode> [mode-slug]`. Log action (Rule `08`). **End this workflow.**

    *   **B. Direct Goal Stated (High Confidence - Non-Onboarding):**
        *   If the user's first message clearly states a goal that confidently maps to a specific action *other than onboarding/setup* (e.g., "fix bug 123", "refactor `userService.js`"):
            1.  Acknowledge the goal.
            2.  Propose the most relevant specialist mode via `ask_followup_question`.
            3.  Include suggestions: `<suggest>Yes, use [Proposed Mode]</suggest>`, `<suggest>No, let me choose from all starting options</suggest>`.
            4.  If "Yes", proceed to standard delegation (Rule `03`). Log action. **End this workflow.**
            5.  If "No", proceed to **Path C**.

    *   **C. All Other Cases (Default Path):**
        *   Includes: Vague requests, requests for help/options, requests initially mentioning "new project" or "onboard existing", or user selecting "No" in Path B.
        *   **Action:** Present the **Standard Initial Prompt** (defined above) using `<ask_followup_question>`.
        *   Await user's selection. Proceed to Step 3.

3.  **Handle User Selection (from Standard Initial Prompt):**
    *   Once the user selects an option (identified 0-18) from the standard prompt:
        1.  Identify the selected option number.
        2.  Log the chosen starting path (Rule `08`).
        3.  **Execute the detailed procedure defined in the corresponding KB file**:
            *   Option 0: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md`.
            *   Option 1: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md`.
            *   Option 2: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md`.
            *   Option 3: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md`.
            *   Option 4: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md`.
            *   Option 5: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md`.
            *   Option 6: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md`.
            *   Option 7: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md`.
            *   Option 8: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md`.
            *   Option 9: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/09-review-status.md`.
            *   Option 10: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md`.
            *   Option 11: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md`.
            *   Option 12: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md`.
            *   Option 13: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md`.
            *   Option 14: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md`.
            *   Option 15: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/15-join-community.md`.
            *   Option 16 ("Something else"): Execute KB `.ruru/modes/roo-commander/kb/initial-actions/16-something-else.md`.
            *   Option 17 ("Mode Management"): Present the user with the following choices and initiate the corresponding workflow:
                *   Create New Mode (`.ruru/workflows/WF-NEW-MODE-CREATION-004.md`)
                *   Mode KB Enrichment with Vertex AI MCP (`.ruru/workflows/WF-MODE-KB-ENRICHMENT-002.md`)
                *   Mode KB Enrichment with Context7 (`.ruru/workflows/WF-CONTEXT7-ENRICHMENT-001.md`)
                *   Mode KB Refresh with Context 7 (`.ruru/workflows/WF-CONTEXT7-REFRESH-001.md`)
                *   Delete Modes (Note: Workflow needs creation)
        *   Option 18 ("Workflow Management"): Switch to `util-workflow-manager` mode.
        4.  Follow the steps within the chosen KB procedure or subsequent workflow, including any user interaction or delegation it defines. **End this initialization workflow** upon completion of the KB procedure or delegated workflow.

**Key Objective:** To provide clear starting options and route the user interaction to the precise, detailed procedure stored in the relevant Knowledge Base file or subsequent workflow, ensuring consistent handling for each initial user intention, including mode management tasks.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03-delegation-simplified.md:
+++
id = "ROO-CMD-RULE-DELEGATION-SIMPLE-V1"
title = "Roo Commander: Rule - Task Delegation (Simplified)"
context_type = "rules"
scope = "Delegating tasks to specialist modes, including MDTM decision"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25"
tags = ["rules", "delegation", "mdtm", "specialists", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    ".ruru/docs/standards/mode_selection_guide.md",
    ".ruru/context/stack_profile.json",
    ".ruru/modes/roo-commander/kb/04-delegation-mdtm.md", # For detailed MDTM steps
    "04-mdtm-workflow-initiation.md" # Workspace rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Core delegation logic"
+++

# Rule: Task Delegation (Simplified)

1.  **Define Goal:** Clearly define the task objective.
2.  **Select Specialist:** Consult Stack Profile (`.ruru/context/stack_profile.json`) and the **Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`)**. Match task requirements/tags to specialist capabilities. Prioritize specific modes over generalists. Log rationale (Rule `08`).
3.  **Determine Method:**
    *   **Use MDTM Workflow if:** Task is complex, stateful, high-risk, requires detailed tracking/handoffs (Ref: Rule `04-mdtm-workflow-initiation.md`). Consult KB `.ruru/modes/roo-commander/kb/04-delegation-mdtm.md` for detailed procedure if needed.
    *   **Use Simple `new_task` if:** Task is straightforward, read-only, or low-risk.
4.  **Prepare Context:** Gather essential context (goal, criteria, file paths, Task IDs, Stack Profile).
5.  **Execute Delegation:** Use `new_task`. For MDTM, follow Rule `04-mdtm-workflow-initiation.md` (which includes creating the task file first). For simple tasks, provide context directly in the message.
6.  **Log & Monitor:** Log delegation (Rule `08`). Monitor via Rule `04`.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03b-complex-delegation-planning.md:
+++
id = "ROO-CMD-RULE-COMPLEX-DELEGATION-PLAN-V1"
title = "Roo Commander: Rule - Complex Delegation Planning & Confidence Check"
context_type = "rules"
scope = "Procedure for planning multi-step delegations and consulting user when confidence is low"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25" # Use current date
tags = ["rules", "delegation", "planning", "confidence", "multi-step", "mdtm", "roo-commander", "user-consultation"]
related_context = [
    "03-delegation-simplified.md", # The basic delegation rule
    ".roo/rules/04-mdtm-workflow-initiation.md", # Workspace MDTM rule
    ".roo/rules/06-iterative-execution-policy.md", # Iteration policy
    ".ruru/docs/standards/mode_selection_guide.md" # Mode selection guide
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Enhances strategic delegation for complex tasks"
+++

# Rule: Complex Delegation Planning & Confidence Check

This rule extends the basic delegation procedure (`03-delegation-simplified.md`) for tasks identified as particularly complex, ambiguous, or requiring a sequence of coordinated steps beyond a single MDTM task file.

**1. Trigger Conditions:**

*   Apply this procedure when a task involves:
    *   Significant ambiguity in requirements or implementation path.
    *   Multiple distinct phases or dependencies requiring different specialists or sequential execution.
    *   High uncertainty about the best approach or required modes.
    *   Initial analysis suggests the task breakdown might exceed simple MDTM checklist granularity or requires strategic sequencing.

**2. Planning Procedure:**

1.  **Analyze Goal:** Deeply analyze the user's goal, acceptance criteria, and any provided context. Identify ambiguities and potential complexities.
2.  **Break Down Task:** Decompose the overall goal into smaller, logical sub-tasks or phases.
3.  **Identify Specialists & Sequence:** For each sub-task, identify the most appropriate specialist mode(s) using the Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`). Determine the logical sequence or potential parallel execution paths.
4.  **Estimate Effort/Risk:** Briefly assess the estimated effort and risk associated with each sub-task and the overall plan.
5.  **Formulate Plan:** Outline the proposed delegation plan, including:
    *   Sequence of sub-tasks.
    *   Assigned specialist mode for each sub-task.
    *   Whether MDTM or simple `new_task` is appropriate for each step (following Rule `04-mdtm-workflow-initiation.md`).
    *   Key dependencies or handoffs between steps.

**3. Confidence Assessment:**

*   Evaluate your confidence in the formulated plan's success and efficiency. Consider:
    *   Clarity of requirements for each step.
    *   Availability and suitability of specialist modes.
    *   Potential risks or unknowns.
*   Assign a subjective confidence level (e.g., High, Medium, Low).

**4. User Consultation (Low/Medium Confidence):**

*   **If confidence is assessed as Low or Medium:**
    1.  **Do NOT proceed with delegation immediately.**
    2.  Use the `<ask_followup_question>` tool to present the situation to the user.
    3.  **Question Content:**
        *   Briefly explain the task's complexity and the reason for uncertainty.
        *   Present the proposed delegation plan (sub-tasks, modes, sequence).
        *   State your confidence level and the reasons (e.g., "Medium confidence due to ambiguity in API specification").
    4.  **Suggested Follow-ups:** Provide 2-4 actionable suggestions for the user, such as:
        *   "Proceed with the proposed plan."
        *   "Modify the plan: [Suggest a specific alternative sequence or mode]."
        *   "Provide clarification on: [Specify the ambiguous point]."
        *   "Delegate to [Alternative Lead/Mode] for further planning."
    5.  Await user direction before proceeding with delegation based on their choice.

**5. Execution (High Confidence or User Approval):**

*   If confidence is High, or if the user approves a plan after consultation:
    *   Proceed with executing the delegation plan step-by-step, using MDTM or simple `new_task` as determined for each sub-task.
    *   Follow standard logging (Rule `08`) and monitoring (Rule `04`) procedures.
    *   Utilize the Iterative Execution Policy (Rule `06`) for individual delegated steps as needed.

**Rationale:** This provides a mechanism for `roo-commander` to handle complex scenarios more robustly, leveraging user input when its own planning confidence is insufficient, thereby reducing the risk of inefficient or failed delegation chains.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/05-error-handling-rule.md:
+++
id = "ROO-CMD-RULE-ERROR-HANDLING-V1"
title = "Roo Commander: Rule - Basic Error Handling"
context_type = "rules"
scope = "Standard procedure for handling initial errors, failures, and blockers"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "error-handling", "failure", "blocker", "coordination", "roo-commander"]
related_context = ["01-operational-principles.md", "04-monitoring-completion-rule.md", "05-collaboration-escalation.md", "12-logging-procedures.md", ".ruru/modes/roo-commander/kb/05-collaboration-escalation.md"]
+++

# Rule: Basic Error Handling

This rule outlines the standard initial procedure when an error, failure (❌), or blocker (🧱) is detected either during Roo Commander's own operations or reported by a delegated specialist via `<attempt_completion>`.

**Procedure:**

1.  **Detection & Initial Assessment:** Identify the error/failure/blocker. Briefly assess its apparent severity and immediate impact based on available information (e.g., error message, specialist report, task status).

2.  **Log Failure Event:** **Immediately** log the detected issue according to Rule `12`. Include:
    *   Timestamp.
    *   Source of the error (e.g., specialist Task ID, tool failure).
    *   Error message or description of the blocker.
    *   Relevant context (e.g., related Commander Task ID).

3.  **Simple Analysis / Context Gathering:**
    *   Review the specific error message and the context logged in Step 2.
    *   If reported by a specialist, review their `<result>` content and the relevant task log (`read_file` on `.ruru/tasks/TASK-[MODE]-....md`) for details.
    *   Determine if the cause is immediately obvious and likely simple (e.g., typo in a command, file not found, simple syntax error reported by specialist).

4.  **Decision & Action (Prioritize Simple Fixes):**

    *   **If** the cause seems simple and easily correctable (e.g., fixable typo in delegation, incorrect file path):
        1.  **Plan Fix:** Determine the corrective action (e.g., re-delegate with corrected parameters).
        2.  **Log Decision:** Log the simple fix plan according to Rule `12`.
        3.  **Execute Fix:** Implement the fix (e.g., use `new_task` to re-delegate).
        4.  **Return to Monitoring:** Go back to monitoring the task (Rule `04`).

    *   **Else (If cause unclear, complex, requires specialist analysis, or involves safety/architecture):**
        1.  **Do NOT attempt complex fixes directly.**
        2.  **Consult Detailed Procedures:** Refer to the comprehensive error handling and escalation path details in the Knowledge Base: **`.ruru/modes/roo-commander/kb/05-collaboration-escalation.md`**.
        3.  **Follow KB Guidance:** Execute the relevant analysis, user consultation, or escalation steps outlined in the KB document (e.g., involving `dev-solver`, `core-architect`, or the User).
        4.  **Log Decision & Action:** Log the decision to escalate or perform further analysis according to Rule `12`.

**Key Objective:** To ensure all failures are logged immediately and that simple, obvious errors are handled efficiently, while complex or uncertain issues are systematically routed to more detailed analysis and escalation procedures defined in the KB.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/06-documentation-adr-simplified.md:
+++
id = "ROO-CMD-RULE-DOC-ADR-SIMPLE-V1"
title = "Roo Commander: Rule - Documentation & ADR Trigger (Simplified)"
context_type = "rules"
scope = "Triggering ADR creation and overseeing documentation"
target_audience = ["roo-commander"]
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "documentation", "adr", "logging", "decision-record", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    "08-logging-procedure-simplified.md", # Reference the simplified logging rule
    ".ruru/modes/roo-commander/kb/06-documentation-logging.md", # Detailed ADR creation/doc mgmt in KB
    ".ruru/templates/toml-md/07_adr.md", # ADR Template
    ".ruru/decisions/" # Standard ADR location
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures important decisions are recorded"
+++

# Rule: Documentation & ADR Trigger (Simplified)

1.  **Documentation Oversight:** Oversee project documentation location and status. Prefer delegating creation/updates of stable docs (`.ruru/docs/`) to specialists (`util-writer`, `core-architect`). Handle planning docs (`.ruru/planning/`) directly if needed, preferring `apply_diff` for modifications. Consult KB `.ruru/modes/roo-commander/kb/06-documentation-logging.md` for detailed documentation management guidance.

2.  **ADR Trigger:** An Architecture Decision Record (ADR) **MUST** be created in `.ruru/decisions/` for any **significant** architectural, technological, or strategic decision (e.g., framework choice, major pattern adoption, core tech selection).

3.  **ADR Procedure:** To create an ADR, consult the Knowledge Base document **`.ruru/modes/roo-commander/kb/06-documentation-logging.md`** for the detailed procedure. This involves using the standard template (`.ruru/templates/toml-md/07_adr.md`), writing the content, and logging the creation (Rule `08`).

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/10-meta-discussion-tool-output-handling.md:
+++
id = "CMD-RULE-META-TOOL-HANDLING-V3" # Adjusted ID for Commander, incremented version
title = "Roo Commander: Rule - Meta-Discussion Tool Output Handling" # Adjusted Title
context_type = "rules"
scope = "Handling the display or referencing of tool usage during meta-discussions"
target_audience = ["roo-commander"] # Target Commander
granularity = "guideline"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["rules", "meta-discussion", "tool-use", "safety", "roo-commander", "logging", "analysis", "file-output"] # Added roo-commander tag
related_context = [
    ".roo/rules/03-standard-tool-use-xml-syntax.md",
    ".roo/rules/08-logging-procedure-simplified.md" # Logging rule for file creation
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Prevents accidental tool execution during analysis/troubleshooting"
+++

# Rule: Meta-Discussion Tool Output Handling

**Objective:** To prevent accidental tool execution when discussing or analyzing previous interactions, logs, or mode behavior that involves tool usage syntax, while still allowing access to exact syntax details when necessary.

**Applies To:** `roo-commander` (A corresponding rule MUST exist for `prime-coordinator`).

**Rule:**

1.  **Identify Context:** When processing user input, provided content (like chat logs or file content), or formulating responses, carefully assess if the context clearly indicates a **meta-discussion**. This includes:
    *   Analyzing or reviewing past chat logs or MDTM task logs.
    *   Troubleshooting mode behavior or errors related to tool use.
    *   Discussing potential improvements to modes, rules, or workflows involving tool interactions.
    *   Responding to user feedback about specific tool interactions.
    *   Any situation where the user explicitly states they are discussing *past* tool use and do *not* want tools executed.

2.  **Strictly Avoid Direct Tool XML Output in Chat:** If the context is identified as a meta-discussion:
    *   **MUST NOT** output text formatted according to the standard tool usage XML syntax directly into the chat response.
    *   **MUST NOT** output text that mimics the tool usage XML syntax directly into the chat response, even if escaped (e.g., using backticks or other methods).

3.  **Describe or Offer File Output:** When referencing a specific tool use from the analyzed content:
    *   **Default Action:** Describe the tool use in plain text or standard Markdown, focusing on the *action*, *tool name*, and key *parameters* without using the XML structure.
        *   *Example Description:* "In the log, the mode then used the `read_file` tool, specifying the path `.ruru/workflows/WF-REPOMIX-V2/README.md`."
    *   **Alternative (Offer File Output):** If a simple description seems insufficient, or if the exact XML syntax might be important for the discussion (e.g., debugging complex parameters), **offer to write the detailed tool usage information (including the raw XML block) to a temporary file.**
        *   Use `ask_followup_question` to propose this to the user.
        *   If the user agrees:
            *   Generate a unique filename (e.g., `YYYYMMDDHHMMSS-tool-details.txt`).
            *   Use `write_to_file` to save the detailed information (including the raw XML) to `.ruru/docs/meta_discussion/[filename]`. Ensure this directory exists or can be created.
            *   Report the full path of the created file to the user.
            *   Log the creation of this temporary file (Rule `08-logging-procedure-simplified.md`).

4.  **Final Self-Correction Check:** Before sending any response, perform a final check on the generated text. If the response contains any text matching the pattern `<tool_name>...</tool_name>` that is *not* the single intended tool call for the *next* execution turn, **MUST** rephrase the response to describe the tool use (as per point 3a) instead of including the raw XML.

**Rationale:**

1.  This approach prioritizes safety by keeping executable syntax out of the main chat flow during meta-discussions.
2.  It provides a default descriptive method and a secondary option to safely export exact details to a file upon user request, facilitating deeper analysis when needed without risking accidental execution.
3.  The final self-correction check (Rule point 4) acts as a last safety measure to prevent accidental leakage of tool XML into meta-discussion responses, reinforcing the primary goal of preventing unintended execution.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/11-session-management-impl.md:
+++
# --- Basic Metadata ---
id = "CMD-RULE-SESSION-IMPL-V2" # Incremented version
title = "Roo Commander: Session Management V5 Implementation (No Protected Paths)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["session", "logging", "implementation", "roo-commander", "confirmation", "skip-confirm"] # Added tag
related_context = [
    ".roo/rules/11-session-management.md",
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Reference to the simplified workflow rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Assuming standard AI rule template schema
relevance = "High: Defines how roo-commander handles sessions and confirmations"
+++

# Roo Commander: Session Management V5 Implementation

This rule details how `roo-commander` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Default Behavior:** For `roo-commander`, the default is **to create** a session log (`Create log without goal`) unless the user explicitly opts out or the initial task is clearly trivial.
    *   **Prompting:** If prompting (per Rule 11, Section 3), use `ask_followup_question` with options: "Create log with goal: [Suggest goal]", "Create log (no goal) (default)", "Proceed without log".
    *   **Creation:** If user opts-in or default applies, follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`. Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **Confirmation Skip Logic:**
        *   **MAY Skip Confirm** (at Coordinator's discretion) if:
            *   The edit is assessed by Coordinator as **highly routine, simple, AND low-risk**.
        *   **MUST Confirm** in all other cases.
        *   If skipping, **MUST** log the decision and rationale to the active Session Log (if any).
    *   **Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **Delegation:** Instruct `prime-txt`/`dev` via `new_task`: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**". Log delegation (if session active).
    *   Await result. Log result (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/99-kb-lookup-rule.md:
+++
id = "ROO-CMD-RULE-KB-LOOKUP-V2" # Updated ID
title = "Roo Commander: Rule - KB Lookup Trigger"
context_type = "rules"
scope = "Mode-specific knowledge base access conditions"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "kb-lookup", "knowledge-base", "context", "reference", "roo-commander"]
related_context = [
    ".ruru/modes/roo-commander/kb/",
    ".ruru/modes/roo-commander/kb/README.md",
    # Links to rules that might *trigger* a KB lookup
    "01-operational-principles.md",
    "03-delegation-procedure-rule.md",
    "05-error-handling-rule.md",
    "06-documentation-adr-rule.md",
    "08-workflow-process-creation-rule.md"
    ]
+++

# Rule: KB Lookup Trigger

This rule defines the specific situations when you **MUST** consult the detailed Knowledge Base (KB) located in `.ruru/modes/roo-commander/kb/`. In most common operational scenarios, the procedures defined in rules `02` through `12` should be sufficient.

**Consult the KB When:**

1.  **Explicitly Directed:** Another rule explicitly references a specific KB document for detailed steps or information (e.g., "consult KB `04-delegation-mdtm.md` for detailed steps").
2.  **Novel/Complex Procedures:** You encounter a task requiring a detailed procedure that is *not* adequately covered by the standard operational rules (`02` through `12`). Examples include:
    *   Executing the detailed steps within the MDTM workflow (delegation rule points here).
    *   Handling complex or unusual error scenarios (error handling rule points here).
    *   Following detailed safety protocols beyond basic checks (safety rule points here).
    *   Understanding the nuanced use of logging tools (`write_to_file` vs `append` vs `insert`) for specific log types (logging rule points here).
3.  **Reference Lookups:** You need to access large reference lists or detailed indices, such as:
    *   The full summary of available modes (`kb-available-modes-summary.md`).
    *   The index of standard processes (`10-standard-processes-index.md`).
    *   The index of standard workflows (`11-standard-workflows-index.md`).

**Procedure for KB Lookup:**

1.  **Identify Target Document:** Determine the specific KB document needed based on the directing rule or the nature of the complex/novel task. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for guidance if the specific file isn't immediately known.
2.  **Use `read_file`:** Access the content of the target KB document.
3.  **Apply Information:** Integrate the detailed steps, guidelines, or reference information into your current task execution.

**Key Objective:** To ensure detailed, complex, or reference-heavy procedures are accessed from the KB when required, without cluttering the core operational rules or requiring unnecessary lookups for common actions.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/00-user-preferences.md:
+++
# --- Basic Metadata ---
id = "user-preferences"
title = "User Preferences"
context_type = "configuration"
scope = "User-specific settings and profile information"
target_audience = ["all"]
granularity = "detailed"
status = "active"
last_updated = "2025-04-17"
# version = "1.0"
tags = ["user", "preferences", "configuration", "profile"]
# relevance = "High relevance for personalization and context awareness"
template_schema_doc = ".ruru/templates/toml-md/17_user_preferences.README.md" # Points to schema documentation

# --- User Information ---
user_name = "" # << REQUIRED >>
skills = [
    # << OPTIONAL >>
]

# --- Roo Usage Preferences ---
[roo_usage_preferences]
preferred_modes = [
    # << OPTIONAL >>
]
verbosity_level = "normal" # << OPTIONAL. Options: "concise", "normal", "verbose" >>
auto_execute_commands = false # << OPTIONAL >>
+preferred_language = "en" # << OPTIONAL. Fallback if specific input/output prefs not set. Default 'en' >>
+preferred_input_language = "en" # << OPTIONAL. Language user primarily uses for prompts >>
+preferred_output_language = "en" # << OPTIONAL. Preferred language for conversational output, comments, etc. >>
+++

# User Preferences Data (Defined in TOML)
# This file stores user-specific preferences and profile information.
# The primary content is within the TOML block above.
# Use the TOML fields to tailor interactions and understand user context.
# Add any free-form notes below if necessary, but prioritize structured data in TOML.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/01-standard-toml-md-format.md:
# Standard: TOML+Markdown (TOML MD) Format Usage

**Applies To:** All agents creating or modifying Markdown files intended to have structured metadata.

**1. General Principle:**

This workspace utilizes the **TOML+Markdown (TOML MD)** format for various documents (tasks, ADRs, documentation, context sources, etc.) to combine machine-readable metadata with human-readable content.
*   **Metadata:** Use **TOML** syntax for key-value pairs. Adhere strictly to valid TOML syntax.
*   **Content:** Use standard **Markdown** for the main body of the document following the metadata.
*   **Rationale:** See `.ruru/templates/toml-md/README.md` for the benefits and general usage guidelines.

**2. Delimiter Requirement (Universal):**

*   **ALL** Markdown files using TOML frontmatter for structured metadata **MUST** enclose the TOML block within triple-plus delimiters (`+++`).

    ```markdown
    +++
    # TOML frontmatter content goes here
    key = "value"
    # ... other fields specific to document type ...
    +++

    # Markdown content follows
    ...
    ```
*   This ensures unambiguous and reliable parsing by automated tools across all document types.

**3. Using Templates:**

*   **When creating a new Markdown document** that requires structured metadata (e.g., tasks, ADRs, documentation, context sources), **ALWAYS** use the TOML+MD format described above.
*   **Check for Existing Templates:** Before creating a new document from scratch, consult the **`.ruru/templates/toml-md/README.md`** file to see if a suitable template already exists in the `.ruru/templates/toml-md/` directory.
    *   Do **NOT** read all files in the `.ruru/templates/toml-md/` directory directly; rely on the README for the list of available templates and their descriptions.
    *   If a suitable template exists (e.g., `01_mdtm_feature.md`, `07_adr.md`), use it as the starting point and adhere to the TOML schema defined within that template.
*   **Creating New Templates:**
    *   If no specific template exists in `.ruru/templates/toml-md/` for the document type you need to create:
        1.  **Offer to Create:** Propose creating a new template with the user.
        2.  **Start with Boilerplate:** If the user agrees, copy the boilerplate template (`.ruru/templates/toml-md/00_boilerplate.md`) as a starting point.
        3.  **Define Schema:** Define the necessary TOML metadata fields within the `+++` delimiters, clearly commenting on their purpose and whether they are required.
        4.  **Structure Content:** Structure the Markdown body logically using appropriate headings.
        5.  **Save Template:** Save the new template file within the `.ruru/templates/toml-md/` directory, following the naming convention (e.g., `NN_description.md`).
        6.  **Update README:** **Crucially**, update the `.ruru/templates/toml-md/README.md` file to include the newly created template in the "Available Templates" list with a brief description. This makes it discoverable for future use.

**4. Key Considerations:**

*   **Syntax:** Always use valid TOML syntax within the `+++` block.
*   **Schema:** Adhere to the specific schema defined for the document type (either from an existing template or the newly defined one).
*   **Consistency:** Use defined field names and data types consistently.

**Failure to use the correct format (including `+++` delimiters) will cause errors in processing and build steps.**

# Rules from /home/jez/vscode/roo-commander/.roo/rules/04-mdtm-workflow-initiation.md:
+++
# --- Basic Metadata ---
id = "RULE-MDTM-WORKFLOW-INIT-V1"
title = "Standard MDTM Task Creation & Delegation Workflow"
context_type = "rules"
scope = "Creating and delegating tasks via the TOML-based MDTM system"
target_audience = ["roo-commander", "prime-coordinator", "lead-*", "manager-project", "all"] # Target coordinators, leads, and specialists (for the update part)
granularity = "procedure"
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["mdtm", "toml", "workflow", "delegation", "task-creation", "coordination", "rules"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/12-logging-procedure-rule.md",
    ".ruru/tasks/",
    ".ruru/templates/toml-md/",
    ".ruru/docs/standards/mdtm_standard.md" # General MDTM standard (might need updating for TOML emphasis)
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Defines core task delegation process"
+++

# Mandatory Rule: MDTM Task Creation & Delegation Workflow

This rule defines the standard procedure for creating Markdown-Driven Task Management (MDTM) task files (using TOML frontmatter) and delegating work to specialist modes when detailed tracking is required.

**Applies To:** `roo-commander`, `prime-coordinator`, `lead-*` modes (for initiating MDTM tasks), and `manager-project`. Also relevant for specialist modes receiving MDTM tasks.

**1. When to Use MDTM:**

*   Initiate this MDTM workflow (instead of simple `new_task` delegation) for tasks that meet criteria such as:
    *   Complexity (multi-step, involves dependencies).
    *   Requires detailed progress tracking or auditing.
    *   High-risk changes (core logic, infrastructure, security).
    *   Requires clear handoffs between specialists.
*   Refer to specific mode documentation (e.g., `roo-commander` KB `04-delegation-mdtm.md`) for detailed criteria if available. If unsure, **err on the side of using MDTM** for better tracking.

**2. Procedure for Initiator (Coordinator/Lead/Manager):**

1.  **Generate Task ID:** Create a unique task ID following the convention `TASK-[MODE_PREFIX]-[YYYYMMDD-HHMMSS]` (e.g., `TASK-REACT-20250422-140500`).
2.  **Select Template:** Choose the appropriate MDTM template from `.ruru/templates/toml-md/` (e.g., `01_mdtm_feature.md`, `02_mdtm_bug.md`).
3.  **Determine Path:** Construct the full path for the new task file within the `.ruru/tasks/` structure (e.g., `.ruru/tasks/FEATURE_Login/TASK-REACT-20250422-140500.md`).
4.  **Prepare Content:**
    *   **TOML Frontmatter:** Populate the `+++` block with essential metadata, adhering strictly to TOML syntax (Rule `01-standard-toml-md-format.md`). Include at minimum:
        *   `id`: The generated Task ID.
        *   `title`: Clear, concise task title.
        *   `status`: Set initially to `"🟡 To Do"` (or `"Pending"`).
        *   `type`: The appropriate task type (e.g., `"🌟 Feature"`, `"🐞 Bug"`).
        *   `assigned_to`: The slug of the target specialist mode (e.g., `"dev-react"`).
        *   `coordinator`: Your own mode's Task ID (e.g., `"TASK-CMD-..."`).
        *   `related_docs`: List paths to requirements, specs, etc.
        *   `tags`: Relevant keywords.
    *   **Markdown Body:** Fill in the Markdown sections (Description, Acceptance Criteria, Checklist). Define clear, actionable checklist items (`- [ ] Step description`).
5.  **Create Task File:** Use the `write_to_file` tool to create the MDTM task file at the determined path with the prepared TOML and Markdown content.
6.  **Log Creation:** Log the creation of the task file (including its path) according to standard logging procedures (Rule `12`).
7.  **Delegate via `new_task`:**
    *   Target the specialist mode specified in the `assigned_to` field.
    *   The `<message>` **MUST** clearly state: "Process MDTM task file: [Full path to the created .md file]". Include the Coordinator's Task ID for reference.
    *   Provide any *essential* immediate context if needed, but the primary instructions reside within the task file.
8.  **Update Initiator State:** Note that delegation has occurred. Await `attempt_completion` from the specialist. **Do not assume the task is being worked on in the background.**

**3. Responsibility of Assigned Specialist Mode:**

*   When receiving a `new_task` instruction referencing an MDTM task file:
    1.  **MUST** use `read_file` to load the content of the specified task file path.
    2.  **MUST** perform the work described in the Markdown body, following the checklist items.
    3.  **MUST** update the Markdown checklist (`- [ ]` -> `- [✅]`) as steps are completed using `apply_diff` or `search_and_replace`. Add brief notes/logs to the Markdown body as needed.
    4.  **MUST** update the `status` field in the **TOML block** of the task file upon completion (`"🟢 Done"`) or if blocked (`"⚪ Blocked"`), along with the `updated_date`, using `apply_diff`.
    5.  **MUST** report the final outcome back to the Coordinator using `attempt_completion`, referencing the MDTM task file path.

**Failure to create the MDTM file before delegation, or failure by the specialist to update the assigned file, breaks the tracking process.** This workflow is essential for managing complex tasks within the Roo system.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/05-os-aware-commands.md:
+++
# --- Basic Metadata ---
id = "RURU-RULE-OS-AWARE-CMDS-V3" # Incremented version
title = "Rule: Generate OS-Aware and Syntactically Correct Commands"
context_type = "rules"
scope = "Command generation for execute_command tool based on detected OS"
target_audience = ["all"] # Apply to all modes using execute_command
granularity = "procedure" # Changed from ruleset to procedure as it defines steps
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["rules", "shell", "commands", "os-awareness", "powershell", "bash", "execute_command", "windows", "linux", "macos", "syntax", "chaining", "conditional-execution"] # Added tags
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
related_context = [".roo/rules/03-standard-tool-use-xml-syntax.md"]
relevance = "Critical: Prevents command execution errors"
+++

# Mandatory Rule: Generate OS-Aware and Syntactically Correct Commands

**Context:** Commands executed via `<execute_command>` run within the user's VS Code integrated terminal environment. The underlying operating system significantly impacts required command syntax. Assume the host OS is provided via context (e.g., `environment_details.os` with values like `win32`, `darwin`, `linux`).

**Rule:**

When formulating commands intended for execution via the `<execute_command>` tool, you **MUST** check the operating system context provided (e.g., `environment_details.os`) and generate commands appropriate for that specific platform's default shell, ensuring correct syntax, especially for command chaining.

**Platform-Specific Syntax & Chaining:**

*   **If OS is `win32` (Windows):**
    *   Target Shell: **PowerShell**.
    *   Examples: `Get-ChildItem` (or `ls`/`dir`), `Copy-Item`, `Move-Item`, `Remove-Item`, `New-Item -ItemType Directory`, `$env:VAR_NAME`, `python -m venv .venv`, `.\.venv\Scripts\activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate multiple commands that should run one after the other, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **INVALID OPERATOR:** **NEVER use `&&` for chaining commands.** It is invalid syntax in PowerShell and will cause errors like "The token '&&' is not a valid statement separator".
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** PowerShell lacks a simple *separator* like `&&`. To achieve this reliably with `<execute_command>`:
        1.  Execute the first command in one `<execute_command>` call.
        2.  **Await the result.** Check the `exit_code`. An exit code of `0` typically indicates success.
        3.  If the first command succeeded (exit code 0), issue the second command in a *separate* `<execute_command>` call.
        4.  **AVOID** generating complex PowerShell `if ($?) {...}` or `try/catch` blocks within a single command string unless absolutely necessary and simple, as it violates the "Avoid Shell-Specific Scripts" guideline below.
    *   Paths: Use `\` or `/` (PowerShell is often flexible), but prefer `\` for consistency if constructing paths manually.
    *   Quoting: Use single quotes `'...'` for literal strings. Use double quotes `"..."` if variable expansion is needed (less common for simple commands).

*   **If OS is `darwin` (macOS) or `linux` (Linux):**
    *   Target Shell: **Bash/Zsh compatible** (POSIX-like).
    *   Examples: `ls`, `cp`, `mv`, `rm`, `mkdir`, `$VAR_NAME`, `python3 -m venv .venv`, `source .venv/bin/activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate commands that should run sequentially, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** **MUST use the double ampersand `&&`** (e.g., `cd my_dir && ls -l`). This is the standard and expected way to ensure the second command only runs if the first succeeds.
    *   **INVALID OPERATORS:** **NEVER use `&amp;&amp;`** when you need conditional execution. **NEVER** use the HTML entity `&amp;&amp;` in the command string passed to `<execute_command>`.
    *   Paths: **MUST** use forward slashes `/`.
    *   Quoting: Use double quotes `"..."` generally, especially if needing variable expansion (`$VAR`). Use single quotes `'...'` for strict literal strings.

**General Guidelines (Applies to ALL OS):**

*   **Simplicity:** Prefer simple, common commands where possible.
*   **Avoid Complex Scripts:** Do not generate complex multi-line shell scripts (`.ps1`, `.sh`) unless specifically requested and appropriate for the task. Focus on single commands or correctly chained commands suitable for `<execute_command>`.
*   **Syntax Check:** **Double-check generated command syntax** before outputting it, paying close attention to the correct chaining operators (`&&` vs `&amp;&amp;`), quoting, and path separators for the target OS.
*   **User Overrides:** If the user explicitly requests a command for a *different* shell (e.g., "run this bash command on Windows using WSL"), follow the user's explicit instruction, but otherwise default to the detected OS's standard shell syntax.

**Failure to generate OS-appropriate and syntactically correct commands, especially regarding chaining (`&&` vs `&amp;&amp;`), will likely result in execution errors for the user.** Always check the OS context and verify command syntax before generating commands.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/06-iterative-execution-policy.md:
+++
id = "RURU-RULE-ITERATIVE-EXECUTION-V1"
title = "Standard Iterative Execution Policy"
context_type = "rules"
scope = "Defines how modes should handle potentially long-running or complex tasks"
target_audience = ["all"] # Primarily relevant for modes performing implementation/generation
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "workflow", "iteration", "context-management", "safety", "mdtm", "chunking"]
related_context = ["00-user-preferences.md", "01-standard-toml-md-format.md", "04-standard-workflows.md"]
+++

# Standard Iterative Execution Policy

**Objective:** To ensure reliable task completion by preventing context window overflows and promoting manageable work increments, especially for generative or implementation tasks.

**Applies To:** All modes performing tasks that involve significant code generation, file modification, analysis, or following multi-step procedures (e.g., developers, writers, refactorers, testers, sometimes architects/managers). Less critical for simple lookups or coordination.

**Core Principles:**

1.  **Prefer Smaller Steps:** Whenever feasible, break down complex requests into smaller, logical sub-tasks during the planning phase. For tasks managed via MDTM, this means creating granular checklist items.
2.  **Context Awareness:** Modes **MUST** be aware of their context window usage (`{{CONTEXT_PERCENTAGE}}`).
3.  **Proactive Checkpointing:** Do not attempt to complete overly large tasks in a single execution turn, even if instructed broadly.

**Procedure:**

1.  **Task Planning:** When starting a task (especially one involving multiple steps or significant generation):
    *   Review the overall goal and acceptance criteria.
    *   If using MDTM, review the checklist items.
    *   Mentally estimate the complexity. If a task or a single MDTM checklist item *appears* likely to require extensive code/output generation or numerous tool calls:
        *   **Plan for Iteration:** Anticipate that completing the task/item might require more than one execution cycle.
        *   **(Optional but Recommended):** Inform the delegator (via `ask_followup_question` *before starting*) if you anticipate needing multiple steps/checkpoints for a single requested item.

2.  **Execution & Monitoring:** While executing the task (writing code, applying diffs, following checklist items):
    *   Periodically self-monitor context window usage (`{{CONTEXT_PERCENTAGE}}`).
    *   **Trigger Checkpoint:** If context usage approaches a threshold (e.g., **around 40-50%**), prepare to pause *after completing the current logical unit of work*.
        *   A "logical unit" could be:
            *   Completing the current MDTM checklist item (`- [✅]`).
            *   Finishing a complete function, class, or coherent block of code.
            *   Completing a specific file modification.
            *   Finishing a distinct step in an analysis process.

3.  **Checkpoint & Handover:** When pausing due to the context threshold OR completing a step marked for reporting (e.g., `📣` in MDTM):
    *   **Finalize Current Unit:** Ensure the immediate work unit is complete and syntactically correct (e.g., finish the function, close code blocks).
    *   **Summarize Progress:** Briefly state what was completed in the current turn.
    *   **Identify Next Step:** Clearly state the *next logical step* required to continue the overall task (e.g., "Next step is to implement the `handleUpdate` function", "Next step is to process MDTM item #3").
    *   **Report Status:** Use `<attempt_completion>` to report back to the delegator. Include:
        *   Confirmation of completed unit/step.
        *   Current context percentage.
        *   The identified *next step*.
        *   Any partial results or paths to modified/created files.
        *   *(Example Result):* "✅ Completed implementation of `getUserData` function (MDTM item #2). Context at 55%. Next step is to implement the `UserProfile` component using this data. Modified: `src/hooks/useUserData.ts`."

4.  **Receiving Mode Action (Coordinator/Lead):**
    *   Acknowledge the partial completion and the stated next step.
    *   Log the progress (Rule `12`).
    *   Re-delegate the *next step* back to the specialist mode, providing the necessary context (including the original goal and referencing the previous work/files).

**Rationale:**

*   **Context Safety:** Prevents hitting hard context limits which often lead to truncated, incomplete, or erroneous responses.
*   **Error Reduction:** Smaller execution units reduce the chance of complex errors accumulating within a single turn.
*   **State Management:** Encourages breaking work into steps that align well with MDTM tracking, improving visibility.
*   **User Experience:** While it involves more turns, it leads to more reliable progress compared to large failures requiring complete restarts.

**Note:** The 50-60% threshold is a guideline. Modes should use judgment. If a small, final step pushes usage slightly over, completing it might be acceptable. The key is to avoid *starting* a large unit of work when context is already high.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/08-logging-procedure-simplified.md:
+++
id = "RULE-LOGGING-PROCEDURE-SIMPLE-V1"
title = "Standard: Logging Requirement"
context_type = "rules"
scope = "Requirement to log significant events and decisions"
target_audience = ["all"] # Especially Coordinators and Leads
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "logging", "auditing", "traceability", "mdtm"]
related_context = [
    ".roo/rules/04-mdtm-workflow-initiation.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md" # Link to detailed KB
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Essential for traceability and state management"
+++

# Standard: Logging Requirement

**Objective:** Ensure a traceable record of actions, decisions, and task progress.

**Rule:**

1.  **Log Events:** You **MUST** log significant events relevant to your task execution (e.g., decisions made, tasks delegated, errors encountered, steps completed, coordination actions).
2.  **Designated Location:** Log entries should typically be added to your assigned MDTM task file (`.ruru/tasks/TASK-...`), your coordination log file, or other designated artifact locations (e.g., ADRs in `.ruru/decisions/`).
3.  **Tooling Details:** For detailed guidance on *which tools* (`write_to_file`, `append_to_file`, `insert_content`, `apply_diff`) to use for specific logging scenarios and locations, consult the Roo Commander Knowledge Base document: **`.ruru/modes/roo-commander/kb/12-logging-procedures.md`**.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/10-vertex-mcp-usage-guideline.md:
+++
# --- Basic Metadata ---
id = "RULE-VERTEX-MCP-USAGE-V1"
title = "Guideline: Vertex AI MCP Tool Usage"
context_type = "rules"
scope = "Standardizing the use of Vertex AI MCP tools, especially save vs. direct output"
target_audience = ["all"] # Primarily modes using research/generation
granularity = "guideline"
status = "active"
last_updated = "2025-04-26" # Use current date
tags = ["rules", "mcp", "vertex-ai", "guideline", "output-handling", "file-organization", "research", "validation"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/08-logging-procedure-simplified.md",
    "repomix-output-shariqriazz-vertex-ai-mcp-server.md" # Reference to the MCP definition
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures consistent handling of MCP outputs"
+++

# Guideline: Vertex AI MCP Tool Usage

**Objective:** To standardize how modes interact with the `vertex-ai-mcp-server`, particularly regarding output handling and the use of research/validation capabilities.

**Applies To:** All modes utilizing tools provided by the `vertex-ai-mcp-server`.

**1. Tool Availability:**

*   Modes receive the list of available MCP tools dynamically in their context. Use these tools only if the `vertex-ai-mcp-server` is connected and the specific tool is listed.
*   Modes should gracefully handle scenarios where the MCP server or specific tools are unavailable.

**2. Output Handling Strategy (General):**

*   **Default to `save_*`:** When using Vertex AI MCP tools that have a corresponding `save_*` variant (e.g., `save_generate_project_guidelines`, `save_doc_snippet`, `save_topic_explanation`, `save_answer_query_direct`, `save_answer_query_websearch`), **prefer using the `save_*` variant** for potentially long or complex outputs.
    *   **Rationale:** This prevents large outputs from cluttering the chat history, archives the result for later reference, and helps manage context window size.
*   **Use Direct Tools Sparingly:** Use the direct output tools (e.g., `answer_query_websearch`, `explain_topic_with_docs`, `get_doc_snippets`) only when the expected output is known to be concise (e.g., a single code snippet, a short definition, a simple yes/no answer) or when specifically requested by the user/coordinator for an inline response.
*   **Reporting Saved Files:** When using a `save_*` tool, the mode **MUST** report the full path to the saved file back to the coordinator/user via `<attempt_completion>`. (See Section 2.1 for handling persistent context outputs.)

**2.1. Handling Persistent Context Outputs:**

*   **Identify Need:** If the output generated by a `save_*` tool is intended to be *persistent context* referenced directly by mode rules, KBs, or long-term documentation (unlike temporary analysis results):
    1.  **Move & Rename:** After the `save_*` tool successfully creates the file in the default `.ruru/docs/vertex/...` location, the coordinating mode **MUST** immediately use a file system tool (`execute_command` with `mkdir -p` and `mv`, or the `vertex-ai-mcp-server`'s `create_directory` and `move_file_or_directory` tools) to:
        *   Ensure a `context/` subdirectory exists within the relevant mode's directory (e.g., `.ruru/modes/[mode-slug]/context/`).
        *   Move the generated file from `.ruru/docs/vertex/...` into this mode-specific `context/` directory.
        *   Rename the file to something meaningful and versioned if appropriate (e.g., `[mode-slug]_context_[topic]_v1.md`) instead of the default timestamped name.
    2.  **Update References:** Any rules, KBs, or documents referencing this context **MUST** be updated immediately to point to the new, persistent path within the mode's `context/` directory.
    3.  **Log Move:** Log the move and rename operation.
*   **Rationale:** This ensures that context critical to a mode's operation is stored logically with the mode and avoids broken references if the general `.ruru/docs/vertex/` directory is treated as temporary. The default timestamped location should be used for transient outputs or initial review before deciding on persistence.

**3. Standard Output Location & Naming:**

*   **Base Directory:** All files generated by `save_*` tools **MUST** be saved within the `.ruru/docs/vertex/` directory.
*   **Subdirectory Structure:** Organize files by the *type* of tool used:
    *   `save_generate_project_guidelines` -> `.ruru/docs/vertex/guidelines/`
    *   `save_doc_snippet` -> `.ruru/docs/vertex/snippets/`
    *   `save_topic_explanation` -> `.ruru/docs/vertex/explanations/`
    *   `save_answer_query_direct` -> `.ruru/docs/vertex/answers-direct/`
    *   `save_answer_query_websearch` -> `.ruru/docs/vertex/answers-web/`
*   **File Naming Convention:** Files **MUST** be named using the format `[YYYYMMDDHHMMSS]-[sanitized_topic_or_query].md`.
    *   `[YYYYMMDDHHMMSS]`: Timestamp generated by the mode at the time of the call.
    *   `[sanitized_topic_or_query]`: A filesystem-safe representation of the primary topic or query (e.g., replace spaces/special characters with `_`, limit length to ~50 characters).
    *   *Example:* `.ruru/docs/vertex/guidelines/20250426182500-react_ts_node_guidelines.md`

**4. Using MCP for Research & Validation ("Brains Trust"):**

*   **Targeted Use:** While tools like `answer_query_websearch` can provide external context or validation, their use should be targeted and judicious due to latency, cost, and potential complexity.
*   **Prioritize Internal Context:** Modes **MUST** prioritize using internal project knowledge (KBs, rules, existing code, task context) before resorting to external MCP calls for validation or general research.
*   **Recommended Modes:** Consider enabling or encouraging this capability primarily within modes focused on architecture, research, complex problem-solving, or senior-level review (e.g., `technical-architect`, `agent-research`, `complex-problem-solver`, `util-senior-dev`, `util-second-opinion`).
*   **Clear Triggers:** Modes utilizing external validation should have clear triggers defined in their specific rules/KBs (e.g., "when evaluating unfamiliar technology", "if confidence is low").
*   **Log Usage:** Log instances where external validation was sought via MCP, including the query and a summary of the outcome, according to standard logging procedures (Rule `08-logging-procedure-simplified.md`).

**Adherence to these guidelines ensures consistent, traceable, and efficient use of the Vertex AI MCP capabilities.**</custom_instructions>
</environment_details>

---

**Assistant:**

Okay, the session directory structure is created. Now I will create the session log file.

```xml
<write_to_file>
<path>.ruru/sessions/SESS-CMD-20250503-002535/session_log.md</path>
<content>
+++
# --- Session Metadata (Auto-Managed) ---
id = "SESS-CMD-20250503-002535" # Auto-generated unique session ID
status = "active" # active, completed, aborted
created_date = "2025-05-03T00:25:35+10:00" # Timestamp of session creation
last_updated = "2025-05-03T00:25:52+10:00" # Timestamp of last update
mode = "roo-commander" # Mode active during session creation
model = "gemini-2.5-pro-exp-03-25" # Model used
cost = 0.00 # Estimated cost (USD)
tokens = 84117 # Estimated tokens used

# --- Session Goal & Context ---
goal = "Generate Repomix artifact for Roo-Code-Docs/docs/advanced-usage" # User-defined or inferred goal
initial_prompt = "i want a repomix of this folder https://github.com/RooVetGit/Roo-Code-Docs/tree/main/docs/advanced-usage" # The user's initial prompt
related_artifacts = [] # List of paths to related files (tasks, ADRs, outputs) relative to session dir

# --- Session Summary ---
summary = "" # A brief summary of the session's outcome (filled upon completion/abortion)
+++

# Session Log: SESS-CMD-20250503-002535

**Goal:** Generate Repomix artifact for Roo-Code-Docs/docs/advanced-usage

**Log Entries:**

*   `[2025-05-03T00:25:52+10:00]` Session initiated. Created directory structure: `.ruru/sessions/SESS-CMD-20250503-002535/artifacts`.
</content>
<line_count>26</line_count>
</write_to_file>
```

---

**User:**

[write_to_file for '.ruru/sessions/SESS-CMD-20250503-002535/session_log.md'] Result:
The content was successfully saved to .ruru/sessions/SESS-CMD-20250503-002535/session_log.md.
<environment_details>
# VSCode Visible Files
.ruru/sessions/SESS-CMD-20250503-002535/session_log.md

# VSCode Open Tabs
.ruru/sessions/SESS-CMD-20250503-002535/session_log.md

# Current Time
03/05/2025, 12:26:08 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
102,366 (10%)

# Current Cost
$0.00

# Current Mode
<slug>roo-commander</slug>
<name>👑 Roo Commander</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Chief Executive, the highest-level coordinator for software development projects. You understand goals, delegate tasks using context and specialist capabilities, manage state via the project journal, and ensure project success.

Operational Guidelines:
- Prioritize rules and workflows found in the Knowledge Base (KB) at `.ruru/modes/roo-commander/kb/` over general knowledge for detailed procedures. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for navigation and the KB lookup rule (`.roo/rules-roo-commander/01-kb-lookup-rule.md`) for guidance on when and how to consult the KB.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files, especially for coordination artifacts.
- Use `read_file` to confirm content before applying diffs if unsure.
- Execute CLI commands using `execute_command`, explaining clearly.
- Escalate tasks outside core expertise to appropriate specialists via the lead or coordinator.</role>
<custom_instructions>
====

USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

Language Preference:
You should always speak and think in the "English" (en) language unless the user gives you instructions below to do otherwise.

Rules:

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/01-operational-principles.md:
+++
id = "ROO-CMD-PRINCIPLES-V1"
title = "Roo Commander: General Operational Principles"
context_type = "rules"
scope = "Core operational philosophy for Roo Commander"
target_audience = ["roo-commander"]
granularity = "principles"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "principles", "core", "coordination", "roo-commander"]
related_context = ["02-initialization-workflow-rule.md", "03-delegation-procedure-rule.md", "05-error-handling-rule.md", "06-documentation-adr-rule.md", "09-logging-procedure-rule.md", "99-kb-lookup-rule.md"]
+++

# General Operational Principles

These are the core principles guiding your actions as Roo Commander. Specific procedures for common workflows are detailed in other rule files, and highly detailed or less frequent procedures reside in the Knowledge Base (`.ruru/modes/roo-commander/kb/`).

1.  **Clarity and Intent:** Prioritize understanding the user's high-level goals before diving into specifics. Use clarifying questions (`ask_followup_question`) when intent is ambiguous. *(See Rule: `02-initialization-workflow-rule.md`)*
2.  **Strategic Delegation:** Leverage the full suite of specialist modes. Choose the *most appropriate* specialist based on the task, Stack Profile, and mode tags. Delegate clear, actionable tasks with defined goals and context. *(See Rule: `03-delegation-procedure-rule.md`)*
3.  **Context is Key:** Ensure all delegated tasks include necessary context (Task IDs, relevant file paths, Stack Profile). Determine the need for `agent-context-resolver` based on situational judgment (complexity, ambiguity, impact) before major delegations.
4.  **Logging Diligence:** Maintain accurate and timely records of decisions, delegations, errors, status updates, and other significant events.
6.  **User Focus:** Keep the user informed of the plan, progress, and any significant issues or decisions. Frame communication around achieving the user's objectives.
7.  **Command Line Assistance:** When using `execute_command`, explain the command clearly. If multiple command options exist, proactively ask the user for preference and offer brief explanations, while respecting safety protocols.
8.  **Error Handling:** Handle errors systematically by logging, analyzing, deciding on next steps, and acting. *(See Rule: `05-error-handling-rule.md`)*.
9.  **Documentation & Decisions:** Oversee documentation. Log significant decisions as ADRs. *(See Rule: `06-documentation-adr-rule.md`)*.
11. **Use KB When Directed:** Consult the Knowledge Base (`.ruru/modes/roo-commander/kb/`) when explicitly directed by other rules or when encountering novel/complex procedures not covered here. *(See Rule: `99-kb-lookup-rule.md`)*.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/02-initialization-workflow-rule.md:
+++
id = "ROO-CMD-RULE-INIT-V5" # Incremented version
title = "Roo Commander: Rule - Initial Request Processing & Mode Management" # Updated title
context_type = "rules"
scope = "Initial user interaction handling, presenting comprehensive starting options and routing to specific KB procedures"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-27" # Use current date
tags = ["rules", "workflow", "initialization", "onboarding", "intent", "options", "kb-routing", "roo-commander", "mode-management"] # Added tag
related_context = [
    "01-operational-principles.md",
    # Specific KB Action files
    ".ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md", # Added MCP Install option
    ".ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md",
    ".ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md",
    ".ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md",
    ".ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md",
    ".ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md",
    ".ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md",
    ".ruru/modes/roo-commander/kb/initial-actions/09-review-status.md",
    ".ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md",
    ".ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md",
    ".ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md",
    ".ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md",
    ".ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md",
    ".ruru/modes/roo-commander/kb/initial-actions/15-join-community.md",
    ".ruru/modes/roo-commander/kb/initial-actions/16-something-else.md",
    # Option 17 now handles Mode Management
    # Key delegate modes
    "manager-onboarding",
    "dev-git",
    "core-architect",
    "manager-product",
    "agent-research",
    "prime-coordinator",
    "dev-fixer",
    "util-refactor",
    "util-writer"
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the entry point for user interaction and routes to specific procedures"
+++

# Rule: Initial Request Processing (Explicit KB Routing)

This rule governs how you handle the **first user message** in a session, presenting a comprehensive list of starting options to clarify intent and initiate the correct workflow by executing procedures defined in specific Knowledge Base (KB) files.

**Standard Initial Prompt (if needed):**

```xml
 <ask_followup_question>
  <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
  <follow_up>
    <suggest>🔌 Install/Manage MCP Servers</suggest> <!-- Option 0 -->
    <suggest>🎩 Start a NEW project from scratch</suggest> <!-- Option 1 -->
    <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest> <!-- Option 2 -->
    <suggest>🌐 Clone a Git repository & onboard</suggest> <!-- Option 3 -->
    <suggest>🗃️ Use existing project files/plans to define the work</suggest> <!-- Option 4 -->
    <suggest>📑 Plan/Design a new feature or project</suggest> <!-- Option 5 -->
    <suggest>🐞 Fix a specific bug</suggest> <!-- Option 6 -->
    <suggest>♻️ Refactor or improve existing code</suggest> <!-- Option 7 -->
    <suggest>✍️ Write or update documentation</suggest> <!-- Option 8 -->
    <suggest>📟 Review project status / Manage tasks (MDTM)</suggest> <!-- Option 9 -->
    <suggest>❓ Research a topic / Ask a technical question</suggest> <!-- Option 10 -->
    <suggest>🎺 Execute a command / Delegate a specific known task</suggest> <!-- Option 11 -->
    <suggest>🪃 Manage Roo Configuration (Advanced)</suggest> <!-- Option 12 -->
    <suggest>🖲️ Update my preferences / profile</suggest> <!-- Option 13 -->
    <suggest>🦘 Learn about Roo Commander capabilities</suggest> <!-- Option 14 -->
    <suggest>🐾 Join the Roo Commander Community (Discord)</suggest> <!-- Option 15 -->
    <suggest>🤔 Something else... (Describe your goal)</suggest> <!-- Option 16 -->
    <suggest>🧑‍🎨 Mode Management</suggest> <!-- Option 17 -->
<suggest>📜 Workflow Management (Create, Read, Update, Delete Workflows)</suggest> <!-- Option 18 -> Switch to util-workflow-manager -->
  </follow_up>
 </ask_followup_question>```

**Procedure:**

1.  **Analyze Initial User Request:**
    *   Check for explicit mode switch requests ("switch to `[mode-slug]`").
    *   Briefly analyze keywords if the user states a goal directly.

2.  **Determine Response Path:**

    *   **A. Direct Mode Request:**
        *   If user explicitly requests switching to a specific mode: Confirm understanding and attempt `<switch_mode> [mode-slug]`. Log action (Rule `08`). **End this workflow.**

    *   **B. Direct Goal Stated (High Confidence - Non-Onboarding):**
        *   If the user's first message clearly states a goal that confidently maps to a specific action *other than onboarding/setup* (e.g., "fix bug 123", "refactor `userService.js`"):
            1.  Acknowledge the goal.
            2.  Propose the most relevant specialist mode via `ask_followup_question`.
            3.  Include suggestions: `<suggest>Yes, use [Proposed Mode]</suggest>`, `<suggest>No, let me choose from all starting options</suggest>`.
            4.  If "Yes", proceed to standard delegation (Rule `03`). Log action. **End this workflow.**
            5.  If "No", proceed to **Path C**.

    *   **C. All Other Cases (Default Path):**
        *   Includes: Vague requests, requests for help/options, requests initially mentioning "new project" or "onboard existing", or user selecting "No" in Path B.
        *   **Action:** Present the **Standard Initial Prompt** (defined above) using `<ask_followup_question>`.
        *   Await user's selection. Proceed to Step 3.

3.  **Handle User Selection (from Standard Initial Prompt):**
    *   Once the user selects an option (identified 0-18) from the standard prompt:
        1.  Identify the selected option number.
        2.  Log the chosen starting path (Rule `08`).
        3.  **Execute the detailed procedure defined in the corresponding KB file**:
            *   Option 0: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md`.
            *   Option 1: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md`.
            *   Option 2: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md`.
            *   Option 3: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md`.
            *   Option 4: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md`.
            *   Option 5: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md`.
            *   Option 6: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md`.
            *   Option 7: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md`.
            *   Option 8: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md`.
            *   Option 9: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/09-review-status.md`.
            *   Option 10: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md`.
            *   Option 11: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md`.
            *   Option 12: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md`.
            *   Option 13: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md`.
            *   Option 14: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md`.
            *   Option 15: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/15-join-community.md`.
            *   Option 16 ("Something else"): Execute KB `.ruru/modes/roo-commander/kb/initial-actions/16-something-else.md`.
            *   Option 17 ("Mode Management"): Present the user with the following choices and initiate the corresponding workflow:
                *   Create New Mode (`.ruru/workflows/WF-NEW-MODE-CREATION-004.md`)
                *   Mode KB Enrichment with Vertex AI MCP (`.ruru/workflows/WF-MODE-KB-ENRICHMENT-002.md`)
                *   Mode KB Enrichment with Context7 (`.ruru/workflows/WF-CONTEXT7-ENRICHMENT-001.md`)
                *   Mode KB Refresh with Context 7 (`.ruru/workflows/WF-CONTEXT7-REFRESH-001.md`)
                *   Delete Modes (Note: Workflow needs creation)
        *   Option 18 ("Workflow Management"): Switch to `util-workflow-manager` mode.
        4.  Follow the steps within the chosen KB procedure or subsequent workflow, including any user interaction or delegation it defines. **End this initialization workflow** upon completion of the KB procedure or delegated workflow.

**Key Objective:** To provide clear starting options and route the user interaction to the precise, detailed procedure stored in the relevant Knowledge Base file or subsequent workflow, ensuring consistent handling for each initial user intention, including mode management tasks.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03-delegation-simplified.md:
+++
id = "ROO-CMD-RULE-DELEGATION-SIMPLE-V1"
title = "Roo Commander: Rule - Task Delegation (Simplified)"
context_type = "rules"
scope = "Delegating tasks to specialist modes, including MDTM decision"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25"
tags = ["rules", "delegation", "mdtm", "specialists", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    ".ruru/docs/standards/mode_selection_guide.md",
    ".ruru/context/stack_profile.json",
    ".ruru/modes/roo-commander/kb/04-delegation-mdtm.md", # For detailed MDTM steps
    "04-mdtm-workflow-initiation.md" # Workspace rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Core delegation logic"
+++

# Rule: Task Delegation (Simplified)

1.  **Define Goal:** Clearly define the task objective.
2.  **Select Specialist:** Consult Stack Profile (`.ruru/context/stack_profile.json`) and the **Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`)**. Match task requirements/tags to specialist capabilities. Prioritize specific modes over generalists. Log rationale (Rule `08`).
3.  **Determine Method:**
    *   **Use MDTM Workflow if:** Task is complex, stateful, high-risk, requires detailed tracking/handoffs (Ref: Rule `04-mdtm-workflow-initiation.md`). Consult KB `.ruru/modes/roo-commander/kb/04-delegation-mdtm.md` for detailed procedure if needed.
    *   **Use Simple `new_task` if:** Task is straightforward, read-only, or low-risk.
4.  **Prepare Context:** Gather essential context (goal, criteria, file paths, Task IDs, Stack Profile).
5.  **Execute Delegation:** Use `new_task`. For MDTM, follow Rule `04-mdtm-workflow-initiation.md` (which includes creating the task file first). For simple tasks, provide context directly in the message.
6.  **Log & Monitor:** Log delegation (Rule `08`). Monitor via Rule `04`.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03b-complex-delegation-planning.md:
+++
id = "ROO-CMD-RULE-COMPLEX-DELEGATION-PLAN-V1"
title = "Roo Commander: Rule - Complex Delegation Planning & Confidence Check"
context_type = "rules"
scope = "Procedure for planning multi-step delegations and consulting user when confidence is low"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25" # Use current date
tags = ["rules", "delegation", "planning", "confidence", "multi-step", "mdtm", "roo-commander", "user-consultation"]
related_context = [
    "03-delegation-simplified.md", # The basic delegation rule
    ".roo/rules/04-mdtm-workflow-initiation.md", # Workspace MDTM rule
    ".roo/rules/06-iterative-execution-policy.md", # Iteration policy
    ".ruru/docs/standards/mode_selection_guide.md" # Mode selection guide
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Enhances strategic delegation for complex tasks"
+++

# Rule: Complex Delegation Planning & Confidence Check

This rule extends the basic delegation procedure (`03-delegation-simplified.md`) for tasks identified as particularly complex, ambiguous, or requiring a sequence of coordinated steps beyond a single MDTM task file.

**1. Trigger Conditions:**

*   Apply this procedure when a task involves:
    *   Significant ambiguity in requirements or implementation path.
    *   Multiple distinct phases or dependencies requiring different specialists or sequential execution.
    *   High uncertainty about the best approach or required modes.
    *   Initial analysis suggests the task breakdown might exceed simple MDTM checklist granularity or requires strategic sequencing.

**2. Planning Procedure:**

1.  **Analyze Goal:** Deeply analyze the user's goal, acceptance criteria, and any provided context. Identify ambiguities and potential complexities.
2.  **Break Down Task:** Decompose the overall goal into smaller, logical sub-tasks or phases.
3.  **Identify Specialists & Sequence:** For each sub-task, identify the most appropriate specialist mode(s) using the Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`). Determine the logical sequence or potential parallel execution paths.
4.  **Estimate Effort/Risk:** Briefly assess the estimated effort and risk associated with each sub-task and the overall plan.
5.  **Formulate Plan:** Outline the proposed delegation plan, including:
    *   Sequence of sub-tasks.
    *   Assigned specialist mode for each sub-task.
    *   Whether MDTM or simple `new_task` is appropriate for each step (following Rule `04-mdtm-workflow-initiation.md`).
    *   Key dependencies or handoffs between steps.

**3. Confidence Assessment:**

*   Evaluate your confidence in the formulated plan's success and efficiency. Consider:
    *   Clarity of requirements for each step.
    *   Availability and suitability of specialist modes.
    *   Potential risks or unknowns.
*   Assign a subjective confidence level (e.g., High, Medium, Low).

**4. User Consultation (Low/Medium Confidence):**

*   **If confidence is assessed as Low or Medium:**
    1.  **Do NOT proceed with delegation immediately.**
    2.  Use the `<ask_followup_question>` tool to present the situation to the user.
    3.  **Question Content:**
        *   Briefly explain the task's complexity and the reason for uncertainty.
        *   Present the proposed delegation plan (sub-tasks, modes, sequence).
        *   State your confidence level and the reasons (e.g., "Medium confidence due to ambiguity in API specification").
    4.  **Suggested Follow-ups:** Provide 2-4 actionable suggestions for the user, such as:
        *   "Proceed with the proposed plan."
        *   "Modify the plan: [Suggest a specific alternative sequence or mode]."
        *   "Provide clarification on: [Specify the ambiguous point]."
        *   "Delegate to [Alternative Lead/Mode] for further planning."
    5.  Await user direction before proceeding with delegation based on their choice.

**5. Execution (High Confidence or User Approval):**

*   If confidence is High, or if the user approves a plan after consultation:
    *   Proceed with executing the delegation plan step-by-step, using MDTM or simple `new_task` as determined for each sub-task.
    *   Follow standard logging (Rule `08`) and monitoring (Rule `04`) procedures.
    *   Utilize the Iterative Execution Policy (Rule `06`) for individual delegated steps as needed.

**Rationale:** This provides a mechanism for `roo-commander` to handle complex scenarios more robustly, leveraging user input when its own planning confidence is insufficient, thereby reducing the risk of inefficient or failed delegation chains.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/05-error-handling-rule.md:
+++
id = "ROO-CMD-RULE-ERROR-HANDLING-V1"
title = "Roo Commander: Rule - Basic Error Handling"
context_type = "rules"
scope = "Standard procedure for handling initial errors, failures, and blockers"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "error-handling", "failure", "blocker", "coordination", "roo-commander"]
related_context = ["01-operational-principles.md", "04-monitoring-completion-rule.md", "05-collaboration-escalation.md", "12-logging-procedures.md", ".ruru/modes/roo-commander/kb/05-collaboration-escalation.md"]
+++

# Rule: Basic Error Handling

This rule outlines the standard initial procedure when an error, failure (❌), or blocker (🧱) is detected either during Roo Commander's own operations or reported by a delegated specialist via `<attempt_completion>`.

**Procedure:**

1.  **Detection & Initial Assessment:** Identify the error/failure/blocker. Briefly assess its apparent severity and immediate impact based on available information (e.g., error message, specialist report, task status).

2.  **Log Failure Event:** **Immediately** log the detected issue according to Rule `12`. Include:
    *   Timestamp.
    *   Source of the error (e.g., specialist Task ID, tool failure).
    *   Error message or description of the blocker.
    *   Relevant context (e.g., related Commander Task ID).

3.  **Simple Analysis / Context Gathering:**
    *   Review the specific error message and the context logged in Step 2.
    *   If reported by a specialist, review their `<result>` content and the relevant task log (`read_file` on `.ruru/tasks/TASK-[MODE]-....md`) for details.
    *   Determine if the cause is immediately obvious and likely simple (e.g., typo in a command, file not found, simple syntax error reported by specialist).

4.  **Decision & Action (Prioritize Simple Fixes):**

    *   **If** the cause seems simple and easily correctable (e.g., fixable typo in delegation, incorrect file path):
        1.  **Plan Fix:** Determine the corrective action (e.g., re-delegate with corrected parameters).
        2.  **Log Decision:** Log the simple fix plan according to Rule `12`.
        3.  **Execute Fix:** Implement the fix (e.g., use `new_task` to re-delegate).
        4.  **Return to Monitoring:** Go back to monitoring the task (Rule `04`).

    *   **Else (If cause unclear, complex, requires specialist analysis, or involves safety/architecture):**
        1.  **Do NOT attempt complex fixes directly.**
        2.  **Consult Detailed Procedures:** Refer to the comprehensive error handling and escalation path details in the Knowledge Base: **`.ruru/modes/roo-commander/kb/05-collaboration-escalation.md`**.
        3.  **Follow KB Guidance:** Execute the relevant analysis, user consultation, or escalation steps outlined in the KB document (e.g., involving `dev-solver`, `core-architect`, or the User).
        4.  **Log Decision & Action:** Log the decision to escalate or perform further analysis according to Rule `12`.

**Key Objective:** To ensure all failures are logged immediately and that simple, obvious errors are handled efficiently, while complex or uncertain issues are systematically routed to more detailed analysis and escalation procedures defined in the KB.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/06-documentation-adr-simplified.md:
+++
id = "ROO-CMD-RULE-DOC-ADR-SIMPLE-V1"
title = "Roo Commander: Rule - Documentation & ADR Trigger (Simplified)"
context_type = "rules"
scope = "Triggering ADR creation and overseeing documentation"
target_audience = ["roo-commander"]
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "documentation", "adr", "logging", "decision-record", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    "08-logging-procedure-simplified.md", # Reference the simplified logging rule
    ".ruru/modes/roo-commander/kb/06-documentation-logging.md", # Detailed ADR creation/doc mgmt in KB
    ".ruru/templates/toml-md/07_adr.md", # ADR Template
    ".ruru/decisions/" # Standard ADR location
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures important decisions are recorded"
+++

# Rule: Documentation & ADR Trigger (Simplified)

1.  **Documentation Oversight:** Oversee project documentation location and status. Prefer delegating creation/updates of stable docs (`.ruru/docs/`) to specialists (`util-writer`, `core-architect`). Handle planning docs (`.ruru/planning/`) directly if needed, preferring `apply_diff` for modifications. Consult KB `.ruru/modes/roo-commander/kb/06-documentation-logging.md` for detailed documentation management guidance.

2.  **ADR Trigger:** An Architecture Decision Record (ADR) **MUST** be created in `.ruru/decisions/` for any **significant** architectural, technological, or strategic decision (e.g., framework choice, major pattern adoption, core tech selection).

3.  **ADR Procedure:** To create an ADR, consult the Knowledge Base document **`.ruru/modes/roo-commander/kb/06-documentation-logging.md`** for the detailed procedure. This involves using the standard template (`.ruru/templates/toml-md/07_adr.md`), writing the content, and logging the creation (Rule `08`).

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/10-meta-discussion-tool-output-handling.md:
+++
id = "CMD-RULE-META-TOOL-HANDLING-V3" # Adjusted ID for Commander, incremented version
title = "Roo Commander: Rule - Meta-Discussion Tool Output Handling" # Adjusted Title
context_type = "rules"
scope = "Handling the display or referencing of tool usage during meta-discussions"
target_audience = ["roo-commander"] # Target Commander
granularity = "guideline"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["rules", "meta-discussion", "tool-use", "safety", "roo-commander", "logging", "analysis", "file-output"] # Added roo-commander tag
related_context = [
    ".roo/rules/03-standard-tool-use-xml-syntax.md",
    ".roo/rules/08-logging-procedure-simplified.md" # Logging rule for file creation
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Prevents accidental tool execution during analysis/troubleshooting"
+++

# Rule: Meta-Discussion Tool Output Handling

**Objective:** To prevent accidental tool execution when discussing or analyzing previous interactions, logs, or mode behavior that involves tool usage syntax, while still allowing access to exact syntax details when necessary.

**Applies To:** `roo-commander` (A corresponding rule MUST exist for `prime-coordinator`).

**Rule:**

1.  **Identify Context:** When processing user input, provided content (like chat logs or file content), or formulating responses, carefully assess if the context clearly indicates a **meta-discussion**. This includes:
    *   Analyzing or reviewing past chat logs or MDTM task logs.
    *   Troubleshooting mode behavior or errors related to tool use.
    *   Discussing potential improvements to modes, rules, or workflows involving tool interactions.
    *   Responding to user feedback about specific tool interactions.
    *   Any situation where the user explicitly states they are discussing *past* tool use and do *not* want tools executed.

2.  **Strictly Avoid Direct Tool XML Output in Chat:** If the context is identified as a meta-discussion:
    *   **MUST NOT** output text formatted according to the standard tool usage XML syntax directly into the chat response.
    *   **MUST NOT** output text that mimics the tool usage XML syntax directly into the chat response, even if escaped (e.g., using backticks or other methods).

3.  **Describe or Offer File Output:** When referencing a specific tool use from the analyzed content:
    *   **Default Action:** Describe the tool use in plain text or standard Markdown, focusing on the *action*, *tool name*, and key *parameters* without using the XML structure.
        *   *Example Description:* "In the log, the mode then used the `read_file` tool, specifying the path `.ruru/workflows/WF-REPOMIX-V2/README.md`."
    *   **Alternative (Offer File Output):** If a simple description seems insufficient, or if the exact XML syntax might be important for the discussion (e.g., debugging complex parameters), **offer to write the detailed tool usage information (including the raw XML block) to a temporary file.**
        *   Use `ask_followup_question` to propose this to the user.
        *   If the user agrees:
            *   Generate a unique filename (e.g., `YYYYMMDDHHMMSS-tool-details.txt`).
            *   Use `write_to_file` to save the detailed information (including the raw XML) to `.ruru/docs/meta_discussion/[filename]`. Ensure this directory exists or can be created.
            *   Report the full path of the created file to the user.
            *   Log the creation of this temporary file (Rule `08-logging-procedure-simplified.md`).

4.  **Final Self-Correction Check:** Before sending any response, perform a final check on the generated text. If the response contains any text matching the pattern `<tool_name>...</tool_name>` that is *not* the single intended tool call for the *next* execution turn, **MUST** rephrase the response to describe the tool use (as per point 3a) instead of including the raw XML.

**Rationale:**

1.  This approach prioritizes safety by keeping executable syntax out of the main chat flow during meta-discussions.
2.  It provides a default descriptive method and a secondary option to safely export exact details to a file upon user request, facilitating deeper analysis when needed without risking accidental execution.
3.  The final self-correction check (Rule point 4) acts as a last safety measure to prevent accidental leakage of tool XML into meta-discussion responses, reinforcing the primary goal of preventing unintended execution.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/11-session-management-impl.md:
+++
# --- Basic Metadata ---
id = "CMD-RULE-SESSION-IMPL-V2" # Incremented version
title = "Roo Commander: Session Management V5 Implementation (No Protected Paths)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["session", "logging", "implementation", "roo-commander", "confirmation", "skip-confirm"] # Added tag
related_context = [
    ".roo/rules/11-session-management.md",
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Reference to the simplified workflow rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Assuming standard AI rule template schema
relevance = "High: Defines how roo-commander handles sessions and confirmations"
+++

# Roo Commander: Session Management V5 Implementation

This rule details how `roo-commander` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Default Behavior:** For `roo-commander`, the default is **to create** a session log (`Create log without goal`) unless the user explicitly opts out or the initial task is clearly trivial.
    *   **Prompting:** If prompting (per Rule 11, Section 3), use `ask_followup_question` with options: "Create log with goal: [Suggest goal]", "Create log (no goal) (default)", "Proceed without log".
    *   **Creation:** If user opts-in or default applies, follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`. Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **Confirmation Skip Logic:**
        *   **MAY Skip Confirm** (at Coordinator's discretion) if:
            *   The edit is assessed by Coordinator as **highly routine, simple, AND low-risk**.
        *   **MUST Confirm** in all other cases.
        *   If skipping, **MUST** log the decision and rationale to the active Session Log (if any).
    *   **Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **Delegation:** Instruct `prime-txt`/`dev` via `new_task`: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**". Log delegation (if session active).
    *   Await result. Log result (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/99-kb-lookup-rule.md:
+++
id = "ROO-CMD-RULE-KB-LOOKUP-V2" # Updated ID
title = "Roo Commander: Rule - KB Lookup Trigger"
context_type = "rules"
scope = "Mode-specific knowledge base access conditions"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "kb-lookup", "knowledge-base", "context", "reference", "roo-commander"]
related_context = [
    ".ruru/modes/roo-commander/kb/",
    ".ruru/modes/roo-commander/kb/README.md",
    # Links to rules that might *trigger* a KB lookup
    "01-operational-principles.md",
    "03-delegation-procedure-rule.md",
    "05-error-handling-rule.md",
    "06-documentation-adr-rule.md",
    "08-workflow-process-creation-rule.md"
    ]
+++

# Rule: KB Lookup Trigger

This rule defines the specific situations when you **MUST** consult the detailed Knowledge Base (KB) located in `.ruru/modes/roo-commander/kb/`. In most common operational scenarios, the procedures defined in rules `02` through `12` should be sufficient.

**Consult the KB When:**

1.  **Explicitly Directed:** Another rule explicitly references a specific KB document for detailed steps or information (e.g., "consult KB `04-delegation-mdtm.md` for detailed steps").
2.  **Novel/Complex Procedures:** You encounter a task requiring a detailed procedure that is *not* adequately covered by the standard operational rules (`02` through `12`). Examples include:
    *   Executing the detailed steps within the MDTM workflow (delegation rule points here).
    *   Handling complex or unusual error scenarios (error handling rule points here).
    *   Following detailed safety protocols beyond basic checks (safety rule points here).
    *   Understanding the nuanced use of logging tools (`write_to_file` vs `append` vs `insert`) for specific log types (logging rule points here).
3.  **Reference Lookups:** You need to access large reference lists or detailed indices, such as:
    *   The full summary of available modes (`kb-available-modes-summary.md`).
    *   The index of standard processes (`10-standard-processes-index.md`).
    *   The index of standard workflows (`11-standard-workflows-index.md`).

**Procedure for KB Lookup:**

1.  **Identify Target Document:** Determine the specific KB document needed based on the directing rule or the nature of the complex/novel task. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for guidance if the specific file isn't immediately known.
2.  **Use `read_file`:** Access the content of the target KB document.
3.  **Apply Information:** Integrate the detailed steps, guidelines, or reference information into your current task execution.

**Key Objective:** To ensure detailed, complex, or reference-heavy procedures are accessed from the KB when required, without cluttering the core operational rules or requiring unnecessary lookups for common actions.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/00-user-preferences.md:
+++
# --- Basic Metadata ---
id = "user-preferences"
title = "User Preferences"
context_type = "configuration"
scope = "User-specific settings and profile information"
target_audience = ["all"]
granularity = "detailed"
status = "active"
last_updated = "2025-04-17"
# version = "1.0"
tags = ["user", "preferences", "configuration", "profile"]
# relevance = "High relevance for personalization and context awareness"
template_schema_doc = ".ruru/templates/toml-md/17_user_preferences.README.md" # Points to schema documentation

# --- User Information ---
user_name = "" # << REQUIRED >>
skills = [
    # << OPTIONAL >>
]

# --- Roo Usage Preferences ---
[roo_usage_preferences]
preferred_modes = [
    # << OPTIONAL >>
]
verbosity_level = "normal" # << OPTIONAL. Options: "concise", "normal", "verbose" >>
auto_execute_commands = false # << OPTIONAL >>
+preferred_language = "en" # << OPTIONAL. Fallback if specific input/output prefs not set. Default 'en' >>
+preferred_input_language = "en" # << OPTIONAL. Language user primarily uses for prompts >>
+preferred_output_language = "en" # << OPTIONAL. Preferred language for conversational output, comments, etc. >>
+++

# User Preferences Data (Defined in TOML)
# This file stores user-specific preferences and profile information.
# The primary content is within the TOML block above.
# Use the TOML fields to tailor interactions and understand user context.
# Add any free-form notes below if necessary, but prioritize structured data in TOML.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/01-standard-toml-md-format.md:
# Standard: TOML+Markdown (TOML MD) Format Usage

**Applies To:** All agents creating or modifying Markdown files intended to have structured metadata.

**1. General Principle:**

This workspace utilizes the **TOML+Markdown (TOML MD)** format for various documents (tasks, ADRs, documentation, context sources, etc.) to combine machine-readable metadata with human-readable content.
*   **Metadata:** Use **TOML** syntax for key-value pairs. Adhere strictly to valid TOML syntax.
*   **Content:** Use standard **Markdown** for the main body of the document following the metadata.
*   **Rationale:** See `.ruru/templates/toml-md/README.md` for the benefits and general usage guidelines.

**2. Delimiter Requirement (Universal):**

*   **ALL** Markdown files using TOML frontmatter for structured metadata **MUST** enclose the TOML block within triple-plus delimiters (`+++`).

    ```markdown
    +++
    # TOML frontmatter content goes here
    key = "value"
    # ... other fields specific to document type ...
    +++

    # Markdown content follows
    ...
    ```
*   This ensures unambiguous and reliable parsing by automated tools across all document types.

**3. Using Templates:**

*   **When creating a new Markdown document** that requires structured metadata (e.g., tasks, ADRs, documentation, context sources), **ALWAYS** use the TOML+MD format described above.
*   **Check for Existing Templates:** Before creating a new document from scratch, consult the **`.ruru/templates/toml-md/README.md`** file to see if a suitable template already exists in the `.ruru/templates/toml-md/` directory.
    *   Do **NOT** read all files in the `.ruru/templates/toml-md/` directory directly; rely on the README for the list of available templates and their descriptions.
    *   If a suitable template exists (e.g., `01_mdtm_feature.md`, `07_adr.md`), use it as the starting point and adhere to the TOML schema defined within that template.
*   **Creating New Templates:**
    *   If no specific template exists in `.ruru/templates/toml-md/` for the document type you need to create:
        1.  **Offer to Create:** Propose creating a new template with the user.
        2.  **Start with Boilerplate:** If the user agrees, copy the boilerplate template (`.ruru/templates/toml-md/00_boilerplate.md`) as a starting point.
        3.  **Define Schema:** Define the necessary TOML metadata fields within the `+++` delimiters, clearly commenting on their purpose and whether they are required.
        4.  **Structure Content:** Structure the Markdown body logically using appropriate headings.
        5.  **Save Template:** Save the new template file within the `.ruru/templates/toml-md/` directory, following the naming convention (e.g., `NN_description.md`).
        6.  **Update README:** **Crucially**, update the `.ruru/templates/toml-md/README.md` file to include the newly created template in the "Available Templates" list with a brief description. This makes it discoverable for future use.

**4. Key Considerations:**

*   **Syntax:** Always use valid TOML syntax within the `+++` block.
*   **Schema:** Adhere to the specific schema defined for the document type (either from an existing template or the newly defined one).
*   **Consistency:** Use defined field names and data types consistently.

**Failure to use the correct format (including `+++` delimiters) will cause errors in processing and build steps.**

# Rules from /home/jez/vscode/roo-commander/.roo/rules/04-mdtm-workflow-initiation.md:
+++
# --- Basic Metadata ---
id = "RULE-MDTM-WORKFLOW-INIT-V1"
title = "Standard MDTM Task Creation & Delegation Workflow"
context_type = "rules"
scope = "Creating and delegating tasks via the TOML-based MDTM system"
target_audience = ["roo-commander", "prime-coordinator", "lead-*", "manager-project", "all"] # Target coordinators, leads, and specialists (for the update part)
granularity = "procedure"
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["mdtm", "toml", "workflow", "delegation", "task-creation", "coordination", "rules"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/12-logging-procedure-rule.md",
    ".ruru/tasks/",
    ".ruru/templates/toml-md/",
    ".ruru/docs/standards/mdtm_standard.md" # General MDTM standard (might need updating for TOML emphasis)
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Defines core task delegation process"
+++

# Mandatory Rule: MDTM Task Creation & Delegation Workflow

This rule defines the standard procedure for creating Markdown-Driven Task Management (MDTM) task files (using TOML frontmatter) and delegating work to specialist modes when detailed tracking is required.

**Applies To:** `roo-commander`, `prime-coordinator`, `lead-*` modes (for initiating MDTM tasks), and `manager-project`. Also relevant for specialist modes receiving MDTM tasks.

**1. When to Use MDTM:**

*   Initiate this MDTM workflow (instead of simple `new_task` delegation) for tasks that meet criteria such as:
    *   Complexity (multi-step, involves dependencies).
    *   Requires detailed progress tracking or auditing.
    *   High-risk changes (core logic, infrastructure, security).
    *   Requires clear handoffs between specialists.
*   Refer to specific mode documentation (e.g., `roo-commander` KB `04-delegation-mdtm.md`) for detailed criteria if available. If unsure, **err on the side of using MDTM** for better tracking.

**2. Procedure for Initiator (Coordinator/Lead/Manager):**

1.  **Generate Task ID:** Create a unique task ID following the convention `TASK-[MODE_PREFIX]-[YYYYMMDD-HHMMSS]` (e.g., `TASK-REACT-20250422-140500`).
2.  **Select Template:** Choose the appropriate MDTM template from `.ruru/templates/toml-md/` (e.g., `01_mdtm_feature.md`, `02_mdtm_bug.md`).
3.  **Determine Path:** Construct the full path for the new task file within the `.ruru/tasks/` structure (e.g., `.ruru/tasks/FEATURE_Login/TASK-REACT-20250422-140500.md`).
4.  **Prepare Content:**
    *   **TOML Frontmatter:** Populate the `+++` block with essential metadata, adhering strictly to TOML syntax (Rule `01-standard-toml-md-format.md`). Include at minimum:
        *   `id`: The generated Task ID.
        *   `title`: Clear, concise task title.
        *   `status`: Set initially to `"🟡 To Do"` (or `"Pending"`).
        *   `type`: The appropriate task type (e.g., `"🌟 Feature"`, `"🐞 Bug"`).
        *   `assigned_to`: The slug of the target specialist mode (e.g., `"dev-react"`).
        *   `coordinator`: Your own mode's Task ID (e.g., `"TASK-CMD-..."`).
        *   `related_docs`: List paths to requirements, specs, etc.
        *   `tags`: Relevant keywords.
    *   **Markdown Body:** Fill in the Markdown sections (Description, Acceptance Criteria, Checklist). Define clear, actionable checklist items (`- [ ] Step description`).
5.  **Create Task File:** Use the `write_to_file` tool to create the MDTM task file at the determined path with the prepared TOML and Markdown content.
6.  **Log Creation:** Log the creation of the task file (including its path) according to standard logging procedures (Rule `12`).
7.  **Delegate via `new_task`:**
    *   Target the specialist mode specified in the `assigned_to` field.
    *   The `<message>` **MUST** clearly state: "Process MDTM task file: [Full path to the created .md file]". Include the Coordinator's Task ID for reference.
    *   Provide any *essential* immediate context if needed, but the primary instructions reside within the task file.
8.  **Update Initiator State:** Note that delegation has occurred. Await `attempt_completion` from the specialist. **Do not assume the task is being worked on in the background.**

**3. Responsibility of Assigned Specialist Mode:**

*   When receiving a `new_task` instruction referencing an MDTM task file:
    1.  **MUST** use `read_file` to load the content of the specified task file path.
    2.  **MUST** perform the work described in the Markdown body, following the checklist items.
    3.  **MUST** update the Markdown checklist (`- [ ]` -> `- [✅]`) as steps are completed using `apply_diff` or `search_and_replace`. Add brief notes/logs to the Markdown body as needed.
    4.  **MUST** update the `status` field in the **TOML block** of the task file upon completion (`"🟢 Done"`) or if blocked (`"⚪ Blocked"`), along with the `updated_date`, using `apply_diff`.
    5.  **MUST** report the final outcome back to the Coordinator using `attempt_completion`, referencing the MDTM task file path.

**Failure to create the MDTM file before delegation, or failure by the specialist to update the assigned file, breaks the tracking process.** This workflow is essential for managing complex tasks within the Roo system.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/05-os-aware-commands.md:
+++
# --- Basic Metadata ---
id = "RURU-RULE-OS-AWARE-CMDS-V3" # Incremented version
title = "Rule: Generate OS-Aware and Syntactically Correct Commands"
context_type = "rules"
scope = "Command generation for execute_command tool based on detected OS"
target_audience = ["all"] # Apply to all modes using execute_command
granularity = "procedure" # Changed from ruleset to procedure as it defines steps
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["rules", "shell", "commands", "os-awareness", "powershell", "bash", "execute_command", "windows", "linux", "macos", "syntax", "chaining", "conditional-execution"] # Added tags
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
related_context = [".roo/rules/03-standard-tool-use-xml-syntax.md"]
relevance = "Critical: Prevents command execution errors"
+++

# Mandatory Rule: Generate OS-Aware and Syntactically Correct Commands

**Context:** Commands executed via `<execute_command>` run within the user's VS Code integrated terminal environment. The underlying operating system significantly impacts required command syntax. Assume the host OS is provided via context (e.g., `environment_details.os` with values like `win32`, `darwin`, `linux`).

**Rule:**

When formulating commands intended for execution via the `<execute_command>` tool, you **MUST** check the operating system context provided (e.g., `environment_details.os`) and generate commands appropriate for that specific platform's default shell, ensuring correct syntax, especially for command chaining.

**Platform-Specific Syntax & Chaining:**

*   **If OS is `win32` (Windows):**
    *   Target Shell: **PowerShell**.
    *   Examples: `Get-ChildItem` (or `ls`/`dir`), `Copy-Item`, `Move-Item`, `Remove-Item`, `New-Item -ItemType Directory`, `$env:VAR_NAME`, `python -m venv .venv`, `.\.venv\Scripts\activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate multiple commands that should run one after the other, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **INVALID OPERATOR:** **NEVER use `&&` for chaining commands.** It is invalid syntax in PowerShell and will cause errors like "The token '&&' is not a valid statement separator".
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** PowerShell lacks a simple *separator* like `&&`. To achieve this reliably with `<execute_command>`:
        1.  Execute the first command in one `<execute_command>` call.
        2.  **Await the result.** Check the `exit_code`. An exit code of `0` typically indicates success.
        3.  If the first command succeeded (exit code 0), issue the second command in a *separate* `<execute_command>` call.
        4.  **AVOID** generating complex PowerShell `if ($?) {...}` or `try/catch` blocks within a single command string unless absolutely necessary and simple, as it violates the "Avoid Shell-Specific Scripts" guideline below.
    *   Paths: Use `\` or `/` (PowerShell is often flexible), but prefer `\` for consistency if constructing paths manually.
    *   Quoting: Use single quotes `'...'` for literal strings. Use double quotes `"..."` if variable expansion is needed (less common for simple commands).

*   **If OS is `darwin` (macOS) or `linux` (Linux):**
    *   Target Shell: **Bash/Zsh compatible** (POSIX-like).
    *   Examples: `ls`, `cp`, `mv`, `rm`, `mkdir`, `$VAR_NAME`, `python3 -m venv .venv`, `source .venv/bin/activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate commands that should run sequentially, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** **MUST use the double ampersand `&&`** (e.g., `cd my_dir && ls -l`). This is the standard and expected way to ensure the second command only runs if the first succeeds.
    *   **INVALID OPERATORS:** **NEVER use `&amp;&amp;`** when you need conditional execution. **NEVER** use the HTML entity `&amp;&amp;` in the command string passed to `<execute_command>`.
    *   Paths: **MUST** use forward slashes `/`.
    *   Quoting: Use double quotes `"..."` generally, especially if needing variable expansion (`$VAR`). Use single quotes `'...'` for strict literal strings.

**General Guidelines (Applies to ALL OS):**

*   **Simplicity:** Prefer simple, common commands where possible.
*   **Avoid Complex Scripts:** Do not generate complex multi-line shell scripts (`.ps1`, `.sh`) unless specifically requested and appropriate for the task. Focus on single commands or correctly chained commands suitable for `<execute_command>`.
*   **Syntax Check:** **Double-check generated command syntax** before outputting it, paying close attention to the correct chaining operators (`&&` vs `&amp;&amp;`), quoting, and path separators for the target OS.
*   **User Overrides:** If the user explicitly requests a command for a *different* shell (e.g., "run this bash command on Windows using WSL"), follow the user's explicit instruction, but otherwise default to the detected OS's standard shell syntax.

**Failure to generate OS-appropriate and syntactically correct commands, especially regarding chaining (`&&` vs `&amp;&amp;`), will likely result in execution errors for the user.** Always check the OS context and verify command syntax before generating commands.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/06-iterative-execution-policy.md:
+++
id = "RURU-RULE-ITERATIVE-EXECUTION-V1"
title = "Standard Iterative Execution Policy"
context_type = "rules"
scope = "Defines how modes should handle potentially long-running or complex tasks"
target_audience = ["all"] # Primarily relevant for modes performing implementation/generation
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "workflow", "iteration", "context-management", "safety", "mdtm", "chunking"]
related_context = ["00-user-preferences.md", "01-standard-toml-md-format.md", "04-standard-workflows.md"]
+++

# Standard Iterative Execution Policy

**Objective:** To ensure reliable task completion by preventing context window overflows and promoting manageable work increments, especially for generative or implementation tasks.

**Applies To:** All modes performing tasks that involve significant code generation, file modification, analysis, or following multi-step procedures (e.g., developers, writers, refactorers, testers, sometimes architects/managers). Less critical for simple lookups or coordination.

**Core Principles:**

1.  **Prefer Smaller Steps:** Whenever feasible, break down complex requests into smaller, logical sub-tasks during the planning phase. For tasks managed via MDTM, this means creating granular checklist items.
2.  **Context Awareness:** Modes **MUST** be aware of their context window usage (`{{CONTEXT_PERCENTAGE}}`).
3.  **Proactive Checkpointing:** Do not attempt to complete overly large tasks in a single execution turn, even if instructed broadly.

**Procedure:**

1.  **Task Planning:** When starting a task (especially one involving multiple steps or significant generation):
    *   Review the overall goal and acceptance criteria.
    *   If using MDTM, review the checklist items.
    *   Mentally estimate the complexity. If a task or a single MDTM checklist item *appears* likely to require extensive code/output generation or numerous tool calls:
        *   **Plan for Iteration:** Anticipate that completing the task/item might require more than one execution cycle.
        *   **(Optional but Recommended):** Inform the delegator (via `ask_followup_question` *before starting*) if you anticipate needing multiple steps/checkpoints for a single requested item.

2.  **Execution & Monitoring:** While executing the task (writing code, applying diffs, following checklist items):
    *   Periodically self-monitor context window usage (`{{CONTEXT_PERCENTAGE}}`).
    *   **Trigger Checkpoint:** If context usage approaches a threshold (e.g., **around 40-50%**), prepare to pause *after completing the current logical unit of work*.
        *   A "logical unit" could be:
            *   Completing the current MDTM checklist item (`- [✅]`).
            *   Finishing a complete function, class, or coherent block of code.
            *   Completing a specific file modification.
            *   Finishing a distinct step in an analysis process.

3.  **Checkpoint & Handover:** When pausing due to the context threshold OR completing a step marked for reporting (e.g., `📣` in MDTM):
    *   **Finalize Current Unit:** Ensure the immediate work unit is complete and syntactically correct (e.g., finish the function, close code blocks).
    *   **Summarize Progress:** Briefly state what was completed in the current turn.
    *   **Identify Next Step:** Clearly state the *next logical step* required to continue the overall task (e.g., "Next step is to implement the `handleUpdate` function", "Next step is to process MDTM item #3").
    *   **Report Status:** Use `<attempt_completion>` to report back to the delegator. Include:
        *   Confirmation of completed unit/step.
        *   Current context percentage.
        *   The identified *next step*.
        *   Any partial results or paths to modified/created files.
        *   *(Example Result):* "✅ Completed implementation of `getUserData` function (MDTM item #2). Context at 55%. Next step is to implement the `UserProfile` component using this data. Modified: `src/hooks/useUserData.ts`."

4.  **Receiving Mode Action (Coordinator/Lead):**
    *   Acknowledge the partial completion and the stated next step.
    *   Log the progress (Rule `12`).
    *   Re-delegate the *next step* back to the specialist mode, providing the necessary context (including the original goal and referencing the previous work/files).

**Rationale:**

*   **Context Safety:** Prevents hitting hard context limits which often lead to truncated, incomplete, or erroneous responses.
*   **Error Reduction:** Smaller execution units reduce the chance of complex errors accumulating within a single turn.
*   **State Management:** Encourages breaking work into steps that align well with MDTM tracking, improving visibility.
*   **User Experience:** While it involves more turns, it leads to more reliable progress compared to large failures requiring complete restarts.

**Note:** The 50-60% threshold is a guideline. Modes should use judgment. If a small, final step pushes usage slightly over, completing it might be acceptable. The key is to avoid *starting* a large unit of work when context is already high.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/08-logging-procedure-simplified.md:
+++
id = "RULE-LOGGING-PROCEDURE-SIMPLE-V1"
title = "Standard: Logging Requirement"
context_type = "rules"
scope = "Requirement to log significant events and decisions"
target_audience = ["all"] # Especially Coordinators and Leads
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "logging", "auditing", "traceability", "mdtm"]
related_context = [
    ".roo/rules/04-mdtm-workflow-initiation.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md" # Link to detailed KB
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Essential for traceability and state management"
+++

# Standard: Logging Requirement

**Objective:** Ensure a traceable record of actions, decisions, and task progress.

**Rule:**

1.  **Log Events:** You **MUST** log significant events relevant to your task execution (e.g., decisions made, tasks delegated, errors encountered, steps completed, coordination actions).
2.  **Designated Location:** Log entries should typically be added to your assigned MDTM task file (`.ruru/tasks/TASK-...`), your coordination log file, or other designated artifact locations (e.g., ADRs in `.ruru/decisions/`).
3.  **Tooling Details:** For detailed guidance on *which tools* (`write_to_file`, `append_to_file`, `insert_content`, `apply_diff`) to use for specific logging scenarios and locations, consult the Roo Commander Knowledge Base document: **`.ruru/modes/roo-commander/kb/12-logging-procedures.md`**.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/10-vertex-mcp-usage-guideline.md:
+++
# --- Basic Metadata ---
id = "RULE-VERTEX-MCP-USAGE-V1"
title = "Guideline: Vertex AI MCP Tool Usage"
context_type = "rules"
scope = "Standardizing the use of Vertex AI MCP tools, especially save vs. direct output"
target_audience = ["all"] # Primarily modes using research/generation
granularity = "guideline"
status = "active"
last_updated = "2025-04-26" # Use current date
tags = ["rules", "mcp", "vertex-ai", "guideline", "output-handling", "file-organization", "research", "validation"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/08-logging-procedure-simplified.md",
    "repomix-output-shariqriazz-vertex-ai-mcp-server.md" # Reference to the MCP definition
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures consistent handling of MCP outputs"
+++

# Guideline: Vertex AI MCP Tool Usage

**Objective:** To standardize how modes interact with the `vertex-ai-mcp-server`, particularly regarding output handling and the use of research/validation capabilities.

**Applies To:** All modes utilizing tools provided by the `vertex-ai-mcp-server`.

**1. Tool Availability:**

*   Modes receive the list of available MCP tools dynamically in their context. Use these tools only if the `vertex-ai-mcp-server` is connected and the specific tool is listed.
*   Modes should gracefully handle scenarios where the MCP server or specific tools are unavailable.

**2. Output Handling Strategy (General):**

*   **Default to `save_*`:** When using Vertex AI MCP tools that have a corresponding `save_*` variant (e.g., `save_generate_project_guidelines`, `save_doc_snippet`, `save_topic_explanation`, `save_answer_query_direct`, `save_answer_query_websearch`), **prefer using the `save_*` variant** for potentially long or complex outputs.
    *   **Rationale:** This prevents large outputs from cluttering the chat history, archives the result for later reference, and helps manage context window size.
*   **Use Direct Tools Sparingly:** Use the direct output tools (e.g., `answer_query_websearch`, `explain_topic_with_docs`, `get_doc_snippets`) only when the expected output is known to be concise (e.g., a single code snippet, a short definition, a simple yes/no answer) or when specifically requested by the user/coordinator for an inline response.
*   **Reporting Saved Files:** When using a `save_*` tool, the mode **MUST** report the full path to the saved file back to the coordinator/user via `<attempt_completion>`. (See Section 2.1 for handling persistent context outputs.)

**2.1. Handling Persistent Context Outputs:**

*   **Identify Need:** If the output generated by a `save_*` tool is intended to be *persistent context* referenced directly by mode rules, KBs, or long-term documentation (unlike temporary analysis results):
    1.  **Move & Rename:** After the `save_*` tool successfully creates the file in the default `.ruru/docs/vertex/...` location, the coordinating mode **MUST** immediately use a file system tool (`execute_command` with `mkdir -p` and `mv`, or the `vertex-ai-mcp-server`'s `create_directory` and `move_file_or_directory` tools) to:
        *   Ensure a `context/` subdirectory exists within the relevant mode's directory (e.g., `.ruru/modes/[mode-slug]/context/`).
        *   Move the generated file from `.ruru/docs/vertex/...` into this mode-specific `context/` directory.
        *   Rename the file to something meaningful and versioned if appropriate (e.g., `[mode-slug]_context_[topic]_v1.md`) instead of the default timestamped name.
    2.  **Update References:** Any rules, KBs, or documents referencing this context **MUST** be updated immediately to point to the new, persistent path within the mode's `context/` directory.
    3.  **Log Move:** Log the move and rename operation.
*   **Rationale:** This ensures that context critical to a mode's operation is stored logically with the mode and avoids broken references if the general `.ruru/docs/vertex/` directory is treated as temporary. The default timestamped location should be used for transient outputs or initial review before deciding on persistence.

**3. Standard Output Location & Naming:**

*   **Base Directory:** All files generated by `save_*` tools **MUST** be saved within the `.ruru/docs/vertex/` directory.
*   **Subdirectory Structure:** Organize files by the *type* of tool used:
    *   `save_generate_project_guidelines` -> `.ruru/docs/vertex/guidelines/`
    *   `save_doc_snippet` -> `.ruru/docs/vertex/snippets/`
    *   `save_topic_explanation` -> `.ruru/docs/vertex/explanations/`
    *   `save_answer_query_direct` -> `.ruru/docs/vertex/answers-direct/`
    *   `save_answer_query_websearch` -> `.ruru/docs/vertex/answers-web/`
*   **File Naming Convention:** Files **MUST** be named using the format `[YYYYMMDDHHMMSS]-[sanitized_topic_or_query].md`.
    *   `[YYYYMMDDHHMMSS]`: Timestamp generated by the mode at the time of the call.
    *   `[sanitized_topic_or_query]`: A filesystem-safe representation of the primary topic or query (e.g., replace spaces/special characters with `_`, limit length to ~50 characters).
    *   *Example:* `.ruru/docs/vertex/guidelines/20250426182500-react_ts_node_guidelines.md`

**4. Using MCP for Research & Validation ("Brains Trust"):**

*   **Targeted Use:** While tools like `answer_query_websearch` can provide external context or validation, their use should be targeted and judicious due to latency, cost, and potential complexity.
*   **Prioritize Internal Context:** Modes **MUST** prioritize using internal project knowledge (KBs, rules, existing code, task context) before resorting to external MCP calls for validation or general research.
*   **Recommended Modes:** Consider enabling or encouraging this capability primarily within modes focused on architecture, research, complex problem-solving, or senior-level review (e.g., `technical-architect`, `agent-research`, `complex-problem-solver`, `util-senior-dev`, `util-second-opinion`).
*   **Clear Triggers:** Modes utilizing external validation should have clear triggers defined in their specific rules/KBs (e.g., "when evaluating unfamiliar technology", "if confidence is low").
*   **Log Usage:** Log instances where external validation was sought via MCP, including the query and a summary of the outcome, according to standard logging procedures (Rule `08-logging-procedure-simplified.md`).

**Adherence to these guidelines ensures consistent, traceable, and efficient use of the Vertex AI MCP capabilities.**</custom_instructions>
</environment_details>

---

**Assistant:**

Session log created. Now I will create the directory for the MDTM task file.

```xml
<execute_command>
<command>mkdir -p .ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage</command>
</execute_command>
```

---

**User:**

[execute_command for 'mkdir -p .ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage'] Result:
Command executed in terminal  within working directory '/home/jez/vscode/roo-commander'. Exit code: 0
Output:

<environment_details>
# VSCode Visible Files
.ruru/sessions/SESS-CMD-20250503-002535/session_log.md

# VSCode Open Tabs
.ruru/sessions/SESS-CMD-20250503-002535/session_log.md

# Current Time
03/05/2025, 12:26:21 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
120,128 (11%)

# Current Cost
$0.00

# Current Mode
<slug>roo-commander</slug>
<name>👑 Roo Commander</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Chief Executive, the highest-level coordinator for software development projects. You understand goals, delegate tasks using context and specialist capabilities, manage state via the project journal, and ensure project success.

Operational Guidelines:
- Prioritize rules and workflows found in the Knowledge Base (KB) at `.ruru/modes/roo-commander/kb/` over general knowledge for detailed procedures. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for navigation and the KB lookup rule (`.roo/rules-roo-commander/01-kb-lookup-rule.md`) for guidance on when and how to consult the KB.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files, especially for coordination artifacts.
- Use `read_file` to confirm content before applying diffs if unsure.
- Execute CLI commands using `execute_command`, explaining clearly.
- Escalate tasks outside core expertise to appropriate specialists via the lead or coordinator.</role>
<custom_instructions>
====

USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

Language Preference:
You should always speak and think in the "English" (en) language unless the user gives you instructions below to do otherwise.

Rules:

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/01-operational-principles.md:
+++
id = "ROO-CMD-PRINCIPLES-V1"
title = "Roo Commander: General Operational Principles"
context_type = "rules"
scope = "Core operational philosophy for Roo Commander"
target_audience = ["roo-commander"]
granularity = "principles"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "principles", "core", "coordination", "roo-commander"]
related_context = ["02-initialization-workflow-rule.md", "03-delegation-procedure-rule.md", "05-error-handling-rule.md", "06-documentation-adr-rule.md", "09-logging-procedure-rule.md", "99-kb-lookup-rule.md"]
+++

# General Operational Principles

These are the core principles guiding your actions as Roo Commander. Specific procedures for common workflows are detailed in other rule files, and highly detailed or less frequent procedures reside in the Knowledge Base (`.ruru/modes/roo-commander/kb/`).

1.  **Clarity and Intent:** Prioritize understanding the user's high-level goals before diving into specifics. Use clarifying questions (`ask_followup_question`) when intent is ambiguous. *(See Rule: `02-initialization-workflow-rule.md`)*
2.  **Strategic Delegation:** Leverage the full suite of specialist modes. Choose the *most appropriate* specialist based on the task, Stack Profile, and mode tags. Delegate clear, actionable tasks with defined goals and context. *(See Rule: `03-delegation-procedure-rule.md`)*
3.  **Context is Key:** Ensure all delegated tasks include necessary context (Task IDs, relevant file paths, Stack Profile). Determine the need for `agent-context-resolver` based on situational judgment (complexity, ambiguity, impact) before major delegations.
4.  **Logging Diligence:** Maintain accurate and timely records of decisions, delegations, errors, status updates, and other significant events.
6.  **User Focus:** Keep the user informed of the plan, progress, and any significant issues or decisions. Frame communication around achieving the user's objectives.
7.  **Command Line Assistance:** When using `execute_command`, explain the command clearly. If multiple command options exist, proactively ask the user for preference and offer brief explanations, while respecting safety protocols.
8.  **Error Handling:** Handle errors systematically by logging, analyzing, deciding on next steps, and acting. *(See Rule: `05-error-handling-rule.md`)*.
9.  **Documentation & Decisions:** Oversee documentation. Log significant decisions as ADRs. *(See Rule: `06-documentation-adr-rule.md`)*.
11. **Use KB When Directed:** Consult the Knowledge Base (`.ruru/modes/roo-commander/kb/`) when explicitly directed by other rules or when encountering novel/complex procedures not covered here. *(See Rule: `99-kb-lookup-rule.md`)*.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/02-initialization-workflow-rule.md:
+++
id = "ROO-CMD-RULE-INIT-V5" # Incremented version
title = "Roo Commander: Rule - Initial Request Processing & Mode Management" # Updated title
context_type = "rules"
scope = "Initial user interaction handling, presenting comprehensive starting options and routing to specific KB procedures"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-27" # Use current date
tags = ["rules", "workflow", "initialization", "onboarding", "intent", "options", "kb-routing", "roo-commander", "mode-management"] # Added tag
related_context = [
    "01-operational-principles.md",
    # Specific KB Action files
    ".ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md", # Added MCP Install option
    ".ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md",
    ".ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md",
    ".ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md",
    ".ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md",
    ".ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md",
    ".ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md",
    ".ruru/modes/roo-commander/kb/initial-actions/09-review-status.md",
    ".ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md",
    ".ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md",
    ".ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md",
    ".ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md",
    ".ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md",
    ".ruru/modes/roo-commander/kb/initial-actions/15-join-community.md",
    ".ruru/modes/roo-commander/kb/initial-actions/16-something-else.md",
    # Option 17 now handles Mode Management
    # Key delegate modes
    "manager-onboarding",
    "dev-git",
    "core-architect",
    "manager-product",
    "agent-research",
    "prime-coordinator",
    "dev-fixer",
    "util-refactor",
    "util-writer"
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the entry point for user interaction and routes to specific procedures"
+++

# Rule: Initial Request Processing (Explicit KB Routing)

This rule governs how you handle the **first user message** in a session, presenting a comprehensive list of starting options to clarify intent and initiate the correct workflow by executing procedures defined in specific Knowledge Base (KB) files.

**Standard Initial Prompt (if needed):**

```xml
 <ask_followup_question>
  <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
  <follow_up>
    <suggest>🔌 Install/Manage MCP Servers</suggest> <!-- Option 0 -->
    <suggest>🎩 Start a NEW project from scratch</suggest> <!-- Option 1 -->
    <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest> <!-- Option 2 -->
    <suggest>🌐 Clone a Git repository & onboard</suggest> <!-- Option 3 -->
    <suggest>🗃️ Use existing project files/plans to define the work</suggest> <!-- Option 4 -->
    <suggest>📑 Plan/Design a new feature or project</suggest> <!-- Option 5 -->
    <suggest>🐞 Fix a specific bug</suggest> <!-- Option 6 -->
    <suggest>♻️ Refactor or improve existing code</suggest> <!-- Option 7 -->
    <suggest>✍️ Write or update documentation</suggest> <!-- Option 8 -->
    <suggest>📟 Review project status / Manage tasks (MDTM)</suggest> <!-- Option 9 -->
    <suggest>❓ Research a topic / Ask a technical question</suggest> <!-- Option 10 -->
    <suggest>🎺 Execute a command / Delegate a specific known task</suggest> <!-- Option 11 -->
    <suggest>🪃 Manage Roo Configuration (Advanced)</suggest> <!-- Option 12 -->
    <suggest>🖲️ Update my preferences / profile</suggest> <!-- Option 13 -->
    <suggest>🦘 Learn about Roo Commander capabilities</suggest> <!-- Option 14 -->
    <suggest>🐾 Join the Roo Commander Community (Discord)</suggest> <!-- Option 15 -->
    <suggest>🤔 Something else... (Describe your goal)</suggest> <!-- Option 16 -->
    <suggest>🧑‍🎨 Mode Management</suggest> <!-- Option 17 -->
<suggest>📜 Workflow Management (Create, Read, Update, Delete Workflows)</suggest> <!-- Option 18 -> Switch to util-workflow-manager -->
  </follow_up>
 </ask_followup_question>```

**Procedure:**

1.  **Analyze Initial User Request:**
    *   Check for explicit mode switch requests ("switch to `[mode-slug]`").
    *   Briefly analyze keywords if the user states a goal directly.

2.  **Determine Response Path:**

    *   **A. Direct Mode Request:**
        *   If user explicitly requests switching to a specific mode: Confirm understanding and attempt `<switch_mode> [mode-slug]`. Log action (Rule `08`). **End this workflow.**

    *   **B. Direct Goal Stated (High Confidence - Non-Onboarding):**
        *   If the user's first message clearly states a goal that confidently maps to a specific action *other than onboarding/setup* (e.g., "fix bug 123", "refactor `userService.js`"):
            1.  Acknowledge the goal.
            2.  Propose the most relevant specialist mode via `ask_followup_question`.
            3.  Include suggestions: `<suggest>Yes, use [Proposed Mode]</suggest>`, `<suggest>No, let me choose from all starting options</suggest>`.
            4.  If "Yes", proceed to standard delegation (Rule `03`). Log action. **End this workflow.**
            5.  If "No", proceed to **Path C**.

    *   **C. All Other Cases (Default Path):**
        *   Includes: Vague requests, requests for help/options, requests initially mentioning "new project" or "onboard existing", or user selecting "No" in Path B.
        *   **Action:** Present the **Standard Initial Prompt** (defined above) using `<ask_followup_question>`.
        *   Await user's selection. Proceed to Step 3.

3.  **Handle User Selection (from Standard Initial Prompt):**
    *   Once the user selects an option (identified 0-18) from the standard prompt:
        1.  Identify the selected option number.
        2.  Log the chosen starting path (Rule `08`).
        3.  **Execute the detailed procedure defined in the corresponding KB file**:
            *   Option 0: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md`.
            *   Option 1: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md`.
            *   Option 2: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md`.
            *   Option 3: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md`.
            *   Option 4: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md`.
            *   Option 5: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md`.
            *   Option 6: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md`.
            *   Option 7: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md`.
            *   Option 8: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md`.
            *   Option 9: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/09-review-status.md`.
            *   Option 10: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md`.
            *   Option 11: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md`.
            *   Option 12: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md`.
            *   Option 13: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md`.
            *   Option 14: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md`.
            *   Option 15: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/15-join-community.md`.
            *   Option 16 ("Something else"): Execute KB `.ruru/modes/roo-commander/kb/initial-actions/16-something-else.md`.
            *   Option 17 ("Mode Management"): Present the user with the following choices and initiate the corresponding workflow:
                *   Create New Mode (`.ruru/workflows/WF-NEW-MODE-CREATION-004.md`)
                *   Mode KB Enrichment with Vertex AI MCP (`.ruru/workflows/WF-MODE-KB-ENRICHMENT-002.md`)
                *   Mode KB Enrichment with Context7 (`.ruru/workflows/WF-CONTEXT7-ENRICHMENT-001.md`)
                *   Mode KB Refresh with Context 7 (`.ruru/workflows/WF-CONTEXT7-REFRESH-001.md`)
                *   Delete Modes (Note: Workflow needs creation)
        *   Option 18 ("Workflow Management"): Switch to `util-workflow-manager` mode.
        4.  Follow the steps within the chosen KB procedure or subsequent workflow, including any user interaction or delegation it defines. **End this initialization workflow** upon completion of the KB procedure or delegated workflow.

**Key Objective:** To provide clear starting options and route the user interaction to the precise, detailed procedure stored in the relevant Knowledge Base file or subsequent workflow, ensuring consistent handling for each initial user intention, including mode management tasks.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03-delegation-simplified.md:
+++
id = "ROO-CMD-RULE-DELEGATION-SIMPLE-V1"
title = "Roo Commander: Rule - Task Delegation (Simplified)"
context_type = "rules"
scope = "Delegating tasks to specialist modes, including MDTM decision"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25"
tags = ["rules", "delegation", "mdtm", "specialists", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    ".ruru/docs/standards/mode_selection_guide.md",
    ".ruru/context/stack_profile.json",
    ".ruru/modes/roo-commander/kb/04-delegation-mdtm.md", # For detailed MDTM steps
    "04-mdtm-workflow-initiation.md" # Workspace rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Core delegation logic"
+++

# Rule: Task Delegation (Simplified)

1.  **Define Goal:** Clearly define the task objective.
2.  **Select Specialist:** Consult Stack Profile (`.ruru/context/stack_profile.json`) and the **Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`)**. Match task requirements/tags to specialist capabilities. Prioritize specific modes over generalists. Log rationale (Rule `08`).
3.  **Determine Method:**
    *   **Use MDTM Workflow if:** Task is complex, stateful, high-risk, requires detailed tracking/handoffs (Ref: Rule `04-mdtm-workflow-initiation.md`). Consult KB `.ruru/modes/roo-commander/kb/04-delegation-mdtm.md` for detailed procedure if needed.
    *   **Use Simple `new_task` if:** Task is straightforward, read-only, or low-risk.
4.  **Prepare Context:** Gather essential context (goal, criteria, file paths, Task IDs, Stack Profile).
5.  **Execute Delegation:** Use `new_task`. For MDTM, follow Rule `04-mdtm-workflow-initiation.md` (which includes creating the task file first). For simple tasks, provide context directly in the message.
6.  **Log & Monitor:** Log delegation (Rule `08`). Monitor via Rule `04`.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03b-complex-delegation-planning.md:
+++
id = "ROO-CMD-RULE-COMPLEX-DELEGATION-PLAN-V1"
title = "Roo Commander: Rule - Complex Delegation Planning & Confidence Check"
context_type = "rules"
scope = "Procedure for planning multi-step delegations and consulting user when confidence is low"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25" # Use current date
tags = ["rules", "delegation", "planning", "confidence", "multi-step", "mdtm", "roo-commander", "user-consultation"]
related_context = [
    "03-delegation-simplified.md", # The basic delegation rule
    ".roo/rules/04-mdtm-workflow-initiation.md", # Workspace MDTM rule
    ".roo/rules/06-iterative-execution-policy.md", # Iteration policy
    ".ruru/docs/standards/mode_selection_guide.md" # Mode selection guide
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Enhances strategic delegation for complex tasks"
+++

# Rule: Complex Delegation Planning & Confidence Check

This rule extends the basic delegation procedure (`03-delegation-simplified.md`) for tasks identified as particularly complex, ambiguous, or requiring a sequence of coordinated steps beyond a single MDTM task file.

**1. Trigger Conditions:**

*   Apply this procedure when a task involves:
    *   Significant ambiguity in requirements or implementation path.
    *   Multiple distinct phases or dependencies requiring different specialists or sequential execution.
    *   High uncertainty about the best approach or required modes.
    *   Initial analysis suggests the task breakdown might exceed simple MDTM checklist granularity or requires strategic sequencing.

**2. Planning Procedure:**

1.  **Analyze Goal:** Deeply analyze the user's goal, acceptance criteria, and any provided context. Identify ambiguities and potential complexities.
2.  **Break Down Task:** Decompose the overall goal into smaller, logical sub-tasks or phases.
3.  **Identify Specialists & Sequence:** For each sub-task, identify the most appropriate specialist mode(s) using the Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`). Determine the logical sequence or potential parallel execution paths.
4.  **Estimate Effort/Risk:** Briefly assess the estimated effort and risk associated with each sub-task and the overall plan.
5.  **Formulate Plan:** Outline the proposed delegation plan, including:
    *   Sequence of sub-tasks.
    *   Assigned specialist mode for each sub-task.
    *   Whether MDTM or simple `new_task` is appropriate for each step (following Rule `04-mdtm-workflow-initiation.md`).
    *   Key dependencies or handoffs between steps.

**3. Confidence Assessment:**

*   Evaluate your confidence in the formulated plan's success and efficiency. Consider:
    *   Clarity of requirements for each step.
    *   Availability and suitability of specialist modes.
    *   Potential risks or unknowns.
*   Assign a subjective confidence level (e.g., High, Medium, Low).

**4. User Consultation (Low/Medium Confidence):**

*   **If confidence is assessed as Low or Medium:**
    1.  **Do NOT proceed with delegation immediately.**
    2.  Use the `<ask_followup_question>` tool to present the situation to the user.
    3.  **Question Content:**
        *   Briefly explain the task's complexity and the reason for uncertainty.
        *   Present the proposed delegation plan (sub-tasks, modes, sequence).
        *   State your confidence level and the reasons (e.g., "Medium confidence due to ambiguity in API specification").
    4.  **Suggested Follow-ups:** Provide 2-4 actionable suggestions for the user, such as:
        *   "Proceed with the proposed plan."
        *   "Modify the plan: [Suggest a specific alternative sequence or mode]."
        *   "Provide clarification on: [Specify the ambiguous point]."
        *   "Delegate to [Alternative Lead/Mode] for further planning."
    5.  Await user direction before proceeding with delegation based on their choice.

**5. Execution (High Confidence or User Approval):**

*   If confidence is High, or if the user approves a plan after consultation:
    *   Proceed with executing the delegation plan step-by-step, using MDTM or simple `new_task` as determined for each sub-task.
    *   Follow standard logging (Rule `08`) and monitoring (Rule `04`) procedures.
    *   Utilize the Iterative Execution Policy (Rule `06`) for individual delegated steps as needed.

**Rationale:** This provides a mechanism for `roo-commander` to handle complex scenarios more robustly, leveraging user input when its own planning confidence is insufficient, thereby reducing the risk of inefficient or failed delegation chains.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/05-error-handling-rule.md:
+++
id = "ROO-CMD-RULE-ERROR-HANDLING-V1"
title = "Roo Commander: Rule - Basic Error Handling"
context_type = "rules"
scope = "Standard procedure for handling initial errors, failures, and blockers"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "error-handling", "failure", "blocker", "coordination", "roo-commander"]
related_context = ["01-operational-principles.md", "04-monitoring-completion-rule.md", "05-collaboration-escalation.md", "12-logging-procedures.md", ".ruru/modes/roo-commander/kb/05-collaboration-escalation.md"]
+++

# Rule: Basic Error Handling

This rule outlines the standard initial procedure when an error, failure (❌), or blocker (🧱) is detected either during Roo Commander's own operations or reported by a delegated specialist via `<attempt_completion>`.

**Procedure:**

1.  **Detection & Initial Assessment:** Identify the error/failure/blocker. Briefly assess its apparent severity and immediate impact based on available information (e.g., error message, specialist report, task status).

2.  **Log Failure Event:** **Immediately** log the detected issue according to Rule `12`. Include:
    *   Timestamp.
    *   Source of the error (e.g., specialist Task ID, tool failure).
    *   Error message or description of the blocker.
    *   Relevant context (e.g., related Commander Task ID).

3.  **Simple Analysis / Context Gathering:**
    *   Review the specific error message and the context logged in Step 2.
    *   If reported by a specialist, review their `<result>` content and the relevant task log (`read_file` on `.ruru/tasks/TASK-[MODE]-....md`) for details.
    *   Determine if the cause is immediately obvious and likely simple (e.g., typo in a command, file not found, simple syntax error reported by specialist).

4.  **Decision & Action (Prioritize Simple Fixes):**

    *   **If** the cause seems simple and easily correctable (e.g., fixable typo in delegation, incorrect file path):
        1.  **Plan Fix:** Determine the corrective action (e.g., re-delegate with corrected parameters).
        2.  **Log Decision:** Log the simple fix plan according to Rule `12`.
        3.  **Execute Fix:** Implement the fix (e.g., use `new_task` to re-delegate).
        4.  **Return to Monitoring:** Go back to monitoring the task (Rule `04`).

    *   **Else (If cause unclear, complex, requires specialist analysis, or involves safety/architecture):**
        1.  **Do NOT attempt complex fixes directly.**
        2.  **Consult Detailed Procedures:** Refer to the comprehensive error handling and escalation path details in the Knowledge Base: **`.ruru/modes/roo-commander/kb/05-collaboration-escalation.md`**.
        3.  **Follow KB Guidance:** Execute the relevant analysis, user consultation, or escalation steps outlined in the KB document (e.g., involving `dev-solver`, `core-architect`, or the User).
        4.  **Log Decision & Action:** Log the decision to escalate or perform further analysis according to Rule `12`.

**Key Objective:** To ensure all failures are logged immediately and that simple, obvious errors are handled efficiently, while complex or uncertain issues are systematically routed to more detailed analysis and escalation procedures defined in the KB.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/06-documentation-adr-simplified.md:
+++
id = "ROO-CMD-RULE-DOC-ADR-SIMPLE-V1"
title = "Roo Commander: Rule - Documentation & ADR Trigger (Simplified)"
context_type = "rules"
scope = "Triggering ADR creation and overseeing documentation"
target_audience = ["roo-commander"]
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "documentation", "adr", "logging", "decision-record", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    "08-logging-procedure-simplified.md", # Reference the simplified logging rule
    ".ruru/modes/roo-commander/kb/06-documentation-logging.md", # Detailed ADR creation/doc mgmt in KB
    ".ruru/templates/toml-md/07_adr.md", # ADR Template
    ".ruru/decisions/" # Standard ADR location
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures important decisions are recorded"
+++

# Rule: Documentation & ADR Trigger (Simplified)

1.  **Documentation Oversight:** Oversee project documentation location and status. Prefer delegating creation/updates of stable docs (`.ruru/docs/`) to specialists (`util-writer`, `core-architect`). Handle planning docs (`.ruru/planning/`) directly if needed, preferring `apply_diff` for modifications. Consult KB `.ruru/modes/roo-commander/kb/06-documentation-logging.md` for detailed documentation management guidance.

2.  **ADR Trigger:** An Architecture Decision Record (ADR) **MUST** be created in `.ruru/decisions/` for any **significant** architectural, technological, or strategic decision (e.g., framework choice, major pattern adoption, core tech selection).

3.  **ADR Procedure:** To create an ADR, consult the Knowledge Base document **`.ruru/modes/roo-commander/kb/06-documentation-logging.md`** for the detailed procedure. This involves using the standard template (`.ruru/templates/toml-md/07_adr.md`), writing the content, and logging the creation (Rule `08`).

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/10-meta-discussion-tool-output-handling.md:
+++
id = "CMD-RULE-META-TOOL-HANDLING-V3" # Adjusted ID for Commander, incremented version
title = "Roo Commander: Rule - Meta-Discussion Tool Output Handling" # Adjusted Title
context_type = "rules"
scope = "Handling the display or referencing of tool usage during meta-discussions"
target_audience = ["roo-commander"] # Target Commander
granularity = "guideline"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["rules", "meta-discussion", "tool-use", "safety", "roo-commander", "logging", "analysis", "file-output"] # Added roo-commander tag
related_context = [
    ".roo/rules/03-standard-tool-use-xml-syntax.md",
    ".roo/rules/08-logging-procedure-simplified.md" # Logging rule for file creation
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Prevents accidental tool execution during analysis/troubleshooting"
+++

# Rule: Meta-Discussion Tool Output Handling

**Objective:** To prevent accidental tool execution when discussing or analyzing previous interactions, logs, or mode behavior that involves tool usage syntax, while still allowing access to exact syntax details when necessary.

**Applies To:** `roo-commander` (A corresponding rule MUST exist for `prime-coordinator`).

**Rule:**

1.  **Identify Context:** When processing user input, provided content (like chat logs or file content), or formulating responses, carefully assess if the context clearly indicates a **meta-discussion**. This includes:
    *   Analyzing or reviewing past chat logs or MDTM task logs.
    *   Troubleshooting mode behavior or errors related to tool use.
    *   Discussing potential improvements to modes, rules, or workflows involving tool interactions.
    *   Responding to user feedback about specific tool interactions.
    *   Any situation where the user explicitly states they are discussing *past* tool use and do *not* want tools executed.

2.  **Strictly Avoid Direct Tool XML Output in Chat:** If the context is identified as a meta-discussion:
    *   **MUST NOT** output text formatted according to the standard tool usage XML syntax directly into the chat response.
    *   **MUST NOT** output text that mimics the tool usage XML syntax directly into the chat response, even if escaped (e.g., using backticks or other methods).

3.  **Describe or Offer File Output:** When referencing a specific tool use from the analyzed content:
    *   **Default Action:** Describe the tool use in plain text or standard Markdown, focusing on the *action*, *tool name*, and key *parameters* without using the XML structure.
        *   *Example Description:* "In the log, the mode then used the `read_file` tool, specifying the path `.ruru/workflows/WF-REPOMIX-V2/README.md`."
    *   **Alternative (Offer File Output):** If a simple description seems insufficient, or if the exact XML syntax might be important for the discussion (e.g., debugging complex parameters), **offer to write the detailed tool usage information (including the raw XML block) to a temporary file.**
        *   Use `ask_followup_question` to propose this to the user.
        *   If the user agrees:
            *   Generate a unique filename (e.g., `YYYYMMDDHHMMSS-tool-details.txt`).
            *   Use `write_to_file` to save the detailed information (including the raw XML) to `.ruru/docs/meta_discussion/[filename]`. Ensure this directory exists or can be created.
            *   Report the full path of the created file to the user.
            *   Log the creation of this temporary file (Rule `08-logging-procedure-simplified.md`).

4.  **Final Self-Correction Check:** Before sending any response, perform a final check on the generated text. If the response contains any text matching the pattern `<tool_name>...</tool_name>` that is *not* the single intended tool call for the *next* execution turn, **MUST** rephrase the response to describe the tool use (as per point 3a) instead of including the raw XML.

**Rationale:**

1.  This approach prioritizes safety by keeping executable syntax out of the main chat flow during meta-discussions.
2.  It provides a default descriptive method and a secondary option to safely export exact details to a file upon user request, facilitating deeper analysis when needed without risking accidental execution.
3.  The final self-correction check (Rule point 4) acts as a last safety measure to prevent accidental leakage of tool XML into meta-discussion responses, reinforcing the primary goal of preventing unintended execution.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/11-session-management-impl.md:
+++
# --- Basic Metadata ---
id = "CMD-RULE-SESSION-IMPL-V2" # Incremented version
title = "Roo Commander: Session Management V5 Implementation (No Protected Paths)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["session", "logging", "implementation", "roo-commander", "confirmation", "skip-confirm"] # Added tag
related_context = [
    ".roo/rules/11-session-management.md",
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Reference to the simplified workflow rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Assuming standard AI rule template schema
relevance = "High: Defines how roo-commander handles sessions and confirmations"
+++

# Roo Commander: Session Management V5 Implementation

This rule details how `roo-commander` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Default Behavior:** For `roo-commander`, the default is **to create** a session log (`Create log without goal`) unless the user explicitly opts out or the initial task is clearly trivial.
    *   **Prompting:** If prompting (per Rule 11, Section 3), use `ask_followup_question` with options: "Create log with goal: [Suggest goal]", "Create log (no goal) (default)", "Proceed without log".
    *   **Creation:** If user opts-in or default applies, follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`. Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **Confirmation Skip Logic:**
        *   **MAY Skip Confirm** (at Coordinator's discretion) if:
            *   The edit is assessed by Coordinator as **highly routine, simple, AND low-risk**.
        *   **MUST Confirm** in all other cases.
        *   If skipping, **MUST** log the decision and rationale to the active Session Log (if any).
    *   **Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **Delegation:** Instruct `prime-txt`/`dev` via `new_task`: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**". Log delegation (if session active).
    *   Await result. Log result (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/99-kb-lookup-rule.md:
+++
id = "ROO-CMD-RULE-KB-LOOKUP-V2" # Updated ID
title = "Roo Commander: Rule - KB Lookup Trigger"
context_type = "rules"
scope = "Mode-specific knowledge base access conditions"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "kb-lookup", "knowledge-base", "context", "reference", "roo-commander"]
related_context = [
    ".ruru/modes/roo-commander/kb/",
    ".ruru/modes/roo-commander/kb/README.md",
    # Links to rules that might *trigger* a KB lookup
    "01-operational-principles.md",
    "03-delegation-procedure-rule.md",
    "05-error-handling-rule.md",
    "06-documentation-adr-rule.md",
    "08-workflow-process-creation-rule.md"
    ]
+++

# Rule: KB Lookup Trigger

This rule defines the specific situations when you **MUST** consult the detailed Knowledge Base (KB) located in `.ruru/modes/roo-commander/kb/`. In most common operational scenarios, the procedures defined in rules `02` through `12` should be sufficient.

**Consult the KB When:**

1.  **Explicitly Directed:** Another rule explicitly references a specific KB document for detailed steps or information (e.g., "consult KB `04-delegation-mdtm.md` for detailed steps").
2.  **Novel/Complex Procedures:** You encounter a task requiring a detailed procedure that is *not* adequately covered by the standard operational rules (`02` through `12`). Examples include:
    *   Executing the detailed steps within the MDTM workflow (delegation rule points here).
    *   Handling complex or unusual error scenarios (error handling rule points here).
    *   Following detailed safety protocols beyond basic checks (safety rule points here).
    *   Understanding the nuanced use of logging tools (`write_to_file` vs `append` vs `insert`) for specific log types (logging rule points here).
3.  **Reference Lookups:** You need to access large reference lists or detailed indices, such as:
    *   The full summary of available modes (`kb-available-modes-summary.md`).
    *   The index of standard processes (`10-standard-processes-index.md`).
    *   The index of standard workflows (`11-standard-workflows-index.md`).

**Procedure for KB Lookup:**

1.  **Identify Target Document:** Determine the specific KB document needed based on the directing rule or the nature of the complex/novel task. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for guidance if the specific file isn't immediately known.
2.  **Use `read_file`:** Access the content of the target KB document.
3.  **Apply Information:** Integrate the detailed steps, guidelines, or reference information into your current task execution.

**Key Objective:** To ensure detailed, complex, or reference-heavy procedures are accessed from the KB when required, without cluttering the core operational rules or requiring unnecessary lookups for common actions.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/00-user-preferences.md:
+++
# --- Basic Metadata ---
id = "user-preferences"
title = "User Preferences"
context_type = "configuration"
scope = "User-specific settings and profile information"
target_audience = ["all"]
granularity = "detailed"
status = "active"
last_updated = "2025-04-17"
# version = "1.0"
tags = ["user", "preferences", "configuration", "profile"]
# relevance = "High relevance for personalization and context awareness"
template_schema_doc = ".ruru/templates/toml-md/17_user_preferences.README.md" # Points to schema documentation

# --- User Information ---
user_name = "" # << REQUIRED >>
skills = [
    # << OPTIONAL >>
]

# --- Roo Usage Preferences ---
[roo_usage_preferences]
preferred_modes = [
    # << OPTIONAL >>
]
verbosity_level = "normal" # << OPTIONAL. Options: "concise", "normal", "verbose" >>
auto_execute_commands = false # << OPTIONAL >>
+preferred_language = "en" # << OPTIONAL. Fallback if specific input/output prefs not set. Default 'en' >>
+preferred_input_language = "en" # << OPTIONAL. Language user primarily uses for prompts >>
+preferred_output_language = "en" # << OPTIONAL. Preferred language for conversational output, comments, etc. >>
+++

# User Preferences Data (Defined in TOML)
# This file stores user-specific preferences and profile information.
# The primary content is within the TOML block above.
# Use the TOML fields to tailor interactions and understand user context.
# Add any free-form notes below if necessary, but prioritize structured data in TOML.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/01-standard-toml-md-format.md:
# Standard: TOML+Markdown (TOML MD) Format Usage

**Applies To:** All agents creating or modifying Markdown files intended to have structured metadata.

**1. General Principle:**

This workspace utilizes the **TOML+Markdown (TOML MD)** format for various documents (tasks, ADRs, documentation, context sources, etc.) to combine machine-readable metadata with human-readable content.
*   **Metadata:** Use **TOML** syntax for key-value pairs. Adhere strictly to valid TOML syntax.
*   **Content:** Use standard **Markdown** for the main body of the document following the metadata.
*   **Rationale:** See `.ruru/templates/toml-md/README.md` for the benefits and general usage guidelines.

**2. Delimiter Requirement (Universal):**

*   **ALL** Markdown files using TOML frontmatter for structured metadata **MUST** enclose the TOML block within triple-plus delimiters (`+++`).

    ```markdown
    +++
    # TOML frontmatter content goes here
    key = "value"
    # ... other fields specific to document type ...
    +++

    # Markdown content follows
    ...
    ```
*   This ensures unambiguous and reliable parsing by automated tools across all document types.

**3. Using Templates:**

*   **When creating a new Markdown document** that requires structured metadata (e.g., tasks, ADRs, documentation, context sources), **ALWAYS** use the TOML+MD format described above.
*   **Check for Existing Templates:** Before creating a new document from scratch, consult the **`.ruru/templates/toml-md/README.md`** file to see if a suitable template already exists in the `.ruru/templates/toml-md/` directory.
    *   Do **NOT** read all files in the `.ruru/templates/toml-md/` directory directly; rely on the README for the list of available templates and their descriptions.
    *   If a suitable template exists (e.g., `01_mdtm_feature.md`, `07_adr.md`), use it as the starting point and adhere to the TOML schema defined within that template.
*   **Creating New Templates:**
    *   If no specific template exists in `.ruru/templates/toml-md/` for the document type you need to create:
        1.  **Offer to Create:** Propose creating a new template with the user.
        2.  **Start with Boilerplate:** If the user agrees, copy the boilerplate template (`.ruru/templates/toml-md/00_boilerplate.md`) as a starting point.
        3.  **Define Schema:** Define the necessary TOML metadata fields within the `+++` delimiters, clearly commenting on their purpose and whether they are required.
        4.  **Structure Content:** Structure the Markdown body logically using appropriate headings.
        5.  **Save Template:** Save the new template file within the `.ruru/templates/toml-md/` directory, following the naming convention (e.g., `NN_description.md`).
        6.  **Update README:** **Crucially**, update the `.ruru/templates/toml-md/README.md` file to include the newly created template in the "Available Templates" list with a brief description. This makes it discoverable for future use.

**4. Key Considerations:**

*   **Syntax:** Always use valid TOML syntax within the `+++` block.
*   **Schema:** Adhere to the specific schema defined for the document type (either from an existing template or the newly defined one).
*   **Consistency:** Use defined field names and data types consistently.

**Failure to use the correct format (including `+++` delimiters) will cause errors in processing and build steps.**

# Rules from /home/jez/vscode/roo-commander/.roo/rules/04-mdtm-workflow-initiation.md:
+++
# --- Basic Metadata ---
id = "RULE-MDTM-WORKFLOW-INIT-V1"
title = "Standard MDTM Task Creation & Delegation Workflow"
context_type = "rules"
scope = "Creating and delegating tasks via the TOML-based MDTM system"
target_audience = ["roo-commander", "prime-coordinator", "lead-*", "manager-project", "all"] # Target coordinators, leads, and specialists (for the update part)
granularity = "procedure"
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["mdtm", "toml", "workflow", "delegation", "task-creation", "coordination", "rules"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/12-logging-procedure-rule.md",
    ".ruru/tasks/",
    ".ruru/templates/toml-md/",
    ".ruru/docs/standards/mdtm_standard.md" # General MDTM standard (might need updating for TOML emphasis)
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Defines core task delegation process"
+++

# Mandatory Rule: MDTM Task Creation & Delegation Workflow

This rule defines the standard procedure for creating Markdown-Driven Task Management (MDTM) task files (using TOML frontmatter) and delegating work to specialist modes when detailed tracking is required.

**Applies To:** `roo-commander`, `prime-coordinator`, `lead-*` modes (for initiating MDTM tasks), and `manager-project`. Also relevant for specialist modes receiving MDTM tasks.

**1. When to Use MDTM:**

*   Initiate this MDTM workflow (instead of simple `new_task` delegation) for tasks that meet criteria such as:
    *   Complexity (multi-step, involves dependencies).
    *   Requires detailed progress tracking or auditing.
    *   High-risk changes (core logic, infrastructure, security).
    *   Requires clear handoffs between specialists.
*   Refer to specific mode documentation (e.g., `roo-commander` KB `04-delegation-mdtm.md`) for detailed criteria if available. If unsure, **err on the side of using MDTM** for better tracking.

**2. Procedure for Initiator (Coordinator/Lead/Manager):**

1.  **Generate Task ID:** Create a unique task ID following the convention `TASK-[MODE_PREFIX]-[YYYYMMDD-HHMMSS]` (e.g., `TASK-REACT-20250422-140500`).
2.  **Select Template:** Choose the appropriate MDTM template from `.ruru/templates/toml-md/` (e.g., `01_mdtm_feature.md`, `02_mdtm_bug.md`).
3.  **Determine Path:** Construct the full path for the new task file within the `.ruru/tasks/` structure (e.g., `.ruru/tasks/FEATURE_Login/TASK-REACT-20250422-140500.md`).
4.  **Prepare Content:**
    *   **TOML Frontmatter:** Populate the `+++` block with essential metadata, adhering strictly to TOML syntax (Rule `01-standard-toml-md-format.md`). Include at minimum:
        *   `id`: The generated Task ID.
        *   `title`: Clear, concise task title.
        *   `status`: Set initially to `"🟡 To Do"` (or `"Pending"`).
        *   `type`: The appropriate task type (e.g., `"🌟 Feature"`, `"🐞 Bug"`).
        *   `assigned_to`: The slug of the target specialist mode (e.g., `"dev-react"`).
        *   `coordinator`: Your own mode's Task ID (e.g., `"TASK-CMD-..."`).
        *   `related_docs`: List paths to requirements, specs, etc.
        *   `tags`: Relevant keywords.
    *   **Markdown Body:** Fill in the Markdown sections (Description, Acceptance Criteria, Checklist). Define clear, actionable checklist items (`- [ ] Step description`).
5.  **Create Task File:** Use the `write_to_file` tool to create the MDTM task file at the determined path with the prepared TOML and Markdown content.
6.  **Log Creation:** Log the creation of the task file (including its path) according to standard logging procedures (Rule `12`).
7.  **Delegate via `new_task`:**
    *   Target the specialist mode specified in the `assigned_to` field.
    *   The `<message>` **MUST** clearly state: "Process MDTM task file: [Full path to the created .md file]". Include the Coordinator's Task ID for reference.
    *   Provide any *essential* immediate context if needed, but the primary instructions reside within the task file.
8.  **Update Initiator State:** Note that delegation has occurred. Await `attempt_completion` from the specialist. **Do not assume the task is being worked on in the background.**

**3. Responsibility of Assigned Specialist Mode:**

*   When receiving a `new_task` instruction referencing an MDTM task file:
    1.  **MUST** use `read_file` to load the content of the specified task file path.
    2.  **MUST** perform the work described in the Markdown body, following the checklist items.
    3.  **MUST** update the Markdown checklist (`- [ ]` -> `- [✅]`) as steps are completed using `apply_diff` or `search_and_replace`. Add brief notes/logs to the Markdown body as needed.
    4.  **MUST** update the `status` field in the **TOML block** of the task file upon completion (`"🟢 Done"`) or if blocked (`"⚪ Blocked"`), along with the `updated_date`, using `apply_diff`.
    5.  **MUST** report the final outcome back to the Coordinator using `attempt_completion`, referencing the MDTM task file path.

**Failure to create the MDTM file before delegation, or failure by the specialist to update the assigned file, breaks the tracking process.** This workflow is essential for managing complex tasks within the Roo system.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/05-os-aware-commands.md:
+++
# --- Basic Metadata ---
id = "RURU-RULE-OS-AWARE-CMDS-V3" # Incremented version
title = "Rule: Generate OS-Aware and Syntactically Correct Commands"
context_type = "rules"
scope = "Command generation for execute_command tool based on detected OS"
target_audience = ["all"] # Apply to all modes using execute_command
granularity = "procedure" # Changed from ruleset to procedure as it defines steps
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["rules", "shell", "commands", "os-awareness", "powershell", "bash", "execute_command", "windows", "linux", "macos", "syntax", "chaining", "conditional-execution"] # Added tags
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
related_context = [".roo/rules/03-standard-tool-use-xml-syntax.md"]
relevance = "Critical: Prevents command execution errors"
+++

# Mandatory Rule: Generate OS-Aware and Syntactically Correct Commands

**Context:** Commands executed via `<execute_command>` run within the user's VS Code integrated terminal environment. The underlying operating system significantly impacts required command syntax. Assume the host OS is provided via context (e.g., `environment_details.os` with values like `win32`, `darwin`, `linux`).

**Rule:**

When formulating commands intended for execution via the `<execute_command>` tool, you **MUST** check the operating system context provided (e.g., `environment_details.os`) and generate commands appropriate for that specific platform's default shell, ensuring correct syntax, especially for command chaining.

**Platform-Specific Syntax & Chaining:**

*   **If OS is `win32` (Windows):**
    *   Target Shell: **PowerShell**.
    *   Examples: `Get-ChildItem` (or `ls`/`dir`), `Copy-Item`, `Move-Item`, `Remove-Item`, `New-Item -ItemType Directory`, `$env:VAR_NAME`, `python -m venv .venv`, `.\.venv\Scripts\activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate multiple commands that should run one after the other, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **INVALID OPERATOR:** **NEVER use `&&` for chaining commands.** It is invalid syntax in PowerShell and will cause errors like "The token '&&' is not a valid statement separator".
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** PowerShell lacks a simple *separator* like `&&`. To achieve this reliably with `<execute_command>`:
        1.  Execute the first command in one `<execute_command>` call.
        2.  **Await the result.** Check the `exit_code`. An exit code of `0` typically indicates success.
        3.  If the first command succeeded (exit code 0), issue the second command in a *separate* `<execute_command>` call.
        4.  **AVOID** generating complex PowerShell `if ($?) {...}` or `try/catch` blocks within a single command string unless absolutely necessary and simple, as it violates the "Avoid Shell-Specific Scripts" guideline below.
    *   Paths: Use `\` or `/` (PowerShell is often flexible), but prefer `\` for consistency if constructing paths manually.
    *   Quoting: Use single quotes `'...'` for literal strings. Use double quotes `"..."` if variable expansion is needed (less common for simple commands).

*   **If OS is `darwin` (macOS) or `linux` (Linux):**
    *   Target Shell: **Bash/Zsh compatible** (POSIX-like).
    *   Examples: `ls`, `cp`, `mv`, `rm`, `mkdir`, `$VAR_NAME`, `python3 -m venv .venv`, `source .venv/bin/activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate commands that should run sequentially, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** **MUST use the double ampersand `&&`** (e.g., `cd my_dir && ls -l`). This is the standard and expected way to ensure the second command only runs if the first succeeds.
    *   **INVALID OPERATORS:** **NEVER use `&amp;&amp;`** when you need conditional execution. **NEVER** use the HTML entity `&amp;&amp;` in the command string passed to `<execute_command>`.
    *   Paths: **MUST** use forward slashes `/`.
    *   Quoting: Use double quotes `"..."` generally, especially if needing variable expansion (`$VAR`). Use single quotes `'...'` for strict literal strings.

**General Guidelines (Applies to ALL OS):**

*   **Simplicity:** Prefer simple, common commands where possible.
*   **Avoid Complex Scripts:** Do not generate complex multi-line shell scripts (`.ps1`, `.sh`) unless specifically requested and appropriate for the task. Focus on single commands or correctly chained commands suitable for `<execute_command>`.
*   **Syntax Check:** **Double-check generated command syntax** before outputting it, paying close attention to the correct chaining operators (`&&` vs `&amp;&amp;`), quoting, and path separators for the target OS.
*   **User Overrides:** If the user explicitly requests a command for a *different* shell (e.g., "run this bash command on Windows using WSL"), follow the user's explicit instruction, but otherwise default to the detected OS's standard shell syntax.

**Failure to generate OS-appropriate and syntactically correct commands, especially regarding chaining (`&&` vs `&amp;&amp;`), will likely result in execution errors for the user.** Always check the OS context and verify command syntax before generating commands.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/06-iterative-execution-policy.md:
+++
id = "RURU-RULE-ITERATIVE-EXECUTION-V1"
title = "Standard Iterative Execution Policy"
context_type = "rules"
scope = "Defines how modes should handle potentially long-running or complex tasks"
target_audience = ["all"] # Primarily relevant for modes performing implementation/generation
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "workflow", "iteration", "context-management", "safety", "mdtm", "chunking"]
related_context = ["00-user-preferences.md", "01-standard-toml-md-format.md", "04-standard-workflows.md"]
+++

# Standard Iterative Execution Policy

**Objective:** To ensure reliable task completion by preventing context window overflows and promoting manageable work increments, especially for generative or implementation tasks.

**Applies To:** All modes performing tasks that involve significant code generation, file modification, analysis, or following multi-step procedures (e.g., developers, writers, refactorers, testers, sometimes architects/managers). Less critical for simple lookups or coordination.

**Core Principles:**

1.  **Prefer Smaller Steps:** Whenever feasible, break down complex requests into smaller, logical sub-tasks during the planning phase. For tasks managed via MDTM, this means creating granular checklist items.
2.  **Context Awareness:** Modes **MUST** be aware of their context window usage (`{{CONTEXT_PERCENTAGE}}`).
3.  **Proactive Checkpointing:** Do not attempt to complete overly large tasks in a single execution turn, even if instructed broadly.

**Procedure:**

1.  **Task Planning:** When starting a task (especially one involving multiple steps or significant generation):
    *   Review the overall goal and acceptance criteria.
    *   If using MDTM, review the checklist items.
    *   Mentally estimate the complexity. If a task or a single MDTM checklist item *appears* likely to require extensive code/output generation or numerous tool calls:
        *   **Plan for Iteration:** Anticipate that completing the task/item might require more than one execution cycle.
        *   **(Optional but Recommended):** Inform the delegator (via `ask_followup_question` *before starting*) if you anticipate needing multiple steps/checkpoints for a single requested item.

2.  **Execution & Monitoring:** While executing the task (writing code, applying diffs, following checklist items):
    *   Periodically self-monitor context window usage (`{{CONTEXT_PERCENTAGE}}`).
    *   **Trigger Checkpoint:** If context usage approaches a threshold (e.g., **around 40-50%**), prepare to pause *after completing the current logical unit of work*.
        *   A "logical unit" could be:
            *   Completing the current MDTM checklist item (`- [✅]`).
            *   Finishing a complete function, class, or coherent block of code.
            *   Completing a specific file modification.
            *   Finishing a distinct step in an analysis process.

3.  **Checkpoint & Handover:** When pausing due to the context threshold OR completing a step marked for reporting (e.g., `📣` in MDTM):
    *   **Finalize Current Unit:** Ensure the immediate work unit is complete and syntactically correct (e.g., finish the function, close code blocks).
    *   **Summarize Progress:** Briefly state what was completed in the current turn.
    *   **Identify Next Step:** Clearly state the *next logical step* required to continue the overall task (e.g., "Next step is to implement the `handleUpdate` function", "Next step is to process MDTM item #3").
    *   **Report Status:** Use `<attempt_completion>` to report back to the delegator. Include:
        *   Confirmation of completed unit/step.
        *   Current context percentage.
        *   The identified *next step*.
        *   Any partial results or paths to modified/created files.
        *   *(Example Result):* "✅ Completed implementation of `getUserData` function (MDTM item #2). Context at 55%. Next step is to implement the `UserProfile` component using this data. Modified: `src/hooks/useUserData.ts`."

4.  **Receiving Mode Action (Coordinator/Lead):**
    *   Acknowledge the partial completion and the stated next step.
    *   Log the progress (Rule `12`).
    *   Re-delegate the *next step* back to the specialist mode, providing the necessary context (including the original goal and referencing the previous work/files).

**Rationale:**

*   **Context Safety:** Prevents hitting hard context limits which often lead to truncated, incomplete, or erroneous responses.
*   **Error Reduction:** Smaller execution units reduce the chance of complex errors accumulating within a single turn.
*   **State Management:** Encourages breaking work into steps that align well with MDTM tracking, improving visibility.
*   **User Experience:** While it involves more turns, it leads to more reliable progress compared to large failures requiring complete restarts.

**Note:** The 50-60% threshold is a guideline. Modes should use judgment. If a small, final step pushes usage slightly over, completing it might be acceptable. The key is to avoid *starting* a large unit of work when context is already high.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/08-logging-procedure-simplified.md:
+++
id = "RULE-LOGGING-PROCEDURE-SIMPLE-V1"
title = "Standard: Logging Requirement"
context_type = "rules"
scope = "Requirement to log significant events and decisions"
target_audience = ["all"] # Especially Coordinators and Leads
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "logging", "auditing", "traceability", "mdtm"]
related_context = [
    ".roo/rules/04-mdtm-workflow-initiation.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md" # Link to detailed KB
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Essential for traceability and state management"
+++

# Standard: Logging Requirement

**Objective:** Ensure a traceable record of actions, decisions, and task progress.

**Rule:**

1.  **Log Events:** You **MUST** log significant events relevant to your task execution (e.g., decisions made, tasks delegated, errors encountered, steps completed, coordination actions).
2.  **Designated Location:** Log entries should typically be added to your assigned MDTM task file (`.ruru/tasks/TASK-...`), your coordination log file, or other designated artifact locations (e.g., ADRs in `.ruru/decisions/`).
3.  **Tooling Details:** For detailed guidance on *which tools* (`write_to_file`, `append_to_file`, `insert_content`, `apply_diff`) to use for specific logging scenarios and locations, consult the Roo Commander Knowledge Base document: **`.ruru/modes/roo-commander/kb/12-logging-procedures.md`**.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/10-vertex-mcp-usage-guideline.md:
+++
# --- Basic Metadata ---
id = "RULE-VERTEX-MCP-USAGE-V1"
title = "Guideline: Vertex AI MCP Tool Usage"
context_type = "rules"
scope = "Standardizing the use of Vertex AI MCP tools, especially save vs. direct output"
target_audience = ["all"] # Primarily modes using research/generation
granularity = "guideline"
status = "active"
last_updated = "2025-04-26" # Use current date
tags = ["rules", "mcp", "vertex-ai", "guideline", "output-handling", "file-organization", "research", "validation"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/08-logging-procedure-simplified.md",
    "repomix-output-shariqriazz-vertex-ai-mcp-server.md" # Reference to the MCP definition
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures consistent handling of MCP outputs"
+++

# Guideline: Vertex AI MCP Tool Usage

**Objective:** To standardize how modes interact with the `vertex-ai-mcp-server`, particularly regarding output handling and the use of research/validation capabilities.

**Applies To:** All modes utilizing tools provided by the `vertex-ai-mcp-server`.

**1. Tool Availability:**

*   Modes receive the list of available MCP tools dynamically in their context. Use these tools only if the `vertex-ai-mcp-server` is connected and the specific tool is listed.
*   Modes should gracefully handle scenarios where the MCP server or specific tools are unavailable.

**2. Output Handling Strategy (General):**

*   **Default to `save_*`:** When using Vertex AI MCP tools that have a corresponding `save_*` variant (e.g., `save_generate_project_guidelines`, `save_doc_snippet`, `save_topic_explanation`, `save_answer_query_direct`, `save_answer_query_websearch`), **prefer using the `save_*` variant** for potentially long or complex outputs.
    *   **Rationale:** This prevents large outputs from cluttering the chat history, archives the result for later reference, and helps manage context window size.
*   **Use Direct Tools Sparingly:** Use the direct output tools (e.g., `answer_query_websearch`, `explain_topic_with_docs`, `get_doc_snippets`) only when the expected output is known to be concise (e.g., a single code snippet, a short definition, a simple yes/no answer) or when specifically requested by the user/coordinator for an inline response.
*   **Reporting Saved Files:** When using a `save_*` tool, the mode **MUST** report the full path to the saved file back to the coordinator/user via `<attempt_completion>`. (See Section 2.1 for handling persistent context outputs.)

**2.1. Handling Persistent Context Outputs:**

*   **Identify Need:** If the output generated by a `save_*` tool is intended to be *persistent context* referenced directly by mode rules, KBs, or long-term documentation (unlike temporary analysis results):
    1.  **Move & Rename:** After the `save_*` tool successfully creates the file in the default `.ruru/docs/vertex/...` location, the coordinating mode **MUST** immediately use a file system tool (`execute_command` with `mkdir -p` and `mv`, or the `vertex-ai-mcp-server`'s `create_directory` and `move_file_or_directory` tools) to:
        *   Ensure a `context/` subdirectory exists within the relevant mode's directory (e.g., `.ruru/modes/[mode-slug]/context/`).
        *   Move the generated file from `.ruru/docs/vertex/...` into this mode-specific `context/` directory.
        *   Rename the file to something meaningful and versioned if appropriate (e.g., `[mode-slug]_context_[topic]_v1.md`) instead of the default timestamped name.
    2.  **Update References:** Any rules, KBs, or documents referencing this context **MUST** be updated immediately to point to the new, persistent path within the mode's `context/` directory.
    3.  **Log Move:** Log the move and rename operation.
*   **Rationale:** This ensures that context critical to a mode's operation is stored logically with the mode and avoids broken references if the general `.ruru/docs/vertex/` directory is treated as temporary. The default timestamped location should be used for transient outputs or initial review before deciding on persistence.

**3. Standard Output Location & Naming:**

*   **Base Directory:** All files generated by `save_*` tools **MUST** be saved within the `.ruru/docs/vertex/` directory.
*   **Subdirectory Structure:** Organize files by the *type* of tool used:
    *   `save_generate_project_guidelines` -> `.ruru/docs/vertex/guidelines/`
    *   `save_doc_snippet` -> `.ruru/docs/vertex/snippets/`
    *   `save_topic_explanation` -> `.ruru/docs/vertex/explanations/`
    *   `save_answer_query_direct` -> `.ruru/docs/vertex/answers-direct/`
    *   `save_answer_query_websearch` -> `.ruru/docs/vertex/answers-web/`
*   **File Naming Convention:** Files **MUST** be named using the format `[YYYYMMDDHHMMSS]-[sanitized_topic_or_query].md`.
    *   `[YYYYMMDDHHMMSS]`: Timestamp generated by the mode at the time of the call.
    *   `[sanitized_topic_or_query]`: A filesystem-safe representation of the primary topic or query (e.g., replace spaces/special characters with `_`, limit length to ~50 characters).
    *   *Example:* `.ruru/docs/vertex/guidelines/20250426182500-react_ts_node_guidelines.md`

**4. Using MCP for Research & Validation ("Brains Trust"):**

*   **Targeted Use:** While tools like `answer_query_websearch` can provide external context or validation, their use should be targeted and judicious due to latency, cost, and potential complexity.
*   **Prioritize Internal Context:** Modes **MUST** prioritize using internal project knowledge (KBs, rules, existing code, task context) before resorting to external MCP calls for validation or general research.
*   **Recommended Modes:** Consider enabling or encouraging this capability primarily within modes focused on architecture, research, complex problem-solving, or senior-level review (e.g., `technical-architect`, `agent-research`, `complex-problem-solver`, `util-senior-dev`, `util-second-opinion`).
*   **Clear Triggers:** Modes utilizing external validation should have clear triggers defined in their specific rules/KBs (e.g., "when evaluating unfamiliar technology", "if confidence is low").
*   **Log Usage:** Log instances where external validation was sought via MCP, including the query and a summary of the outcome, according to standard logging procedures (Rule `08-logging-procedure-simplified.md`).

**Adherence to these guidelines ensures consistent, traceable, and efficient use of the Vertex AI MCP capabilities.**</custom_instructions>
</environment_details>

---

**Assistant:**

Directory created. Now I will create the MDTM task file for the `spec-repomix` specialist.

```xml
<write_to_file>
<path>.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md</path>
<content>
+++
# --- Task Metadata ---
id = "TASK-REPOMIX-20250503-002621"
title = "Generate Repomix artifact for Roo-Code-Docs/docs/advanced-usage"
status = "🟡 To Do" # 🟡 To Do, 🟠 In Progress, 🟢 Done, 🔴 Error, ⚪ Blocked, 🔵 Pending External
type = "🛠️ Task" # 🌟 Feature, 🐞 Bug, 🛠️ Task, ❓ Question, 📄 Documentation, 🧪 Test, ♻️ Refactor
priority = "Medium" # Low, Medium, High, Critical
created_date = "2025-05-03T00:26:21+10:00"
updated_date = "2025-05-03T00:26:21+10:00"
assigned_to = "spec-repomix" # Slug of the specialist mode
coordinator = "SESS-CMD-20250503-002535" # Session ID or Task ID of the coordinator
related_docs = [] # List of paths to related documents (requirements, ADRs, etc.)
tags = ["repomix", "github", "documentation", "context-generation"]

# --- Optional Fields ---
# estimate = "2h" # Estimated time to complete
# deadline = "2025-05-10" # Target completion date
# dependencies = ["TASK-XYZ-123"] # List of prerequisite Task IDs
# subtasks = ["TASK-ABC-456"] # List of child Task IDs
+++

# Task: Generate Repomix artifact for Roo-Code-Docs/docs/advanced-usage

## 📝 Description

The user wants to generate a Repomix artifact containing the content from the `docs/advanced-usage` directory within the `RooVetGit/Roo-Code-Docs` GitHub repository.

**Source URL:** https://github.com/RooVetGit/Roo-Code-Docs/tree/main/docs/advanced-usage

## ✅ Acceptance Criteria

*   A valid Repomix artifact (`.repomix.json`) is generated.
*   The artifact contains the processed content from the specified GitHub directory.
*   The artifact is saved to a standard location within the workspace.
*   The path to the generated artifact is reported back to the coordinator.

## 📋 Checklist

- [ ] Identify source type (GitHub directory).
- [ ] Determine appropriate Repomix configuration for GitHub directory source.
- [ ] Execute Repomix generation process for the source URL: `https://github.com/RooVetGit/Roo-Code-Docs/tree/main/docs/advanced-usage`.
- [ ] Define output path (Suggest: `.ruru/context/repomix/roo-code-docs-advanced-usage.repomix.json`).
- [ ] Save the generated artifact to the determined output path.
- [ ] Report completion and the full artifact path back to the coordinator (`SESS-CMD-20250503-002535`).

## 🪵 Log

*   `[2025-05-03T00:26:21+10:00]` Task created by `roo-commander`.
</content>
<line_count>47</line_count>
</write_to_file>
```

---

**User:**

[write_to_file for '.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md'] Result:
The content was successfully saved to .ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md.
<environment_details>
# VSCode Visible Files
.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md

# VSCode Open Tabs
.ruru/sessions/SESS-CMD-20250503-002535/session_log.md,.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md

# Recently Modified Files
These files have been modified since you last accessed them (file was just edited so you may need to re-read it before editing):
.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md

# Current Time
03/05/2025, 12:26:39 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
138,665 (13%)

# Current Cost
$0.00

# Current Mode
<slug>roo-commander</slug>
<name>👑 Roo Commander</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Chief Executive, the highest-level coordinator for software development projects. You understand goals, delegate tasks using context and specialist capabilities, manage state via the project journal, and ensure project success.

Operational Guidelines:
- Prioritize rules and workflows found in the Knowledge Base (KB) at `.ruru/modes/roo-commander/kb/` over general knowledge for detailed procedures. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for navigation and the KB lookup rule (`.roo/rules-roo-commander/01-kb-lookup-rule.md`) for guidance on when and how to consult the KB.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files, especially for coordination artifacts.
- Use `read_file` to confirm content before applying diffs if unsure.
- Execute CLI commands using `execute_command`, explaining clearly.
- Escalate tasks outside core expertise to appropriate specialists via the lead or coordinator.</role>
<custom_instructions>
====

USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

Language Preference:
You should always speak and think in the "English" (en) language unless the user gives you instructions below to do otherwise.

Rules:

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/01-operational-principles.md:
+++
id = "ROO-CMD-PRINCIPLES-V1"
title = "Roo Commander: General Operational Principles"
context_type = "rules"
scope = "Core operational philosophy for Roo Commander"
target_audience = ["roo-commander"]
granularity = "principles"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "principles", "core", "coordination", "roo-commander"]
related_context = ["02-initialization-workflow-rule.md", "03-delegation-procedure-rule.md", "05-error-handling-rule.md", "06-documentation-adr-rule.md", "09-logging-procedure-rule.md", "99-kb-lookup-rule.md"]
+++

# General Operational Principles

These are the core principles guiding your actions as Roo Commander. Specific procedures for common workflows are detailed in other rule files, and highly detailed or less frequent procedures reside in the Knowledge Base (`.ruru/modes/roo-commander/kb/`).

1.  **Clarity and Intent:** Prioritize understanding the user's high-level goals before diving into specifics. Use clarifying questions (`ask_followup_question`) when intent is ambiguous. *(See Rule: `02-initialization-workflow-rule.md`)*
2.  **Strategic Delegation:** Leverage the full suite of specialist modes. Choose the *most appropriate* specialist based on the task, Stack Profile, and mode tags. Delegate clear, actionable tasks with defined goals and context. *(See Rule: `03-delegation-procedure-rule.md`)*
3.  **Context is Key:** Ensure all delegated tasks include necessary context (Task IDs, relevant file paths, Stack Profile). Determine the need for `agent-context-resolver` based on situational judgment (complexity, ambiguity, impact) before major delegations.
4.  **Logging Diligence:** Maintain accurate and timely records of decisions, delegations, errors, status updates, and other significant events.
6.  **User Focus:** Keep the user informed of the plan, progress, and any significant issues or decisions. Frame communication around achieving the user's objectives.
7.  **Command Line Assistance:** When using `execute_command`, explain the command clearly. If multiple command options exist, proactively ask the user for preference and offer brief explanations, while respecting safety protocols.
8.  **Error Handling:** Handle errors systematically by logging, analyzing, deciding on next steps, and acting. *(See Rule: `05-error-handling-rule.md`)*.
9.  **Documentation & Decisions:** Oversee documentation. Log significant decisions as ADRs. *(See Rule: `06-documentation-adr-rule.md`)*.
11. **Use KB When Directed:** Consult the Knowledge Base (`.ruru/modes/roo-commander/kb/`) when explicitly directed by other rules or when encountering novel/complex procedures not covered here. *(See Rule: `99-kb-lookup-rule.md`)*.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/02-initialization-workflow-rule.md:
+++
id = "ROO-CMD-RULE-INIT-V5" # Incremented version
title = "Roo Commander: Rule - Initial Request Processing & Mode Management" # Updated title
context_type = "rules"
scope = "Initial user interaction handling, presenting comprehensive starting options and routing to specific KB procedures"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-27" # Use current date
tags = ["rules", "workflow", "initialization", "onboarding", "intent", "options", "kb-routing", "roo-commander", "mode-management"] # Added tag
related_context = [
    "01-operational-principles.md",
    # Specific KB Action files
    ".ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md", # Added MCP Install option
    ".ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md",
    ".ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md",
    ".ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md",
    ".ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md",
    ".ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md",
    ".ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md",
    ".ruru/modes/roo-commander/kb/initial-actions/09-review-status.md",
    ".ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md",
    ".ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md",
    ".ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md",
    ".ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md",
    ".ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md",
    ".ruru/modes/roo-commander/kb/initial-actions/15-join-community.md",
    ".ruru/modes/roo-commander/kb/initial-actions/16-something-else.md",
    # Option 17 now handles Mode Management
    # Key delegate modes
    "manager-onboarding",
    "dev-git",
    "core-architect",
    "manager-product",
    "agent-research",
    "prime-coordinator",
    "dev-fixer",
    "util-refactor",
    "util-writer"
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the entry point for user interaction and routes to specific procedures"
+++

# Rule: Initial Request Processing (Explicit KB Routing)

This rule governs how you handle the **first user message** in a session, presenting a comprehensive list of starting options to clarify intent and initiate the correct workflow by executing procedures defined in specific Knowledge Base (KB) files.

**Standard Initial Prompt (if needed):**

```xml
 <ask_followup_question>
  <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
  <follow_up>
    <suggest>🔌 Install/Manage MCP Servers</suggest> <!-- Option 0 -->
    <suggest>🎩 Start a NEW project from scratch</suggest> <!-- Option 1 -->
    <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest> <!-- Option 2 -->
    <suggest>🌐 Clone a Git repository & onboard</suggest> <!-- Option 3 -->
    <suggest>🗃️ Use existing project files/plans to define the work</suggest> <!-- Option 4 -->
    <suggest>📑 Plan/Design a new feature or project</suggest> <!-- Option 5 -->
    <suggest>🐞 Fix a specific bug</suggest> <!-- Option 6 -->
    <suggest>♻️ Refactor or improve existing code</suggest> <!-- Option 7 -->
    <suggest>✍️ Write or update documentation</suggest> <!-- Option 8 -->
    <suggest>📟 Review project status / Manage tasks (MDTM)</suggest> <!-- Option 9 -->
    <suggest>❓ Research a topic / Ask a technical question</suggest> <!-- Option 10 -->
    <suggest>🎺 Execute a command / Delegate a specific known task</suggest> <!-- Option 11 -->
    <suggest>🪃 Manage Roo Configuration (Advanced)</suggest> <!-- Option 12 -->
    <suggest>🖲️ Update my preferences / profile</suggest> <!-- Option 13 -->
    <suggest>🦘 Learn about Roo Commander capabilities</suggest> <!-- Option 14 -->
    <suggest>🐾 Join the Roo Commander Community (Discord)</suggest> <!-- Option 15 -->
    <suggest>🤔 Something else... (Describe your goal)</suggest> <!-- Option 16 -->
    <suggest>🧑‍🎨 Mode Management</suggest> <!-- Option 17 -->
<suggest>📜 Workflow Management (Create, Read, Update, Delete Workflows)</suggest> <!-- Option 18 -> Switch to util-workflow-manager -->
  </follow_up>
 </ask_followup_question>```

**Procedure:**

1.  **Analyze Initial User Request:**
    *   Check for explicit mode switch requests ("switch to `[mode-slug]`").
    *   Briefly analyze keywords if the user states a goal directly.

2.  **Determine Response Path:**

    *   **A. Direct Mode Request:**
        *   If user explicitly requests switching to a specific mode: Confirm understanding and attempt `<switch_mode> [mode-slug]`. Log action (Rule `08`). **End this workflow.**

    *   **B. Direct Goal Stated (High Confidence - Non-Onboarding):**
        *   If the user's first message clearly states a goal that confidently maps to a specific action *other than onboarding/setup* (e.g., "fix bug 123", "refactor `userService.js`"):
            1.  Acknowledge the goal.
            2.  Propose the most relevant specialist mode via `ask_followup_question`.
            3.  Include suggestions: `<suggest>Yes, use [Proposed Mode]</suggest>`, `<suggest>No, let me choose from all starting options</suggest>`.
            4.  If "Yes", proceed to standard delegation (Rule `03`). Log action. **End this workflow.**
            5.  If "No", proceed to **Path C**.

    *   **C. All Other Cases (Default Path):**
        *   Includes: Vague requests, requests for help/options, requests initially mentioning "new project" or "onboard existing", or user selecting "No" in Path B.
        *   **Action:** Present the **Standard Initial Prompt** (defined above) using `<ask_followup_question>`.
        *   Await user's selection. Proceed to Step 3.

3.  **Handle User Selection (from Standard Initial Prompt):**
    *   Once the user selects an option (identified 0-18) from the standard prompt:
        1.  Identify the selected option number.
        2.  Log the chosen starting path (Rule `08`).
        3.  **Execute the detailed procedure defined in the corresponding KB file**:
            *   Option 0: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md`.
            *   Option 1: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md`.
            *   Option 2: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md`.
            *   Option 3: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md`.
            *   Option 4: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md`.
            *   Option 5: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md`.
            *   Option 6: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md`.
            *   Option 7: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md`.
            *   Option 8: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md`.
            *   Option 9: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/09-review-status.md`.
            *   Option 10: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md`.
            *   Option 11: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md`.
            *   Option 12: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md`.
            *   Option 13: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md`.
            *   Option 14: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md`.
            *   Option 15: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/15-join-community.md`.
            *   Option 16 ("Something else"): Execute KB `.ruru/modes/roo-commander/kb/initial-actions/16-something-else.md`.
            *   Option 17 ("Mode Management"): Present the user with the following choices and initiate the corresponding workflow:
                *   Create New Mode (`.ruru/workflows/WF-NEW-MODE-CREATION-004.md`)
                *   Mode KB Enrichment with Vertex AI MCP (`.ruru/workflows/WF-MODE-KB-ENRICHMENT-002.md`)
                *   Mode KB Enrichment with Context7 (`.ruru/workflows/WF-CONTEXT7-ENRICHMENT-001.md`)
                *   Mode KB Refresh with Context 7 (`.ruru/workflows/WF-CONTEXT7-REFRESH-001.md`)
                *   Delete Modes (Note: Workflow needs creation)
        *   Option 18 ("Workflow Management"): Switch to `util-workflow-manager` mode.
        4.  Follow the steps within the chosen KB procedure or subsequent workflow, including any user interaction or delegation it defines. **End this initialization workflow** upon completion of the KB procedure or delegated workflow.

**Key Objective:** To provide clear starting options and route the user interaction to the precise, detailed procedure stored in the relevant Knowledge Base file or subsequent workflow, ensuring consistent handling for each initial user intention, including mode management tasks.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03-delegation-simplified.md:
+++
id = "ROO-CMD-RULE-DELEGATION-SIMPLE-V1"
title = "Roo Commander: Rule - Task Delegation (Simplified)"
context_type = "rules"
scope = "Delegating tasks to specialist modes, including MDTM decision"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25"
tags = ["rules", "delegation", "mdtm", "specialists", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    ".ruru/docs/standards/mode_selection_guide.md",
    ".ruru/context/stack_profile.json",
    ".ruru/modes/roo-commander/kb/04-delegation-mdtm.md", # For detailed MDTM steps
    "04-mdtm-workflow-initiation.md" # Workspace rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Core delegation logic"
+++

# Rule: Task Delegation (Simplified)

1.  **Define Goal:** Clearly define the task objective.
2.  **Select Specialist:** Consult Stack Profile (`.ruru/context/stack_profile.json`) and the **Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`)**. Match task requirements/tags to specialist capabilities. Prioritize specific modes over generalists. Log rationale (Rule `08`).
3.  **Determine Method:**
    *   **Use MDTM Workflow if:** Task is complex, stateful, high-risk, requires detailed tracking/handoffs (Ref: Rule `04-mdtm-workflow-initiation.md`). Consult KB `.ruru/modes/roo-commander/kb/04-delegation-mdtm.md` for detailed procedure if needed.
    *   **Use Simple `new_task` if:** Task is straightforward, read-only, or low-risk.
4.  **Prepare Context:** Gather essential context (goal, criteria, file paths, Task IDs, Stack Profile).
5.  **Execute Delegation:** Use `new_task`. For MDTM, follow Rule `04-mdtm-workflow-initiation.md` (which includes creating the task file first). For simple tasks, provide context directly in the message.
6.  **Log & Monitor:** Log delegation (Rule `08`). Monitor via Rule `04`.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03b-complex-delegation-planning.md:
+++
id = "ROO-CMD-RULE-COMPLEX-DELEGATION-PLAN-V1"
title = "Roo Commander: Rule - Complex Delegation Planning & Confidence Check"
context_type = "rules"
scope = "Procedure for planning multi-step delegations and consulting user when confidence is low"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25" # Use current date
tags = ["rules", "delegation", "planning", "confidence", "multi-step", "mdtm", "roo-commander", "user-consultation"]
related_context = [
    "03-delegation-simplified.md", # The basic delegation rule
    ".roo/rules/04-mdtm-workflow-initiation.md", # Workspace MDTM rule
    ".roo/rules/06-iterative-execution-policy.md", # Iteration policy
    ".ruru/docs/standards/mode_selection_guide.md" # Mode selection guide
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Enhances strategic delegation for complex tasks"
+++

# Rule: Complex Delegation Planning & Confidence Check

This rule extends the basic delegation procedure (`03-delegation-simplified.md`) for tasks identified as particularly complex, ambiguous, or requiring a sequence of coordinated steps beyond a single MDTM task file.

**1. Trigger Conditions:**

*   Apply this procedure when a task involves:
    *   Significant ambiguity in requirements or implementation path.
    *   Multiple distinct phases or dependencies requiring different specialists or sequential execution.
    *   High uncertainty about the best approach or required modes.
    *   Initial analysis suggests the task breakdown might exceed simple MDTM checklist granularity or requires strategic sequencing.

**2. Planning Procedure:**

1.  **Analyze Goal:** Deeply analyze the user's goal, acceptance criteria, and any provided context. Identify ambiguities and potential complexities.
2.  **Break Down Task:** Decompose the overall goal into smaller, logical sub-tasks or phases.
3.  **Identify Specialists & Sequence:** For each sub-task, identify the most appropriate specialist mode(s) using the Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`). Determine the logical sequence or potential parallel execution paths.
4.  **Estimate Effort/Risk:** Briefly assess the estimated effort and risk associated with each sub-task and the overall plan.
5.  **Formulate Plan:** Outline the proposed delegation plan, including:
    *   Sequence of sub-tasks.
    *   Assigned specialist mode for each sub-task.
    *   Whether MDTM or simple `new_task` is appropriate for each step (following Rule `04-mdtm-workflow-initiation.md`).
    *   Key dependencies or handoffs between steps.

**3. Confidence Assessment:**

*   Evaluate your confidence in the formulated plan's success and efficiency. Consider:
    *   Clarity of requirements for each step.
    *   Availability and suitability of specialist modes.
    *   Potential risks or unknowns.
*   Assign a subjective confidence level (e.g., High, Medium, Low).

**4. User Consultation (Low/Medium Confidence):**

*   **If confidence is assessed as Low or Medium:**
    1.  **Do NOT proceed with delegation immediately.**
    2.  Use the `<ask_followup_question>` tool to present the situation to the user.
    3.  **Question Content:**
        *   Briefly explain the task's complexity and the reason for uncertainty.
        *   Present the proposed delegation plan (sub-tasks, modes, sequence).
        *   State your confidence level and the reasons (e.g., "Medium confidence due to ambiguity in API specification").
    4.  **Suggested Follow-ups:** Provide 2-4 actionable suggestions for the user, such as:
        *   "Proceed with the proposed plan."
        *   "Modify the plan: [Suggest a specific alternative sequence or mode]."
        *   "Provide clarification on: [Specify the ambiguous point]."
        *   "Delegate to [Alternative Lead/Mode] for further planning."
    5.  Await user direction before proceeding with delegation based on their choice.

**5. Execution (High Confidence or User Approval):**

*   If confidence is High, or if the user approves a plan after consultation:
    *   Proceed with executing the delegation plan step-by-step, using MDTM or simple `new_task` as determined for each sub-task.
    *   Follow standard logging (Rule `08`) and monitoring (Rule `04`) procedures.
    *   Utilize the Iterative Execution Policy (Rule `06`) for individual delegated steps as needed.

**Rationale:** This provides a mechanism for `roo-commander` to handle complex scenarios more robustly, leveraging user input when its own planning confidence is insufficient, thereby reducing the risk of inefficient or failed delegation chains.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/05-error-handling-rule.md:
+++
id = "ROO-CMD-RULE-ERROR-HANDLING-V1"
title = "Roo Commander: Rule - Basic Error Handling"
context_type = "rules"
scope = "Standard procedure for handling initial errors, failures, and blockers"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "error-handling", "failure", "blocker", "coordination", "roo-commander"]
related_context = ["01-operational-principles.md", "04-monitoring-completion-rule.md", "05-collaboration-escalation.md", "12-logging-procedures.md", ".ruru/modes/roo-commander/kb/05-collaboration-escalation.md"]
+++

# Rule: Basic Error Handling

This rule outlines the standard initial procedure when an error, failure (❌), or blocker (🧱) is detected either during Roo Commander's own operations or reported by a delegated specialist via `<attempt_completion>`.

**Procedure:**

1.  **Detection & Initial Assessment:** Identify the error/failure/blocker. Briefly assess its apparent severity and immediate impact based on available information (e.g., error message, specialist report, task status).

2.  **Log Failure Event:** **Immediately** log the detected issue according to Rule `12`. Include:
    *   Timestamp.
    *   Source of the error (e.g., specialist Task ID, tool failure).
    *   Error message or description of the blocker.
    *   Relevant context (e.g., related Commander Task ID).

3.  **Simple Analysis / Context Gathering:**
    *   Review the specific error message and the context logged in Step 2.
    *   If reported by a specialist, review their `<result>` content and the relevant task log (`read_file` on `.ruru/tasks/TASK-[MODE]-....md`) for details.
    *   Determine if the cause is immediately obvious and likely simple (e.g., typo in a command, file not found, simple syntax error reported by specialist).

4.  **Decision & Action (Prioritize Simple Fixes):**

    *   **If** the cause seems simple and easily correctable (e.g., fixable typo in delegation, incorrect file path):
        1.  **Plan Fix:** Determine the corrective action (e.g., re-delegate with corrected parameters).
        2.  **Log Decision:** Log the simple fix plan according to Rule `12`.
        3.  **Execute Fix:** Implement the fix (e.g., use `new_task` to re-delegate).
        4.  **Return to Monitoring:** Go back to monitoring the task (Rule `04`).

    *   **Else (If cause unclear, complex, requires specialist analysis, or involves safety/architecture):**
        1.  **Do NOT attempt complex fixes directly.**
        2.  **Consult Detailed Procedures:** Refer to the comprehensive error handling and escalation path details in the Knowledge Base: **`.ruru/modes/roo-commander/kb/05-collaboration-escalation.md`**.
        3.  **Follow KB Guidance:** Execute the relevant analysis, user consultation, or escalation steps outlined in the KB document (e.g., involving `dev-solver`, `core-architect`, or the User).
        4.  **Log Decision & Action:** Log the decision to escalate or perform further analysis according to Rule `12`.

**Key Objective:** To ensure all failures are logged immediately and that simple, obvious errors are handled efficiently, while complex or uncertain issues are systematically routed to more detailed analysis and escalation procedures defined in the KB.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/06-documentation-adr-simplified.md:
+++
id = "ROO-CMD-RULE-DOC-ADR-SIMPLE-V1"
title = "Roo Commander: Rule - Documentation & ADR Trigger (Simplified)"
context_type = "rules"
scope = "Triggering ADR creation and overseeing documentation"
target_audience = ["roo-commander"]
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "documentation", "adr", "logging", "decision-record", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    "08-logging-procedure-simplified.md", # Reference the simplified logging rule
    ".ruru/modes/roo-commander/kb/06-documentation-logging.md", # Detailed ADR creation/doc mgmt in KB
    ".ruru/templates/toml-md/07_adr.md", # ADR Template
    ".ruru/decisions/" # Standard ADR location
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures important decisions are recorded"
+++

# Rule: Documentation & ADR Trigger (Simplified)

1.  **Documentation Oversight:** Oversee project documentation location and status. Prefer delegating creation/updates of stable docs (`.ruru/docs/`) to specialists (`util-writer`, `core-architect`). Handle planning docs (`.ruru/planning/`) directly if needed, preferring `apply_diff` for modifications. Consult KB `.ruru/modes/roo-commander/kb/06-documentation-logging.md` for detailed documentation management guidance.

2.  **ADR Trigger:** An Architecture Decision Record (ADR) **MUST** be created in `.ruru/decisions/` for any **significant** architectural, technological, or strategic decision (e.g., framework choice, major pattern adoption, core tech selection).

3.  **ADR Procedure:** To create an ADR, consult the Knowledge Base document **`.ruru/modes/roo-commander/kb/06-documentation-logging.md`** for the detailed procedure. This involves using the standard template (`.ruru/templates/toml-md/07_adr.md`), writing the content, and logging the creation (Rule `08`).

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/10-meta-discussion-tool-output-handling.md:
+++
id = "CMD-RULE-META-TOOL-HANDLING-V3" # Adjusted ID for Commander, incremented version
title = "Roo Commander: Rule - Meta-Discussion Tool Output Handling" # Adjusted Title
context_type = "rules"
scope = "Handling the display or referencing of tool usage during meta-discussions"
target_audience = ["roo-commander"] # Target Commander
granularity = "guideline"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["rules", "meta-discussion", "tool-use", "safety", "roo-commander", "logging", "analysis", "file-output"] # Added roo-commander tag
related_context = [
    ".roo/rules/03-standard-tool-use-xml-syntax.md",
    ".roo/rules/08-logging-procedure-simplified.md" # Logging rule for file creation
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Prevents accidental tool execution during analysis/troubleshooting"
+++

# Rule: Meta-Discussion Tool Output Handling

**Objective:** To prevent accidental tool execution when discussing or analyzing previous interactions, logs, or mode behavior that involves tool usage syntax, while still allowing access to exact syntax details when necessary.

**Applies To:** `roo-commander` (A corresponding rule MUST exist for `prime-coordinator`).

**Rule:**

1.  **Identify Context:** When processing user input, provided content (like chat logs or file content), or formulating responses, carefully assess if the context clearly indicates a **meta-discussion**. This includes:
    *   Analyzing or reviewing past chat logs or MDTM task logs.
    *   Troubleshooting mode behavior or errors related to tool use.
    *   Discussing potential improvements to modes, rules, or workflows involving tool interactions.
    *   Responding to user feedback about specific tool interactions.
    *   Any situation where the user explicitly states they are discussing *past* tool use and do *not* want tools executed.

2.  **Strictly Avoid Direct Tool XML Output in Chat:** If the context is identified as a meta-discussion:
    *   **MUST NOT** output text formatted according to the standard tool usage XML syntax directly into the chat response.
    *   **MUST NOT** output text that mimics the tool usage XML syntax directly into the chat response, even if escaped (e.g., using backticks or other methods).

3.  **Describe or Offer File Output:** When referencing a specific tool use from the analyzed content:
    *   **Default Action:** Describe the tool use in plain text or standard Markdown, focusing on the *action*, *tool name*, and key *parameters* without using the XML structure.
        *   *Example Description:* "In the log, the mode then used the `read_file` tool, specifying the path `.ruru/workflows/WF-REPOMIX-V2/README.md`."
    *   **Alternative (Offer File Output):** If a simple description seems insufficient, or if the exact XML syntax might be important for the discussion (e.g., debugging complex parameters), **offer to write the detailed tool usage information (including the raw XML block) to a temporary file.**
        *   Use `ask_followup_question` to propose this to the user.
        *   If the user agrees:
            *   Generate a unique filename (e.g., `YYYYMMDDHHMMSS-tool-details.txt`).
            *   Use `write_to_file` to save the detailed information (including the raw XML) to `.ruru/docs/meta_discussion/[filename]`. Ensure this directory exists or can be created.
            *   Report the full path of the created file to the user.
            *   Log the creation of this temporary file (Rule `08-logging-procedure-simplified.md`).

4.  **Final Self-Correction Check:** Before sending any response, perform a final check on the generated text. If the response contains any text matching the pattern `<tool_name>...</tool_name>` that is *not* the single intended tool call for the *next* execution turn, **MUST** rephrase the response to describe the tool use (as per point 3a) instead of including the raw XML.

**Rationale:**

1.  This approach prioritizes safety by keeping executable syntax out of the main chat flow during meta-discussions.
2.  It provides a default descriptive method and a secondary option to safely export exact details to a file upon user request, facilitating deeper analysis when needed without risking accidental execution.
3.  The final self-correction check (Rule point 4) acts as a last safety measure to prevent accidental leakage of tool XML into meta-discussion responses, reinforcing the primary goal of preventing unintended execution.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/11-session-management-impl.md:
+++
# --- Basic Metadata ---
id = "CMD-RULE-SESSION-IMPL-V2" # Incremented version
title = "Roo Commander: Session Management V5 Implementation (No Protected Paths)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["session", "logging", "implementation", "roo-commander", "confirmation", "skip-confirm"] # Added tag
related_context = [
    ".roo/rules/11-session-management.md",
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Reference to the simplified workflow rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Assuming standard AI rule template schema
relevance = "High: Defines how roo-commander handles sessions and confirmations"
+++

# Roo Commander: Session Management V5 Implementation

This rule details how `roo-commander` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Default Behavior:** For `roo-commander`, the default is **to create** a session log (`Create log without goal`) unless the user explicitly opts out or the initial task is clearly trivial.
    *   **Prompting:** If prompting (per Rule 11, Section 3), use `ask_followup_question` with options: "Create log with goal: [Suggest goal]", "Create log (no goal) (default)", "Proceed without log".
    *   **Creation:** If user opts-in or default applies, follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`. Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **Confirmation Skip Logic:**
        *   **MAY Skip Confirm** (at Coordinator's discretion) if:
            *   The edit is assessed by Coordinator as **highly routine, simple, AND low-risk**.
        *   **MUST Confirm** in all other cases.
        *   If skipping, **MUST** log the decision and rationale to the active Session Log (if any).
    *   **Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **Delegation:** Instruct `prime-txt`/`dev` via `new_task`: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**". Log delegation (if session active).
    *   Await result. Log result (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/99-kb-lookup-rule.md:
+++
id = "ROO-CMD-RULE-KB-LOOKUP-V2" # Updated ID
title = "Roo Commander: Rule - KB Lookup Trigger"
context_type = "rules"
scope = "Mode-specific knowledge base access conditions"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "kb-lookup", "knowledge-base", "context", "reference", "roo-commander"]
related_context = [
    ".ruru/modes/roo-commander/kb/",
    ".ruru/modes/roo-commander/kb/README.md",
    # Links to rules that might *trigger* a KB lookup
    "01-operational-principles.md",
    "03-delegation-procedure-rule.md",
    "05-error-handling-rule.md",
    "06-documentation-adr-rule.md",
    "08-workflow-process-creation-rule.md"
    ]
+++

# Rule: KB Lookup Trigger

This rule defines the specific situations when you **MUST** consult the detailed Knowledge Base (KB) located in `.ruru/modes/roo-commander/kb/`. In most common operational scenarios, the procedures defined in rules `02` through `12` should be sufficient.

**Consult the KB When:**

1.  **Explicitly Directed:** Another rule explicitly references a specific KB document for detailed steps or information (e.g., "consult KB `04-delegation-mdtm.md` for detailed steps").
2.  **Novel/Complex Procedures:** You encounter a task requiring a detailed procedure that is *not* adequately covered by the standard operational rules (`02` through `12`). Examples include:
    *   Executing the detailed steps within the MDTM workflow (delegation rule points here).
    *   Handling complex or unusual error scenarios (error handling rule points here).
    *   Following detailed safety protocols beyond basic checks (safety rule points here).
    *   Understanding the nuanced use of logging tools (`write_to_file` vs `append` vs `insert`) for specific log types (logging rule points here).
3.  **Reference Lookups:** You need to access large reference lists or detailed indices, such as:
    *   The full summary of available modes (`kb-available-modes-summary.md`).
    *   The index of standard processes (`10-standard-processes-index.md`).
    *   The index of standard workflows (`11-standard-workflows-index.md`).

**Procedure for KB Lookup:**

1.  **Identify Target Document:** Determine the specific KB document needed based on the directing rule or the nature of the complex/novel task. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for guidance if the specific file isn't immediately known.
2.  **Use `read_file`:** Access the content of the target KB document.
3.  **Apply Information:** Integrate the detailed steps, guidelines, or reference information into your current task execution.

**Key Objective:** To ensure detailed, complex, or reference-heavy procedures are accessed from the KB when required, without cluttering the core operational rules or requiring unnecessary lookups for common actions.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/00-user-preferences.md:
+++
# --- Basic Metadata ---
id = "user-preferences"
title = "User Preferences"
context_type = "configuration"
scope = "User-specific settings and profile information"
target_audience = ["all"]
granularity = "detailed"
status = "active"
last_updated = "2025-04-17"
# version = "1.0"
tags = ["user", "preferences", "configuration", "profile"]
# relevance = "High relevance for personalization and context awareness"
template_schema_doc = ".ruru/templates/toml-md/17_user_preferences.README.md" # Points to schema documentation

# --- User Information ---
user_name = "" # << REQUIRED >>
skills = [
    # << OPTIONAL >>
]

# --- Roo Usage Preferences ---
[roo_usage_preferences]
preferred_modes = [
    # << OPTIONAL >>
]
verbosity_level = "normal" # << OPTIONAL. Options: "concise", "normal", "verbose" >>
auto_execute_commands = false # << OPTIONAL >>
+preferred_language = "en" # << OPTIONAL. Fallback if specific input/output prefs not set. Default 'en' >>
+preferred_input_language = "en" # << OPTIONAL. Language user primarily uses for prompts >>
+preferred_output_language = "en" # << OPTIONAL. Preferred language for conversational output, comments, etc. >>
+++

# User Preferences Data (Defined in TOML)
# This file stores user-specific preferences and profile information.
# The primary content is within the TOML block above.
# Use the TOML fields to tailor interactions and understand user context.
# Add any free-form notes below if necessary, but prioritize structured data in TOML.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/01-standard-toml-md-format.md:
# Standard: TOML+Markdown (TOML MD) Format Usage

**Applies To:** All agents creating or modifying Markdown files intended to have structured metadata.

**1. General Principle:**

This workspace utilizes the **TOML+Markdown (TOML MD)** format for various documents (tasks, ADRs, documentation, context sources, etc.) to combine machine-readable metadata with human-readable content.
*   **Metadata:** Use **TOML** syntax for key-value pairs. Adhere strictly to valid TOML syntax.
*   **Content:** Use standard **Markdown** for the main body of the document following the metadata.
*   **Rationale:** See `.ruru/templates/toml-md/README.md` for the benefits and general usage guidelines.

**2. Delimiter Requirement (Universal):**

*   **ALL** Markdown files using TOML frontmatter for structured metadata **MUST** enclose the TOML block within triple-plus delimiters (`+++`).

    ```markdown
    +++
    # TOML frontmatter content goes here
    key = "value"
    # ... other fields specific to document type ...
    +++

    # Markdown content follows
    ...
    ```
*   This ensures unambiguous and reliable parsing by automated tools across all document types.

**3. Using Templates:**

*   **When creating a new Markdown document** that requires structured metadata (e.g., tasks, ADRs, documentation, context sources), **ALWAYS** use the TOML+MD format described above.
*   **Check for Existing Templates:** Before creating a new document from scratch, consult the **`.ruru/templates/toml-md/README.md`** file to see if a suitable template already exists in the `.ruru/templates/toml-md/` directory.
    *   Do **NOT** read all files in the `.ruru/templates/toml-md/` directory directly; rely on the README for the list of available templates and their descriptions.
    *   If a suitable template exists (e.g., `01_mdtm_feature.md`, `07_adr.md`), use it as the starting point and adhere to the TOML schema defined within that template.
*   **Creating New Templates:**
    *   If no specific template exists in `.ruru/templates/toml-md/` for the document type you need to create:
        1.  **Offer to Create:** Propose creating a new template with the user.
        2.  **Start with Boilerplate:** If the user agrees, copy the boilerplate template (`.ruru/templates/toml-md/00_boilerplate.md`) as a starting point.
        3.  **Define Schema:** Define the necessary TOML metadata fields within the `+++` delimiters, clearly commenting on their purpose and whether they are required.
        4.  **Structure Content:** Structure the Markdown body logically using appropriate headings.
        5.  **Save Template:** Save the new template file within the `.ruru/templates/toml-md/` directory, following the naming convention (e.g., `NN_description.md`).
        6.  **Update README:** **Crucially**, update the `.ruru/templates/toml-md/README.md` file to include the newly created template in the "Available Templates" list with a brief description. This makes it discoverable for future use.

**4. Key Considerations:**

*   **Syntax:** Always use valid TOML syntax within the `+++` block.
*   **Schema:** Adhere to the specific schema defined for the document type (either from an existing template or the newly defined one).
*   **Consistency:** Use defined field names and data types consistently.

**Failure to use the correct format (including `+++` delimiters) will cause errors in processing and build steps.**

# Rules from /home/jez/vscode/roo-commander/.roo/rules/04-mdtm-workflow-initiation.md:
+++
# --- Basic Metadata ---
id = "RULE-MDTM-WORKFLOW-INIT-V1"
title = "Standard MDTM Task Creation & Delegation Workflow"
context_type = "rules"
scope = "Creating and delegating tasks via the TOML-based MDTM system"
target_audience = ["roo-commander", "prime-coordinator", "lead-*", "manager-project", "all"] # Target coordinators, leads, and specialists (for the update part)
granularity = "procedure"
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["mdtm", "toml", "workflow", "delegation", "task-creation", "coordination", "rules"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/12-logging-procedure-rule.md",
    ".ruru/tasks/",
    ".ruru/templates/toml-md/",
    ".ruru/docs/standards/mdtm_standard.md" # General MDTM standard (might need updating for TOML emphasis)
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Defines core task delegation process"
+++

# Mandatory Rule: MDTM Task Creation & Delegation Workflow

This rule defines the standard procedure for creating Markdown-Driven Task Management (MDTM) task files (using TOML frontmatter) and delegating work to specialist modes when detailed tracking is required.

**Applies To:** `roo-commander`, `prime-coordinator`, `lead-*` modes (for initiating MDTM tasks), and `manager-project`. Also relevant for specialist modes receiving MDTM tasks.

**1. When to Use MDTM:**

*   Initiate this MDTM workflow (instead of simple `new_task` delegation) for tasks that meet criteria such as:
    *   Complexity (multi-step, involves dependencies).
    *   Requires detailed progress tracking or auditing.
    *   High-risk changes (core logic, infrastructure, security).
    *   Requires clear handoffs between specialists.
*   Refer to specific mode documentation (e.g., `roo-commander` KB `04-delegation-mdtm.md`) for detailed criteria if available. If unsure, **err on the side of using MDTM** for better tracking.

**2. Procedure for Initiator (Coordinator/Lead/Manager):**

1.  **Generate Task ID:** Create a unique task ID following the convention `TASK-[MODE_PREFIX]-[YYYYMMDD-HHMMSS]` (e.g., `TASK-REACT-20250422-140500`).
2.  **Select Template:** Choose the appropriate MDTM template from `.ruru/templates/toml-md/` (e.g., `01_mdtm_feature.md`, `02_mdtm_bug.md`).
3.  **Determine Path:** Construct the full path for the new task file within the `.ruru/tasks/` structure (e.g., `.ruru/tasks/FEATURE_Login/TASK-REACT-20250422-140500.md`).
4.  **Prepare Content:**
    *   **TOML Frontmatter:** Populate the `+++` block with essential metadata, adhering strictly to TOML syntax (Rule `01-standard-toml-md-format.md`). Include at minimum:
        *   `id`: The generated Task ID.
        *   `title`: Clear, concise task title.
        *   `status`: Set initially to `"🟡 To Do"` (or `"Pending"`).
        *   `type`: The appropriate task type (e.g., `"🌟 Feature"`, `"🐞 Bug"`).
        *   `assigned_to`: The slug of the target specialist mode (e.g., `"dev-react"`).
        *   `coordinator`: Your own mode's Task ID (e.g., `"TASK-CMD-..."`).
        *   `related_docs`: List paths to requirements, specs, etc.
        *   `tags`: Relevant keywords.
    *   **Markdown Body:** Fill in the Markdown sections (Description, Acceptance Criteria, Checklist). Define clear, actionable checklist items (`- [ ] Step description`).
5.  **Create Task File:** Use the `write_to_file` tool to create the MDTM task file at the determined path with the prepared TOML and Markdown content.
6.  **Log Creation:** Log the creation of the task file (including its path) according to standard logging procedures (Rule `12`).
7.  **Delegate via `new_task`:**
    *   Target the specialist mode specified in the `assigned_to` field.
    *   The `<message>` **MUST** clearly state: "Process MDTM task file: [Full path to the created .md file]". Include the Coordinator's Task ID for reference.
    *   Provide any *essential* immediate context if needed, but the primary instructions reside within the task file.
8.  **Update Initiator State:** Note that delegation has occurred. Await `attempt_completion` from the specialist. **Do not assume the task is being worked on in the background.**

**3. Responsibility of Assigned Specialist Mode:**

*   When receiving a `new_task` instruction referencing an MDTM task file:
    1.  **MUST** use `read_file` to load the content of the specified task file path.
    2.  **MUST** perform the work described in the Markdown body, following the checklist items.
    3.  **MUST** update the Markdown checklist (`- [ ]` -> `- [✅]`) as steps are completed using `apply_diff` or `search_and_replace`. Add brief notes/logs to the Markdown body as needed.
    4.  **MUST** update the `status` field in the **TOML block** of the task file upon completion (`"🟢 Done"`) or if blocked (`"⚪ Blocked"`), along with the `updated_date`, using `apply_diff`.
    5.  **MUST** report the final outcome back to the Coordinator using `attempt_completion`, referencing the MDTM task file path.

**Failure to create the MDTM file before delegation, or failure by the specialist to update the assigned file, breaks the tracking process.** This workflow is essential for managing complex tasks within the Roo system.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/05-os-aware-commands.md:
+++
# --- Basic Metadata ---
id = "RURU-RULE-OS-AWARE-CMDS-V3" # Incremented version
title = "Rule: Generate OS-Aware and Syntactically Correct Commands"
context_type = "rules"
scope = "Command generation for execute_command tool based on detected OS"
target_audience = ["all"] # Apply to all modes using execute_command
granularity = "procedure" # Changed from ruleset to procedure as it defines steps
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["rules", "shell", "commands", "os-awareness", "powershell", "bash", "execute_command", "windows", "linux", "macos", "syntax", "chaining", "conditional-execution"] # Added tags
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
related_context = [".roo/rules/03-standard-tool-use-xml-syntax.md"]
relevance = "Critical: Prevents command execution errors"
+++

# Mandatory Rule: Generate OS-Aware and Syntactically Correct Commands

**Context:** Commands executed via `<execute_command>` run within the user's VS Code integrated terminal environment. The underlying operating system significantly impacts required command syntax. Assume the host OS is provided via context (e.g., `environment_details.os` with values like `win32`, `darwin`, `linux`).

**Rule:**

When formulating commands intended for execution via the `<execute_command>` tool, you **MUST** check the operating system context provided (e.g., `environment_details.os`) and generate commands appropriate for that specific platform's default shell, ensuring correct syntax, especially for command chaining.

**Platform-Specific Syntax & Chaining:**

*   **If OS is `win32` (Windows):**
    *   Target Shell: **PowerShell**.
    *   Examples: `Get-ChildItem` (or `ls`/`dir`), `Copy-Item`, `Move-Item`, `Remove-Item`, `New-Item -ItemType Directory`, `$env:VAR_NAME`, `python -m venv .venv`, `.\.venv\Scripts\activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate multiple commands that should run one after the other, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **INVALID OPERATOR:** **NEVER use `&&` for chaining commands.** It is invalid syntax in PowerShell and will cause errors like "The token '&&' is not a valid statement separator".
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** PowerShell lacks a simple *separator* like `&&`. To achieve this reliably with `<execute_command>`:
        1.  Execute the first command in one `<execute_command>` call.
        2.  **Await the result.** Check the `exit_code`. An exit code of `0` typically indicates success.
        3.  If the first command succeeded (exit code 0), issue the second command in a *separate* `<execute_command>` call.
        4.  **AVOID** generating complex PowerShell `if ($?) {...}` or `try/catch` blocks within a single command string unless absolutely necessary and simple, as it violates the "Avoid Shell-Specific Scripts" guideline below.
    *   Paths: Use `\` or `/` (PowerShell is often flexible), but prefer `\` for consistency if constructing paths manually.
    *   Quoting: Use single quotes `'...'` for literal strings. Use double quotes `"..."` if variable expansion is needed (less common for simple commands).

*   **If OS is `darwin` (macOS) or `linux` (Linux):**
    *   Target Shell: **Bash/Zsh compatible** (POSIX-like).
    *   Examples: `ls`, `cp`, `mv`, `rm`, `mkdir`, `$VAR_NAME`, `python3 -m venv .venv`, `source .venv/bin/activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate commands that should run sequentially, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** **MUST use the double ampersand `&&`** (e.g., `cd my_dir && ls -l`). This is the standard and expected way to ensure the second command only runs if the first succeeds.
    *   **INVALID OPERATORS:** **NEVER use `&amp;&amp;`** when you need conditional execution. **NEVER** use the HTML entity `&amp;&amp;` in the command string passed to `<execute_command>`.
    *   Paths: **MUST** use forward slashes `/`.
    *   Quoting: Use double quotes `"..."` generally, especially if needing variable expansion (`$VAR`). Use single quotes `'...'` for strict literal strings.

**General Guidelines (Applies to ALL OS):**

*   **Simplicity:** Prefer simple, common commands where possible.
*   **Avoid Complex Scripts:** Do not generate complex multi-line shell scripts (`.ps1`, `.sh`) unless specifically requested and appropriate for the task. Focus on single commands or correctly chained commands suitable for `<execute_command>`.
*   **Syntax Check:** **Double-check generated command syntax** before outputting it, paying close attention to the correct chaining operators (`&&` vs `&amp;&amp;`), quoting, and path separators for the target OS.
*   **User Overrides:** If the user explicitly requests a command for a *different* shell (e.g., "run this bash command on Windows using WSL"), follow the user's explicit instruction, but otherwise default to the detected OS's standard shell syntax.

**Failure to generate OS-appropriate and syntactically correct commands, especially regarding chaining (`&&` vs `&amp;&amp;`), will likely result in execution errors for the user.** Always check the OS context and verify command syntax before generating commands.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/06-iterative-execution-policy.md:
+++
id = "RURU-RULE-ITERATIVE-EXECUTION-V1"
title = "Standard Iterative Execution Policy"
context_type = "rules"
scope = "Defines how modes should handle potentially long-running or complex tasks"
target_audience = ["all"] # Primarily relevant for modes performing implementation/generation
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "workflow", "iteration", "context-management", "safety", "mdtm", "chunking"]
related_context = ["00-user-preferences.md", "01-standard-toml-md-format.md", "04-standard-workflows.md"]
+++

# Standard Iterative Execution Policy

**Objective:** To ensure reliable task completion by preventing context window overflows and promoting manageable work increments, especially for generative or implementation tasks.

**Applies To:** All modes performing tasks that involve significant code generation, file modification, analysis, or following multi-step procedures (e.g., developers, writers, refactorers, testers, sometimes architects/managers). Less critical for simple lookups or coordination.

**Core Principles:**

1.  **Prefer Smaller Steps:** Whenever feasible, break down complex requests into smaller, logical sub-tasks during the planning phase. For tasks managed via MDTM, this means creating granular checklist items.
2.  **Context Awareness:** Modes **MUST** be aware of their context window usage (`{{CONTEXT_PERCENTAGE}}`).
3.  **Proactive Checkpointing:** Do not attempt to complete overly large tasks in a single execution turn, even if instructed broadly.

**Procedure:**

1.  **Task Planning:** When starting a task (especially one involving multiple steps or significant generation):
    *   Review the overall goal and acceptance criteria.
    *   If using MDTM, review the checklist items.
    *   Mentally estimate the complexity. If a task or a single MDTM checklist item *appears* likely to require extensive code/output generation or numerous tool calls:
        *   **Plan for Iteration:** Anticipate that completing the task/item might require more than one execution cycle.
        *   **(Optional but Recommended):** Inform the delegator (via `ask_followup_question` *before starting*) if you anticipate needing multiple steps/checkpoints for a single requested item.

2.  **Execution & Monitoring:** While executing the task (writing code, applying diffs, following checklist items):
    *   Periodically self-monitor context window usage (`{{CONTEXT_PERCENTAGE}}`).
    *   **Trigger Checkpoint:** If context usage approaches a threshold (e.g., **around 40-50%**), prepare to pause *after completing the current logical unit of work*.
        *   A "logical unit" could be:
            *   Completing the current MDTM checklist item (`- [✅]`).
            *   Finishing a complete function, class, or coherent block of code.
            *   Completing a specific file modification.
            *   Finishing a distinct step in an analysis process.

3.  **Checkpoint & Handover:** When pausing due to the context threshold OR completing a step marked for reporting (e.g., `📣` in MDTM):
    *   **Finalize Current Unit:** Ensure the immediate work unit is complete and syntactically correct (e.g., finish the function, close code blocks).
    *   **Summarize Progress:** Briefly state what was completed in the current turn.
    *   **Identify Next Step:** Clearly state the *next logical step* required to continue the overall task (e.g., "Next step is to implement the `handleUpdate` function", "Next step is to process MDTM item #3").
    *   **Report Status:** Use `<attempt_completion>` to report back to the delegator. Include:
        *   Confirmation of completed unit/step.
        *   Current context percentage.
        *   The identified *next step*.
        *   Any partial results or paths to modified/created files.
        *   *(Example Result):* "✅ Completed implementation of `getUserData` function (MDTM item #2). Context at 55%. Next step is to implement the `UserProfile` component using this data. Modified: `src/hooks/useUserData.ts`."

4.  **Receiving Mode Action (Coordinator/Lead):**
    *   Acknowledge the partial completion and the stated next step.
    *   Log the progress (Rule `12`).
    *   Re-delegate the *next step* back to the specialist mode, providing the necessary context (including the original goal and referencing the previous work/files).

**Rationale:**

*   **Context Safety:** Prevents hitting hard context limits which often lead to truncated, incomplete, or erroneous responses.
*   **Error Reduction:** Smaller execution units reduce the chance of complex errors accumulating within a single turn.
*   **State Management:** Encourages breaking work into steps that align well with MDTM tracking, improving visibility.
*   **User Experience:** While it involves more turns, it leads to more reliable progress compared to large failures requiring complete restarts.

**Note:** The 50-60% threshold is a guideline. Modes should use judgment. If a small, final step pushes usage slightly over, completing it might be acceptable. The key is to avoid *starting* a large unit of work when context is already high.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/08-logging-procedure-simplified.md:
+++
id = "RULE-LOGGING-PROCEDURE-SIMPLE-V1"
title = "Standard: Logging Requirement"
context_type = "rules"
scope = "Requirement to log significant events and decisions"
target_audience = ["all"] # Especially Coordinators and Leads
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "logging", "auditing", "traceability", "mdtm"]
related_context = [
    ".roo/rules/04-mdtm-workflow-initiation.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md" # Link to detailed KB
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Essential for traceability and state management"
+++

# Standard: Logging Requirement

**Objective:** Ensure a traceable record of actions, decisions, and task progress.

**Rule:**

1.  **Log Events:** You **MUST** log significant events relevant to your task execution (e.g., decisions made, tasks delegated, errors encountered, steps completed, coordination actions).
2.  **Designated Location:** Log entries should typically be added to your assigned MDTM task file (`.ruru/tasks/TASK-...`), your coordination log file, or other designated artifact locations (e.g., ADRs in `.ruru/decisions/`).
3.  **Tooling Details:** For detailed guidance on *which tools* (`write_to_file`, `append_to_file`, `insert_content`, `apply_diff`) to use for specific logging scenarios and locations, consult the Roo Commander Knowledge Base document: **`.ruru/modes/roo-commander/kb/12-logging-procedures.md`**.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/10-vertex-mcp-usage-guideline.md:
+++
# --- Basic Metadata ---
id = "RULE-VERTEX-MCP-USAGE-V1"
title = "Guideline: Vertex AI MCP Tool Usage"
context_type = "rules"
scope = "Standardizing the use of Vertex AI MCP tools, especially save vs. direct output"
target_audience = ["all"] # Primarily modes using research/generation
granularity = "guideline"
status = "active"
last_updated = "2025-04-26" # Use current date
tags = ["rules", "mcp", "vertex-ai", "guideline", "output-handling", "file-organization", "research", "validation"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/08-logging-procedure-simplified.md",
    "repomix-output-shariqriazz-vertex-ai-mcp-server.md" # Reference to the MCP definition
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures consistent handling of MCP outputs"
+++

# Guideline: Vertex AI MCP Tool Usage

**Objective:** To standardize how modes interact with the `vertex-ai-mcp-server`, particularly regarding output handling and the use of research/validation capabilities.

**Applies To:** All modes utilizing tools provided by the `vertex-ai-mcp-server`.

**1. Tool Availability:**

*   Modes receive the list of available MCP tools dynamically in their context. Use these tools only if the `vertex-ai-mcp-server` is connected and the specific tool is listed.
*   Modes should gracefully handle scenarios where the MCP server or specific tools are unavailable.

**2. Output Handling Strategy (General):**

*   **Default to `save_*`:** When using Vertex AI MCP tools that have a corresponding `save_*` variant (e.g., `save_generate_project_guidelines`, `save_doc_snippet`, `save_topic_explanation`, `save_answer_query_direct`, `save_answer_query_websearch`), **prefer using the `save_*` variant** for potentially long or complex outputs.
    *   **Rationale:** This prevents large outputs from cluttering the chat history, archives the result for later reference, and helps manage context window size.
*   **Use Direct Tools Sparingly:** Use the direct output tools (e.g., `answer_query_websearch`, `explain_topic_with_docs`, `get_doc_snippets`) only when the expected output is known to be concise (e.g., a single code snippet, a short definition, a simple yes/no answer) or when specifically requested by the user/coordinator for an inline response.
*   **Reporting Saved Files:** When using a `save_*` tool, the mode **MUST** report the full path to the saved file back to the coordinator/user via `<attempt_completion>`. (See Section 2.1 for handling persistent context outputs.)

**2.1. Handling Persistent Context Outputs:**

*   **Identify Need:** If the output generated by a `save_*` tool is intended to be *persistent context* referenced directly by mode rules, KBs, or long-term documentation (unlike temporary analysis results):
    1.  **Move & Rename:** After the `save_*` tool successfully creates the file in the default `.ruru/docs/vertex/...` location, the coordinating mode **MUST** immediately use a file system tool (`execute_command` with `mkdir -p` and `mv`, or the `vertex-ai-mcp-server`'s `create_directory` and `move_file_or_directory` tools) to:
        *   Ensure a `context/` subdirectory exists within the relevant mode's directory (e.g., `.ruru/modes/[mode-slug]/context/`).
        *   Move the generated file from `.ruru/docs/vertex/...` into this mode-specific `context/` directory.
        *   Rename the file to something meaningful and versioned if appropriate (e.g., `[mode-slug]_context_[topic]_v1.md`) instead of the default timestamped name.
    2.  **Update References:** Any rules, KBs, or documents referencing this context **MUST** be updated immediately to point to the new, persistent path within the mode's `context/` directory.
    3.  **Log Move:** Log the move and rename operation.
*   **Rationale:** This ensures that context critical to a mode's operation is stored logically with the mode and avoids broken references if the general `.ruru/docs/vertex/` directory is treated as temporary. The default timestamped location should be used for transient outputs or initial review before deciding on persistence.

**3. Standard Output Location & Naming:**

*   **Base Directory:** All files generated by `save_*` tools **MUST** be saved within the `.ruru/docs/vertex/` directory.
*   **Subdirectory Structure:** Organize files by the *type* of tool used:
    *   `save_generate_project_guidelines` -> `.ruru/docs/vertex/guidelines/`
    *   `save_doc_snippet` -> `.ruru/docs/vertex/snippets/`
    *   `save_topic_explanation` -> `.ruru/docs/vertex/explanations/`
    *   `save_answer_query_direct` -> `.ruru/docs/vertex/answers-direct/`
    *   `save_answer_query_websearch` -> `.ruru/docs/vertex/answers-web/`
*   **File Naming Convention:** Files **MUST** be named using the format `[YYYYMMDDHHMMSS]-[sanitized_topic_or_query].md`.
    *   `[YYYYMMDDHHMMSS]`: Timestamp generated by the mode at the time of the call.
    *   `[sanitized_topic_or_query]`: A filesystem-safe representation of the primary topic or query (e.g., replace spaces/special characters with `_`, limit length to ~50 characters).
    *   *Example:* `.ruru/docs/vertex/guidelines/20250426182500-react_ts_node_guidelines.md`

**4. Using MCP for Research & Validation ("Brains Trust"):**

*   **Targeted Use:** While tools like `answer_query_websearch` can provide external context or validation, their use should be targeted and judicious due to latency, cost, and potential complexity.
*   **Prioritize Internal Context:** Modes **MUST** prioritize using internal project knowledge (KBs, rules, existing code, task context) before resorting to external MCP calls for validation or general research.
*   **Recommended Modes:** Consider enabling or encouraging this capability primarily within modes focused on architecture, research, complex problem-solving, or senior-level review (e.g., `technical-architect`, `agent-research`, `complex-problem-solver`, `util-senior-dev`, `util-second-opinion`).
*   **Clear Triggers:** Modes utilizing external validation should have clear triggers defined in their specific rules/KBs (e.g., "when evaluating unfamiliar technology", "if confidence is low").
*   **Log Usage:** Log instances where external validation was sought via MCP, including the query and a summary of the outcome, according to standard logging procedures (Rule `08-logging-procedure-simplified.md`).

**Adherence to these guidelines ensures consistent, traceable, and efficient use of the Vertex AI MCP capabilities.**</custom_instructions>
</environment_details>

---

**Assistant:**

MDTM task file created successfully.

Now I will log the task creation and delegation event to the session log.

```xml
<insert_content>
<path>.ruru/sessions/SESS-CMD-20250503-002535/session_log.md</path>
<line>28</line>
<content>
*   `[2025-05-03T00:26:39+10:00]` Created MDTM task file: `artifacts/../tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md`. Delegating to `spec-repomix`.
</content>
</insert_content>
```

---

**User:**

[insert_content for '.ruru/sessions/SESS-CMD-20250503-002535/session_log.md'] Result:
The content was successfully inserted in .ruru/sessions/SESS-CMD-20250503-002535/session_log.md at line 28.
<environment_details>
# VSCode Visible Files
.ruru/sessions/SESS-CMD-20250503-002535/session_log.md

# VSCode Open Tabs
.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md,.ruru/sessions/SESS-CMD-20250503-002535/session_log.md

# Current Time
03/05/2025, 12:26:52 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
156,688 (15%)

# Current Cost
$0.00

# Current Mode
<slug>roo-commander</slug>
<name>👑 Roo Commander</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Chief Executive, the highest-level coordinator for software development projects. You understand goals, delegate tasks using context and specialist capabilities, manage state via the project journal, and ensure project success.

Operational Guidelines:
- Prioritize rules and workflows found in the Knowledge Base (KB) at `.ruru/modes/roo-commander/kb/` over general knowledge for detailed procedures. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for navigation and the KB lookup rule (`.roo/rules-roo-commander/01-kb-lookup-rule.md`) for guidance on when and how to consult the KB.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files, especially for coordination artifacts.
- Use `read_file` to confirm content before applying diffs if unsure.
- Execute CLI commands using `execute_command`, explaining clearly.
- Escalate tasks outside core expertise to appropriate specialists via the lead or coordinator.</role>
<custom_instructions>
====

USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

Language Preference:
You should always speak and think in the "English" (en) language unless the user gives you instructions below to do otherwise.

Rules:

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/01-operational-principles.md:
+++
id = "ROO-CMD-PRINCIPLES-V1"
title = "Roo Commander: General Operational Principles"
context_type = "rules"
scope = "Core operational philosophy for Roo Commander"
target_audience = ["roo-commander"]
granularity = "principles"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "principles", "core", "coordination", "roo-commander"]
related_context = ["02-initialization-workflow-rule.md", "03-delegation-procedure-rule.md", "05-error-handling-rule.md", "06-documentation-adr-rule.md", "09-logging-procedure-rule.md", "99-kb-lookup-rule.md"]
+++

# General Operational Principles

These are the core principles guiding your actions as Roo Commander. Specific procedures for common workflows are detailed in other rule files, and highly detailed or less frequent procedures reside in the Knowledge Base (`.ruru/modes/roo-commander/kb/`).

1.  **Clarity and Intent:** Prioritize understanding the user's high-level goals before diving into specifics. Use clarifying questions (`ask_followup_question`) when intent is ambiguous. *(See Rule: `02-initialization-workflow-rule.md`)*
2.  **Strategic Delegation:** Leverage the full suite of specialist modes. Choose the *most appropriate* specialist based on the task, Stack Profile, and mode tags. Delegate clear, actionable tasks with defined goals and context. *(See Rule: `03-delegation-procedure-rule.md`)*
3.  **Context is Key:** Ensure all delegated tasks include necessary context (Task IDs, relevant file paths, Stack Profile). Determine the need for `agent-context-resolver` based on situational judgment (complexity, ambiguity, impact) before major delegations.
4.  **Logging Diligence:** Maintain accurate and timely records of decisions, delegations, errors, status updates, and other significant events.
6.  **User Focus:** Keep the user informed of the plan, progress, and any significant issues or decisions. Frame communication around achieving the user's objectives.
7.  **Command Line Assistance:** When using `execute_command`, explain the command clearly. If multiple command options exist, proactively ask the user for preference and offer brief explanations, while respecting safety protocols.
8.  **Error Handling:** Handle errors systematically by logging, analyzing, deciding on next steps, and acting. *(See Rule: `05-error-handling-rule.md`)*.
9.  **Documentation & Decisions:** Oversee documentation. Log significant decisions as ADRs. *(See Rule: `06-documentation-adr-rule.md`)*.
11. **Use KB When Directed:** Consult the Knowledge Base (`.ruru/modes/roo-commander/kb/`) when explicitly directed by other rules or when encountering novel/complex procedures not covered here. *(See Rule: `99-kb-lookup-rule.md`)*.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/02-initialization-workflow-rule.md:
+++
id = "ROO-CMD-RULE-INIT-V5" # Incremented version
title = "Roo Commander: Rule - Initial Request Processing & Mode Management" # Updated title
context_type = "rules"
scope = "Initial user interaction handling, presenting comprehensive starting options and routing to specific KB procedures"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-27" # Use current date
tags = ["rules", "workflow", "initialization", "onboarding", "intent", "options", "kb-routing", "roo-commander", "mode-management"] # Added tag
related_context = [
    "01-operational-principles.md",
    # Specific KB Action files
    ".ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md", # Added MCP Install option
    ".ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md",
    ".ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md",
    ".ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md",
    ".ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md",
    ".ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md",
    ".ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md",
    ".ruru/modes/roo-commander/kb/initial-actions/09-review-status.md",
    ".ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md",
    ".ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md",
    ".ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md",
    ".ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md",
    ".ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md",
    ".ruru/modes/roo-commander/kb/initial-actions/15-join-community.md",
    ".ruru/modes/roo-commander/kb/initial-actions/16-something-else.md",
    # Option 17 now handles Mode Management
    # Key delegate modes
    "manager-onboarding",
    "dev-git",
    "core-architect",
    "manager-product",
    "agent-research",
    "prime-coordinator",
    "dev-fixer",
    "util-refactor",
    "util-writer"
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the entry point for user interaction and routes to specific procedures"
+++

# Rule: Initial Request Processing (Explicit KB Routing)

This rule governs how you handle the **first user message** in a session, presenting a comprehensive list of starting options to clarify intent and initiate the correct workflow by executing procedures defined in specific Knowledge Base (KB) files.

**Standard Initial Prompt (if needed):**

```xml
 <ask_followup_question>
  <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
  <follow_up>
    <suggest>🔌 Install/Manage MCP Servers</suggest> <!-- Option 0 -->
    <suggest>🎩 Start a NEW project from scratch</suggest> <!-- Option 1 -->
    <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest> <!-- Option 2 -->
    <suggest>🌐 Clone a Git repository & onboard</suggest> <!-- Option 3 -->
    <suggest>🗃️ Use existing project files/plans to define the work</suggest> <!-- Option 4 -->
    <suggest>📑 Plan/Design a new feature or project</suggest> <!-- Option 5 -->
    <suggest>🐞 Fix a specific bug</suggest> <!-- Option 6 -->
    <suggest>♻️ Refactor or improve existing code</suggest> <!-- Option 7 -->
    <suggest>✍️ Write or update documentation</suggest> <!-- Option 8 -->
    <suggest>📟 Review project status / Manage tasks (MDTM)</suggest> <!-- Option 9 -->
    <suggest>❓ Research a topic / Ask a technical question</suggest> <!-- Option 10 -->
    <suggest>🎺 Execute a command / Delegate a specific known task</suggest> <!-- Option 11 -->
    <suggest>🪃 Manage Roo Configuration (Advanced)</suggest> <!-- Option 12 -->
    <suggest>🖲️ Update my preferences / profile</suggest> <!-- Option 13 -->
    <suggest>🦘 Learn about Roo Commander capabilities</suggest> <!-- Option 14 -->
    <suggest>🐾 Join the Roo Commander Community (Discord)</suggest> <!-- Option 15 -->
    <suggest>🤔 Something else... (Describe your goal)</suggest> <!-- Option 16 -->
    <suggest>🧑‍🎨 Mode Management</suggest> <!-- Option 17 -->
<suggest>📜 Workflow Management (Create, Read, Update, Delete Workflows)</suggest> <!-- Option 18 -> Switch to util-workflow-manager -->
  </follow_up>
 </ask_followup_question>```

**Procedure:**

1.  **Analyze Initial User Request:**
    *   Check for explicit mode switch requests ("switch to `[mode-slug]`").
    *   Briefly analyze keywords if the user states a goal directly.

2.  **Determine Response Path:**

    *   **A. Direct Mode Request:**
        *   If user explicitly requests switching to a specific mode: Confirm understanding and attempt `<switch_mode> [mode-slug]`. Log action (Rule `08`). **End this workflow.**

    *   **B. Direct Goal Stated (High Confidence - Non-Onboarding):**
        *   If the user's first message clearly states a goal that confidently maps to a specific action *other than onboarding/setup* (e.g., "fix bug 123", "refactor `userService.js`"):
            1.  Acknowledge the goal.
            2.  Propose the most relevant specialist mode via `ask_followup_question`.
            3.  Include suggestions: `<suggest>Yes, use [Proposed Mode]</suggest>`, `<suggest>No, let me choose from all starting options</suggest>`.
            4.  If "Yes", proceed to standard delegation (Rule `03`). Log action. **End this workflow.**
            5.  If "No", proceed to **Path C**.

    *   **C. All Other Cases (Default Path):**
        *   Includes: Vague requests, requests for help/options, requests initially mentioning "new project" or "onboard existing", or user selecting "No" in Path B.
        *   **Action:** Present the **Standard Initial Prompt** (defined above) using `<ask_followup_question>`.
        *   Await user's selection. Proceed to Step 3.

3.  **Handle User Selection (from Standard Initial Prompt):**
    *   Once the user selects an option (identified 0-18) from the standard prompt:
        1.  Identify the selected option number.
        2.  Log the chosen starting path (Rule `08`).
        3.  **Execute the detailed procedure defined in the corresponding KB file**:
            *   Option 0: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md`.
            *   Option 1: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md`.
            *   Option 2: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md`.
            *   Option 3: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md`.
            *   Option 4: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md`.
            *   Option 5: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md`.
            *   Option 6: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md`.
            *   Option 7: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md`.
            *   Option 8: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md`.
            *   Option 9: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/09-review-status.md`.
            *   Option 10: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md`.
            *   Option 11: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md`.
            *   Option 12: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md`.
            *   Option 13: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md`.
            *   Option 14: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md`.
            *   Option 15: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/15-join-community.md`.
            *   Option 16 ("Something else"): Execute KB `.ruru/modes/roo-commander/kb/initial-actions/16-something-else.md`.
            *   Option 17 ("Mode Management"): Present the user with the following choices and initiate the corresponding workflow:
                *   Create New Mode (`.ruru/workflows/WF-NEW-MODE-CREATION-004.md`)
                *   Mode KB Enrichment with Vertex AI MCP (`.ruru/workflows/WF-MODE-KB-ENRICHMENT-002.md`)
                *   Mode KB Enrichment with Context7 (`.ruru/workflows/WF-CONTEXT7-ENRICHMENT-001.md`)
                *   Mode KB Refresh with Context 7 (`.ruru/workflows/WF-CONTEXT7-REFRESH-001.md`)
                *   Delete Modes (Note: Workflow needs creation)
        *   Option 18 ("Workflow Management"): Switch to `util-workflow-manager` mode.
        4.  Follow the steps within the chosen KB procedure or subsequent workflow, including any user interaction or delegation it defines. **End this initialization workflow** upon completion of the KB procedure or delegated workflow.

**Key Objective:** To provide clear starting options and route the user interaction to the precise, detailed procedure stored in the relevant Knowledge Base file or subsequent workflow, ensuring consistent handling for each initial user intention, including mode management tasks.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03-delegation-simplified.md:
+++
id = "ROO-CMD-RULE-DELEGATION-SIMPLE-V1"
title = "Roo Commander: Rule - Task Delegation (Simplified)"
context_type = "rules"
scope = "Delegating tasks to specialist modes, including MDTM decision"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25"
tags = ["rules", "delegation", "mdtm", "specialists", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    ".ruru/docs/standards/mode_selection_guide.md",
    ".ruru/context/stack_profile.json",
    ".ruru/modes/roo-commander/kb/04-delegation-mdtm.md", # For detailed MDTM steps
    "04-mdtm-workflow-initiation.md" # Workspace rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Core delegation logic"
+++

# Rule: Task Delegation (Simplified)

1.  **Define Goal:** Clearly define the task objective.
2.  **Select Specialist:** Consult Stack Profile (`.ruru/context/stack_profile.json`) and the **Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`)**. Match task requirements/tags to specialist capabilities. Prioritize specific modes over generalists. Log rationale (Rule `08`).
3.  **Determine Method:**
    *   **Use MDTM Workflow if:** Task is complex, stateful, high-risk, requires detailed tracking/handoffs (Ref: Rule `04-mdtm-workflow-initiation.md`). Consult KB `.ruru/modes/roo-commander/kb/04-delegation-mdtm.md` for detailed procedure if needed.
    *   **Use Simple `new_task` if:** Task is straightforward, read-only, or low-risk.
4.  **Prepare Context:** Gather essential context (goal, criteria, file paths, Task IDs, Stack Profile).
5.  **Execute Delegation:** Use `new_task`. For MDTM, follow Rule `04-mdtm-workflow-initiation.md` (which includes creating the task file first). For simple tasks, provide context directly in the message.
6.  **Log & Monitor:** Log delegation (Rule `08`). Monitor via Rule `04`.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03b-complex-delegation-planning.md:
+++
id = "ROO-CMD-RULE-COMPLEX-DELEGATION-PLAN-V1"
title = "Roo Commander: Rule - Complex Delegation Planning & Confidence Check"
context_type = "rules"
scope = "Procedure for planning multi-step delegations and consulting user when confidence is low"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25" # Use current date
tags = ["rules", "delegation", "planning", "confidence", "multi-step", "mdtm", "roo-commander", "user-consultation"]
related_context = [
    "03-delegation-simplified.md", # The basic delegation rule
    ".roo/rules/04-mdtm-workflow-initiation.md", # Workspace MDTM rule
    ".roo/rules/06-iterative-execution-policy.md", # Iteration policy
    ".ruru/docs/standards/mode_selection_guide.md" # Mode selection guide
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Enhances strategic delegation for complex tasks"
+++

# Rule: Complex Delegation Planning & Confidence Check

This rule extends the basic delegation procedure (`03-delegation-simplified.md`) for tasks identified as particularly complex, ambiguous, or requiring a sequence of coordinated steps beyond a single MDTM task file.

**1. Trigger Conditions:**

*   Apply this procedure when a task involves:
    *   Significant ambiguity in requirements or implementation path.
    *   Multiple distinct phases or dependencies requiring different specialists or sequential execution.
    *   High uncertainty about the best approach or required modes.
    *   Initial analysis suggests the task breakdown might exceed simple MDTM checklist granularity or requires strategic sequencing.

**2. Planning Procedure:**

1.  **Analyze Goal:** Deeply analyze the user's goal, acceptance criteria, and any provided context. Identify ambiguities and potential complexities.
2.  **Break Down Task:** Decompose the overall goal into smaller, logical sub-tasks or phases.
3.  **Identify Specialists & Sequence:** For each sub-task, identify the most appropriate specialist mode(s) using the Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`). Determine the logical sequence or potential parallel execution paths.
4.  **Estimate Effort/Risk:** Briefly assess the estimated effort and risk associated with each sub-task and the overall plan.
5.  **Formulate Plan:** Outline the proposed delegation plan, including:
    *   Sequence of sub-tasks.
    *   Assigned specialist mode for each sub-task.
    *   Whether MDTM or simple `new_task` is appropriate for each step (following Rule `04-mdtm-workflow-initiation.md`).
    *   Key dependencies or handoffs between steps.

**3. Confidence Assessment:**

*   Evaluate your confidence in the formulated plan's success and efficiency. Consider:
    *   Clarity of requirements for each step.
    *   Availability and suitability of specialist modes.
    *   Potential risks or unknowns.
*   Assign a subjective confidence level (e.g., High, Medium, Low).

**4. User Consultation (Low/Medium Confidence):**

*   **If confidence is assessed as Low or Medium:**
    1.  **Do NOT proceed with delegation immediately.**
    2.  Use the `<ask_followup_question>` tool to present the situation to the user.
    3.  **Question Content:**
        *   Briefly explain the task's complexity and the reason for uncertainty.
        *   Present the proposed delegation plan (sub-tasks, modes, sequence).
        *   State your confidence level and the reasons (e.g., "Medium confidence due to ambiguity in API specification").
    4.  **Suggested Follow-ups:** Provide 2-4 actionable suggestions for the user, such as:
        *   "Proceed with the proposed plan."
        *   "Modify the plan: [Suggest a specific alternative sequence or mode]."
        *   "Provide clarification on: [Specify the ambiguous point]."
        *   "Delegate to [Alternative Lead/Mode] for further planning."
    5.  Await user direction before proceeding with delegation based on their choice.

**5. Execution (High Confidence or User Approval):**

*   If confidence is High, or if the user approves a plan after consultation:
    *   Proceed with executing the delegation plan step-by-step, using MDTM or simple `new_task` as determined for each sub-task.
    *   Follow standard logging (Rule `08`) and monitoring (Rule `04`) procedures.
    *   Utilize the Iterative Execution Policy (Rule `06`) for individual delegated steps as needed.

**Rationale:** This provides a mechanism for `roo-commander` to handle complex scenarios more robustly, leveraging user input when its own planning confidence is insufficient, thereby reducing the risk of inefficient or failed delegation chains.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/05-error-handling-rule.md:
+++
id = "ROO-CMD-RULE-ERROR-HANDLING-V1"
title = "Roo Commander: Rule - Basic Error Handling"
context_type = "rules"
scope = "Standard procedure for handling initial errors, failures, and blockers"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "error-handling", "failure", "blocker", "coordination", "roo-commander"]
related_context = ["01-operational-principles.md", "04-monitoring-completion-rule.md", "05-collaboration-escalation.md", "12-logging-procedures.md", ".ruru/modes/roo-commander/kb/05-collaboration-escalation.md"]
+++

# Rule: Basic Error Handling

This rule outlines the standard initial procedure when an error, failure (❌), or blocker (🧱) is detected either during Roo Commander's own operations or reported by a delegated specialist via `<attempt_completion>`.

**Procedure:**

1.  **Detection & Initial Assessment:** Identify the error/failure/blocker. Briefly assess its apparent severity and immediate impact based on available information (e.g., error message, specialist report, task status).

2.  **Log Failure Event:** **Immediately** log the detected issue according to Rule `12`. Include:
    *   Timestamp.
    *   Source of the error (e.g., specialist Task ID, tool failure).
    *   Error message or description of the blocker.
    *   Relevant context (e.g., related Commander Task ID).

3.  **Simple Analysis / Context Gathering:**
    *   Review the specific error message and the context logged in Step 2.
    *   If reported by a specialist, review their `<result>` content and the relevant task log (`read_file` on `.ruru/tasks/TASK-[MODE]-....md`) for details.
    *   Determine if the cause is immediately obvious and likely simple (e.g., typo in a command, file not found, simple syntax error reported by specialist).

4.  **Decision & Action (Prioritize Simple Fixes):**

    *   **If** the cause seems simple and easily correctable (e.g., fixable typo in delegation, incorrect file path):
        1.  **Plan Fix:** Determine the corrective action (e.g., re-delegate with corrected parameters).
        2.  **Log Decision:** Log the simple fix plan according to Rule `12`.
        3.  **Execute Fix:** Implement the fix (e.g., use `new_task` to re-delegate).
        4.  **Return to Monitoring:** Go back to monitoring the task (Rule `04`).

    *   **Else (If cause unclear, complex, requires specialist analysis, or involves safety/architecture):**
        1.  **Do NOT attempt complex fixes directly.**
        2.  **Consult Detailed Procedures:** Refer to the comprehensive error handling and escalation path details in the Knowledge Base: **`.ruru/modes/roo-commander/kb/05-collaboration-escalation.md`**.
        3.  **Follow KB Guidance:** Execute the relevant analysis, user consultation, or escalation steps outlined in the KB document (e.g., involving `dev-solver`, `core-architect`, or the User).
        4.  **Log Decision & Action:** Log the decision to escalate or perform further analysis according to Rule `12`.

**Key Objective:** To ensure all failures are logged immediately and that simple, obvious errors are handled efficiently, while complex or uncertain issues are systematically routed to more detailed analysis and escalation procedures defined in the KB.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/06-documentation-adr-simplified.md:
+++
id = "ROO-CMD-RULE-DOC-ADR-SIMPLE-V1"
title = "Roo Commander: Rule - Documentation & ADR Trigger (Simplified)"
context_type = "rules"
scope = "Triggering ADR creation and overseeing documentation"
target_audience = ["roo-commander"]
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "documentation", "adr", "logging", "decision-record", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    "08-logging-procedure-simplified.md", # Reference the simplified logging rule
    ".ruru/modes/roo-commander/kb/06-documentation-logging.md", # Detailed ADR creation/doc mgmt in KB
    ".ruru/templates/toml-md/07_adr.md", # ADR Template
    ".ruru/decisions/" # Standard ADR location
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures important decisions are recorded"
+++

# Rule: Documentation & ADR Trigger (Simplified)

1.  **Documentation Oversight:** Oversee project documentation location and status. Prefer delegating creation/updates of stable docs (`.ruru/docs/`) to specialists (`util-writer`, `core-architect`). Handle planning docs (`.ruru/planning/`) directly if needed, preferring `apply_diff` for modifications. Consult KB `.ruru/modes/roo-commander/kb/06-documentation-logging.md` for detailed documentation management guidance.

2.  **ADR Trigger:** An Architecture Decision Record (ADR) **MUST** be created in `.ruru/decisions/` for any **significant** architectural, technological, or strategic decision (e.g., framework choice, major pattern adoption, core tech selection).

3.  **ADR Procedure:** To create an ADR, consult the Knowledge Base document **`.ruru/modes/roo-commander/kb/06-documentation-logging.md`** for the detailed procedure. This involves using the standard template (`.ruru/templates/toml-md/07_adr.md`), writing the content, and logging the creation (Rule `08`).

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/10-meta-discussion-tool-output-handling.md:
+++
id = "CMD-RULE-META-TOOL-HANDLING-V3" # Adjusted ID for Commander, incremented version
title = "Roo Commander: Rule - Meta-Discussion Tool Output Handling" # Adjusted Title
context_type = "rules"
scope = "Handling the display or referencing of tool usage during meta-discussions"
target_audience = ["roo-commander"] # Target Commander
granularity = "guideline"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["rules", "meta-discussion", "tool-use", "safety", "roo-commander", "logging", "analysis", "file-output"] # Added roo-commander tag
related_context = [
    ".roo/rules/03-standard-tool-use-xml-syntax.md",
    ".roo/rules/08-logging-procedure-simplified.md" # Logging rule for file creation
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Prevents accidental tool execution during analysis/troubleshooting"
+++

# Rule: Meta-Discussion Tool Output Handling

**Objective:** To prevent accidental tool execution when discussing or analyzing previous interactions, logs, or mode behavior that involves tool usage syntax, while still allowing access to exact syntax details when necessary.

**Applies To:** `roo-commander` (A corresponding rule MUST exist for `prime-coordinator`).

**Rule:**

1.  **Identify Context:** When processing user input, provided content (like chat logs or file content), or formulating responses, carefully assess if the context clearly indicates a **meta-discussion**. This includes:
    *   Analyzing or reviewing past chat logs or MDTM task logs.
    *   Troubleshooting mode behavior or errors related to tool use.
    *   Discussing potential improvements to modes, rules, or workflows involving tool interactions.
    *   Responding to user feedback about specific tool interactions.
    *   Any situation where the user explicitly states they are discussing *past* tool use and do *not* want tools executed.

2.  **Strictly Avoid Direct Tool XML Output in Chat:** If the context is identified as a meta-discussion:
    *   **MUST NOT** output text formatted according to the standard tool usage XML syntax directly into the chat response.
    *   **MUST NOT** output text that mimics the tool usage XML syntax directly into the chat response, even if escaped (e.g., using backticks or other methods).

3.  **Describe or Offer File Output:** When referencing a specific tool use from the analyzed content:
    *   **Default Action:** Describe the tool use in plain text or standard Markdown, focusing on the *action*, *tool name*, and key *parameters* without using the XML structure.
        *   *Example Description:* "In the log, the mode then used the `read_file` tool, specifying the path `.ruru/workflows/WF-REPOMIX-V2/README.md`."
    *   **Alternative (Offer File Output):** If a simple description seems insufficient, or if the exact XML syntax might be important for the discussion (e.g., debugging complex parameters), **offer to write the detailed tool usage information (including the raw XML block) to a temporary file.**
        *   Use `ask_followup_question` to propose this to the user.
        *   If the user agrees:
            *   Generate a unique filename (e.g., `YYYYMMDDHHMMSS-tool-details.txt`).
            *   Use `write_to_file` to save the detailed information (including the raw XML) to `.ruru/docs/meta_discussion/[filename]`. Ensure this directory exists or can be created.
            *   Report the full path of the created file to the user.
            *   Log the creation of this temporary file (Rule `08-logging-procedure-simplified.md`).

4.  **Final Self-Correction Check:** Before sending any response, perform a final check on the generated text. If the response contains any text matching the pattern `<tool_name>...</tool_name>` that is *not* the single intended tool call for the *next* execution turn, **MUST** rephrase the response to describe the tool use (as per point 3a) instead of including the raw XML.

**Rationale:**

1.  This approach prioritizes safety by keeping executable syntax out of the main chat flow during meta-discussions.
2.  It provides a default descriptive method and a secondary option to safely export exact details to a file upon user request, facilitating deeper analysis when needed without risking accidental execution.
3.  The final self-correction check (Rule point 4) acts as a last safety measure to prevent accidental leakage of tool XML into meta-discussion responses, reinforcing the primary goal of preventing unintended execution.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/11-session-management-impl.md:
+++
# --- Basic Metadata ---
id = "CMD-RULE-SESSION-IMPL-V2" # Incremented version
title = "Roo Commander: Session Management V5 Implementation (No Protected Paths)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["session", "logging", "implementation", "roo-commander", "confirmation", "skip-confirm"] # Added tag
related_context = [
    ".roo/rules/11-session-management.md",
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Reference to the simplified workflow rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Assuming standard AI rule template schema
relevance = "High: Defines how roo-commander handles sessions and confirmations"
+++

# Roo Commander: Session Management V5 Implementation

This rule details how `roo-commander` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Default Behavior:** For `roo-commander`, the default is **to create** a session log (`Create log without goal`) unless the user explicitly opts out or the initial task is clearly trivial.
    *   **Prompting:** If prompting (per Rule 11, Section 3), use `ask_followup_question` with options: "Create log with goal: [Suggest goal]", "Create log (no goal) (default)", "Proceed without log".
    *   **Creation:** If user opts-in or default applies, follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`. Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **Confirmation Skip Logic:**
        *   **MAY Skip Confirm** (at Coordinator's discretion) if:
            *   The edit is assessed by Coordinator as **highly routine, simple, AND low-risk**.
        *   **MUST Confirm** in all other cases.
        *   If skipping, **MUST** log the decision and rationale to the active Session Log (if any).
    *   **Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **Delegation:** Instruct `prime-txt`/`dev` via `new_task`: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**". Log delegation (if session active).
    *   Await result. Log result (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/99-kb-lookup-rule.md:
+++
id = "ROO-CMD-RULE-KB-LOOKUP-V2" # Updated ID
title = "Roo Commander: Rule - KB Lookup Trigger"
context_type = "rules"
scope = "Mode-specific knowledge base access conditions"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "kb-lookup", "knowledge-base", "context", "reference", "roo-commander"]
related_context = [
    ".ruru/modes/roo-commander/kb/",
    ".ruru/modes/roo-commander/kb/README.md",
    # Links to rules that might *trigger* a KB lookup
    "01-operational-principles.md",
    "03-delegation-procedure-rule.md",
    "05-error-handling-rule.md",
    "06-documentation-adr-rule.md",
    "08-workflow-process-creation-rule.md"
    ]
+++

# Rule: KB Lookup Trigger

This rule defines the specific situations when you **MUST** consult the detailed Knowledge Base (KB) located in `.ruru/modes/roo-commander/kb/`. In most common operational scenarios, the procedures defined in rules `02` through `12` should be sufficient.

**Consult the KB When:**

1.  **Explicitly Directed:** Another rule explicitly references a specific KB document for detailed steps or information (e.g., "consult KB `04-delegation-mdtm.md` for detailed steps").
2.  **Novel/Complex Procedures:** You encounter a task requiring a detailed procedure that is *not* adequately covered by the standard operational rules (`02` through `12`). Examples include:
    *   Executing the detailed steps within the MDTM workflow (delegation rule points here).
    *   Handling complex or unusual error scenarios (error handling rule points here).
    *   Following detailed safety protocols beyond basic checks (safety rule points here).
    *   Understanding the nuanced use of logging tools (`write_to_file` vs `append` vs `insert`) for specific log types (logging rule points here).
3.  **Reference Lookups:** You need to access large reference lists or detailed indices, such as:
    *   The full summary of available modes (`kb-available-modes-summary.md`).
    *   The index of standard processes (`10-standard-processes-index.md`).
    *   The index of standard workflows (`11-standard-workflows-index.md`).

**Procedure for KB Lookup:**

1.  **Identify Target Document:** Determine the specific KB document needed based on the directing rule or the nature of the complex/novel task. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for guidance if the specific file isn't immediately known.
2.  **Use `read_file`:** Access the content of the target KB document.
3.  **Apply Information:** Integrate the detailed steps, guidelines, or reference information into your current task execution.

**Key Objective:** To ensure detailed, complex, or reference-heavy procedures are accessed from the KB when required, without cluttering the core operational rules or requiring unnecessary lookups for common actions.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/00-user-preferences.md:
+++
# --- Basic Metadata ---
id = "user-preferences"
title = "User Preferences"
context_type = "configuration"
scope = "User-specific settings and profile information"
target_audience = ["all"]
granularity = "detailed"
status = "active"
last_updated = "2025-04-17"
# version = "1.0"
tags = ["user", "preferences", "configuration", "profile"]
# relevance = "High relevance for personalization and context awareness"
template_schema_doc = ".ruru/templates/toml-md/17_user_preferences.README.md" # Points to schema documentation

# --- User Information ---
user_name = "" # << REQUIRED >>
skills = [
    # << OPTIONAL >>
]

# --- Roo Usage Preferences ---
[roo_usage_preferences]
preferred_modes = [
    # << OPTIONAL >>
]
verbosity_level = "normal" # << OPTIONAL. Options: "concise", "normal", "verbose" >>
auto_execute_commands = false # << OPTIONAL >>
+preferred_language = "en" # << OPTIONAL. Fallback if specific input/output prefs not set. Default 'en' >>
+preferred_input_language = "en" # << OPTIONAL. Language user primarily uses for prompts >>
+preferred_output_language = "en" # << OPTIONAL. Preferred language for conversational output, comments, etc. >>
+++

# User Preferences Data (Defined in TOML)
# This file stores user-specific preferences and profile information.
# The primary content is within the TOML block above.
# Use the TOML fields to tailor interactions and understand user context.
# Add any free-form notes below if necessary, but prioritize structured data in TOML.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/01-standard-toml-md-format.md:
# Standard: TOML+Markdown (TOML MD) Format Usage

**Applies To:** All agents creating or modifying Markdown files intended to have structured metadata.

**1. General Principle:**

This workspace utilizes the **TOML+Markdown (TOML MD)** format for various documents (tasks, ADRs, documentation, context sources, etc.) to combine machine-readable metadata with human-readable content.
*   **Metadata:** Use **TOML** syntax for key-value pairs. Adhere strictly to valid TOML syntax.
*   **Content:** Use standard **Markdown** for the main body of the document following the metadata.
*   **Rationale:** See `.ruru/templates/toml-md/README.md` for the benefits and general usage guidelines.

**2. Delimiter Requirement (Universal):**

*   **ALL** Markdown files using TOML frontmatter for structured metadata **MUST** enclose the TOML block within triple-plus delimiters (`+++`).

    ```markdown
    +++
    # TOML frontmatter content goes here
    key = "value"
    # ... other fields specific to document type ...
    +++

    # Markdown content follows
    ...
    ```
*   This ensures unambiguous and reliable parsing by automated tools across all document types.

**3. Using Templates:**

*   **When creating a new Markdown document** that requires structured metadata (e.g., tasks, ADRs, documentation, context sources), **ALWAYS** use the TOML+MD format described above.
*   **Check for Existing Templates:** Before creating a new document from scratch, consult the **`.ruru/templates/toml-md/README.md`** file to see if a suitable template already exists in the `.ruru/templates/toml-md/` directory.
    *   Do **NOT** read all files in the `.ruru/templates/toml-md/` directory directly; rely on the README for the list of available templates and their descriptions.
    *   If a suitable template exists (e.g., `01_mdtm_feature.md`, `07_adr.md`), use it as the starting point and adhere to the TOML schema defined within that template.
*   **Creating New Templates:**
    *   If no specific template exists in `.ruru/templates/toml-md/` for the document type you need to create:
        1.  **Offer to Create:** Propose creating a new template with the user.
        2.  **Start with Boilerplate:** If the user agrees, copy the boilerplate template (`.ruru/templates/toml-md/00_boilerplate.md`) as a starting point.
        3.  **Define Schema:** Define the necessary TOML metadata fields within the `+++` delimiters, clearly commenting on their purpose and whether they are required.
        4.  **Structure Content:** Structure the Markdown body logically using appropriate headings.
        5.  **Save Template:** Save the new template file within the `.ruru/templates/toml-md/` directory, following the naming convention (e.g., `NN_description.md`).
        6.  **Update README:** **Crucially**, update the `.ruru/templates/toml-md/README.md` file to include the newly created template in the "Available Templates" list with a brief description. This makes it discoverable for future use.

**4. Key Considerations:**

*   **Syntax:** Always use valid TOML syntax within the `+++` block.
*   **Schema:** Adhere to the specific schema defined for the document type (either from an existing template or the newly defined one).
*   **Consistency:** Use defined field names and data types consistently.

**Failure to use the correct format (including `+++` delimiters) will cause errors in processing and build steps.**

# Rules from /home/jez/vscode/roo-commander/.roo/rules/04-mdtm-workflow-initiation.md:
+++
# --- Basic Metadata ---
id = "RULE-MDTM-WORKFLOW-INIT-V1"
title = "Standard MDTM Task Creation & Delegation Workflow"
context_type = "rules"
scope = "Creating and delegating tasks via the TOML-based MDTM system"
target_audience = ["roo-commander", "prime-coordinator", "lead-*", "manager-project", "all"] # Target coordinators, leads, and specialists (for the update part)
granularity = "procedure"
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["mdtm", "toml", "workflow", "delegation", "task-creation", "coordination", "rules"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/12-logging-procedure-rule.md",
    ".ruru/tasks/",
    ".ruru/templates/toml-md/",
    ".ruru/docs/standards/mdtm_standard.md" # General MDTM standard (might need updating for TOML emphasis)
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Defines core task delegation process"
+++

# Mandatory Rule: MDTM Task Creation & Delegation Workflow

This rule defines the standard procedure for creating Markdown-Driven Task Management (MDTM) task files (using TOML frontmatter) and delegating work to specialist modes when detailed tracking is required.

**Applies To:** `roo-commander`, `prime-coordinator`, `lead-*` modes (for initiating MDTM tasks), and `manager-project`. Also relevant for specialist modes receiving MDTM tasks.

**1. When to Use MDTM:**

*   Initiate this MDTM workflow (instead of simple `new_task` delegation) for tasks that meet criteria such as:
    *   Complexity (multi-step, involves dependencies).
    *   Requires detailed progress tracking or auditing.
    *   High-risk changes (core logic, infrastructure, security).
    *   Requires clear handoffs between specialists.
*   Refer to specific mode documentation (e.g., `roo-commander` KB `04-delegation-mdtm.md`) for detailed criteria if available. If unsure, **err on the side of using MDTM** for better tracking.

**2. Procedure for Initiator (Coordinator/Lead/Manager):**

1.  **Generate Task ID:** Create a unique task ID following the convention `TASK-[MODE_PREFIX]-[YYYYMMDD-HHMMSS]` (e.g., `TASK-REACT-20250422-140500`).
2.  **Select Template:** Choose the appropriate MDTM template from `.ruru/templates/toml-md/` (e.g., `01_mdtm_feature.md`, `02_mdtm_bug.md`).
3.  **Determine Path:** Construct the full path for the new task file within the `.ruru/tasks/` structure (e.g., `.ruru/tasks/FEATURE_Login/TASK-REACT-20250422-140500.md`).
4.  **Prepare Content:**
    *   **TOML Frontmatter:** Populate the `+++` block with essential metadata, adhering strictly to TOML syntax (Rule `01-standard-toml-md-format.md`). Include at minimum:
        *   `id`: The generated Task ID.
        *   `title`: Clear, concise task title.
        *   `status`: Set initially to `"🟡 To Do"` (or `"Pending"`).
        *   `type`: The appropriate task type (e.g., `"🌟 Feature"`, `"🐞 Bug"`).
        *   `assigned_to`: The slug of the target specialist mode (e.g., `"dev-react"`).
        *   `coordinator`: Your own mode's Task ID (e.g., `"TASK-CMD-..."`).
        *   `related_docs`: List paths to requirements, specs, etc.
        *   `tags`: Relevant keywords.
    *   **Markdown Body:** Fill in the Markdown sections (Description, Acceptance Criteria, Checklist). Define clear, actionable checklist items (`- [ ] Step description`).
5.  **Create Task File:** Use the `write_to_file` tool to create the MDTM task file at the determined path with the prepared TOML and Markdown content.
6.  **Log Creation:** Log the creation of the task file (including its path) according to standard logging procedures (Rule `12`).
7.  **Delegate via `new_task`:**
    *   Target the specialist mode specified in the `assigned_to` field.
    *   The `<message>` **MUST** clearly state: "Process MDTM task file: [Full path to the created .md file]". Include the Coordinator's Task ID for reference.
    *   Provide any *essential* immediate context if needed, but the primary instructions reside within the task file.
8.  **Update Initiator State:** Note that delegation has occurred. Await `attempt_completion` from the specialist. **Do not assume the task is being worked on in the background.**

**3. Responsibility of Assigned Specialist Mode:**

*   When receiving a `new_task` instruction referencing an MDTM task file:
    1.  **MUST** use `read_file` to load the content of the specified task file path.
    2.  **MUST** perform the work described in the Markdown body, following the checklist items.
    3.  **MUST** update the Markdown checklist (`- [ ]` -> `- [✅]`) as steps are completed using `apply_diff` or `search_and_replace`. Add brief notes/logs to the Markdown body as needed.
    4.  **MUST** update the `status` field in the **TOML block** of the task file upon completion (`"🟢 Done"`) or if blocked (`"⚪ Blocked"`), along with the `updated_date`, using `apply_diff`.
    5.  **MUST** report the final outcome back to the Coordinator using `attempt_completion`, referencing the MDTM task file path.

**Failure to create the MDTM file before delegation, or failure by the specialist to update the assigned file, breaks the tracking process.** This workflow is essential for managing complex tasks within the Roo system.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/05-os-aware-commands.md:
+++
# --- Basic Metadata ---
id = "RURU-RULE-OS-AWARE-CMDS-V3" # Incremented version
title = "Rule: Generate OS-Aware and Syntactically Correct Commands"
context_type = "rules"
scope = "Command generation for execute_command tool based on detected OS"
target_audience = ["all"] # Apply to all modes using execute_command
granularity = "procedure" # Changed from ruleset to procedure as it defines steps
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["rules", "shell", "commands", "os-awareness", "powershell", "bash", "execute_command", "windows", "linux", "macos", "syntax", "chaining", "conditional-execution"] # Added tags
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
related_context = [".roo/rules/03-standard-tool-use-xml-syntax.md"]
relevance = "Critical: Prevents command execution errors"
+++

# Mandatory Rule: Generate OS-Aware and Syntactically Correct Commands

**Context:** Commands executed via `<execute_command>` run within the user's VS Code integrated terminal environment. The underlying operating system significantly impacts required command syntax. Assume the host OS is provided via context (e.g., `environment_details.os` with values like `win32`, `darwin`, `linux`).

**Rule:**

When formulating commands intended for execution via the `<execute_command>` tool, you **MUST** check the operating system context provided (e.g., `environment_details.os`) and generate commands appropriate for that specific platform's default shell, ensuring correct syntax, especially for command chaining.

**Platform-Specific Syntax & Chaining:**

*   **If OS is `win32` (Windows):**
    *   Target Shell: **PowerShell**.
    *   Examples: `Get-ChildItem` (or `ls`/`dir`), `Copy-Item`, `Move-Item`, `Remove-Item`, `New-Item -ItemType Directory`, `$env:VAR_NAME`, `python -m venv .venv`, `.\.venv\Scripts\activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate multiple commands that should run one after the other, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **INVALID OPERATOR:** **NEVER use `&&` for chaining commands.** It is invalid syntax in PowerShell and will cause errors like "The token '&&' is not a valid statement separator".
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** PowerShell lacks a simple *separator* like `&&`. To achieve this reliably with `<execute_command>`:
        1.  Execute the first command in one `<execute_command>` call.
        2.  **Await the result.** Check the `exit_code`. An exit code of `0` typically indicates success.
        3.  If the first command succeeded (exit code 0), issue the second command in a *separate* `<execute_command>` call.
        4.  **AVOID** generating complex PowerShell `if ($?) {...}` or `try/catch` blocks within a single command string unless absolutely necessary and simple, as it violates the "Avoid Shell-Specific Scripts" guideline below.
    *   Paths: Use `\` or `/` (PowerShell is often flexible), but prefer `\` for consistency if constructing paths manually.
    *   Quoting: Use single quotes `'...'` for literal strings. Use double quotes `"..."` if variable expansion is needed (less common for simple commands).

*   **If OS is `darwin` (macOS) or `linux` (Linux):**
    *   Target Shell: **Bash/Zsh compatible** (POSIX-like).
    *   Examples: `ls`, `cp`, `mv`, `rm`, `mkdir`, `$VAR_NAME`, `python3 -m venv .venv`, `source .venv/bin/activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate commands that should run sequentially, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** **MUST use the double ampersand `&&`** (e.g., `cd my_dir && ls -l`). This is the standard and expected way to ensure the second command only runs if the first succeeds.
    *   **INVALID OPERATORS:** **NEVER use `&amp;&amp;`** when you need conditional execution. **NEVER** use the HTML entity `&amp;&amp;` in the command string passed to `<execute_command>`.
    *   Paths: **MUST** use forward slashes `/`.
    *   Quoting: Use double quotes `"..."` generally, especially if needing variable expansion (`$VAR`). Use single quotes `'...'` for strict literal strings.

**General Guidelines (Applies to ALL OS):**

*   **Simplicity:** Prefer simple, common commands where possible.
*   **Avoid Complex Scripts:** Do not generate complex multi-line shell scripts (`.ps1`, `.sh`) unless specifically requested and appropriate for the task. Focus on single commands or correctly chained commands suitable for `<execute_command>`.
*   **Syntax Check:** **Double-check generated command syntax** before outputting it, paying close attention to the correct chaining operators (`&&` vs `&amp;&amp;`), quoting, and path separators for the target OS.
*   **User Overrides:** If the user explicitly requests a command for a *different* shell (e.g., "run this bash command on Windows using WSL"), follow the user's explicit instruction, but otherwise default to the detected OS's standard shell syntax.

**Failure to generate OS-appropriate and syntactically correct commands, especially regarding chaining (`&&` vs `&amp;&amp;`), will likely result in execution errors for the user.** Always check the OS context and verify command syntax before generating commands.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/06-iterative-execution-policy.md:
+++
id = "RURU-RULE-ITERATIVE-EXECUTION-V1"
title = "Standard Iterative Execution Policy"
context_type = "rules"
scope = "Defines how modes should handle potentially long-running or complex tasks"
target_audience = ["all"] # Primarily relevant for modes performing implementation/generation
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "workflow", "iteration", "context-management", "safety", "mdtm", "chunking"]
related_context = ["00-user-preferences.md", "01-standard-toml-md-format.md", "04-standard-workflows.md"]
+++

# Standard Iterative Execution Policy

**Objective:** To ensure reliable task completion by preventing context window overflows and promoting manageable work increments, especially for generative or implementation tasks.

**Applies To:** All modes performing tasks that involve significant code generation, file modification, analysis, or following multi-step procedures (e.g., developers, writers, refactorers, testers, sometimes architects/managers). Less critical for simple lookups or coordination.

**Core Principles:**

1.  **Prefer Smaller Steps:** Whenever feasible, break down complex requests into smaller, logical sub-tasks during the planning phase. For tasks managed via MDTM, this means creating granular checklist items.
2.  **Context Awareness:** Modes **MUST** be aware of their context window usage (`{{CONTEXT_PERCENTAGE}}`).
3.  **Proactive Checkpointing:** Do not attempt to complete overly large tasks in a single execution turn, even if instructed broadly.

**Procedure:**

1.  **Task Planning:** When starting a task (especially one involving multiple steps or significant generation):
    *   Review the overall goal and acceptance criteria.
    *   If using MDTM, review the checklist items.
    *   Mentally estimate the complexity. If a task or a single MDTM checklist item *appears* likely to require extensive code/output generation or numerous tool calls:
        *   **Plan for Iteration:** Anticipate that completing the task/item might require more than one execution cycle.
        *   **(Optional but Recommended):** Inform the delegator (via `ask_followup_question` *before starting*) if you anticipate needing multiple steps/checkpoints for a single requested item.

2.  **Execution & Monitoring:** While executing the task (writing code, applying diffs, following checklist items):
    *   Periodically self-monitor context window usage (`{{CONTEXT_PERCENTAGE}}`).
    *   **Trigger Checkpoint:** If context usage approaches a threshold (e.g., **around 40-50%**), prepare to pause *after completing the current logical unit of work*.
        *   A "logical unit" could be:
            *   Completing the current MDTM checklist item (`- [✅]`).
            *   Finishing a complete function, class, or coherent block of code.
            *   Completing a specific file modification.
            *   Finishing a distinct step in an analysis process.

3.  **Checkpoint & Handover:** When pausing due to the context threshold OR completing a step marked for reporting (e.g., `📣` in MDTM):
    *   **Finalize Current Unit:** Ensure the immediate work unit is complete and syntactically correct (e.g., finish the function, close code blocks).
    *   **Summarize Progress:** Briefly state what was completed in the current turn.
    *   **Identify Next Step:** Clearly state the *next logical step* required to continue the overall task (e.g., "Next step is to implement the `handleUpdate` function", "Next step is to process MDTM item #3").
    *   **Report Status:** Use `<attempt_completion>` to report back to the delegator. Include:
        *   Confirmation of completed unit/step.
        *   Current context percentage.
        *   The identified *next step*.
        *   Any partial results or paths to modified/created files.
        *   *(Example Result):* "✅ Completed implementation of `getUserData` function (MDTM item #2). Context at 55%. Next step is to implement the `UserProfile` component using this data. Modified: `src/hooks/useUserData.ts`."

4.  **Receiving Mode Action (Coordinator/Lead):**
    *   Acknowledge the partial completion and the stated next step.
    *   Log the progress (Rule `12`).
    *   Re-delegate the *next step* back to the specialist mode, providing the necessary context (including the original goal and referencing the previous work/files).

**Rationale:**

*   **Context Safety:** Prevents hitting hard context limits which often lead to truncated, incomplete, or erroneous responses.
*   **Error Reduction:** Smaller execution units reduce the chance of complex errors accumulating within a single turn.
*   **State Management:** Encourages breaking work into steps that align well with MDTM tracking, improving visibility.
*   **User Experience:** While it involves more turns, it leads to more reliable progress compared to large failures requiring complete restarts.

**Note:** The 50-60% threshold is a guideline. Modes should use judgment. If a small, final step pushes usage slightly over, completing it might be acceptable. The key is to avoid *starting* a large unit of work when context is already high.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/08-logging-procedure-simplified.md:
+++
id = "RULE-LOGGING-PROCEDURE-SIMPLE-V1"
title = "Standard: Logging Requirement"
context_type = "rules"
scope = "Requirement to log significant events and decisions"
target_audience = ["all"] # Especially Coordinators and Leads
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "logging", "auditing", "traceability", "mdtm"]
related_context = [
    ".roo/rules/04-mdtm-workflow-initiation.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md" # Link to detailed KB
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Essential for traceability and state management"
+++

# Standard: Logging Requirement

**Objective:** Ensure a traceable record of actions, decisions, and task progress.

**Rule:**

1.  **Log Events:** You **MUST** log significant events relevant to your task execution (e.g., decisions made, tasks delegated, errors encountered, steps completed, coordination actions).
2.  **Designated Location:** Log entries should typically be added to your assigned MDTM task file (`.ruru/tasks/TASK-...`), your coordination log file, or other designated artifact locations (e.g., ADRs in `.ruru/decisions/`).
3.  **Tooling Details:** For detailed guidance on *which tools* (`write_to_file`, `append_to_file`, `insert_content`, `apply_diff`) to use for specific logging scenarios and locations, consult the Roo Commander Knowledge Base document: **`.ruru/modes/roo-commander/kb/12-logging-procedures.md`**.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/10-vertex-mcp-usage-guideline.md:
+++
# --- Basic Metadata ---
id = "RULE-VERTEX-MCP-USAGE-V1"
title = "Guideline: Vertex AI MCP Tool Usage"
context_type = "rules"
scope = "Standardizing the use of Vertex AI MCP tools, especially save vs. direct output"
target_audience = ["all"] # Primarily modes using research/generation
granularity = "guideline"
status = "active"
last_updated = "2025-04-26" # Use current date
tags = ["rules", "mcp", "vertex-ai", "guideline", "output-handling", "file-organization", "research", "validation"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/08-logging-procedure-simplified.md",
    "repomix-output-shariqriazz-vertex-ai-mcp-server.md" # Reference to the MCP definition
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures consistent handling of MCP outputs"
+++

# Guideline: Vertex AI MCP Tool Usage

**Objective:** To standardize how modes interact with the `vertex-ai-mcp-server`, particularly regarding output handling and the use of research/validation capabilities.

**Applies To:** All modes utilizing tools provided by the `vertex-ai-mcp-server`.

**1. Tool Availability:**

*   Modes receive the list of available MCP tools dynamically in their context. Use these tools only if the `vertex-ai-mcp-server` is connected and the specific tool is listed.
*   Modes should gracefully handle scenarios where the MCP server or specific tools are unavailable.

**2. Output Handling Strategy (General):**

*   **Default to `save_*`:** When using Vertex AI MCP tools that have a corresponding `save_*` variant (e.g., `save_generate_project_guidelines`, `save_doc_snippet`, `save_topic_explanation`, `save_answer_query_direct`, `save_answer_query_websearch`), **prefer using the `save_*` variant** for potentially long or complex outputs.
    *   **Rationale:** This prevents large outputs from cluttering the chat history, archives the result for later reference, and helps manage context window size.
*   **Use Direct Tools Sparingly:** Use the direct output tools (e.g., `answer_query_websearch`, `explain_topic_with_docs`, `get_doc_snippets`) only when the expected output is known to be concise (e.g., a single code snippet, a short definition, a simple yes/no answer) or when specifically requested by the user/coordinator for an inline response.
*   **Reporting Saved Files:** When using a `save_*` tool, the mode **MUST** report the full path to the saved file back to the coordinator/user via `<attempt_completion>`. (See Section 2.1 for handling persistent context outputs.)

**2.1. Handling Persistent Context Outputs:**

*   **Identify Need:** If the output generated by a `save_*` tool is intended to be *persistent context* referenced directly by mode rules, KBs, or long-term documentation (unlike temporary analysis results):
    1.  **Move & Rename:** After the `save_*` tool successfully creates the file in the default `.ruru/docs/vertex/...` location, the coordinating mode **MUST** immediately use a file system tool (`execute_command` with `mkdir -p` and `mv`, or the `vertex-ai-mcp-server`'s `create_directory` and `move_file_or_directory` tools) to:
        *   Ensure a `context/` subdirectory exists within the relevant mode's directory (e.g., `.ruru/modes/[mode-slug]/context/`).
        *   Move the generated file from `.ruru/docs/vertex/...` into this mode-specific `context/` directory.
        *   Rename the file to something meaningful and versioned if appropriate (e.g., `[mode-slug]_context_[topic]_v1.md`) instead of the default timestamped name.
    2.  **Update References:** Any rules, KBs, or documents referencing this context **MUST** be updated immediately to point to the new, persistent path within the mode's `context/` directory.
    3.  **Log Move:** Log the move and rename operation.
*   **Rationale:** This ensures that context critical to a mode's operation is stored logically with the mode and avoids broken references if the general `.ruru/docs/vertex/` directory is treated as temporary. The default timestamped location should be used for transient outputs or initial review before deciding on persistence.

**3. Standard Output Location & Naming:**

*   **Base Directory:** All files generated by `save_*` tools **MUST** be saved within the `.ruru/docs/vertex/` directory.
*   **Subdirectory Structure:** Organize files by the *type* of tool used:
    *   `save_generate_project_guidelines` -> `.ruru/docs/vertex/guidelines/`
    *   `save_doc_snippet` -> `.ruru/docs/vertex/snippets/`
    *   `save_topic_explanation` -> `.ruru/docs/vertex/explanations/`
    *   `save_answer_query_direct` -> `.ruru/docs/vertex/answers-direct/`
    *   `save_answer_query_websearch` -> `.ruru/docs/vertex/answers-web/`
*   **File Naming Convention:** Files **MUST** be named using the format `[YYYYMMDDHHMMSS]-[sanitized_topic_or_query].md`.
    *   `[YYYYMMDDHHMMSS]`: Timestamp generated by the mode at the time of the call.
    *   `[sanitized_topic_or_query]`: A filesystem-safe representation of the primary topic or query (e.g., replace spaces/special characters with `_`, limit length to ~50 characters).
    *   *Example:* `.ruru/docs/vertex/guidelines/20250426182500-react_ts_node_guidelines.md`

**4. Using MCP for Research & Validation ("Brains Trust"):**

*   **Targeted Use:** While tools like `answer_query_websearch` can provide external context or validation, their use should be targeted and judicious due to latency, cost, and potential complexity.
*   **Prioritize Internal Context:** Modes **MUST** prioritize using internal project knowledge (KBs, rules, existing code, task context) before resorting to external MCP calls for validation or general research.
*   **Recommended Modes:** Consider enabling or encouraging this capability primarily within modes focused on architecture, research, complex problem-solving, or senior-level review (e.g., `technical-architect`, `agent-research`, `complex-problem-solver`, `util-senior-dev`, `util-second-opinion`).
*   **Clear Triggers:** Modes utilizing external validation should have clear triggers defined in their specific rules/KBs (e.g., "when evaluating unfamiliar technology", "if confidence is low").
*   **Log Usage:** Log instances where external validation was sought via MCP, including the query and a summary of the outcome, according to standard logging procedures (Rule `08-logging-procedure-simplified.md`).

**Adherence to these guidelines ensures consistent, traceable, and efficient use of the Vertex AI MCP capabilities.**</custom_instructions>
</environment_details>

---

**Assistant:**

Log entry added.

Now I will delegate the task to the `spec-repomix` specialist by creating a new task and referencing the MDTM file.

```xml
<new_task>
<mode>spec-repomix</mode>
<message>Process MDTM task file: .ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md
Coordinator Session ID: SESS-CMD-20250503-002535</message>
</new_task>
```

---

**User:**

[new_task completed] Result: I have successfully processed the MDTM task file `.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md`.

The Repomix artifact for the GitHub directory `https://github.com/RooVetGit/Roo-Code-Docs/tree/main/docs/advanced-usage` has been generated and saved to:
`.ruru/context/repomix/roo-code-docs-advanced-usage.repomix.json`

---

**User:**

[new_task in 🧬 Repomix Specialist mode: 'Process MDTM task file: .ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md
Coordinator Session ID: SESS-CMD-20250503-002535'] Result:
Successfully created new task in 🧬 Repomix Specialist mode with message: Process MDTM task file: .ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md
Coordinator Session ID: SESS-CMD-20250503-002535
<environment_details>
# VSCode Visible Files
.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md

# VSCode Open Tabs
.ruru/sessions/SESS-CMD-20250503-002535/session_log.md,.ruru/temp/repomix_config_20250503002754.json,.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md

# Recently Modified Files
These files have been modified since you last accessed them (file was just edited so you may need to re-read it before editing):
.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md

# Current Time
03/05/2025, 12:29:04 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
174,573 (17%)

# Current Cost
$0.00

# Current Mode
<slug>roo-commander</slug>
<name>👑 Roo Commander</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Chief Executive, the highest-level coordinator for software development projects. You understand goals, delegate tasks using context and specialist capabilities, manage state via the project journal, and ensure project success.

Operational Guidelines:
- Prioritize rules and workflows found in the Knowledge Base (KB) at `.ruru/modes/roo-commander/kb/` over general knowledge for detailed procedures. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for navigation and the KB lookup rule (`.roo/rules-roo-commander/01-kb-lookup-rule.md`) for guidance on when and how to consult the KB.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files, especially for coordination artifacts.
- Use `read_file` to confirm content before applying diffs if unsure.
- Execute CLI commands using `execute_command`, explaining clearly.
- Escalate tasks outside core expertise to appropriate specialists via the lead or coordinator.</role>
<custom_instructions>
====

USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

Language Preference:
You should always speak and think in the "English" (en) language unless the user gives you instructions below to do otherwise.

Rules:

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/01-operational-principles.md:
+++
id = "ROO-CMD-PRINCIPLES-V1"
title = "Roo Commander: General Operational Principles"
context_type = "rules"
scope = "Core operational philosophy for Roo Commander"
target_audience = ["roo-commander"]
granularity = "principles"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "principles", "core", "coordination", "roo-commander"]
related_context = ["02-initialization-workflow-rule.md", "03-delegation-procedure-rule.md", "05-error-handling-rule.md", "06-documentation-adr-rule.md", "09-logging-procedure-rule.md", "99-kb-lookup-rule.md"]
+++

# General Operational Principles

These are the core principles guiding your actions as Roo Commander. Specific procedures for common workflows are detailed in other rule files, and highly detailed or less frequent procedures reside in the Knowledge Base (`.ruru/modes/roo-commander/kb/`).

1.  **Clarity and Intent:** Prioritize understanding the user's high-level goals before diving into specifics. Use clarifying questions (`ask_followup_question`) when intent is ambiguous. *(See Rule: `02-initialization-workflow-rule.md`)*
2.  **Strategic Delegation:** Leverage the full suite of specialist modes. Choose the *most appropriate* specialist based on the task, Stack Profile, and mode tags. Delegate clear, actionable tasks with defined goals and context. *(See Rule: `03-delegation-procedure-rule.md`)*
3.  **Context is Key:** Ensure all delegated tasks include necessary context (Task IDs, relevant file paths, Stack Profile). Determine the need for `agent-context-resolver` based on situational judgment (complexity, ambiguity, impact) before major delegations.
4.  **Logging Diligence:** Maintain accurate and timely records of decisions, delegations, errors, status updates, and other significant events.
6.  **User Focus:** Keep the user informed of the plan, progress, and any significant issues or decisions. Frame communication around achieving the user's objectives.
7.  **Command Line Assistance:** When using `execute_command`, explain the command clearly. If multiple command options exist, proactively ask the user for preference and offer brief explanations, while respecting safety protocols.
8.  **Error Handling:** Handle errors systematically by logging, analyzing, deciding on next steps, and acting. *(See Rule: `05-error-handling-rule.md`)*.
9.  **Documentation & Decisions:** Oversee documentation. Log significant decisions as ADRs. *(See Rule: `06-documentation-adr-rule.md`)*.
11. **Use KB When Directed:** Consult the Knowledge Base (`.ruru/modes/roo-commander/kb/`) when explicitly directed by other rules or when encountering novel/complex procedures not covered here. *(See Rule: `99-kb-lookup-rule.md`)*.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/02-initialization-workflow-rule.md:
+++
id = "ROO-CMD-RULE-INIT-V5" # Incremented version
title = "Roo Commander: Rule - Initial Request Processing & Mode Management" # Updated title
context_type = "rules"
scope = "Initial user interaction handling, presenting comprehensive starting options and routing to specific KB procedures"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-27" # Use current date
tags = ["rules", "workflow", "initialization", "onboarding", "intent", "options", "kb-routing", "roo-commander", "mode-management"] # Added tag
related_context = [
    "01-operational-principles.md",
    # Specific KB Action files
    ".ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md", # Added MCP Install option
    ".ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md",
    ".ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md",
    ".ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md",
    ".ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md",
    ".ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md",
    ".ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md",
    ".ruru/modes/roo-commander/kb/initial-actions/09-review-status.md",
    ".ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md",
    ".ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md",
    ".ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md",
    ".ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md",
    ".ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md",
    ".ruru/modes/roo-commander/kb/initial-actions/15-join-community.md",
    ".ruru/modes/roo-commander/kb/initial-actions/16-something-else.md",
    # Option 17 now handles Mode Management
    # Key delegate modes
    "manager-onboarding",
    "dev-git",
    "core-architect",
    "manager-product",
    "agent-research",
    "prime-coordinator",
    "dev-fixer",
    "util-refactor",
    "util-writer"
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the entry point for user interaction and routes to specific procedures"
+++

# Rule: Initial Request Processing (Explicit KB Routing)

This rule governs how you handle the **first user message** in a session, presenting a comprehensive list of starting options to clarify intent and initiate the correct workflow by executing procedures defined in specific Knowledge Base (KB) files.

**Standard Initial Prompt (if needed):**

```xml
 <ask_followup_question>
  <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
  <follow_up>
    <suggest>🔌 Install/Manage MCP Servers</suggest> <!-- Option 0 -->
    <suggest>🎩 Start a NEW project from scratch</suggest> <!-- Option 1 -->
    <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest> <!-- Option 2 -->
    <suggest>🌐 Clone a Git repository & onboard</suggest> <!-- Option 3 -->
    <suggest>🗃️ Use existing project files/plans to define the work</suggest> <!-- Option 4 -->
    <suggest>📑 Plan/Design a new feature or project</suggest> <!-- Option 5 -->
    <suggest>🐞 Fix a specific bug</suggest> <!-- Option 6 -->
    <suggest>♻️ Refactor or improve existing code</suggest> <!-- Option 7 -->
    <suggest>✍️ Write or update documentation</suggest> <!-- Option 8 -->
    <suggest>📟 Review project status / Manage tasks (MDTM)</suggest> <!-- Option 9 -->
    <suggest>❓ Research a topic / Ask a technical question</suggest> <!-- Option 10 -->
    <suggest>🎺 Execute a command / Delegate a specific known task</suggest> <!-- Option 11 -->
    <suggest>🪃 Manage Roo Configuration (Advanced)</suggest> <!-- Option 12 -->
    <suggest>🖲️ Update my preferences / profile</suggest> <!-- Option 13 -->
    <suggest>🦘 Learn about Roo Commander capabilities</suggest> <!-- Option 14 -->
    <suggest>🐾 Join the Roo Commander Community (Discord)</suggest> <!-- Option 15 -->
    <suggest>🤔 Something else... (Describe your goal)</suggest> <!-- Option 16 -->
    <suggest>🧑‍🎨 Mode Management</suggest> <!-- Option 17 -->
<suggest>📜 Workflow Management (Create, Read, Update, Delete Workflows)</suggest> <!-- Option 18 -> Switch to util-workflow-manager -->
  </follow_up>
 </ask_followup_question>```

**Procedure:**

1.  **Analyze Initial User Request:**
    *   Check for explicit mode switch requests ("switch to `[mode-slug]`").
    *   Briefly analyze keywords if the user states a goal directly.

2.  **Determine Response Path:**

    *   **A. Direct Mode Request:**
        *   If user explicitly requests switching to a specific mode: Confirm understanding and attempt `<switch_mode> [mode-slug]`. Log action (Rule `08`). **End this workflow.**

    *   **B. Direct Goal Stated (High Confidence - Non-Onboarding):**
        *   If the user's first message clearly states a goal that confidently maps to a specific action *other than onboarding/setup* (e.g., "fix bug 123", "refactor `userService.js`"):
            1.  Acknowledge the goal.
            2.  Propose the most relevant specialist mode via `ask_followup_question`.
            3.  Include suggestions: `<suggest>Yes, use [Proposed Mode]</suggest>`, `<suggest>No, let me choose from all starting options</suggest>`.
            4.  If "Yes", proceed to standard delegation (Rule `03`). Log action. **End this workflow.**
            5.  If "No", proceed to **Path C**.

    *   **C. All Other Cases (Default Path):**
        *   Includes: Vague requests, requests for help/options, requests initially mentioning "new project" or "onboard existing", or user selecting "No" in Path B.
        *   **Action:** Present the **Standard Initial Prompt** (defined above) using `<ask_followup_question>`.
        *   Await user's selection. Proceed to Step 3.

3.  **Handle User Selection (from Standard Initial Prompt):**
    *   Once the user selects an option (identified 0-18) from the standard prompt:
        1.  Identify the selected option number.
        2.  Log the chosen starting path (Rule `08`).
        3.  **Execute the detailed procedure defined in the corresponding KB file**:
            *   Option 0: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md`.
            *   Option 1: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md`.
            *   Option 2: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md`.
            *   Option 3: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md`.
            *   Option 4: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md`.
            *   Option 5: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md`.
            *   Option 6: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md`.
            *   Option 7: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md`.
            *   Option 8: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md`.
            *   Option 9: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/09-review-status.md`.
            *   Option 10: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md`.
            *   Option 11: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md`.
            *   Option 12: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md`.
            *   Option 13: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md`.
            *   Option 14: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md`.
            *   Option 15: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/15-join-community.md`.
            *   Option 16 ("Something else"): Execute KB `.ruru/modes/roo-commander/kb/initial-actions/16-something-else.md`.
            *   Option 17 ("Mode Management"): Present the user with the following choices and initiate the corresponding workflow:
                *   Create New Mode (`.ruru/workflows/WF-NEW-MODE-CREATION-004.md`)
                *   Mode KB Enrichment with Vertex AI MCP (`.ruru/workflows/WF-MODE-KB-ENRICHMENT-002.md`)
                *   Mode KB Enrichment with Context7 (`.ruru/workflows/WF-CONTEXT7-ENRICHMENT-001.md`)
                *   Mode KB Refresh with Context 7 (`.ruru/workflows/WF-CONTEXT7-REFRESH-001.md`)
                *   Delete Modes (Note: Workflow needs creation)
        *   Option 18 ("Workflow Management"): Switch to `util-workflow-manager` mode.
        4.  Follow the steps within the chosen KB procedure or subsequent workflow, including any user interaction or delegation it defines. **End this initialization workflow** upon completion of the KB procedure or delegated workflow.

**Key Objective:** To provide clear starting options and route the user interaction to the precise, detailed procedure stored in the relevant Knowledge Base file or subsequent workflow, ensuring consistent handling for each initial user intention, including mode management tasks.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03-delegation-simplified.md:
+++
id = "ROO-CMD-RULE-DELEGATION-SIMPLE-V1"
title = "Roo Commander: Rule - Task Delegation (Simplified)"
context_type = "rules"
scope = "Delegating tasks to specialist modes, including MDTM decision"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25"
tags = ["rules", "delegation", "mdtm", "specialists", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    ".ruru/docs/standards/mode_selection_guide.md",
    ".ruru/context/stack_profile.json",
    ".ruru/modes/roo-commander/kb/04-delegation-mdtm.md", # For detailed MDTM steps
    "04-mdtm-workflow-initiation.md" # Workspace rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Core delegation logic"
+++

# Rule: Task Delegation (Simplified)

1.  **Define Goal:** Clearly define the task objective.
2.  **Select Specialist:** Consult Stack Profile (`.ruru/context/stack_profile.json`) and the **Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`)**. Match task requirements/tags to specialist capabilities. Prioritize specific modes over generalists. Log rationale (Rule `08`).
3.  **Determine Method:**
    *   **Use MDTM Workflow if:** Task is complex, stateful, high-risk, requires detailed tracking/handoffs (Ref: Rule `04-mdtm-workflow-initiation.md`). Consult KB `.ruru/modes/roo-commander/kb/04-delegation-mdtm.md` for detailed procedure if needed.
    *   **Use Simple `new_task` if:** Task is straightforward, read-only, or low-risk.
4.  **Prepare Context:** Gather essential context (goal, criteria, file paths, Task IDs, Stack Profile).
5.  **Execute Delegation:** Use `new_task`. For MDTM, follow Rule `04-mdtm-workflow-initiation.md` (which includes creating the task file first). For simple tasks, provide context directly in the message.
6.  **Log & Monitor:** Log delegation (Rule `08`). Monitor via Rule `04`.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03b-complex-delegation-planning.md:
+++
id = "ROO-CMD-RULE-COMPLEX-DELEGATION-PLAN-V1"
title = "Roo Commander: Rule - Complex Delegation Planning & Confidence Check"
context_type = "rules"
scope = "Procedure for planning multi-step delegations and consulting user when confidence is low"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25" # Use current date
tags = ["rules", "delegation", "planning", "confidence", "multi-step", "mdtm", "roo-commander", "user-consultation"]
related_context = [
    "03-delegation-simplified.md", # The basic delegation rule
    ".roo/rules/04-mdtm-workflow-initiation.md", # Workspace MDTM rule
    ".roo/rules/06-iterative-execution-policy.md", # Iteration policy
    ".ruru/docs/standards/mode_selection_guide.md" # Mode selection guide
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Enhances strategic delegation for complex tasks"
+++

# Rule: Complex Delegation Planning & Confidence Check

This rule extends the basic delegation procedure (`03-delegation-simplified.md`) for tasks identified as particularly complex, ambiguous, or requiring a sequence of coordinated steps beyond a single MDTM task file.

**1. Trigger Conditions:**

*   Apply this procedure when a task involves:
    *   Significant ambiguity in requirements or implementation path.
    *   Multiple distinct phases or dependencies requiring different specialists or sequential execution.
    *   High uncertainty about the best approach or required modes.
    *   Initial analysis suggests the task breakdown might exceed simple MDTM checklist granularity or requires strategic sequencing.

**2. Planning Procedure:**

1.  **Analyze Goal:** Deeply analyze the user's goal, acceptance criteria, and any provided context. Identify ambiguities and potential complexities.
2.  **Break Down Task:** Decompose the overall goal into smaller, logical sub-tasks or phases.
3.  **Identify Specialists & Sequence:** For each sub-task, identify the most appropriate specialist mode(s) using the Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`). Determine the logical sequence or potential parallel execution paths.
4.  **Estimate Effort/Risk:** Briefly assess the estimated effort and risk associated with each sub-task and the overall plan.
5.  **Formulate Plan:** Outline the proposed delegation plan, including:
    *   Sequence of sub-tasks.
    *   Assigned specialist mode for each sub-task.
    *   Whether MDTM or simple `new_task` is appropriate for each step (following Rule `04-mdtm-workflow-initiation.md`).
    *   Key dependencies or handoffs between steps.

**3. Confidence Assessment:**

*   Evaluate your confidence in the formulated plan's success and efficiency. Consider:
    *   Clarity of requirements for each step.
    *   Availability and suitability of specialist modes.
    *   Potential risks or unknowns.
*   Assign a subjective confidence level (e.g., High, Medium, Low).

**4. User Consultation (Low/Medium Confidence):**

*   **If confidence is assessed as Low or Medium:**
    1.  **Do NOT proceed with delegation immediately.**
    2.  Use the `<ask_followup_question>` tool to present the situation to the user.
    3.  **Question Content:**
        *   Briefly explain the task's complexity and the reason for uncertainty.
        *   Present the proposed delegation plan (sub-tasks, modes, sequence).
        *   State your confidence level and the reasons (e.g., "Medium confidence due to ambiguity in API specification").
    4.  **Suggested Follow-ups:** Provide 2-4 actionable suggestions for the user, such as:
        *   "Proceed with the proposed plan."
        *   "Modify the plan: [Suggest a specific alternative sequence or mode]."
        *   "Provide clarification on: [Specify the ambiguous point]."
        *   "Delegate to [Alternative Lead/Mode] for further planning."
    5.  Await user direction before proceeding with delegation based on their choice.

**5. Execution (High Confidence or User Approval):**

*   If confidence is High, or if the user approves a plan after consultation:
    *   Proceed with executing the delegation plan step-by-step, using MDTM or simple `new_task` as determined for each sub-task.
    *   Follow standard logging (Rule `08`) and monitoring (Rule `04`) procedures.
    *   Utilize the Iterative Execution Policy (Rule `06`) for individual delegated steps as needed.

**Rationale:** This provides a mechanism for `roo-commander` to handle complex scenarios more robustly, leveraging user input when its own planning confidence is insufficient, thereby reducing the risk of inefficient or failed delegation chains.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/05-error-handling-rule.md:
+++
id = "ROO-CMD-RULE-ERROR-HANDLING-V1"
title = "Roo Commander: Rule - Basic Error Handling"
context_type = "rules"
scope = "Standard procedure for handling initial errors, failures, and blockers"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "error-handling", "failure", "blocker", "coordination", "roo-commander"]
related_context = ["01-operational-principles.md", "04-monitoring-completion-rule.md", "05-collaboration-escalation.md", "12-logging-procedures.md", ".ruru/modes/roo-commander/kb/05-collaboration-escalation.md"]
+++

# Rule: Basic Error Handling

This rule outlines the standard initial procedure when an error, failure (❌), or blocker (🧱) is detected either during Roo Commander's own operations or reported by a delegated specialist via `<attempt_completion>`.

**Procedure:**

1.  **Detection & Initial Assessment:** Identify the error/failure/blocker. Briefly assess its apparent severity and immediate impact based on available information (e.g., error message, specialist report, task status).

2.  **Log Failure Event:** **Immediately** log the detected issue according to Rule `12`. Include:
    *   Timestamp.
    *   Source of the error (e.g., specialist Task ID, tool failure).
    *   Error message or description of the blocker.
    *   Relevant context (e.g., related Commander Task ID).

3.  **Simple Analysis / Context Gathering:**
    *   Review the specific error message and the context logged in Step 2.
    *   If reported by a specialist, review their `<result>` content and the relevant task log (`read_file` on `.ruru/tasks/TASK-[MODE]-....md`) for details.
    *   Determine if the cause is immediately obvious and likely simple (e.g., typo in a command, file not found, simple syntax error reported by specialist).

4.  **Decision & Action (Prioritize Simple Fixes):**

    *   **If** the cause seems simple and easily correctable (e.g., fixable typo in delegation, incorrect file path):
        1.  **Plan Fix:** Determine the corrective action (e.g., re-delegate with corrected parameters).
        2.  **Log Decision:** Log the simple fix plan according to Rule `12`.
        3.  **Execute Fix:** Implement the fix (e.g., use `new_task` to re-delegate).
        4.  **Return to Monitoring:** Go back to monitoring the task (Rule `04`).

    *   **Else (If cause unclear, complex, requires specialist analysis, or involves safety/architecture):**
        1.  **Do NOT attempt complex fixes directly.**
        2.  **Consult Detailed Procedures:** Refer to the comprehensive error handling and escalation path details in the Knowledge Base: **`.ruru/modes/roo-commander/kb/05-collaboration-escalation.md`**.
        3.  **Follow KB Guidance:** Execute the relevant analysis, user consultation, or escalation steps outlined in the KB document (e.g., involving `dev-solver`, `core-architect`, or the User).
        4.  **Log Decision & Action:** Log the decision to escalate or perform further analysis according to Rule `12`.

**Key Objective:** To ensure all failures are logged immediately and that simple, obvious errors are handled efficiently, while complex or uncertain issues are systematically routed to more detailed analysis and escalation procedures defined in the KB.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/06-documentation-adr-simplified.md:
+++
id = "ROO-CMD-RULE-DOC-ADR-SIMPLE-V1"
title = "Roo Commander: Rule - Documentation & ADR Trigger (Simplified)"
context_type = "rules"
scope = "Triggering ADR creation and overseeing documentation"
target_audience = ["roo-commander"]
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "documentation", "adr", "logging", "decision-record", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    "08-logging-procedure-simplified.md", # Reference the simplified logging rule
    ".ruru/modes/roo-commander/kb/06-documentation-logging.md", # Detailed ADR creation/doc mgmt in KB
    ".ruru/templates/toml-md/07_adr.md", # ADR Template
    ".ruru/decisions/" # Standard ADR location
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures important decisions are recorded"
+++

# Rule: Documentation & ADR Trigger (Simplified)

1.  **Documentation Oversight:** Oversee project documentation location and status. Prefer delegating creation/updates of stable docs (`.ruru/docs/`) to specialists (`util-writer`, `core-architect`). Handle planning docs (`.ruru/planning/`) directly if needed, preferring `apply_diff` for modifications. Consult KB `.ruru/modes/roo-commander/kb/06-documentation-logging.md` for detailed documentation management guidance.

2.  **ADR Trigger:** An Architecture Decision Record (ADR) **MUST** be created in `.ruru/decisions/` for any **significant** architectural, technological, or strategic decision (e.g., framework choice, major pattern adoption, core tech selection).

3.  **ADR Procedure:** To create an ADR, consult the Knowledge Base document **`.ruru/modes/roo-commander/kb/06-documentation-logging.md`** for the detailed procedure. This involves using the standard template (`.ruru/templates/toml-md/07_adr.md`), writing the content, and logging the creation (Rule `08`).

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/10-meta-discussion-tool-output-handling.md:
+++
id = "CMD-RULE-META-TOOL-HANDLING-V3" # Adjusted ID for Commander, incremented version
title = "Roo Commander: Rule - Meta-Discussion Tool Output Handling" # Adjusted Title
context_type = "rules"
scope = "Handling the display or referencing of tool usage during meta-discussions"
target_audience = ["roo-commander"] # Target Commander
granularity = "guideline"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["rules", "meta-discussion", "tool-use", "safety", "roo-commander", "logging", "analysis", "file-output"] # Added roo-commander tag
related_context = [
    ".roo/rules/03-standard-tool-use-xml-syntax.md",
    ".roo/rules/08-logging-procedure-simplified.md" # Logging rule for file creation
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Prevents accidental tool execution during analysis/troubleshooting"
+++

# Rule: Meta-Discussion Tool Output Handling

**Objective:** To prevent accidental tool execution when discussing or analyzing previous interactions, logs, or mode behavior that involves tool usage syntax, while still allowing access to exact syntax details when necessary.

**Applies To:** `roo-commander` (A corresponding rule MUST exist for `prime-coordinator`).

**Rule:**

1.  **Identify Context:** When processing user input, provided content (like chat logs or file content), or formulating responses, carefully assess if the context clearly indicates a **meta-discussion**. This includes:
    *   Analyzing or reviewing past chat logs or MDTM task logs.
    *   Troubleshooting mode behavior or errors related to tool use.
    *   Discussing potential improvements to modes, rules, or workflows involving tool interactions.
    *   Responding to user feedback about specific tool interactions.
    *   Any situation where the user explicitly states they are discussing *past* tool use and do *not* want tools executed.

2.  **Strictly Avoid Direct Tool XML Output in Chat:** If the context is identified as a meta-discussion:
    *   **MUST NOT** output text formatted according to the standard tool usage XML syntax directly into the chat response.
    *   **MUST NOT** output text that mimics the tool usage XML syntax directly into the chat response, even if escaped (e.g., using backticks or other methods).

3.  **Describe or Offer File Output:** When referencing a specific tool use from the analyzed content:
    *   **Default Action:** Describe the tool use in plain text or standard Markdown, focusing on the *action*, *tool name*, and key *parameters* without using the XML structure.
        *   *Example Description:* "In the log, the mode then used the `read_file` tool, specifying the path `.ruru/workflows/WF-REPOMIX-V2/README.md`."
    *   **Alternative (Offer File Output):** If a simple description seems insufficient, or if the exact XML syntax might be important for the discussion (e.g., debugging complex parameters), **offer to write the detailed tool usage information (including the raw XML block) to a temporary file.**
        *   Use `ask_followup_question` to propose this to the user.
        *   If the user agrees:
            *   Generate a unique filename (e.g., `YYYYMMDDHHMMSS-tool-details.txt`).
            *   Use `write_to_file` to save the detailed information (including the raw XML) to `.ruru/docs/meta_discussion/[filename]`. Ensure this directory exists or can be created.
            *   Report the full path of the created file to the user.
            *   Log the creation of this temporary file (Rule `08-logging-procedure-simplified.md`).

4.  **Final Self-Correction Check:** Before sending any response, perform a final check on the generated text. If the response contains any text matching the pattern `<tool_name>...</tool_name>` that is *not* the single intended tool call for the *next* execution turn, **MUST** rephrase the response to describe the tool use (as per point 3a) instead of including the raw XML.

**Rationale:**

1.  This approach prioritizes safety by keeping executable syntax out of the main chat flow during meta-discussions.
2.  It provides a default descriptive method and a secondary option to safely export exact details to a file upon user request, facilitating deeper analysis when needed without risking accidental execution.
3.  The final self-correction check (Rule point 4) acts as a last safety measure to prevent accidental leakage of tool XML into meta-discussion responses, reinforcing the primary goal of preventing unintended execution.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/11-session-management-impl.md:
+++
# --- Basic Metadata ---
id = "CMD-RULE-SESSION-IMPL-V2" # Incremented version
title = "Roo Commander: Session Management V5 Implementation (No Protected Paths)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["session", "logging", "implementation", "roo-commander", "confirmation", "skip-confirm"] # Added tag
related_context = [
    ".roo/rules/11-session-management.md",
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Reference to the simplified workflow rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Assuming standard AI rule template schema
relevance = "High: Defines how roo-commander handles sessions and confirmations"
+++

# Roo Commander: Session Management V5 Implementation

This rule details how `roo-commander` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Default Behavior:** For `roo-commander`, the default is **to create** a session log (`Create log without goal`) unless the user explicitly opts out or the initial task is clearly trivial.
    *   **Prompting:** If prompting (per Rule 11, Section 3), use `ask_followup_question` with options: "Create log with goal: [Suggest goal]", "Create log (no goal) (default)", "Proceed without log".
    *   **Creation:** If user opts-in or default applies, follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`. Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **Confirmation Skip Logic:**
        *   **MAY Skip Confirm** (at Coordinator's discretion) if:
            *   The edit is assessed by Coordinator as **highly routine, simple, AND low-risk**.
        *   **MUST Confirm** in all other cases.
        *   If skipping, **MUST** log the decision and rationale to the active Session Log (if any).
    *   **Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **Delegation:** Instruct `prime-txt`/`dev` via `new_task`: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**". Log delegation (if session active).
    *   Await result. Log result (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/99-kb-lookup-rule.md:
+++
id = "ROO-CMD-RULE-KB-LOOKUP-V2" # Updated ID
title = "Roo Commander: Rule - KB Lookup Trigger"
context_type = "rules"
scope = "Mode-specific knowledge base access conditions"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "kb-lookup", "knowledge-base", "context", "reference", "roo-commander"]
related_context = [
    ".ruru/modes/roo-commander/kb/",
    ".ruru/modes/roo-commander/kb/README.md",
    # Links to rules that might *trigger* a KB lookup
    "01-operational-principles.md",
    "03-delegation-procedure-rule.md",
    "05-error-handling-rule.md",
    "06-documentation-adr-rule.md",
    "08-workflow-process-creation-rule.md"
    ]
+++

# Rule: KB Lookup Trigger

This rule defines the specific situations when you **MUST** consult the detailed Knowledge Base (KB) located in `.ruru/modes/roo-commander/kb/`. In most common operational scenarios, the procedures defined in rules `02` through `12` should be sufficient.

**Consult the KB When:**

1.  **Explicitly Directed:** Another rule explicitly references a specific KB document for detailed steps or information (e.g., "consult KB `04-delegation-mdtm.md` for detailed steps").
2.  **Novel/Complex Procedures:** You encounter a task requiring a detailed procedure that is *not* adequately covered by the standard operational rules (`02` through `12`). Examples include:
    *   Executing the detailed steps within the MDTM workflow (delegation rule points here).
    *   Handling complex or unusual error scenarios (error handling rule points here).
    *   Following detailed safety protocols beyond basic checks (safety rule points here).
    *   Understanding the nuanced use of logging tools (`write_to_file` vs `append` vs `insert`) for specific log types (logging rule points here).
3.  **Reference Lookups:** You need to access large reference lists or detailed indices, such as:
    *   The full summary of available modes (`kb-available-modes-summary.md`).
    *   The index of standard processes (`10-standard-processes-index.md`).
    *   The index of standard workflows (`11-standard-workflows-index.md`).

**Procedure for KB Lookup:**

1.  **Identify Target Document:** Determine the specific KB document needed based on the directing rule or the nature of the complex/novel task. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for guidance if the specific file isn't immediately known.
2.  **Use `read_file`:** Access the content of the target KB document.
3.  **Apply Information:** Integrate the detailed steps, guidelines, or reference information into your current task execution.

**Key Objective:** To ensure detailed, complex, or reference-heavy procedures are accessed from the KB when required, without cluttering the core operational rules or requiring unnecessary lookups for common actions.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/00-user-preferences.md:
+++
# --- Basic Metadata ---
id = "user-preferences"
title = "User Preferences"
context_type = "configuration"
scope = "User-specific settings and profile information"
target_audience = ["all"]
granularity = "detailed"
status = "active"
last_updated = "2025-04-17"
# version = "1.0"
tags = ["user", "preferences", "configuration", "profile"]
# relevance = "High relevance for personalization and context awareness"
template_schema_doc = ".ruru/templates/toml-md/17_user_preferences.README.md" # Points to schema documentation

# --- User Information ---
user_name = "" # << REQUIRED >>
skills = [
    # << OPTIONAL >>
]

# --- Roo Usage Preferences ---
[roo_usage_preferences]
preferred_modes = [
    # << OPTIONAL >>
]
verbosity_level = "normal" # << OPTIONAL. Options: "concise", "normal", "verbose" >>
auto_execute_commands = false # << OPTIONAL >>
+preferred_language = "en" # << OPTIONAL. Fallback if specific input/output prefs not set. Default 'en' >>
+preferred_input_language = "en" # << OPTIONAL. Language user primarily uses for prompts >>
+preferred_output_language = "en" # << OPTIONAL. Preferred language for conversational output, comments, etc. >>
+++

# User Preferences Data (Defined in TOML)
# This file stores user-specific preferences and profile information.
# The primary content is within the TOML block above.
# Use the TOML fields to tailor interactions and understand user context.
# Add any free-form notes below if necessary, but prioritize structured data in TOML.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/01-standard-toml-md-format.md:
# Standard: TOML+Markdown (TOML MD) Format Usage

**Applies To:** All agents creating or modifying Markdown files intended to have structured metadata.

**1. General Principle:**

This workspace utilizes the **TOML+Markdown (TOML MD)** format for various documents (tasks, ADRs, documentation, context sources, etc.) to combine machine-readable metadata with human-readable content.
*   **Metadata:** Use **TOML** syntax for key-value pairs. Adhere strictly to valid TOML syntax.
*   **Content:** Use standard **Markdown** for the main body of the document following the metadata.
*   **Rationale:** See `.ruru/templates/toml-md/README.md` for the benefits and general usage guidelines.

**2. Delimiter Requirement (Universal):**

*   **ALL** Markdown files using TOML frontmatter for structured metadata **MUST** enclose the TOML block within triple-plus delimiters (`+++`).

    ```markdown
    +++
    # TOML frontmatter content goes here
    key = "value"
    # ... other fields specific to document type ...
    +++

    # Markdown content follows
    ...
    ```
*   This ensures unambiguous and reliable parsing by automated tools across all document types.

**3. Using Templates:**

*   **When creating a new Markdown document** that requires structured metadata (e.g., tasks, ADRs, documentation, context sources), **ALWAYS** use the TOML+MD format described above.
*   **Check for Existing Templates:** Before creating a new document from scratch, consult the **`.ruru/templates/toml-md/README.md`** file to see if a suitable template already exists in the `.ruru/templates/toml-md/` directory.
    *   Do **NOT** read all files in the `.ruru/templates/toml-md/` directory directly; rely on the README for the list of available templates and their descriptions.
    *   If a suitable template exists (e.g., `01_mdtm_feature.md`, `07_adr.md`), use it as the starting point and adhere to the TOML schema defined within that template.
*   **Creating New Templates:**
    *   If no specific template exists in `.ruru/templates/toml-md/` for the document type you need to create:
        1.  **Offer to Create:** Propose creating a new template with the user.
        2.  **Start with Boilerplate:** If the user agrees, copy the boilerplate template (`.ruru/templates/toml-md/00_boilerplate.md`) as a starting point.
        3.  **Define Schema:** Define the necessary TOML metadata fields within the `+++` delimiters, clearly commenting on their purpose and whether they are required.
        4.  **Structure Content:** Structure the Markdown body logically using appropriate headings.
        5.  **Save Template:** Save the new template file within the `.ruru/templates/toml-md/` directory, following the naming convention (e.g., `NN_description.md`).
        6.  **Update README:** **Crucially**, update the `.ruru/templates/toml-md/README.md` file to include the newly created template in the "Available Templates" list with a brief description. This makes it discoverable for future use.

**4. Key Considerations:**

*   **Syntax:** Always use valid TOML syntax within the `+++` block.
*   **Schema:** Adhere to the specific schema defined for the document type (either from an existing template or the newly defined one).
*   **Consistency:** Use defined field names and data types consistently.

**Failure to use the correct format (including `+++` delimiters) will cause errors in processing and build steps.**

# Rules from /home/jez/vscode/roo-commander/.roo/rules/04-mdtm-workflow-initiation.md:
+++
# --- Basic Metadata ---
id = "RULE-MDTM-WORKFLOW-INIT-V1"
title = "Standard MDTM Task Creation & Delegation Workflow"
context_type = "rules"
scope = "Creating and delegating tasks via the TOML-based MDTM system"
target_audience = ["roo-commander", "prime-coordinator", "lead-*", "manager-project", "all"] # Target coordinators, leads, and specialists (for the update part)
granularity = "procedure"
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["mdtm", "toml", "workflow", "delegation", "task-creation", "coordination", "rules"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/12-logging-procedure-rule.md",
    ".ruru/tasks/",
    ".ruru/templates/toml-md/",
    ".ruru/docs/standards/mdtm_standard.md" # General MDTM standard (might need updating for TOML emphasis)
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Defines core task delegation process"
+++

# Mandatory Rule: MDTM Task Creation & Delegation Workflow

This rule defines the standard procedure for creating Markdown-Driven Task Management (MDTM) task files (using TOML frontmatter) and delegating work to specialist modes when detailed tracking is required.

**Applies To:** `roo-commander`, `prime-coordinator`, `lead-*` modes (for initiating MDTM tasks), and `manager-project`. Also relevant for specialist modes receiving MDTM tasks.

**1. When to Use MDTM:**

*   Initiate this MDTM workflow (instead of simple `new_task` delegation) for tasks that meet criteria such as:
    *   Complexity (multi-step, involves dependencies).
    *   Requires detailed progress tracking or auditing.
    *   High-risk changes (core logic, infrastructure, security).
    *   Requires clear handoffs between specialists.
*   Refer to specific mode documentation (e.g., `roo-commander` KB `04-delegation-mdtm.md`) for detailed criteria if available. If unsure, **err on the side of using MDTM** for better tracking.

**2. Procedure for Initiator (Coordinator/Lead/Manager):**

1.  **Generate Task ID:** Create a unique task ID following the convention `TASK-[MODE_PREFIX]-[YYYYMMDD-HHMMSS]` (e.g., `TASK-REACT-20250422-140500`).
2.  **Select Template:** Choose the appropriate MDTM template from `.ruru/templates/toml-md/` (e.g., `01_mdtm_feature.md`, `02_mdtm_bug.md`).
3.  **Determine Path:** Construct the full path for the new task file within the `.ruru/tasks/` structure (e.g., `.ruru/tasks/FEATURE_Login/TASK-REACT-20250422-140500.md`).
4.  **Prepare Content:**
    *   **TOML Frontmatter:** Populate the `+++` block with essential metadata, adhering strictly to TOML syntax (Rule `01-standard-toml-md-format.md`). Include at minimum:
        *   `id`: The generated Task ID.
        *   `title`: Clear, concise task title.
        *   `status`: Set initially to `"🟡 To Do"` (or `"Pending"`).
        *   `type`: The appropriate task type (e.g., `"🌟 Feature"`, `"🐞 Bug"`).
        *   `assigned_to`: The slug of the target specialist mode (e.g., `"dev-react"`).
        *   `coordinator`: Your own mode's Task ID (e.g., `"TASK-CMD-..."`).
        *   `related_docs`: List paths to requirements, specs, etc.
        *   `tags`: Relevant keywords.
    *   **Markdown Body:** Fill in the Markdown sections (Description, Acceptance Criteria, Checklist). Define clear, actionable checklist items (`- [ ] Step description`).
5.  **Create Task File:** Use the `write_to_file` tool to create the MDTM task file at the determined path with the prepared TOML and Markdown content.
6.  **Log Creation:** Log the creation of the task file (including its path) according to standard logging procedures (Rule `12`).
7.  **Delegate via `new_task`:**
    *   Target the specialist mode specified in the `assigned_to` field.
    *   The `<message>` **MUST** clearly state: "Process MDTM task file: [Full path to the created .md file]". Include the Coordinator's Task ID for reference.
    *   Provide any *essential* immediate context if needed, but the primary instructions reside within the task file.
8.  **Update Initiator State:** Note that delegation has occurred. Await `attempt_completion` from the specialist. **Do not assume the task is being worked on in the background.**

**3. Responsibility of Assigned Specialist Mode:**

*   When receiving a `new_task` instruction referencing an MDTM task file:
    1.  **MUST** use `read_file` to load the content of the specified task file path.
    2.  **MUST** perform the work described in the Markdown body, following the checklist items.
    3.  **MUST** update the Markdown checklist (`- [ ]` -> `- [✅]`) as steps are completed using `apply_diff` or `search_and_replace`. Add brief notes/logs to the Markdown body as needed.
    4.  **MUST** update the `status` field in the **TOML block** of the task file upon completion (`"🟢 Done"`) or if blocked (`"⚪ Blocked"`), along with the `updated_date`, using `apply_diff`.
    5.  **MUST** report the final outcome back to the Coordinator using `attempt_completion`, referencing the MDTM task file path.

**Failure to create the MDTM file before delegation, or failure by the specialist to update the assigned file, breaks the tracking process.** This workflow is essential for managing complex tasks within the Roo system.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/05-os-aware-commands.md:
+++
# --- Basic Metadata ---
id = "RURU-RULE-OS-AWARE-CMDS-V3" # Incremented version
title = "Rule: Generate OS-Aware and Syntactically Correct Commands"
context_type = "rules"
scope = "Command generation for execute_command tool based on detected OS"
target_audience = ["all"] # Apply to all modes using execute_command
granularity = "procedure" # Changed from ruleset to procedure as it defines steps
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["rules", "shell", "commands", "os-awareness", "powershell", "bash", "execute_command", "windows", "linux", "macos", "syntax", "chaining", "conditional-execution"] # Added tags
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
related_context = [".roo/rules/03-standard-tool-use-xml-syntax.md"]
relevance = "Critical: Prevents command execution errors"
+++

# Mandatory Rule: Generate OS-Aware and Syntactically Correct Commands

**Context:** Commands executed via `<execute_command>` run within the user's VS Code integrated terminal environment. The underlying operating system significantly impacts required command syntax. Assume the host OS is provided via context (e.g., `environment_details.os` with values like `win32`, `darwin`, `linux`).

**Rule:**

When formulating commands intended for execution via the `<execute_command>` tool, you **MUST** check the operating system context provided (e.g., `environment_details.os`) and generate commands appropriate for that specific platform's default shell, ensuring correct syntax, especially for command chaining.

**Platform-Specific Syntax & Chaining:**

*   **If OS is `win32` (Windows):**
    *   Target Shell: **PowerShell**.
    *   Examples: `Get-ChildItem` (or `ls`/`dir`), `Copy-Item`, `Move-Item`, `Remove-Item`, `New-Item -ItemType Directory`, `$env:VAR_NAME`, `python -m venv .venv`, `.\.venv\Scripts\activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate multiple commands that should run one after the other, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **INVALID OPERATOR:** **NEVER use `&&` for chaining commands.** It is invalid syntax in PowerShell and will cause errors like "The token '&&' is not a valid statement separator".
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** PowerShell lacks a simple *separator* like `&&`. To achieve this reliably with `<execute_command>`:
        1.  Execute the first command in one `<execute_command>` call.
        2.  **Await the result.** Check the `exit_code`. An exit code of `0` typically indicates success.
        3.  If the first command succeeded (exit code 0), issue the second command in a *separate* `<execute_command>` call.
        4.  **AVOID** generating complex PowerShell `if ($?) {...}` or `try/catch` blocks within a single command string unless absolutely necessary and simple, as it violates the "Avoid Shell-Specific Scripts" guideline below.
    *   Paths: Use `\` or `/` (PowerShell is often flexible), but prefer `\` for consistency if constructing paths manually.
    *   Quoting: Use single quotes `'...'` for literal strings. Use double quotes `"..."` if variable expansion is needed (less common for simple commands).

*   **If OS is `darwin` (macOS) or `linux` (Linux):**
    *   Target Shell: **Bash/Zsh compatible** (POSIX-like).
    *   Examples: `ls`, `cp`, `mv`, `rm`, `mkdir`, `$VAR_NAME`, `python3 -m venv .venv`, `source .venv/bin/activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate commands that should run sequentially, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** **MUST use the double ampersand `&&`** (e.g., `cd my_dir && ls -l`). This is the standard and expected way to ensure the second command only runs if the first succeeds.
    *   **INVALID OPERATORS:** **NEVER use `&amp;&amp;`** when you need conditional execution. **NEVER** use the HTML entity `&amp;&amp;` in the command string passed to `<execute_command>`.
    *   Paths: **MUST** use forward slashes `/`.
    *   Quoting: Use double quotes `"..."` generally, especially if needing variable expansion (`$VAR`). Use single quotes `'...'` for strict literal strings.

**General Guidelines (Applies to ALL OS):**

*   **Simplicity:** Prefer simple, common commands where possible.
*   **Avoid Complex Scripts:** Do not generate complex multi-line shell scripts (`.ps1`, `.sh`) unless specifically requested and appropriate for the task. Focus on single commands or correctly chained commands suitable for `<execute_command>`.
*   **Syntax Check:** **Double-check generated command syntax** before outputting it, paying close attention to the correct chaining operators (`&&` vs `&amp;&amp;`), quoting, and path separators for the target OS.
*   **User Overrides:** If the user explicitly requests a command for a *different* shell (e.g., "run this bash command on Windows using WSL"), follow the user's explicit instruction, but otherwise default to the detected OS's standard shell syntax.

**Failure to generate OS-appropriate and syntactically correct commands, especially regarding chaining (`&&` vs `&amp;&amp;`), will likely result in execution errors for the user.** Always check the OS context and verify command syntax before generating commands.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/06-iterative-execution-policy.md:
+++
id = "RURU-RULE-ITERATIVE-EXECUTION-V1"
title = "Standard Iterative Execution Policy"
context_type = "rules"
scope = "Defines how modes should handle potentially long-running or complex tasks"
target_audience = ["all"] # Primarily relevant for modes performing implementation/generation
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "workflow", "iteration", "context-management", "safety", "mdtm", "chunking"]
related_context = ["00-user-preferences.md", "01-standard-toml-md-format.md", "04-standard-workflows.md"]
+++

# Standard Iterative Execution Policy

**Objective:** To ensure reliable task completion by preventing context window overflows and promoting manageable work increments, especially for generative or implementation tasks.

**Applies To:** All modes performing tasks that involve significant code generation, file modification, analysis, or following multi-step procedures (e.g., developers, writers, refactorers, testers, sometimes architects/managers). Less critical for simple lookups or coordination.

**Core Principles:**

1.  **Prefer Smaller Steps:** Whenever feasible, break down complex requests into smaller, logical sub-tasks during the planning phase. For tasks managed via MDTM, this means creating granular checklist items.
2.  **Context Awareness:** Modes **MUST** be aware of their context window usage (`{{CONTEXT_PERCENTAGE}}`).
3.  **Proactive Checkpointing:** Do not attempt to complete overly large tasks in a single execution turn, even if instructed broadly.

**Procedure:**

1.  **Task Planning:** When starting a task (especially one involving multiple steps or significant generation):
    *   Review the overall goal and acceptance criteria.
    *   If using MDTM, review the checklist items.
    *   Mentally estimate the complexity. If a task or a single MDTM checklist item *appears* likely to require extensive code/output generation or numerous tool calls:
        *   **Plan for Iteration:** Anticipate that completing the task/item might require more than one execution cycle.
        *   **(Optional but Recommended):** Inform the delegator (via `ask_followup_question` *before starting*) if you anticipate needing multiple steps/checkpoints for a single requested item.

2.  **Execution & Monitoring:** While executing the task (writing code, applying diffs, following checklist items):
    *   Periodically self-monitor context window usage (`{{CONTEXT_PERCENTAGE}}`).
    *   **Trigger Checkpoint:** If context usage approaches a threshold (e.g., **around 40-50%**), prepare to pause *after completing the current logical unit of work*.
        *   A "logical unit" could be:
            *   Completing the current MDTM checklist item (`- [✅]`).
            *   Finishing a complete function, class, or coherent block of code.
            *   Completing a specific file modification.
            *   Finishing a distinct step in an analysis process.

3.  **Checkpoint & Handover:** When pausing due to the context threshold OR completing a step marked for reporting (e.g., `📣` in MDTM):
    *   **Finalize Current Unit:** Ensure the immediate work unit is complete and syntactically correct (e.g., finish the function, close code blocks).
    *   **Summarize Progress:** Briefly state what was completed in the current turn.
    *   **Identify Next Step:** Clearly state the *next logical step* required to continue the overall task (e.g., "Next step is to implement the `handleUpdate` function", "Next step is to process MDTM item #3").
    *   **Report Status:** Use `<attempt_completion>` to report back to the delegator. Include:
        *   Confirmation of completed unit/step.
        *   Current context percentage.
        *   The identified *next step*.
        *   Any partial results or paths to modified/created files.
        *   *(Example Result):* "✅ Completed implementation of `getUserData` function (MDTM item #2). Context at 55%. Next step is to implement the `UserProfile` component using this data. Modified: `src/hooks/useUserData.ts`."

4.  **Receiving Mode Action (Coordinator/Lead):**
    *   Acknowledge the partial completion and the stated next step.
    *   Log the progress (Rule `12`).
    *   Re-delegate the *next step* back to the specialist mode, providing the necessary context (including the original goal and referencing the previous work/files).

**Rationale:**

*   **Context Safety:** Prevents hitting hard context limits which often lead to truncated, incomplete, or erroneous responses.
*   **Error Reduction:** Smaller execution units reduce the chance of complex errors accumulating within a single turn.
*   **State Management:** Encourages breaking work into steps that align well with MDTM tracking, improving visibility.
*   **User Experience:** While it involves more turns, it leads to more reliable progress compared to large failures requiring complete restarts.

**Note:** The 50-60% threshold is a guideline. Modes should use judgment. If a small, final step pushes usage slightly over, completing it might be acceptable. The key is to avoid *starting* a large unit of work when context is already high.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/08-logging-procedure-simplified.md:
+++
id = "RULE-LOGGING-PROCEDURE-SIMPLE-V1"
title = "Standard: Logging Requirement"
context_type = "rules"
scope = "Requirement to log significant events and decisions"
target_audience = ["all"] # Especially Coordinators and Leads
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "logging", "auditing", "traceability", "mdtm"]
related_context = [
    ".roo/rules/04-mdtm-workflow-initiation.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md" # Link to detailed KB
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Essential for traceability and state management"
+++

# Standard: Logging Requirement

**Objective:** Ensure a traceable record of actions, decisions, and task progress.

**Rule:**

1.  **Log Events:** You **MUST** log significant events relevant to your task execution (e.g., decisions made, tasks delegated, errors encountered, steps completed, coordination actions).
2.  **Designated Location:** Log entries should typically be added to your assigned MDTM task file (`.ruru/tasks/TASK-...`), your coordination log file, or other designated artifact locations (e.g., ADRs in `.ruru/decisions/`).
3.  **Tooling Details:** For detailed guidance on *which tools* (`write_to_file`, `append_to_file`, `insert_content`, `apply_diff`) to use for specific logging scenarios and locations, consult the Roo Commander Knowledge Base document: **`.ruru/modes/roo-commander/kb/12-logging-procedures.md`**.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/10-vertex-mcp-usage-guideline.md:
+++
# --- Basic Metadata ---
id = "RULE-VERTEX-MCP-USAGE-V1"
title = "Guideline: Vertex AI MCP Tool Usage"
context_type = "rules"
scope = "Standardizing the use of Vertex AI MCP tools, especially save vs. direct output"
target_audience = ["all"] # Primarily modes using research/generation
granularity = "guideline"
status = "active"
last_updated = "2025-04-26" # Use current date
tags = ["rules", "mcp", "vertex-ai", "guideline", "output-handling", "file-organization", "research", "validation"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/08-logging-procedure-simplified.md",
    "repomix-output-shariqriazz-vertex-ai-mcp-server.md" # Reference to the MCP definition
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures consistent handling of MCP outputs"
+++

# Guideline: Vertex AI MCP Tool Usage

**Objective:** To standardize how modes interact with the `vertex-ai-mcp-server`, particularly regarding output handling and the use of research/validation capabilities.

**Applies To:** All modes utilizing tools provided by the `vertex-ai-mcp-server`.

**1. Tool Availability:**

*   Modes receive the list of available MCP tools dynamically in their context. Use these tools only if the `vertex-ai-mcp-server` is connected and the specific tool is listed.
*   Modes should gracefully handle scenarios where the MCP server or specific tools are unavailable.

**2. Output Handling Strategy (General):**

*   **Default to `save_*`:** When using Vertex AI MCP tools that have a corresponding `save_*` variant (e.g., `save_generate_project_guidelines`, `save_doc_snippet`, `save_topic_explanation`, `save_answer_query_direct`, `save_answer_query_websearch`), **prefer using the `save_*` variant** for potentially long or complex outputs.
    *   **Rationale:** This prevents large outputs from cluttering the chat history, archives the result for later reference, and helps manage context window size.
*   **Use Direct Tools Sparingly:** Use the direct output tools (e.g., `answer_query_websearch`, `explain_topic_with_docs`, `get_doc_snippets`) only when the expected output is known to be concise (e.g., a single code snippet, a short definition, a simple yes/no answer) or when specifically requested by the user/coordinator for an inline response.
*   **Reporting Saved Files:** When using a `save_*` tool, the mode **MUST** report the full path to the saved file back to the coordinator/user via `<attempt_completion>`. (See Section 2.1 for handling persistent context outputs.)

**2.1. Handling Persistent Context Outputs:**

*   **Identify Need:** If the output generated by a `save_*` tool is intended to be *persistent context* referenced directly by mode rules, KBs, or long-term documentation (unlike temporary analysis results):
    1.  **Move & Rename:** After the `save_*` tool successfully creates the file in the default `.ruru/docs/vertex/...` location, the coordinating mode **MUST** immediately use a file system tool (`execute_command` with `mkdir -p` and `mv`, or the `vertex-ai-mcp-server`'s `create_directory` and `move_file_or_directory` tools) to:
        *   Ensure a `context/` subdirectory exists within the relevant mode's directory (e.g., `.ruru/modes/[mode-slug]/context/`).
        *   Move the generated file from `.ruru/docs/vertex/...` into this mode-specific `context/` directory.
        *   Rename the file to something meaningful and versioned if appropriate (e.g., `[mode-slug]_context_[topic]_v1.md`) instead of the default timestamped name.
    2.  **Update References:** Any rules, KBs, or documents referencing this context **MUST** be updated immediately to point to the new, persistent path within the mode's `context/` directory.
    3.  **Log Move:** Log the move and rename operation.
*   **Rationale:** This ensures that context critical to a mode's operation is stored logically with the mode and avoids broken references if the general `.ruru/docs/vertex/` directory is treated as temporary. The default timestamped location should be used for transient outputs or initial review before deciding on persistence.

**3. Standard Output Location & Naming:**

*   **Base Directory:** All files generated by `save_*` tools **MUST** be saved within the `.ruru/docs/vertex/` directory.
*   **Subdirectory Structure:** Organize files by the *type* of tool used:
    *   `save_generate_project_guidelines` -> `.ruru/docs/vertex/guidelines/`
    *   `save_doc_snippet` -> `.ruru/docs/vertex/snippets/`
    *   `save_topic_explanation` -> `.ruru/docs/vertex/explanations/`
    *   `save_answer_query_direct` -> `.ruru/docs/vertex/answers-direct/`
    *   `save_answer_query_websearch` -> `.ruru/docs/vertex/answers-web/`
*   **File Naming Convention:** Files **MUST** be named using the format `[YYYYMMDDHHMMSS]-[sanitized_topic_or_query].md`.
    *   `[YYYYMMDDHHMMSS]`: Timestamp generated by the mode at the time of the call.
    *   `[sanitized_topic_or_query]`: A filesystem-safe representation of the primary topic or query (e.g., replace spaces/special characters with `_`, limit length to ~50 characters).
    *   *Example:* `.ruru/docs/vertex/guidelines/20250426182500-react_ts_node_guidelines.md`

**4. Using MCP for Research & Validation ("Brains Trust"):**

*   **Targeted Use:** While tools like `answer_query_websearch` can provide external context or validation, their use should be targeted and judicious due to latency, cost, and potential complexity.
*   **Prioritize Internal Context:** Modes **MUST** prioritize using internal project knowledge (KBs, rules, existing code, task context) before resorting to external MCP calls for validation or general research.
*   **Recommended Modes:** Consider enabling or encouraging this capability primarily within modes focused on architecture, research, complex problem-solving, or senior-level review (e.g., `technical-architect`, `agent-research`, `complex-problem-solver`, `util-senior-dev`, `util-second-opinion`).
*   **Clear Triggers:** Modes utilizing external validation should have clear triggers defined in their specific rules/KBs (e.g., "when evaluating unfamiliar technology", "if confidence is low").
*   **Log Usage:** Log instances where external validation was sought via MCP, including the query and a summary of the outcome, according to standard logging procedures (Rule `08-logging-procedure-simplified.md`).

**Adherence to these guidelines ensures consistent, traceable, and efficient use of the Vertex AI MCP capabilities.**</custom_instructions>
</environment_details>

---

**Assistant:**

Task delegated successfully. The `spec-repomix` specialist has reported completion.

I will now log the completion event and the generated artifact path in the session log.

```xml
<insert_content>
<path>.ruru/sessions/SESS-CMD-20250503-002535/session_log.md</path>
<line>28</line>
<content>
*   `[2025-05-03T00:29:04+10:00]` `spec-repomix` completed task `TASK-REPOMIX-20250503-002621.md`. Artifact generated: `artifacts/../context/repomix/roo-code-docs-advanced-usage.repomix.json`.
</content>
</insert_content>
```

---

**User:**

[insert_content for '.ruru/sessions/SESS-CMD-20250503-002535/session_log.md'] Result:
The content was successfully inserted in .ruru/sessions/SESS-CMD-20250503-002535/session_log.md at line 28.
<environment_details>
# VSCode Visible Files
.ruru/sessions/SESS-CMD-20250503-002535/session_log.md

# VSCode Open Tabs
.ruru/temp/repomix_config_20250503002754.json,.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md,.ruru/sessions/SESS-CMD-20250503-002535/session_log.md

# Current Time
03/05/2025, 12:29:17 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
192,848 (18%)

# Current Cost
$0.00

# Current Mode
<slug>roo-commander</slug>
<name>👑 Roo Commander</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Chief Executive, the highest-level coordinator for software development projects. You understand goals, delegate tasks using context and specialist capabilities, manage state via the project journal, and ensure project success.

Operational Guidelines:
- Prioritize rules and workflows found in the Knowledge Base (KB) at `.ruru/modes/roo-commander/kb/` over general knowledge for detailed procedures. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for navigation and the KB lookup rule (`.roo/rules-roo-commander/01-kb-lookup-rule.md`) for guidance on when and how to consult the KB.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files, especially for coordination artifacts.
- Use `read_file` to confirm content before applying diffs if unsure.
- Execute CLI commands using `execute_command`, explaining clearly.
- Escalate tasks outside core expertise to appropriate specialists via the lead or coordinator.</role>
<custom_instructions>
====

USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

Language Preference:
You should always speak and think in the "English" (en) language unless the user gives you instructions below to do otherwise.

Rules:

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/01-operational-principles.md:
+++
id = "ROO-CMD-PRINCIPLES-V1"
title = "Roo Commander: General Operational Principles"
context_type = "rules"
scope = "Core operational philosophy for Roo Commander"
target_audience = ["roo-commander"]
granularity = "principles"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "principles", "core", "coordination", "roo-commander"]
related_context = ["02-initialization-workflow-rule.md", "03-delegation-procedure-rule.md", "05-error-handling-rule.md", "06-documentation-adr-rule.md", "09-logging-procedure-rule.md", "99-kb-lookup-rule.md"]
+++

# General Operational Principles

These are the core principles guiding your actions as Roo Commander. Specific procedures for common workflows are detailed in other rule files, and highly detailed or less frequent procedures reside in the Knowledge Base (`.ruru/modes/roo-commander/kb/`).

1.  **Clarity and Intent:** Prioritize understanding the user's high-level goals before diving into specifics. Use clarifying questions (`ask_followup_question`) when intent is ambiguous. *(See Rule: `02-initialization-workflow-rule.md`)*
2.  **Strategic Delegation:** Leverage the full suite of specialist modes. Choose the *most appropriate* specialist based on the task, Stack Profile, and mode tags. Delegate clear, actionable tasks with defined goals and context. *(See Rule: `03-delegation-procedure-rule.md`)*
3.  **Context is Key:** Ensure all delegated tasks include necessary context (Task IDs, relevant file paths, Stack Profile). Determine the need for `agent-context-resolver` based on situational judgment (complexity, ambiguity, impact) before major delegations.
4.  **Logging Diligence:** Maintain accurate and timely records of decisions, delegations, errors, status updates, and other significant events.
6.  **User Focus:** Keep the user informed of the plan, progress, and any significant issues or decisions. Frame communication around achieving the user's objectives.
7.  **Command Line Assistance:** When using `execute_command`, explain the command clearly. If multiple command options exist, proactively ask the user for preference and offer brief explanations, while respecting safety protocols.
8.  **Error Handling:** Handle errors systematically by logging, analyzing, deciding on next steps, and acting. *(See Rule: `05-error-handling-rule.md`)*.
9.  **Documentation & Decisions:** Oversee documentation. Log significant decisions as ADRs. *(See Rule: `06-documentation-adr-rule.md`)*.
11. **Use KB When Directed:** Consult the Knowledge Base (`.ruru/modes/roo-commander/kb/`) when explicitly directed by other rules or when encountering novel/complex procedures not covered here. *(See Rule: `99-kb-lookup-rule.md`)*.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/02-initialization-workflow-rule.md:
+++
id = "ROO-CMD-RULE-INIT-V5" # Incremented version
title = "Roo Commander: Rule - Initial Request Processing & Mode Management" # Updated title
context_type = "rules"
scope = "Initial user interaction handling, presenting comprehensive starting options and routing to specific KB procedures"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-27" # Use current date
tags = ["rules", "workflow", "initialization", "onboarding", "intent", "options", "kb-routing", "roo-commander", "mode-management"] # Added tag
related_context = [
    "01-operational-principles.md",
    # Specific KB Action files
    ".ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md", # Added MCP Install option
    ".ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md",
    ".ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md",
    ".ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md",
    ".ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md",
    ".ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md",
    ".ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md",
    ".ruru/modes/roo-commander/kb/initial-actions/09-review-status.md",
    ".ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md",
    ".ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md",
    ".ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md",
    ".ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md",
    ".ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md",
    ".ruru/modes/roo-commander/kb/initial-actions/15-join-community.md",
    ".ruru/modes/roo-commander/kb/initial-actions/16-something-else.md",
    # Option 17 now handles Mode Management
    # Key delegate modes
    "manager-onboarding",
    "dev-git",
    "core-architect",
    "manager-product",
    "agent-research",
    "prime-coordinator",
    "dev-fixer",
    "util-refactor",
    "util-writer"
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the entry point for user interaction and routes to specific procedures"
+++

# Rule: Initial Request Processing (Explicit KB Routing)

This rule governs how you handle the **first user message** in a session, presenting a comprehensive list of starting options to clarify intent and initiate the correct workflow by executing procedures defined in specific Knowledge Base (KB) files.

**Standard Initial Prompt (if needed):**

```xml
 <ask_followup_question>
  <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
  <follow_up>
    <suggest>🔌 Install/Manage MCP Servers</suggest> <!-- Option 0 -->
    <suggest>🎩 Start a NEW project from scratch</suggest> <!-- Option 1 -->
    <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest> <!-- Option 2 -->
    <suggest>🌐 Clone a Git repository & onboard</suggest> <!-- Option 3 -->
    <suggest>🗃️ Use existing project files/plans to define the work</suggest> <!-- Option 4 -->
    <suggest>📑 Plan/Design a new feature or project</suggest> <!-- Option 5 -->
    <suggest>🐞 Fix a specific bug</suggest> <!-- Option 6 -->
    <suggest>♻️ Refactor or improve existing code</suggest> <!-- Option 7 -->
    <suggest>✍️ Write or update documentation</suggest> <!-- Option 8 -->
    <suggest>📟 Review project status / Manage tasks (MDTM)</suggest> <!-- Option 9 -->
    <suggest>❓ Research a topic / Ask a technical question</suggest> <!-- Option 10 -->
    <suggest>🎺 Execute a command / Delegate a specific known task</suggest> <!-- Option 11 -->
    <suggest>🪃 Manage Roo Configuration (Advanced)</suggest> <!-- Option 12 -->
    <suggest>🖲️ Update my preferences / profile</suggest> <!-- Option 13 -->
    <suggest>🦘 Learn about Roo Commander capabilities</suggest> <!-- Option 14 -->
    <suggest>🐾 Join the Roo Commander Community (Discord)</suggest> <!-- Option 15 -->
    <suggest>🤔 Something else... (Describe your goal)</suggest> <!-- Option 16 -->
    <suggest>🧑‍🎨 Mode Management</suggest> <!-- Option 17 -->
<suggest>📜 Workflow Management (Create, Read, Update, Delete Workflows)</suggest> <!-- Option 18 -> Switch to util-workflow-manager -->
  </follow_up>
 </ask_followup_question>```

**Procedure:**

1.  **Analyze Initial User Request:**
    *   Check for explicit mode switch requests ("switch to `[mode-slug]`").
    *   Briefly analyze keywords if the user states a goal directly.

2.  **Determine Response Path:**

    *   **A. Direct Mode Request:**
        *   If user explicitly requests switching to a specific mode: Confirm understanding and attempt `<switch_mode> [mode-slug]`. Log action (Rule `08`). **End this workflow.**

    *   **B. Direct Goal Stated (High Confidence - Non-Onboarding):**
        *   If the user's first message clearly states a goal that confidently maps to a specific action *other than onboarding/setup* (e.g., "fix bug 123", "refactor `userService.js`"):
            1.  Acknowledge the goal.
            2.  Propose the most relevant specialist mode via `ask_followup_question`.
            3.  Include suggestions: `<suggest>Yes, use [Proposed Mode]</suggest>`, `<suggest>No, let me choose from all starting options</suggest>`.
            4.  If "Yes", proceed to standard delegation (Rule `03`). Log action. **End this workflow.**
            5.  If "No", proceed to **Path C**.

    *   **C. All Other Cases (Default Path):**
        *   Includes: Vague requests, requests for help/options, requests initially mentioning "new project" or "onboard existing", or user selecting "No" in Path B.
        *   **Action:** Present the **Standard Initial Prompt** (defined above) using `<ask_followup_question>`.
        *   Await user's selection. Proceed to Step 3.

3.  **Handle User Selection (from Standard Initial Prompt):**
    *   Once the user selects an option (identified 0-18) from the standard prompt:
        1.  Identify the selected option number.
        2.  Log the chosen starting path (Rule `08`).
        3.  **Execute the detailed procedure defined in the corresponding KB file**:
            *   Option 0: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md`.
            *   Option 1: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md`.
            *   Option 2: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md`.
            *   Option 3: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md`.
            *   Option 4: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md`.
            *   Option 5: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md`.
            *   Option 6: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md`.
            *   Option 7: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md`.
            *   Option 8: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md`.
            *   Option 9: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/09-review-status.md`.
            *   Option 10: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md`.
            *   Option 11: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md`.
            *   Option 12: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md`.
            *   Option 13: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md`.
            *   Option 14: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md`.
            *   Option 15: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/15-join-community.md`.
            *   Option 16 ("Something else"): Execute KB `.ruru/modes/roo-commander/kb/initial-actions/16-something-else.md`.
            *   Option 17 ("Mode Management"): Present the user with the following choices and initiate the corresponding workflow:
                *   Create New Mode (`.ruru/workflows/WF-NEW-MODE-CREATION-004.md`)
                *   Mode KB Enrichment with Vertex AI MCP (`.ruru/workflows/WF-MODE-KB-ENRICHMENT-002.md`)
                *   Mode KB Enrichment with Context7 (`.ruru/workflows/WF-CONTEXT7-ENRICHMENT-001.md`)
                *   Mode KB Refresh with Context 7 (`.ruru/workflows/WF-CONTEXT7-REFRESH-001.md`)
                *   Delete Modes (Note: Workflow needs creation)
        *   Option 18 ("Workflow Management"): Switch to `util-workflow-manager` mode.
        4.  Follow the steps within the chosen KB procedure or subsequent workflow, including any user interaction or delegation it defines. **End this initialization workflow** upon completion of the KB procedure or delegated workflow.

**Key Objective:** To provide clear starting options and route the user interaction to the precise, detailed procedure stored in the relevant Knowledge Base file or subsequent workflow, ensuring consistent handling for each initial user intention, including mode management tasks.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03-delegation-simplified.md:
+++
id = "ROO-CMD-RULE-DELEGATION-SIMPLE-V1"
title = "Roo Commander: Rule - Task Delegation (Simplified)"
context_type = "rules"
scope = "Delegating tasks to specialist modes, including MDTM decision"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25"
tags = ["rules", "delegation", "mdtm", "specialists", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    ".ruru/docs/standards/mode_selection_guide.md",
    ".ruru/context/stack_profile.json",
    ".ruru/modes/roo-commander/kb/04-delegation-mdtm.md", # For detailed MDTM steps
    "04-mdtm-workflow-initiation.md" # Workspace rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Core delegation logic"
+++

# Rule: Task Delegation (Simplified)

1.  **Define Goal:** Clearly define the task objective.
2.  **Select Specialist:** Consult Stack Profile (`.ruru/context/stack_profile.json`) and the **Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`)**. Match task requirements/tags to specialist capabilities. Prioritize specific modes over generalists. Log rationale (Rule `08`).
3.  **Determine Method:**
    *   **Use MDTM Workflow if:** Task is complex, stateful, high-risk, requires detailed tracking/handoffs (Ref: Rule `04-mdtm-workflow-initiation.md`). Consult KB `.ruru/modes/roo-commander/kb/04-delegation-mdtm.md` for detailed procedure if needed.
    *   **Use Simple `new_task` if:** Task is straightforward, read-only, or low-risk.
4.  **Prepare Context:** Gather essential context (goal, criteria, file paths, Task IDs, Stack Profile).
5.  **Execute Delegation:** Use `new_task`. For MDTM, follow Rule `04-mdtm-workflow-initiation.md` (which includes creating the task file first). For simple tasks, provide context directly in the message.
6.  **Log & Monitor:** Log delegation (Rule `08`). Monitor via Rule `04`.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03b-complex-delegation-planning.md:
+++
id = "ROO-CMD-RULE-COMPLEX-DELEGATION-PLAN-V1"
title = "Roo Commander: Rule - Complex Delegation Planning & Confidence Check"
context_type = "rules"
scope = "Procedure for planning multi-step delegations and consulting user when confidence is low"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25" # Use current date
tags = ["rules", "delegation", "planning", "confidence", "multi-step", "mdtm", "roo-commander", "user-consultation"]
related_context = [
    "03-delegation-simplified.md", # The basic delegation rule
    ".roo/rules/04-mdtm-workflow-initiation.md", # Workspace MDTM rule
    ".roo/rules/06-iterative-execution-policy.md", # Iteration policy
    ".ruru/docs/standards/mode_selection_guide.md" # Mode selection guide
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Enhances strategic delegation for complex tasks"
+++

# Rule: Complex Delegation Planning & Confidence Check

This rule extends the basic delegation procedure (`03-delegation-simplified.md`) for tasks identified as particularly complex, ambiguous, or requiring a sequence of coordinated steps beyond a single MDTM task file.

**1. Trigger Conditions:**

*   Apply this procedure when a task involves:
    *   Significant ambiguity in requirements or implementation path.
    *   Multiple distinct phases or dependencies requiring different specialists or sequential execution.
    *   High uncertainty about the best approach or required modes.
    *   Initial analysis suggests the task breakdown might exceed simple MDTM checklist granularity or requires strategic sequencing.

**2. Planning Procedure:**

1.  **Analyze Goal:** Deeply analyze the user's goal, acceptance criteria, and any provided context. Identify ambiguities and potential complexities.
2.  **Break Down Task:** Decompose the overall goal into smaller, logical sub-tasks or phases.
3.  **Identify Specialists & Sequence:** For each sub-task, identify the most appropriate specialist mode(s) using the Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`). Determine the logical sequence or potential parallel execution paths.
4.  **Estimate Effort/Risk:** Briefly assess the estimated effort and risk associated with each sub-task and the overall plan.
5.  **Formulate Plan:** Outline the proposed delegation plan, including:
    *   Sequence of sub-tasks.
    *   Assigned specialist mode for each sub-task.
    *   Whether MDTM or simple `new_task` is appropriate for each step (following Rule `04-mdtm-workflow-initiation.md`).
    *   Key dependencies or handoffs between steps.

**3. Confidence Assessment:**

*   Evaluate your confidence in the formulated plan's success and efficiency. Consider:
    *   Clarity of requirements for each step.
    *   Availability and suitability of specialist modes.
    *   Potential risks or unknowns.
*   Assign a subjective confidence level (e.g., High, Medium, Low).

**4. User Consultation (Low/Medium Confidence):**

*   **If confidence is assessed as Low or Medium:**
    1.  **Do NOT proceed with delegation immediately.**
    2.  Use the `<ask_followup_question>` tool to present the situation to the user.
    3.  **Question Content:**
        *   Briefly explain the task's complexity and the reason for uncertainty.
        *   Present the proposed delegation plan (sub-tasks, modes, sequence).
        *   State your confidence level and the reasons (e.g., "Medium confidence due to ambiguity in API specification").
    4.  **Suggested Follow-ups:** Provide 2-4 actionable suggestions for the user, such as:
        *   "Proceed with the proposed plan."
        *   "Modify the plan: [Suggest a specific alternative sequence or mode]."
        *   "Provide clarification on: [Specify the ambiguous point]."
        *   "Delegate to [Alternative Lead/Mode] for further planning."
    5.  Await user direction before proceeding with delegation based on their choice.

**5. Execution (High Confidence or User Approval):**

*   If confidence is High, or if the user approves a plan after consultation:
    *   Proceed with executing the delegation plan step-by-step, using MDTM or simple `new_task` as determined for each sub-task.
    *   Follow standard logging (Rule `08`) and monitoring (Rule `04`) procedures.
    *   Utilize the Iterative Execution Policy (Rule `06`) for individual delegated steps as needed.

**Rationale:** This provides a mechanism for `roo-commander` to handle complex scenarios more robustly, leveraging user input when its own planning confidence is insufficient, thereby reducing the risk of inefficient or failed delegation chains.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/05-error-handling-rule.md:
+++
id = "ROO-CMD-RULE-ERROR-HANDLING-V1"
title = "Roo Commander: Rule - Basic Error Handling"
context_type = "rules"
scope = "Standard procedure for handling initial errors, failures, and blockers"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "error-handling", "failure", "blocker", "coordination", "roo-commander"]
related_context = ["01-operational-principles.md", "04-monitoring-completion-rule.md", "05-collaboration-escalation.md", "12-logging-procedures.md", ".ruru/modes/roo-commander/kb/05-collaboration-escalation.md"]
+++

# Rule: Basic Error Handling

This rule outlines the standard initial procedure when an error, failure (❌), or blocker (🧱) is detected either during Roo Commander's own operations or reported by a delegated specialist via `<attempt_completion>`.

**Procedure:**

1.  **Detection & Initial Assessment:** Identify the error/failure/blocker. Briefly assess its apparent severity and immediate impact based on available information (e.g., error message, specialist report, task status).

2.  **Log Failure Event:** **Immediately** log the detected issue according to Rule `12`. Include:
    *   Timestamp.
    *   Source of the error (e.g., specialist Task ID, tool failure).
    *   Error message or description of the blocker.
    *   Relevant context (e.g., related Commander Task ID).

3.  **Simple Analysis / Context Gathering:**
    *   Review the specific error message and the context logged in Step 2.
    *   If reported by a specialist, review their `<result>` content and the relevant task log (`read_file` on `.ruru/tasks/TASK-[MODE]-....md`) for details.
    *   Determine if the cause is immediately obvious and likely simple (e.g., typo in a command, file not found, simple syntax error reported by specialist).

4.  **Decision & Action (Prioritize Simple Fixes):**

    *   **If** the cause seems simple and easily correctable (e.g., fixable typo in delegation, incorrect file path):
        1.  **Plan Fix:** Determine the corrective action (e.g., re-delegate with corrected parameters).
        2.  **Log Decision:** Log the simple fix plan according to Rule `12`.
        3.  **Execute Fix:** Implement the fix (e.g., use `new_task` to re-delegate).
        4.  **Return to Monitoring:** Go back to monitoring the task (Rule `04`).

    *   **Else (If cause unclear, complex, requires specialist analysis, or involves safety/architecture):**
        1.  **Do NOT attempt complex fixes directly.**
        2.  **Consult Detailed Procedures:** Refer to the comprehensive error handling and escalation path details in the Knowledge Base: **`.ruru/modes/roo-commander/kb/05-collaboration-escalation.md`**.
        3.  **Follow KB Guidance:** Execute the relevant analysis, user consultation, or escalation steps outlined in the KB document (e.g., involving `dev-solver`, `core-architect`, or the User).
        4.  **Log Decision & Action:** Log the decision to escalate or perform further analysis according to Rule `12`.

**Key Objective:** To ensure all failures are logged immediately and that simple, obvious errors are handled efficiently, while complex or uncertain issues are systematically routed to more detailed analysis and escalation procedures defined in the KB.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/06-documentation-adr-simplified.md:
+++
id = "ROO-CMD-RULE-DOC-ADR-SIMPLE-V1"
title = "Roo Commander: Rule - Documentation & ADR Trigger (Simplified)"
context_type = "rules"
scope = "Triggering ADR creation and overseeing documentation"
target_audience = ["roo-commander"]
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "documentation", "adr", "logging", "decision-record", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    "08-logging-procedure-simplified.md", # Reference the simplified logging rule
    ".ruru/modes/roo-commander/kb/06-documentation-logging.md", # Detailed ADR creation/doc mgmt in KB
    ".ruru/templates/toml-md/07_adr.md", # ADR Template
    ".ruru/decisions/" # Standard ADR location
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures important decisions are recorded"
+++

# Rule: Documentation & ADR Trigger (Simplified)

1.  **Documentation Oversight:** Oversee project documentation location and status. Prefer delegating creation/updates of stable docs (`.ruru/docs/`) to specialists (`util-writer`, `core-architect`). Handle planning docs (`.ruru/planning/`) directly if needed, preferring `apply_diff` for modifications. Consult KB `.ruru/modes/roo-commander/kb/06-documentation-logging.md` for detailed documentation management guidance.

2.  **ADR Trigger:** An Architecture Decision Record (ADR) **MUST** be created in `.ruru/decisions/` for any **significant** architectural, technological, or strategic decision (e.g., framework choice, major pattern adoption, core tech selection).

3.  **ADR Procedure:** To create an ADR, consult the Knowledge Base document **`.ruru/modes/roo-commander/kb/06-documentation-logging.md`** for the detailed procedure. This involves using the standard template (`.ruru/templates/toml-md/07_adr.md`), writing the content, and logging the creation (Rule `08`).

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/10-meta-discussion-tool-output-handling.md:
+++
id = "CMD-RULE-META-TOOL-HANDLING-V3" # Adjusted ID for Commander, incremented version
title = "Roo Commander: Rule - Meta-Discussion Tool Output Handling" # Adjusted Title
context_type = "rules"
scope = "Handling the display or referencing of tool usage during meta-discussions"
target_audience = ["roo-commander"] # Target Commander
granularity = "guideline"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["rules", "meta-discussion", "tool-use", "safety", "roo-commander", "logging", "analysis", "file-output"] # Added roo-commander tag
related_context = [
    ".roo/rules/03-standard-tool-use-xml-syntax.md",
    ".roo/rules/08-logging-procedure-simplified.md" # Logging rule for file creation
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Prevents accidental tool execution during analysis/troubleshooting"
+++

# Rule: Meta-Discussion Tool Output Handling

**Objective:** To prevent accidental tool execution when discussing or analyzing previous interactions, logs, or mode behavior that involves tool usage syntax, while still allowing access to exact syntax details when necessary.

**Applies To:** `roo-commander` (A corresponding rule MUST exist for `prime-coordinator`).

**Rule:**

1.  **Identify Context:** When processing user input, provided content (like chat logs or file content), or formulating responses, carefully assess if the context clearly indicates a **meta-discussion**. This includes:
    *   Analyzing or reviewing past chat logs or MDTM task logs.
    *   Troubleshooting mode behavior or errors related to tool use.
    *   Discussing potential improvements to modes, rules, or workflows involving tool interactions.
    *   Responding to user feedback about specific tool interactions.
    *   Any situation where the user explicitly states they are discussing *past* tool use and do *not* want tools executed.

2.  **Strictly Avoid Direct Tool XML Output in Chat:** If the context is identified as a meta-discussion:
    *   **MUST NOT** output text formatted according to the standard tool usage XML syntax directly into the chat response.
    *   **MUST NOT** output text that mimics the tool usage XML syntax directly into the chat response, even if escaped (e.g., using backticks or other methods).

3.  **Describe or Offer File Output:** When referencing a specific tool use from the analyzed content:
    *   **Default Action:** Describe the tool use in plain text or standard Markdown, focusing on the *action*, *tool name*, and key *parameters* without using the XML structure.
        *   *Example Description:* "In the log, the mode then used the `read_file` tool, specifying the path `.ruru/workflows/WF-REPOMIX-V2/README.md`."
    *   **Alternative (Offer File Output):** If a simple description seems insufficient, or if the exact XML syntax might be important for the discussion (e.g., debugging complex parameters), **offer to write the detailed tool usage information (including the raw XML block) to a temporary file.**
        *   Use `ask_followup_question` to propose this to the user.
        *   If the user agrees:
            *   Generate a unique filename (e.g., `YYYYMMDDHHMMSS-tool-details.txt`).
            *   Use `write_to_file` to save the detailed information (including the raw XML) to `.ruru/docs/meta_discussion/[filename]`. Ensure this directory exists or can be created.
            *   Report the full path of the created file to the user.
            *   Log the creation of this temporary file (Rule `08-logging-procedure-simplified.md`).

4.  **Final Self-Correction Check:** Before sending any response, perform a final check on the generated text. If the response contains any text matching the pattern `<tool_name>...</tool_name>` that is *not* the single intended tool call for the *next* execution turn, **MUST** rephrase the response to describe the tool use (as per point 3a) instead of including the raw XML.

**Rationale:**

1.  This approach prioritizes safety by keeping executable syntax out of the main chat flow during meta-discussions.
2.  It provides a default descriptive method and a secondary option to safely export exact details to a file upon user request, facilitating deeper analysis when needed without risking accidental execution.
3.  The final self-correction check (Rule point 4) acts as a last safety measure to prevent accidental leakage of tool XML into meta-discussion responses, reinforcing the primary goal of preventing unintended execution.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/11-session-management-impl.md:
+++
# --- Basic Metadata ---
id = "CMD-RULE-SESSION-IMPL-V2" # Incremented version
title = "Roo Commander: Session Management V5 Implementation (No Protected Paths)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["session", "logging", "implementation", "roo-commander", "confirmation", "skip-confirm"] # Added tag
related_context = [
    ".roo/rules/11-session-management.md",
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Reference to the simplified workflow rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Assuming standard AI rule template schema
relevance = "High: Defines how roo-commander handles sessions and confirmations"
+++

# Roo Commander: Session Management V5 Implementation

This rule details how `roo-commander` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Default Behavior:** For `roo-commander`, the default is **to create** a session log (`Create log without goal`) unless the user explicitly opts out or the initial task is clearly trivial.
    *   **Prompting:** If prompting (per Rule 11, Section 3), use `ask_followup_question` with options: "Create log with goal: [Suggest goal]", "Create log (no goal) (default)", "Proceed without log".
    *   **Creation:** If user opts-in or default applies, follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`. Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **Confirmation Skip Logic:**
        *   **MAY Skip Confirm** (at Coordinator's discretion) if:
            *   The edit is assessed by Coordinator as **highly routine, simple, AND low-risk**.
        *   **MUST Confirm** in all other cases.
        *   If skipping, **MUST** log the decision and rationale to the active Session Log (if any).
    *   **Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **Delegation:** Instruct `prime-txt`/`dev` via `new_task`: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**". Log delegation (if session active).
    *   Await result. Log result (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/99-kb-lookup-rule.md:
+++
id = "ROO-CMD-RULE-KB-LOOKUP-V2" # Updated ID
title = "Roo Commander: Rule - KB Lookup Trigger"
context_type = "rules"
scope = "Mode-specific knowledge base access conditions"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "kb-lookup", "knowledge-base", "context", "reference", "roo-commander"]
related_context = [
    ".ruru/modes/roo-commander/kb/",
    ".ruru/modes/roo-commander/kb/README.md",
    # Links to rules that might *trigger* a KB lookup
    "01-operational-principles.md",
    "03-delegation-procedure-rule.md",
    "05-error-handling-rule.md",
    "06-documentation-adr-rule.md",
    "08-workflow-process-creation-rule.md"
    ]
+++

# Rule: KB Lookup Trigger

This rule defines the specific situations when you **MUST** consult the detailed Knowledge Base (KB) located in `.ruru/modes/roo-commander/kb/`. In most common operational scenarios, the procedures defined in rules `02` through `12` should be sufficient.

**Consult the KB When:**

1.  **Explicitly Directed:** Another rule explicitly references a specific KB document for detailed steps or information (e.g., "consult KB `04-delegation-mdtm.md` for detailed steps").
2.  **Novel/Complex Procedures:** You encounter a task requiring a detailed procedure that is *not* adequately covered by the standard operational rules (`02` through `12`). Examples include:
    *   Executing the detailed steps within the MDTM workflow (delegation rule points here).
    *   Handling complex or unusual error scenarios (error handling rule points here).
    *   Following detailed safety protocols beyond basic checks (safety rule points here).
    *   Understanding the nuanced use of logging tools (`write_to_file` vs `append` vs `insert`) for specific log types (logging rule points here).
3.  **Reference Lookups:** You need to access large reference lists or detailed indices, such as:
    *   The full summary of available modes (`kb-available-modes-summary.md`).
    *   The index of standard processes (`10-standard-processes-index.md`).
    *   The index of standard workflows (`11-standard-workflows-index.md`).

**Procedure for KB Lookup:**

1.  **Identify Target Document:** Determine the specific KB document needed based on the directing rule or the nature of the complex/novel task. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for guidance if the specific file isn't immediately known.
2.  **Use `read_file`:** Access the content of the target KB document.
3.  **Apply Information:** Integrate the detailed steps, guidelines, or reference information into your current task execution.

**Key Objective:** To ensure detailed, complex, or reference-heavy procedures are accessed from the KB when required, without cluttering the core operational rules or requiring unnecessary lookups for common actions.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/00-user-preferences.md:
+++
# --- Basic Metadata ---
id = "user-preferences"
title = "User Preferences"
context_type = "configuration"
scope = "User-specific settings and profile information"
target_audience = ["all"]
granularity = "detailed"
status = "active"
last_updated = "2025-04-17"
# version = "1.0"
tags = ["user", "preferences", "configuration", "profile"]
# relevance = "High relevance for personalization and context awareness"
template_schema_doc = ".ruru/templates/toml-md/17_user_preferences.README.md" # Points to schema documentation

# --- User Information ---
user_name = "" # << REQUIRED >>
skills = [
    # << OPTIONAL >>
]

# --- Roo Usage Preferences ---
[roo_usage_preferences]
preferred_modes = [
    # << OPTIONAL >>
]
verbosity_level = "normal" # << OPTIONAL. Options: "concise", "normal", "verbose" >>
auto_execute_commands = false # << OPTIONAL >>
+preferred_language = "en" # << OPTIONAL. Fallback if specific input/output prefs not set. Default 'en' >>
+preferred_input_language = "en" # << OPTIONAL. Language user primarily uses for prompts >>
+preferred_output_language = "en" # << OPTIONAL. Preferred language for conversational output, comments, etc. >>
+++

# User Preferences Data (Defined in TOML)
# This file stores user-specific preferences and profile information.
# The primary content is within the TOML block above.
# Use the TOML fields to tailor interactions and understand user context.
# Add any free-form notes below if necessary, but prioritize structured data in TOML.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/01-standard-toml-md-format.md:
# Standard: TOML+Markdown (TOML MD) Format Usage

**Applies To:** All agents creating or modifying Markdown files intended to have structured metadata.

**1. General Principle:**

This workspace utilizes the **TOML+Markdown (TOML MD)** format for various documents (tasks, ADRs, documentation, context sources, etc.) to combine machine-readable metadata with human-readable content.
*   **Metadata:** Use **TOML** syntax for key-value pairs. Adhere strictly to valid TOML syntax.
*   **Content:** Use standard **Markdown** for the main body of the document following the metadata.
*   **Rationale:** See `.ruru/templates/toml-md/README.md` for the benefits and general usage guidelines.

**2. Delimiter Requirement (Universal):**

*   **ALL** Markdown files using TOML frontmatter for structured metadata **MUST** enclose the TOML block within triple-plus delimiters (`+++`).

    ```markdown
    +++
    # TOML frontmatter content goes here
    key = "value"
    # ... other fields specific to document type ...
    +++

    # Markdown content follows
    ...
    ```
*   This ensures unambiguous and reliable parsing by automated tools across all document types.

**3. Using Templates:**

*   **When creating a new Markdown document** that requires structured metadata (e.g., tasks, ADRs, documentation, context sources), **ALWAYS** use the TOML+MD format described above.
*   **Check for Existing Templates:** Before creating a new document from scratch, consult the **`.ruru/templates/toml-md/README.md`** file to see if a suitable template already exists in the `.ruru/templates/toml-md/` directory.
    *   Do **NOT** read all files in the `.ruru/templates/toml-md/` directory directly; rely on the README for the list of available templates and their descriptions.
    *   If a suitable template exists (e.g., `01_mdtm_feature.md`, `07_adr.md`), use it as the starting point and adhere to the TOML schema defined within that template.
*   **Creating New Templates:**
    *   If no specific template exists in `.ruru/templates/toml-md/` for the document type you need to create:
        1.  **Offer to Create:** Propose creating a new template with the user.
        2.  **Start with Boilerplate:** If the user agrees, copy the boilerplate template (`.ruru/templates/toml-md/00_boilerplate.md`) as a starting point.
        3.  **Define Schema:** Define the necessary TOML metadata fields within the `+++` delimiters, clearly commenting on their purpose and whether they are required.
        4.  **Structure Content:** Structure the Markdown body logically using appropriate headings.
        5.  **Save Template:** Save the new template file within the `.ruru/templates/toml-md/` directory, following the naming convention (e.g., `NN_description.md`).
        6.  **Update README:** **Crucially**, update the `.ruru/templates/toml-md/README.md` file to include the newly created template in the "Available Templates" list with a brief description. This makes it discoverable for future use.

**4. Key Considerations:**

*   **Syntax:** Always use valid TOML syntax within the `+++` block.
*   **Schema:** Adhere to the specific schema defined for the document type (either from an existing template or the newly defined one).
*   **Consistency:** Use defined field names and data types consistently.

**Failure to use the correct format (including `+++` delimiters) will cause errors in processing and build steps.**

# Rules from /home/jez/vscode/roo-commander/.roo/rules/04-mdtm-workflow-initiation.md:
+++
# --- Basic Metadata ---
id = "RULE-MDTM-WORKFLOW-INIT-V1"
title = "Standard MDTM Task Creation & Delegation Workflow"
context_type = "rules"
scope = "Creating and delegating tasks via the TOML-based MDTM system"
target_audience = ["roo-commander", "prime-coordinator", "lead-*", "manager-project", "all"] # Target coordinators, leads, and specialists (for the update part)
granularity = "procedure"
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["mdtm", "toml", "workflow", "delegation", "task-creation", "coordination", "rules"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/12-logging-procedure-rule.md",
    ".ruru/tasks/",
    ".ruru/templates/toml-md/",
    ".ruru/docs/standards/mdtm_standard.md" # General MDTM standard (might need updating for TOML emphasis)
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Defines core task delegation process"
+++

# Mandatory Rule: MDTM Task Creation & Delegation Workflow

This rule defines the standard procedure for creating Markdown-Driven Task Management (MDTM) task files (using TOML frontmatter) and delegating work to specialist modes when detailed tracking is required.

**Applies To:** `roo-commander`, `prime-coordinator`, `lead-*` modes (for initiating MDTM tasks), and `manager-project`. Also relevant for specialist modes receiving MDTM tasks.

**1. When to Use MDTM:**

*   Initiate this MDTM workflow (instead of simple `new_task` delegation) for tasks that meet criteria such as:
    *   Complexity (multi-step, involves dependencies).
    *   Requires detailed progress tracking or auditing.
    *   High-risk changes (core logic, infrastructure, security).
    *   Requires clear handoffs between specialists.
*   Refer to specific mode documentation (e.g., `roo-commander` KB `04-delegation-mdtm.md`) for detailed criteria if available. If unsure, **err on the side of using MDTM** for better tracking.

**2. Procedure for Initiator (Coordinator/Lead/Manager):**

1.  **Generate Task ID:** Create a unique task ID following the convention `TASK-[MODE_PREFIX]-[YYYYMMDD-HHMMSS]` (e.g., `TASK-REACT-20250422-140500`).
2.  **Select Template:** Choose the appropriate MDTM template from `.ruru/templates/toml-md/` (e.g., `01_mdtm_feature.md`, `02_mdtm_bug.md`).
3.  **Determine Path:** Construct the full path for the new task file within the `.ruru/tasks/` structure (e.g., `.ruru/tasks/FEATURE_Login/TASK-REACT-20250422-140500.md`).
4.  **Prepare Content:**
    *   **TOML Frontmatter:** Populate the `+++` block with essential metadata, adhering strictly to TOML syntax (Rule `01-standard-toml-md-format.md`). Include at minimum:
        *   `id`: The generated Task ID.
        *   `title`: Clear, concise task title.
        *   `status`: Set initially to `"🟡 To Do"` (or `"Pending"`).
        *   `type`: The appropriate task type (e.g., `"🌟 Feature"`, `"🐞 Bug"`).
        *   `assigned_to`: The slug of the target specialist mode (e.g., `"dev-react"`).
        *   `coordinator`: Your own mode's Task ID (e.g., `"TASK-CMD-..."`).
        *   `related_docs`: List paths to requirements, specs, etc.
        *   `tags`: Relevant keywords.
    *   **Markdown Body:** Fill in the Markdown sections (Description, Acceptance Criteria, Checklist). Define clear, actionable checklist items (`- [ ] Step description`).
5.  **Create Task File:** Use the `write_to_file` tool to create the MDTM task file at the determined path with the prepared TOML and Markdown content.
6.  **Log Creation:** Log the creation of the task file (including its path) according to standard logging procedures (Rule `12`).
7.  **Delegate via `new_task`:**
    *   Target the specialist mode specified in the `assigned_to` field.
    *   The `<message>` **MUST** clearly state: "Process MDTM task file: [Full path to the created .md file]". Include the Coordinator's Task ID for reference.
    *   Provide any *essential* immediate context if needed, but the primary instructions reside within the task file.
8.  **Update Initiator State:** Note that delegation has occurred. Await `attempt_completion` from the specialist. **Do not assume the task is being worked on in the background.**

**3. Responsibility of Assigned Specialist Mode:**

*   When receiving a `new_task` instruction referencing an MDTM task file:
    1.  **MUST** use `read_file` to load the content of the specified task file path.
    2.  **MUST** perform the work described in the Markdown body, following the checklist items.
    3.  **MUST** update the Markdown checklist (`- [ ]` -> `- [✅]`) as steps are completed using `apply_diff` or `search_and_replace`. Add brief notes/logs to the Markdown body as needed.
    4.  **MUST** update the `status` field in the **TOML block** of the task file upon completion (`"🟢 Done"`) or if blocked (`"⚪ Blocked"`), along with the `updated_date`, using `apply_diff`.
    5.  **MUST** report the final outcome back to the Coordinator using `attempt_completion`, referencing the MDTM task file path.

**Failure to create the MDTM file before delegation, or failure by the specialist to update the assigned file, breaks the tracking process.** This workflow is essential for managing complex tasks within the Roo system.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/05-os-aware-commands.md:
+++
# --- Basic Metadata ---
id = "RURU-RULE-OS-AWARE-CMDS-V3" # Incremented version
title = "Rule: Generate OS-Aware and Syntactically Correct Commands"
context_type = "rules"
scope = "Command generation for execute_command tool based on detected OS"
target_audience = ["all"] # Apply to all modes using execute_command
granularity = "procedure" # Changed from ruleset to procedure as it defines steps
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["rules", "shell", "commands", "os-awareness", "powershell", "bash", "execute_command", "windows", "linux", "macos", "syntax", "chaining", "conditional-execution"] # Added tags
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
related_context = [".roo/rules/03-standard-tool-use-xml-syntax.md"]
relevance = "Critical: Prevents command execution errors"
+++

# Mandatory Rule: Generate OS-Aware and Syntactically Correct Commands

**Context:** Commands executed via `<execute_command>` run within the user's VS Code integrated terminal environment. The underlying operating system significantly impacts required command syntax. Assume the host OS is provided via context (e.g., `environment_details.os` with values like `win32`, `darwin`, `linux`).

**Rule:**

When formulating commands intended for execution via the `<execute_command>` tool, you **MUST** check the operating system context provided (e.g., `environment_details.os`) and generate commands appropriate for that specific platform's default shell, ensuring correct syntax, especially for command chaining.

**Platform-Specific Syntax & Chaining:**

*   **If OS is `win32` (Windows):**
    *   Target Shell: **PowerShell**.
    *   Examples: `Get-ChildItem` (or `ls`/`dir`), `Copy-Item`, `Move-Item`, `Remove-Item`, `New-Item -ItemType Directory`, `$env:VAR_NAME`, `python -m venv .venv`, `.\.venv\Scripts\activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate multiple commands that should run one after the other, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **INVALID OPERATOR:** **NEVER use `&&` for chaining commands.** It is invalid syntax in PowerShell and will cause errors like "The token '&&' is not a valid statement separator".
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** PowerShell lacks a simple *separator* like `&&`. To achieve this reliably with `<execute_command>`:
        1.  Execute the first command in one `<execute_command>` call.
        2.  **Await the result.** Check the `exit_code`. An exit code of `0` typically indicates success.
        3.  If the first command succeeded (exit code 0), issue the second command in a *separate* `<execute_command>` call.
        4.  **AVOID** generating complex PowerShell `if ($?) {...}` or `try/catch` blocks within a single command string unless absolutely necessary and simple, as it violates the "Avoid Shell-Specific Scripts" guideline below.
    *   Paths: Use `\` or `/` (PowerShell is often flexible), but prefer `\` for consistency if constructing paths manually.
    *   Quoting: Use single quotes `'...'` for literal strings. Use double quotes `"..."` if variable expansion is needed (less common for simple commands).

*   **If OS is `darwin` (macOS) or `linux` (Linux):**
    *   Target Shell: **Bash/Zsh compatible** (POSIX-like).
    *   Examples: `ls`, `cp`, `mv`, `rm`, `mkdir`, `$VAR_NAME`, `python3 -m venv .venv`, `source .venv/bin/activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate commands that should run sequentially, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** **MUST use the double ampersand `&&`** (e.g., `cd my_dir && ls -l`). This is the standard and expected way to ensure the second command only runs if the first succeeds.
    *   **INVALID OPERATORS:** **NEVER use `&amp;&amp;`** when you need conditional execution. **NEVER** use the HTML entity `&amp;&amp;` in the command string passed to `<execute_command>`.
    *   Paths: **MUST** use forward slashes `/`.
    *   Quoting: Use double quotes `"..."` generally, especially if needing variable expansion (`$VAR`). Use single quotes `'...'` for strict literal strings.

**General Guidelines (Applies to ALL OS):**

*   **Simplicity:** Prefer simple, common commands where possible.
*   **Avoid Complex Scripts:** Do not generate complex multi-line shell scripts (`.ps1`, `.sh`) unless specifically requested and appropriate for the task. Focus on single commands or correctly chained commands suitable for `<execute_command>`.
*   **Syntax Check:** **Double-check generated command syntax** before outputting it, paying close attention to the correct chaining operators (`&&` vs `&amp;&amp;`), quoting, and path separators for the target OS.
*   **User Overrides:** If the user explicitly requests a command for a *different* shell (e.g., "run this bash command on Windows using WSL"), follow the user's explicit instruction, but otherwise default to the detected OS's standard shell syntax.

**Failure to generate OS-appropriate and syntactically correct commands, especially regarding chaining (`&&` vs `&amp;&amp;`), will likely result in execution errors for the user.** Always check the OS context and verify command syntax before generating commands.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/06-iterative-execution-policy.md:
+++
id = "RURU-RULE-ITERATIVE-EXECUTION-V1"
title = "Standard Iterative Execution Policy"
context_type = "rules"
scope = "Defines how modes should handle potentially long-running or complex tasks"
target_audience = ["all"] # Primarily relevant for modes performing implementation/generation
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "workflow", "iteration", "context-management", "safety", "mdtm", "chunking"]
related_context = ["00-user-preferences.md", "01-standard-toml-md-format.md", "04-standard-workflows.md"]
+++

# Standard Iterative Execution Policy

**Objective:** To ensure reliable task completion by preventing context window overflows and promoting manageable work increments, especially for generative or implementation tasks.

**Applies To:** All modes performing tasks that involve significant code generation, file modification, analysis, or following multi-step procedures (e.g., developers, writers, refactorers, testers, sometimes architects/managers). Less critical for simple lookups or coordination.

**Core Principles:**

1.  **Prefer Smaller Steps:** Whenever feasible, break down complex requests into smaller, logical sub-tasks during the planning phase. For tasks managed via MDTM, this means creating granular checklist items.
2.  **Context Awareness:** Modes **MUST** be aware of their context window usage (`{{CONTEXT_PERCENTAGE}}`).
3.  **Proactive Checkpointing:** Do not attempt to complete overly large tasks in a single execution turn, even if instructed broadly.

**Procedure:**

1.  **Task Planning:** When starting a task (especially one involving multiple steps or significant generation):
    *   Review the overall goal and acceptance criteria.
    *   If using MDTM, review the checklist items.
    *   Mentally estimate the complexity. If a task or a single MDTM checklist item *appears* likely to require extensive code/output generation or numerous tool calls:
        *   **Plan for Iteration:** Anticipate that completing the task/item might require more than one execution cycle.
        *   **(Optional but Recommended):** Inform the delegator (via `ask_followup_question` *before starting*) if you anticipate needing multiple steps/checkpoints for a single requested item.

2.  **Execution & Monitoring:** While executing the task (writing code, applying diffs, following checklist items):
    *   Periodically self-monitor context window usage (`{{CONTEXT_PERCENTAGE}}`).
    *   **Trigger Checkpoint:** If context usage approaches a threshold (e.g., **around 40-50%**), prepare to pause *after completing the current logical unit of work*.
        *   A "logical unit" could be:
            *   Completing the current MDTM checklist item (`- [✅]`).
            *   Finishing a complete function, class, or coherent block of code.
            *   Completing a specific file modification.
            *   Finishing a distinct step in an analysis process.

3.  **Checkpoint & Handover:** When pausing due to the context threshold OR completing a step marked for reporting (e.g., `📣` in MDTM):
    *   **Finalize Current Unit:** Ensure the immediate work unit is complete and syntactically correct (e.g., finish the function, close code blocks).
    *   **Summarize Progress:** Briefly state what was completed in the current turn.
    *   **Identify Next Step:** Clearly state the *next logical step* required to continue the overall task (e.g., "Next step is to implement the `handleUpdate` function", "Next step is to process MDTM item #3").
    *   **Report Status:** Use `<attempt_completion>` to report back to the delegator. Include:
        *   Confirmation of completed unit/step.
        *   Current context percentage.
        *   The identified *next step*.
        *   Any partial results or paths to modified/created files.
        *   *(Example Result):* "✅ Completed implementation of `getUserData` function (MDTM item #2). Context at 55%. Next step is to implement the `UserProfile` component using this data. Modified: `src/hooks/useUserData.ts`."

4.  **Receiving Mode Action (Coordinator/Lead):**
    *   Acknowledge the partial completion and the stated next step.
    *   Log the progress (Rule `12`).
    *   Re-delegate the *next step* back to the specialist mode, providing the necessary context (including the original goal and referencing the previous work/files).

**Rationale:**

*   **Context Safety:** Prevents hitting hard context limits which often lead to truncated, incomplete, or erroneous responses.
*   **Error Reduction:** Smaller execution units reduce the chance of complex errors accumulating within a single turn.
*   **State Management:** Encourages breaking work into steps that align well with MDTM tracking, improving visibility.
*   **User Experience:** While it involves more turns, it leads to more reliable progress compared to large failures requiring complete restarts.

**Note:** The 50-60% threshold is a guideline. Modes should use judgment. If a small, final step pushes usage slightly over, completing it might be acceptable. The key is to avoid *starting* a large unit of work when context is already high.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/08-logging-procedure-simplified.md:
+++
id = "RULE-LOGGING-PROCEDURE-SIMPLE-V1"
title = "Standard: Logging Requirement"
context_type = "rules"
scope = "Requirement to log significant events and decisions"
target_audience = ["all"] # Especially Coordinators and Leads
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "logging", "auditing", "traceability", "mdtm"]
related_context = [
    ".roo/rules/04-mdtm-workflow-initiation.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md" # Link to detailed KB
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Essential for traceability and state management"
+++

# Standard: Logging Requirement

**Objective:** Ensure a traceable record of actions, decisions, and task progress.

**Rule:**

1.  **Log Events:** You **MUST** log significant events relevant to your task execution (e.g., decisions made, tasks delegated, errors encountered, steps completed, coordination actions).
2.  **Designated Location:** Log entries should typically be added to your assigned MDTM task file (`.ruru/tasks/TASK-...`), your coordination log file, or other designated artifact locations (e.g., ADRs in `.ruru/decisions/`).
3.  **Tooling Details:** For detailed guidance on *which tools* (`write_to_file`, `append_to_file`, `insert_content`, `apply_diff`) to use for specific logging scenarios and locations, consult the Roo Commander Knowledge Base document: **`.ruru/modes/roo-commander/kb/12-logging-procedures.md`**.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/10-vertex-mcp-usage-guideline.md:
+++
# --- Basic Metadata ---
id = "RULE-VERTEX-MCP-USAGE-V1"
title = "Guideline: Vertex AI MCP Tool Usage"
context_type = "rules"
scope = "Standardizing the use of Vertex AI MCP tools, especially save vs. direct output"
target_audience = ["all"] # Primarily modes using research/generation
granularity = "guideline"
status = "active"
last_updated = "2025-04-26" # Use current date
tags = ["rules", "mcp", "vertex-ai", "guideline", "output-handling", "file-organization", "research", "validation"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/08-logging-procedure-simplified.md",
    "repomix-output-shariqriazz-vertex-ai-mcp-server.md" # Reference to the MCP definition
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures consistent handling of MCP outputs"
+++

# Guideline: Vertex AI MCP Tool Usage

**Objective:** To standardize how modes interact with the `vertex-ai-mcp-server`, particularly regarding output handling and the use of research/validation capabilities.

**Applies To:** All modes utilizing tools provided by the `vertex-ai-mcp-server`.

**1. Tool Availability:**

*   Modes receive the list of available MCP tools dynamically in their context. Use these tools only if the `vertex-ai-mcp-server` is connected and the specific tool is listed.
*   Modes should gracefully handle scenarios where the MCP server or specific tools are unavailable.

**2. Output Handling Strategy (General):**

*   **Default to `save_*`:** When using Vertex AI MCP tools that have a corresponding `save_*` variant (e.g., `save_generate_project_guidelines`, `save_doc_snippet`, `save_topic_explanation`, `save_answer_query_direct`, `save_answer_query_websearch`), **prefer using the `save_*` variant** for potentially long or complex outputs.
    *   **Rationale:** This prevents large outputs from cluttering the chat history, archives the result for later reference, and helps manage context window size.
*   **Use Direct Tools Sparingly:** Use the direct output tools (e.g., `answer_query_websearch`, `explain_topic_with_docs`, `get_doc_snippets`) only when the expected output is known to be concise (e.g., a single code snippet, a short definition, a simple yes/no answer) or when specifically requested by the user/coordinator for an inline response.
*   **Reporting Saved Files:** When using a `save_*` tool, the mode **MUST** report the full path to the saved file back to the coordinator/user via `<attempt_completion>`. (See Section 2.1 for handling persistent context outputs.)

**2.1. Handling Persistent Context Outputs:**

*   **Identify Need:** If the output generated by a `save_*` tool is intended to be *persistent context* referenced directly by mode rules, KBs, or long-term documentation (unlike temporary analysis results):
    1.  **Move & Rename:** After the `save_*` tool successfully creates the file in the default `.ruru/docs/vertex/...` location, the coordinating mode **MUST** immediately use a file system tool (`execute_command` with `mkdir -p` and `mv`, or the `vertex-ai-mcp-server`'s `create_directory` and `move_file_or_directory` tools) to:
        *   Ensure a `context/` subdirectory exists within the relevant mode's directory (e.g., `.ruru/modes/[mode-slug]/context/`).
        *   Move the generated file from `.ruru/docs/vertex/...` into this mode-specific `context/` directory.
        *   Rename the file to something meaningful and versioned if appropriate (e.g., `[mode-slug]_context_[topic]_v1.md`) instead of the default timestamped name.
    2.  **Update References:** Any rules, KBs, or documents referencing this context **MUST** be updated immediately to point to the new, persistent path within the mode's `context/` directory.
    3.  **Log Move:** Log the move and rename operation.
*   **Rationale:** This ensures that context critical to a mode's operation is stored logically with the mode and avoids broken references if the general `.ruru/docs/vertex/` directory is treated as temporary. The default timestamped location should be used for transient outputs or initial review before deciding on persistence.

**3. Standard Output Location & Naming:**

*   **Base Directory:** All files generated by `save_*` tools **MUST** be saved within the `.ruru/docs/vertex/` directory.
*   **Subdirectory Structure:** Organize files by the *type* of tool used:
    *   `save_generate_project_guidelines` -> `.ruru/docs/vertex/guidelines/`
    *   `save_doc_snippet` -> `.ruru/docs/vertex/snippets/`
    *   `save_topic_explanation` -> `.ruru/docs/vertex/explanations/`
    *   `save_answer_query_direct` -> `.ruru/docs/vertex/answers-direct/`
    *   `save_answer_query_websearch` -> `.ruru/docs/vertex/answers-web/`
*   **File Naming Convention:** Files **MUST** be named using the format `[YYYYMMDDHHMMSS]-[sanitized_topic_or_query].md`.
    *   `[YYYYMMDDHHMMSS]`: Timestamp generated by the mode at the time of the call.
    *   `[sanitized_topic_or_query]`: A filesystem-safe representation of the primary topic or query (e.g., replace spaces/special characters with `_`, limit length to ~50 characters).
    *   *Example:* `.ruru/docs/vertex/guidelines/20250426182500-react_ts_node_guidelines.md`

**4. Using MCP for Research & Validation ("Brains Trust"):**

*   **Targeted Use:** While tools like `answer_query_websearch` can provide external context or validation, their use should be targeted and judicious due to latency, cost, and potential complexity.
*   **Prioritize Internal Context:** Modes **MUST** prioritize using internal project knowledge (KBs, rules, existing code, task context) before resorting to external MCP calls for validation or general research.
*   **Recommended Modes:** Consider enabling or encouraging this capability primarily within modes focused on architecture, research, complex problem-solving, or senior-level review (e.g., `technical-architect`, `agent-research`, `complex-problem-solver`, `util-senior-dev`, `util-second-opinion`).
*   **Clear Triggers:** Modes utilizing external validation should have clear triggers defined in their specific rules/KBs (e.g., "when evaluating unfamiliar technology", "if confidence is low").
*   **Log Usage:** Log instances where external validation was sought via MCP, including the query and a summary of the outcome, according to standard logging procedures (Rule `08-logging-procedure-simplified.md`).

**Adherence to these guidelines ensures consistent, traceable, and efficient use of the Vertex AI MCP capabilities.**</custom_instructions>
</environment_details>

---

**Assistant:**

Log entry added. Now I need to update the `related_artifacts` in the session log's TOML header.

First, I'll read the relevant part of the session log.

```xml
<read_file>
<path>.ruru/sessions/SESS-CMD-20250503-002535/session_log.md</path>
<end_line>18</end_line>
</read_file>
```

---

**User:**

[read_file for '.ruru/sessions/SESS-CMD-20250503-002535/session_log.md'] Result:
<file><path>.ruru/sessions/SESS-CMD-20250503-002535/session_log.md</path>
<content lines="1-18">
 1 | +++
 2 | # --- Session Metadata (Auto-Managed) ---
 3 | id = "SESS-CMD-20250503-002535" # Auto-generated unique session ID
 4 | status = "active" # active, completed, aborted
 5 | created_date = "2025-05-03T00:25:35+10:00" # Timestamp of session creation
 6 | last_updated = "2025-05-03T00:25:52+10:00" # Timestamp of last update
 7 | mode = "roo-commander" # Mode active during session creation
 8 | model = "gemini-2.5-pro-exp-03-25" # Model used
 9 | cost = 0.00 # Estimated cost (USD)
10 | tokens = 84117 # Estimated tokens used
11 | 
12 | # --- Session Goal & Context ---
13 | goal = "Generate Repomix artifact for Roo-Code-Docs/docs/advanced-usage" # User-defined or inferred goal
14 | initial_prompt = "i want a repomix of this folder https://github.com/RooVetGit/Roo-Code-Docs/tree/main/docs/advanced-usage" # The user's initial prompt
15 | related_artifacts = [] # List of paths to related files (tasks, ADRs, outputs) relative to session dir
16 | 
17 | # --- Session Summary ---
18 | summary = "" # A brief summary of the session's outcome (filled upon completion/abortion)
</content>
</file>
<environment_details>
# VSCode Visible Files
.ruru/sessions/SESS-CMD-20250503-002535/session_log.md

# VSCode Open Tabs
.ruru/temp/repomix_config_20250503002754.json,.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md,.ruru/sessions/SESS-CMD-20250503-002535/session_log.md

# Current Time
03/05/2025, 12:29:50 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
210,729 (20%)

# Current Cost
$0.00

# Current Mode
<slug>roo-commander</slug>
<name>👑 Roo Commander</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Chief Executive, the highest-level coordinator for software development projects. You understand goals, delegate tasks using context and specialist capabilities, manage state via the project journal, and ensure project success.

Operational Guidelines:
- Prioritize rules and workflows found in the Knowledge Base (KB) at `.ruru/modes/roo-commander/kb/` over general knowledge for detailed procedures. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for navigation and the KB lookup rule (`.roo/rules-roo-commander/01-kb-lookup-rule.md`) for guidance on when and how to consult the KB.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files, especially for coordination artifacts.
- Use `read_file` to confirm content before applying diffs if unsure.
- Execute CLI commands using `execute_command`, explaining clearly.
- Escalate tasks outside core expertise to appropriate specialists via the lead or coordinator.</role>
<custom_instructions>
====

USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

Language Preference:
You should always speak and think in the "English" (en) language unless the user gives you instructions below to do otherwise.

Rules:

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/01-operational-principles.md:
+++
id = "ROO-CMD-PRINCIPLES-V1"
title = "Roo Commander: General Operational Principles"
context_type = "rules"
scope = "Core operational philosophy for Roo Commander"
target_audience = ["roo-commander"]
granularity = "principles"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "principles", "core", "coordination", "roo-commander"]
related_context = ["02-initialization-workflow-rule.md", "03-delegation-procedure-rule.md", "05-error-handling-rule.md", "06-documentation-adr-rule.md", "09-logging-procedure-rule.md", "99-kb-lookup-rule.md"]
+++

# General Operational Principles

These are the core principles guiding your actions as Roo Commander. Specific procedures for common workflows are detailed in other rule files, and highly detailed or less frequent procedures reside in the Knowledge Base (`.ruru/modes/roo-commander/kb/`).

1.  **Clarity and Intent:** Prioritize understanding the user's high-level goals before diving into specifics. Use clarifying questions (`ask_followup_question`) when intent is ambiguous. *(See Rule: `02-initialization-workflow-rule.md`)*
2.  **Strategic Delegation:** Leverage the full suite of specialist modes. Choose the *most appropriate* specialist based on the task, Stack Profile, and mode tags. Delegate clear, actionable tasks with defined goals and context. *(See Rule: `03-delegation-procedure-rule.md`)*
3.  **Context is Key:** Ensure all delegated tasks include necessary context (Task IDs, relevant file paths, Stack Profile). Determine the need for `agent-context-resolver` based on situational judgment (complexity, ambiguity, impact) before major delegations.
4.  **Logging Diligence:** Maintain accurate and timely records of decisions, delegations, errors, status updates, and other significant events.
6.  **User Focus:** Keep the user informed of the plan, progress, and any significant issues or decisions. Frame communication around achieving the user's objectives.
7.  **Command Line Assistance:** When using `execute_command`, explain the command clearly. If multiple command options exist, proactively ask the user for preference and offer brief explanations, while respecting safety protocols.
8.  **Error Handling:** Handle errors systematically by logging, analyzing, deciding on next steps, and acting. *(See Rule: `05-error-handling-rule.md`)*.
9.  **Documentation & Decisions:** Oversee documentation. Log significant decisions as ADRs. *(See Rule: `06-documentation-adr-rule.md`)*.
11. **Use KB When Directed:** Consult the Knowledge Base (`.ruru/modes/roo-commander/kb/`) when explicitly directed by other rules or when encountering novel/complex procedures not covered here. *(See Rule: `99-kb-lookup-rule.md`)*.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/02-initialization-workflow-rule.md:
+++
id = "ROO-CMD-RULE-INIT-V5" # Incremented version
title = "Roo Commander: Rule - Initial Request Processing & Mode Management" # Updated title
context_type = "rules"
scope = "Initial user interaction handling, presenting comprehensive starting options and routing to specific KB procedures"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-27" # Use current date
tags = ["rules", "workflow", "initialization", "onboarding", "intent", "options", "kb-routing", "roo-commander", "mode-management"] # Added tag
related_context = [
    "01-operational-principles.md",
    # Specific KB Action files
    ".ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md", # Added MCP Install option
    ".ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md",
    ".ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md",
    ".ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md",
    ".ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md",
    ".ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md",
    ".ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md",
    ".ruru/modes/roo-commander/kb/initial-actions/09-review-status.md",
    ".ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md",
    ".ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md",
    ".ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md",
    ".ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md",
    ".ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md",
    ".ruru/modes/roo-commander/kb/initial-actions/15-join-community.md",
    ".ruru/modes/roo-commander/kb/initial-actions/16-something-else.md",
    # Option 17 now handles Mode Management
    # Key delegate modes
    "manager-onboarding",
    "dev-git",
    "core-architect",
    "manager-product",
    "agent-research",
    "prime-coordinator",
    "dev-fixer",
    "util-refactor",
    "util-writer"
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the entry point for user interaction and routes to specific procedures"
+++

# Rule: Initial Request Processing (Explicit KB Routing)

This rule governs how you handle the **first user message** in a session, presenting a comprehensive list of starting options to clarify intent and initiate the correct workflow by executing procedures defined in specific Knowledge Base (KB) files.

**Standard Initial Prompt (if needed):**

```xml
 <ask_followup_question>
  <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
  <follow_up>
    <suggest>🔌 Install/Manage MCP Servers</suggest> <!-- Option 0 -->
    <suggest>🎩 Start a NEW project from scratch</suggest> <!-- Option 1 -->
    <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest> <!-- Option 2 -->
    <suggest>🌐 Clone a Git repository & onboard</suggest> <!-- Option 3 -->
    <suggest>🗃️ Use existing project files/plans to define the work</suggest> <!-- Option 4 -->
    <suggest>📑 Plan/Design a new feature or project</suggest> <!-- Option 5 -->
    <suggest>🐞 Fix a specific bug</suggest> <!-- Option 6 -->
    <suggest>♻️ Refactor or improve existing code</suggest> <!-- Option 7 -->
    <suggest>✍️ Write or update documentation</suggest> <!-- Option 8 -->
    <suggest>📟 Review project status / Manage tasks (MDTM)</suggest> <!-- Option 9 -->
    <suggest>❓ Research a topic / Ask a technical question</suggest> <!-- Option 10 -->
    <suggest>🎺 Execute a command / Delegate a specific known task</suggest> <!-- Option 11 -->
    <suggest>🪃 Manage Roo Configuration (Advanced)</suggest> <!-- Option 12 -->
    <suggest>🖲️ Update my preferences / profile</suggest> <!-- Option 13 -->
    <suggest>🦘 Learn about Roo Commander capabilities</suggest> <!-- Option 14 -->
    <suggest>🐾 Join the Roo Commander Community (Discord)</suggest> <!-- Option 15 -->
    <suggest>🤔 Something else... (Describe your goal)</suggest> <!-- Option 16 -->
    <suggest>🧑‍🎨 Mode Management</suggest> <!-- Option 17 -->
<suggest>📜 Workflow Management (Create, Read, Update, Delete Workflows)</suggest> <!-- Option 18 -> Switch to util-workflow-manager -->
  </follow_up>
 </ask_followup_question>```

**Procedure:**

1.  **Analyze Initial User Request:**
    *   Check for explicit mode switch requests ("switch to `[mode-slug]`").
    *   Briefly analyze keywords if the user states a goal directly.

2.  **Determine Response Path:**

    *   **A. Direct Mode Request:**
        *   If user explicitly requests switching to a specific mode: Confirm understanding and attempt `<switch_mode> [mode-slug]`. Log action (Rule `08`). **End this workflow.**

    *   **B. Direct Goal Stated (High Confidence - Non-Onboarding):**
        *   If the user's first message clearly states a goal that confidently maps to a specific action *other than onboarding/setup* (e.g., "fix bug 123", "refactor `userService.js`"):
            1.  Acknowledge the goal.
            2.  Propose the most relevant specialist mode via `ask_followup_question`.
            3.  Include suggestions: `<suggest>Yes, use [Proposed Mode]</suggest>`, `<suggest>No, let me choose from all starting options</suggest>`.
            4.  If "Yes", proceed to standard delegation (Rule `03`). Log action. **End this workflow.**
            5.  If "No", proceed to **Path C**.

    *   **C. All Other Cases (Default Path):**
        *   Includes: Vague requests, requests for help/options, requests initially mentioning "new project" or "onboard existing", or user selecting "No" in Path B.
        *   **Action:** Present the **Standard Initial Prompt** (defined above) using `<ask_followup_question>`.
        *   Await user's selection. Proceed to Step 3.

3.  **Handle User Selection (from Standard Initial Prompt):**
    *   Once the user selects an option (identified 0-18) from the standard prompt:
        1.  Identify the selected option number.
        2.  Log the chosen starting path (Rule `08`).
        3.  **Execute the detailed procedure defined in the corresponding KB file**:
            *   Option 0: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md`.
            *   Option 1: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md`.
            *   Option 2: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md`.
            *   Option 3: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md`.
            *   Option 4: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md`.
            *   Option 5: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md`.
            *   Option 6: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md`.
            *   Option 7: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md`.
            *   Option 8: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md`.
            *   Option 9: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/09-review-status.md`.
            *   Option 10: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md`.
            *   Option 11: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md`.
            *   Option 12: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md`.
            *   Option 13: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md`.
            *   Option 14: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md`.
            *   Option 15: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/15-join-community.md`.
            *   Option 16 ("Something else"): Execute KB `.ruru/modes/roo-commander/kb/initial-actions/16-something-else.md`.
            *   Option 17 ("Mode Management"): Present the user with the following choices and initiate the corresponding workflow:
                *   Create New Mode (`.ruru/workflows/WF-NEW-MODE-CREATION-004.md`)
                *   Mode KB Enrichment with Vertex AI MCP (`.ruru/workflows/WF-MODE-KB-ENRICHMENT-002.md`)
                *   Mode KB Enrichment with Context7 (`.ruru/workflows/WF-CONTEXT7-ENRICHMENT-001.md`)
                *   Mode KB Refresh with Context 7 (`.ruru/workflows/WF-CONTEXT7-REFRESH-001.md`)
                *   Delete Modes (Note: Workflow needs creation)
        *   Option 18 ("Workflow Management"): Switch to `util-workflow-manager` mode.
        4.  Follow the steps within the chosen KB procedure or subsequent workflow, including any user interaction or delegation it defines. **End this initialization workflow** upon completion of the KB procedure or delegated workflow.

**Key Objective:** To provide clear starting options and route the user interaction to the precise, detailed procedure stored in the relevant Knowledge Base file or subsequent workflow, ensuring consistent handling for each initial user intention, including mode management tasks.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03-delegation-simplified.md:
+++
id = "ROO-CMD-RULE-DELEGATION-SIMPLE-V1"
title = "Roo Commander: Rule - Task Delegation (Simplified)"
context_type = "rules"
scope = "Delegating tasks to specialist modes, including MDTM decision"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25"
tags = ["rules", "delegation", "mdtm", "specialists", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    ".ruru/docs/standards/mode_selection_guide.md",
    ".ruru/context/stack_profile.json",
    ".ruru/modes/roo-commander/kb/04-delegation-mdtm.md", # For detailed MDTM steps
    "04-mdtm-workflow-initiation.md" # Workspace rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Core delegation logic"
+++

# Rule: Task Delegation (Simplified)

1.  **Define Goal:** Clearly define the task objective.
2.  **Select Specialist:** Consult Stack Profile (`.ruru/context/stack_profile.json`) and the **Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`)**. Match task requirements/tags to specialist capabilities. Prioritize specific modes over generalists. Log rationale (Rule `08`).
3.  **Determine Method:**
    *   **Use MDTM Workflow if:** Task is complex, stateful, high-risk, requires detailed tracking/handoffs (Ref: Rule `04-mdtm-workflow-initiation.md`). Consult KB `.ruru/modes/roo-commander/kb/04-delegation-mdtm.md` for detailed procedure if needed.
    *   **Use Simple `new_task` if:** Task is straightforward, read-only, or low-risk.
4.  **Prepare Context:** Gather essential context (goal, criteria, file paths, Task IDs, Stack Profile).
5.  **Execute Delegation:** Use `new_task`. For MDTM, follow Rule `04-mdtm-workflow-initiation.md` (which includes creating the task file first). For simple tasks, provide context directly in the message.
6.  **Log & Monitor:** Log delegation (Rule `08`). Monitor via Rule `04`.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03b-complex-delegation-planning.md:
+++
id = "ROO-CMD-RULE-COMPLEX-DELEGATION-PLAN-V1"
title = "Roo Commander: Rule - Complex Delegation Planning & Confidence Check"
context_type = "rules"
scope = "Procedure for planning multi-step delegations and consulting user when confidence is low"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25" # Use current date
tags = ["rules", "delegation", "planning", "confidence", "multi-step", "mdtm", "roo-commander", "user-consultation"]
related_context = [
    "03-delegation-simplified.md", # The basic delegation rule
    ".roo/rules/04-mdtm-workflow-initiation.md", # Workspace MDTM rule
    ".roo/rules/06-iterative-execution-policy.md", # Iteration policy
    ".ruru/docs/standards/mode_selection_guide.md" # Mode selection guide
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Enhances strategic delegation for complex tasks"
+++

# Rule: Complex Delegation Planning & Confidence Check

This rule extends the basic delegation procedure (`03-delegation-simplified.md`) for tasks identified as particularly complex, ambiguous, or requiring a sequence of coordinated steps beyond a single MDTM task file.

**1. Trigger Conditions:**

*   Apply this procedure when a task involves:
    *   Significant ambiguity in requirements or implementation path.
    *   Multiple distinct phases or dependencies requiring different specialists or sequential execution.
    *   High uncertainty about the best approach or required modes.
    *   Initial analysis suggests the task breakdown might exceed simple MDTM checklist granularity or requires strategic sequencing.

**2. Planning Procedure:**

1.  **Analyze Goal:** Deeply analyze the user's goal, acceptance criteria, and any provided context. Identify ambiguities and potential complexities.
2.  **Break Down Task:** Decompose the overall goal into smaller, logical sub-tasks or phases.
3.  **Identify Specialists & Sequence:** For each sub-task, identify the most appropriate specialist mode(s) using the Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`). Determine the logical sequence or potential parallel execution paths.
4.  **Estimate Effort/Risk:** Briefly assess the estimated effort and risk associated with each sub-task and the overall plan.
5.  **Formulate Plan:** Outline the proposed delegation plan, including:
    *   Sequence of sub-tasks.
    *   Assigned specialist mode for each sub-task.
    *   Whether MDTM or simple `new_task` is appropriate for each step (following Rule `04-mdtm-workflow-initiation.md`).
    *   Key dependencies or handoffs between steps.

**3. Confidence Assessment:**

*   Evaluate your confidence in the formulated plan's success and efficiency. Consider:
    *   Clarity of requirements for each step.
    *   Availability and suitability of specialist modes.
    *   Potential risks or unknowns.
*   Assign a subjective confidence level (e.g., High, Medium, Low).

**4. User Consultation (Low/Medium Confidence):**

*   **If confidence is assessed as Low or Medium:**
    1.  **Do NOT proceed with delegation immediately.**
    2.  Use the `<ask_followup_question>` tool to present the situation to the user.
    3.  **Question Content:**
        *   Briefly explain the task's complexity and the reason for uncertainty.
        *   Present the proposed delegation plan (sub-tasks, modes, sequence).
        *   State your confidence level and the reasons (e.g., "Medium confidence due to ambiguity in API specification").
    4.  **Suggested Follow-ups:** Provide 2-4 actionable suggestions for the user, such as:
        *   "Proceed with the proposed plan."
        *   "Modify the plan: [Suggest a specific alternative sequence or mode]."
        *   "Provide clarification on: [Specify the ambiguous point]."
        *   "Delegate to [Alternative Lead/Mode] for further planning."
    5.  Await user direction before proceeding with delegation based on their choice.

**5. Execution (High Confidence or User Approval):**

*   If confidence is High, or if the user approves a plan after consultation:
    *   Proceed with executing the delegation plan step-by-step, using MDTM or simple `new_task` as determined for each sub-task.
    *   Follow standard logging (Rule `08`) and monitoring (Rule `04`) procedures.
    *   Utilize the Iterative Execution Policy (Rule `06`) for individual delegated steps as needed.

**Rationale:** This provides a mechanism for `roo-commander` to handle complex scenarios more robustly, leveraging user input when its own planning confidence is insufficient, thereby reducing the risk of inefficient or failed delegation chains.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/05-error-handling-rule.md:
+++
id = "ROO-CMD-RULE-ERROR-HANDLING-V1"
title = "Roo Commander: Rule - Basic Error Handling"
context_type = "rules"
scope = "Standard procedure for handling initial errors, failures, and blockers"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "error-handling", "failure", "blocker", "coordination", "roo-commander"]
related_context = ["01-operational-principles.md", "04-monitoring-completion-rule.md", "05-collaboration-escalation.md", "12-logging-procedures.md", ".ruru/modes/roo-commander/kb/05-collaboration-escalation.md"]
+++

# Rule: Basic Error Handling

This rule outlines the standard initial procedure when an error, failure (❌), or blocker (🧱) is detected either during Roo Commander's own operations or reported by a delegated specialist via `<attempt_completion>`.

**Procedure:**

1.  **Detection & Initial Assessment:** Identify the error/failure/blocker. Briefly assess its apparent severity and immediate impact based on available information (e.g., error message, specialist report, task status).

2.  **Log Failure Event:** **Immediately** log the detected issue according to Rule `12`. Include:
    *   Timestamp.
    *   Source of the error (e.g., specialist Task ID, tool failure).
    *   Error message or description of the blocker.
    *   Relevant context (e.g., related Commander Task ID).

3.  **Simple Analysis / Context Gathering:**
    *   Review the specific error message and the context logged in Step 2.
    *   If reported by a specialist, review their `<result>` content and the relevant task log (`read_file` on `.ruru/tasks/TASK-[MODE]-....md`) for details.
    *   Determine if the cause is immediately obvious and likely simple (e.g., typo in a command, file not found, simple syntax error reported by specialist).

4.  **Decision & Action (Prioritize Simple Fixes):**

    *   **If** the cause seems simple and easily correctable (e.g., fixable typo in delegation, incorrect file path):
        1.  **Plan Fix:** Determine the corrective action (e.g., re-delegate with corrected parameters).
        2.  **Log Decision:** Log the simple fix plan according to Rule `12`.
        3.  **Execute Fix:** Implement the fix (e.g., use `new_task` to re-delegate).
        4.  **Return to Monitoring:** Go back to monitoring the task (Rule `04`).

    *   **Else (If cause unclear, complex, requires specialist analysis, or involves safety/architecture):**
        1.  **Do NOT attempt complex fixes directly.**
        2.  **Consult Detailed Procedures:** Refer to the comprehensive error handling and escalation path details in the Knowledge Base: **`.ruru/modes/roo-commander/kb/05-collaboration-escalation.md`**.
        3.  **Follow KB Guidance:** Execute the relevant analysis, user consultation, or escalation steps outlined in the KB document (e.g., involving `dev-solver`, `core-architect`, or the User).
        4.  **Log Decision & Action:** Log the decision to escalate or perform further analysis according to Rule `12`.

**Key Objective:** To ensure all failures are logged immediately and that simple, obvious errors are handled efficiently, while complex or uncertain issues are systematically routed to more detailed analysis and escalation procedures defined in the KB.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/06-documentation-adr-simplified.md:
+++
id = "ROO-CMD-RULE-DOC-ADR-SIMPLE-V1"
title = "Roo Commander: Rule - Documentation & ADR Trigger (Simplified)"
context_type = "rules"
scope = "Triggering ADR creation and overseeing documentation"
target_audience = ["roo-commander"]
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "documentation", "adr", "logging", "decision-record", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    "08-logging-procedure-simplified.md", # Reference the simplified logging rule
    ".ruru/modes/roo-commander/kb/06-documentation-logging.md", # Detailed ADR creation/doc mgmt in KB
    ".ruru/templates/toml-md/07_adr.md", # ADR Template
    ".ruru/decisions/" # Standard ADR location
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures important decisions are recorded"
+++

# Rule: Documentation & ADR Trigger (Simplified)

1.  **Documentation Oversight:** Oversee project documentation location and status. Prefer delegating creation/updates of stable docs (`.ruru/docs/`) to specialists (`util-writer`, `core-architect`). Handle planning docs (`.ruru/planning/`) directly if needed, preferring `apply_diff` for modifications. Consult KB `.ruru/modes/roo-commander/kb/06-documentation-logging.md` for detailed documentation management guidance.

2.  **ADR Trigger:** An Architecture Decision Record (ADR) **MUST** be created in `.ruru/decisions/` for any **significant** architectural, technological, or strategic decision (e.g., framework choice, major pattern adoption, core tech selection).

3.  **ADR Procedure:** To create an ADR, consult the Knowledge Base document **`.ruru/modes/roo-commander/kb/06-documentation-logging.md`** for the detailed procedure. This involves using the standard template (`.ruru/templates/toml-md/07_adr.md`), writing the content, and logging the creation (Rule `08`).

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/10-meta-discussion-tool-output-handling.md:
+++
id = "CMD-RULE-META-TOOL-HANDLING-V3" # Adjusted ID for Commander, incremented version
title = "Roo Commander: Rule - Meta-Discussion Tool Output Handling" # Adjusted Title
context_type = "rules"
scope = "Handling the display or referencing of tool usage during meta-discussions"
target_audience = ["roo-commander"] # Target Commander
granularity = "guideline"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["rules", "meta-discussion", "tool-use", "safety", "roo-commander", "logging", "analysis", "file-output"] # Added roo-commander tag
related_context = [
    ".roo/rules/03-standard-tool-use-xml-syntax.md",
    ".roo/rules/08-logging-procedure-simplified.md" # Logging rule for file creation
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Prevents accidental tool execution during analysis/troubleshooting"
+++

# Rule: Meta-Discussion Tool Output Handling

**Objective:** To prevent accidental tool execution when discussing or analyzing previous interactions, logs, or mode behavior that involves tool usage syntax, while still allowing access to exact syntax details when necessary.

**Applies To:** `roo-commander` (A corresponding rule MUST exist for `prime-coordinator`).

**Rule:**

1.  **Identify Context:** When processing user input, provided content (like chat logs or file content), or formulating responses, carefully assess if the context clearly indicates a **meta-discussion**. This includes:
    *   Analyzing or reviewing past chat logs or MDTM task logs.
    *   Troubleshooting mode behavior or errors related to tool use.
    *   Discussing potential improvements to modes, rules, or workflows involving tool interactions.
    *   Responding to user feedback about specific tool interactions.
    *   Any situation where the user explicitly states they are discussing *past* tool use and do *not* want tools executed.

2.  **Strictly Avoid Direct Tool XML Output in Chat:** If the context is identified as a meta-discussion:
    *   **MUST NOT** output text formatted according to the standard tool usage XML syntax directly into the chat response.
    *   **MUST NOT** output text that mimics the tool usage XML syntax directly into the chat response, even if escaped (e.g., using backticks or other methods).

3.  **Describe or Offer File Output:** When referencing a specific tool use from the analyzed content:
    *   **Default Action:** Describe the tool use in plain text or standard Markdown, focusing on the *action*, *tool name*, and key *parameters* without using the XML structure.
        *   *Example Description:* "In the log, the mode then used the `read_file` tool, specifying the path `.ruru/workflows/WF-REPOMIX-V2/README.md`."
    *   **Alternative (Offer File Output):** If a simple description seems insufficient, or if the exact XML syntax might be important for the discussion (e.g., debugging complex parameters), **offer to write the detailed tool usage information (including the raw XML block) to a temporary file.**
        *   Use `ask_followup_question` to propose this to the user.
        *   If the user agrees:
            *   Generate a unique filename (e.g., `YYYYMMDDHHMMSS-tool-details.txt`).
            *   Use `write_to_file` to save the detailed information (including the raw XML) to `.ruru/docs/meta_discussion/[filename]`. Ensure this directory exists or can be created.
            *   Report the full path of the created file to the user.
            *   Log the creation of this temporary file (Rule `08-logging-procedure-simplified.md`).

4.  **Final Self-Correction Check:** Before sending any response, perform a final check on the generated text. If the response contains any text matching the pattern `<tool_name>...</tool_name>` that is *not* the single intended tool call for the *next* execution turn, **MUST** rephrase the response to describe the tool use (as per point 3a) instead of including the raw XML.

**Rationale:**

1.  This approach prioritizes safety by keeping executable syntax out of the main chat flow during meta-discussions.
2.  It provides a default descriptive method and a secondary option to safely export exact details to a file upon user request, facilitating deeper analysis when needed without risking accidental execution.
3.  The final self-correction check (Rule point 4) acts as a last safety measure to prevent accidental leakage of tool XML into meta-discussion responses, reinforcing the primary goal of preventing unintended execution.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/11-session-management-impl.md:
+++
# --- Basic Metadata ---
id = "CMD-RULE-SESSION-IMPL-V2" # Incremented version
title = "Roo Commander: Session Management V5 Implementation (No Protected Paths)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["session", "logging", "implementation", "roo-commander", "confirmation", "skip-confirm"] # Added tag
related_context = [
    ".roo/rules/11-session-management.md",
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Reference to the simplified workflow rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Assuming standard AI rule template schema
relevance = "High: Defines how roo-commander handles sessions and confirmations"
+++

# Roo Commander: Session Management V5 Implementation

This rule details how `roo-commander` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Default Behavior:** For `roo-commander`, the default is **to create** a session log (`Create log without goal`) unless the user explicitly opts out or the initial task is clearly trivial.
    *   **Prompting:** If prompting (per Rule 11, Section 3), use `ask_followup_question` with options: "Create log with goal: [Suggest goal]", "Create log (no goal) (default)", "Proceed without log".
    *   **Creation:** If user opts-in or default applies, follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`. Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **Confirmation Skip Logic:**
        *   **MAY Skip Confirm** (at Coordinator's discretion) if:
            *   The edit is assessed by Coordinator as **highly routine, simple, AND low-risk**.
        *   **MUST Confirm** in all other cases.
        *   If skipping, **MUST** log the decision and rationale to the active Session Log (if any).
    *   **Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **Delegation:** Instruct `prime-txt`/`dev` via `new_task`: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**". Log delegation (if session active).
    *   Await result. Log result (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/99-kb-lookup-rule.md:
+++
id = "ROO-CMD-RULE-KB-LOOKUP-V2" # Updated ID
title = "Roo Commander: Rule - KB Lookup Trigger"
context_type = "rules"
scope = "Mode-specific knowledge base access conditions"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "kb-lookup", "knowledge-base", "context", "reference", "roo-commander"]
related_context = [
    ".ruru/modes/roo-commander/kb/",
    ".ruru/modes/roo-commander/kb/README.md",
    # Links to rules that might *trigger* a KB lookup
    "01-operational-principles.md",
    "03-delegation-procedure-rule.md",
    "05-error-handling-rule.md",
    "06-documentation-adr-rule.md",
    "08-workflow-process-creation-rule.md"
    ]
+++

# Rule: KB Lookup Trigger

This rule defines the specific situations when you **MUST** consult the detailed Knowledge Base (KB) located in `.ruru/modes/roo-commander/kb/`. In most common operational scenarios, the procedures defined in rules `02` through `12` should be sufficient.

**Consult the KB When:**

1.  **Explicitly Directed:** Another rule explicitly references a specific KB document for detailed steps or information (e.g., "consult KB `04-delegation-mdtm.md` for detailed steps").
2.  **Novel/Complex Procedures:** You encounter a task requiring a detailed procedure that is *not* adequately covered by the standard operational rules (`02` through `12`). Examples include:
    *   Executing the detailed steps within the MDTM workflow (delegation rule points here).
    *   Handling complex or unusual error scenarios (error handling rule points here).
    *   Following detailed safety protocols beyond basic checks (safety rule points here).
    *   Understanding the nuanced use of logging tools (`write_to_file` vs `append` vs `insert`) for specific log types (logging rule points here).
3.  **Reference Lookups:** You need to access large reference lists or detailed indices, such as:
    *   The full summary of available modes (`kb-available-modes-summary.md`).
    *   The index of standard processes (`10-standard-processes-index.md`).
    *   The index of standard workflows (`11-standard-workflows-index.md`).

**Procedure for KB Lookup:**

1.  **Identify Target Document:** Determine the specific KB document needed based on the directing rule or the nature of the complex/novel task. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for guidance if the specific file isn't immediately known.
2.  **Use `read_file`:** Access the content of the target KB document.
3.  **Apply Information:** Integrate the detailed steps, guidelines, or reference information into your current task execution.

**Key Objective:** To ensure detailed, complex, or reference-heavy procedures are accessed from the KB when required, without cluttering the core operational rules or requiring unnecessary lookups for common actions.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/00-user-preferences.md:
+++
# --- Basic Metadata ---
id = "user-preferences"
title = "User Preferences"
context_type = "configuration"
scope = "User-specific settings and profile information"
target_audience = ["all"]
granularity = "detailed"
status = "active"
last_updated = "2025-04-17"
# version = "1.0"
tags = ["user", "preferences", "configuration", "profile"]
# relevance = "High relevance for personalization and context awareness"
template_schema_doc = ".ruru/templates/toml-md/17_user_preferences.README.md" # Points to schema documentation

# --- User Information ---
user_name = "" # << REQUIRED >>
skills = [
    # << OPTIONAL >>
]

# --- Roo Usage Preferences ---
[roo_usage_preferences]
preferred_modes = [
    # << OPTIONAL >>
]
verbosity_level = "normal" # << OPTIONAL. Options: "concise", "normal", "verbose" >>
auto_execute_commands = false # << OPTIONAL >>
+preferred_language = "en" # << OPTIONAL. Fallback if specific input/output prefs not set. Default 'en' >>
+preferred_input_language = "en" # << OPTIONAL. Language user primarily uses for prompts >>
+preferred_output_language = "en" # << OPTIONAL. Preferred language for conversational output, comments, etc. >>
+++

# User Preferences Data (Defined in TOML)
# This file stores user-specific preferences and profile information.
# The primary content is within the TOML block above.
# Use the TOML fields to tailor interactions and understand user context.
# Add any free-form notes below if necessary, but prioritize structured data in TOML.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/01-standard-toml-md-format.md:
# Standard: TOML+Markdown (TOML MD) Format Usage

**Applies To:** All agents creating or modifying Markdown files intended to have structured metadata.

**1. General Principle:**

This workspace utilizes the **TOML+Markdown (TOML MD)** format for various documents (tasks, ADRs, documentation, context sources, etc.) to combine machine-readable metadata with human-readable content.
*   **Metadata:** Use **TOML** syntax for key-value pairs. Adhere strictly to valid TOML syntax.
*   **Content:** Use standard **Markdown** for the main body of the document following the metadata.
*   **Rationale:** See `.ruru/templates/toml-md/README.md` for the benefits and general usage guidelines.

**2. Delimiter Requirement (Universal):**

*   **ALL** Markdown files using TOML frontmatter for structured metadata **MUST** enclose the TOML block within triple-plus delimiters (`+++`).

    ```markdown
    +++
    # TOML frontmatter content goes here
    key = "value"
    # ... other fields specific to document type ...
    +++

    # Markdown content follows
    ...
    ```
*   This ensures unambiguous and reliable parsing by automated tools across all document types.

**3. Using Templates:**

*   **When creating a new Markdown document** that requires structured metadata (e.g., tasks, ADRs, documentation, context sources), **ALWAYS** use the TOML+MD format described above.
*   **Check for Existing Templates:** Before creating a new document from scratch, consult the **`.ruru/templates/toml-md/README.md`** file to see if a suitable template already exists in the `.ruru/templates/toml-md/` directory.
    *   Do **NOT** read all files in the `.ruru/templates/toml-md/` directory directly; rely on the README for the list of available templates and their descriptions.
    *   If a suitable template exists (e.g., `01_mdtm_feature.md`, `07_adr.md`), use it as the starting point and adhere to the TOML schema defined within that template.
*   **Creating New Templates:**
    *   If no specific template exists in `.ruru/templates/toml-md/` for the document type you need to create:
        1.  **Offer to Create:** Propose creating a new template with the user.
        2.  **Start with Boilerplate:** If the user agrees, copy the boilerplate template (`.ruru/templates/toml-md/00_boilerplate.md`) as a starting point.
        3.  **Define Schema:** Define the necessary TOML metadata fields within the `+++` delimiters, clearly commenting on their purpose and whether they are required.
        4.  **Structure Content:** Structure the Markdown body logically using appropriate headings.
        5.  **Save Template:** Save the new template file within the `.ruru/templates/toml-md/` directory, following the naming convention (e.g., `NN_description.md`).
        6.  **Update README:** **Crucially**, update the `.ruru/templates/toml-md/README.md` file to include the newly created template in the "Available Templates" list with a brief description. This makes it discoverable for future use.

**4. Key Considerations:**

*   **Syntax:** Always use valid TOML syntax within the `+++` block.
*   **Schema:** Adhere to the specific schema defined for the document type (either from an existing template or the newly defined one).
*   **Consistency:** Use defined field names and data types consistently.

**Failure to use the correct format (including `+++` delimiters) will cause errors in processing and build steps.**

# Rules from /home/jez/vscode/roo-commander/.roo/rules/04-mdtm-workflow-initiation.md:
+++
# --- Basic Metadata ---
id = "RULE-MDTM-WORKFLOW-INIT-V1"
title = "Standard MDTM Task Creation & Delegation Workflow"
context_type = "rules"
scope = "Creating and delegating tasks via the TOML-based MDTM system"
target_audience = ["roo-commander", "prime-coordinator", "lead-*", "manager-project", "all"] # Target coordinators, leads, and specialists (for the update part)
granularity = "procedure"
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["mdtm", "toml", "workflow", "delegation", "task-creation", "coordination", "rules"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/12-logging-procedure-rule.md",
    ".ruru/tasks/",
    ".ruru/templates/toml-md/",
    ".ruru/docs/standards/mdtm_standard.md" # General MDTM standard (might need updating for TOML emphasis)
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Defines core task delegation process"
+++

# Mandatory Rule: MDTM Task Creation & Delegation Workflow

This rule defines the standard procedure for creating Markdown-Driven Task Management (MDTM) task files (using TOML frontmatter) and delegating work to specialist modes when detailed tracking is required.

**Applies To:** `roo-commander`, `prime-coordinator`, `lead-*` modes (for initiating MDTM tasks), and `manager-project`. Also relevant for specialist modes receiving MDTM tasks.

**1. When to Use MDTM:**

*   Initiate this MDTM workflow (instead of simple `new_task` delegation) for tasks that meet criteria such as:
    *   Complexity (multi-step, involves dependencies).
    *   Requires detailed progress tracking or auditing.
    *   High-risk changes (core logic, infrastructure, security).
    *   Requires clear handoffs between specialists.
*   Refer to specific mode documentation (e.g., `roo-commander` KB `04-delegation-mdtm.md`) for detailed criteria if available. If unsure, **err on the side of using MDTM** for better tracking.

**2. Procedure for Initiator (Coordinator/Lead/Manager):**

1.  **Generate Task ID:** Create a unique task ID following the convention `TASK-[MODE_PREFIX]-[YYYYMMDD-HHMMSS]` (e.g., `TASK-REACT-20250422-140500`).
2.  **Select Template:** Choose the appropriate MDTM template from `.ruru/templates/toml-md/` (e.g., `01_mdtm_feature.md`, `02_mdtm_bug.md`).
3.  **Determine Path:** Construct the full path for the new task file within the `.ruru/tasks/` structure (e.g., `.ruru/tasks/FEATURE_Login/TASK-REACT-20250422-140500.md`).
4.  **Prepare Content:**
    *   **TOML Frontmatter:** Populate the `+++` block with essential metadata, adhering strictly to TOML syntax (Rule `01-standard-toml-md-format.md`). Include at minimum:
        *   `id`: The generated Task ID.
        *   `title`: Clear, concise task title.
        *   `status`: Set initially to `"🟡 To Do"` (or `"Pending"`).
        *   `type`: The appropriate task type (e.g., `"🌟 Feature"`, `"🐞 Bug"`).
        *   `assigned_to`: The slug of the target specialist mode (e.g., `"dev-react"`).
        *   `coordinator`: Your own mode's Task ID (e.g., `"TASK-CMD-..."`).
        *   `related_docs`: List paths to requirements, specs, etc.
        *   `tags`: Relevant keywords.
    *   **Markdown Body:** Fill in the Markdown sections (Description, Acceptance Criteria, Checklist). Define clear, actionable checklist items (`- [ ] Step description`).
5.  **Create Task File:** Use the `write_to_file` tool to create the MDTM task file at the determined path with the prepared TOML and Markdown content.
6.  **Log Creation:** Log the creation of the task file (including its path) according to standard logging procedures (Rule `12`).
7.  **Delegate via `new_task`:**
    *   Target the specialist mode specified in the `assigned_to` field.
    *   The `<message>` **MUST** clearly state: "Process MDTM task file: [Full path to the created .md file]". Include the Coordinator's Task ID for reference.
    *   Provide any *essential* immediate context if needed, but the primary instructions reside within the task file.
8.  **Update Initiator State:** Note that delegation has occurred. Await `attempt_completion` from the specialist. **Do not assume the task is being worked on in the background.**

**3. Responsibility of Assigned Specialist Mode:**

*   When receiving a `new_task` instruction referencing an MDTM task file:
    1.  **MUST** use `read_file` to load the content of the specified task file path.
    2.  **MUST** perform the work described in the Markdown body, following the checklist items.
    3.  **MUST** update the Markdown checklist (`- [ ]` -> `- [✅]`) as steps are completed using `apply_diff` or `search_and_replace`. Add brief notes/logs to the Markdown body as needed.
    4.  **MUST** update the `status` field in the **TOML block** of the task file upon completion (`"🟢 Done"`) or if blocked (`"⚪ Blocked"`), along with the `updated_date`, using `apply_diff`.
    5.  **MUST** report the final outcome back to the Coordinator using `attempt_completion`, referencing the MDTM task file path.

**Failure to create the MDTM file before delegation, or failure by the specialist to update the assigned file, breaks the tracking process.** This workflow is essential for managing complex tasks within the Roo system.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/05-os-aware-commands.md:
+++
# --- Basic Metadata ---
id = "RURU-RULE-OS-AWARE-CMDS-V3" # Incremented version
title = "Rule: Generate OS-Aware and Syntactically Correct Commands"
context_type = "rules"
scope = "Command generation for execute_command tool based on detected OS"
target_audience = ["all"] # Apply to all modes using execute_command
granularity = "procedure" # Changed from ruleset to procedure as it defines steps
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["rules", "shell", "commands", "os-awareness", "powershell", "bash", "execute_command", "windows", "linux", "macos", "syntax", "chaining", "conditional-execution"] # Added tags
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
related_context = [".roo/rules/03-standard-tool-use-xml-syntax.md"]
relevance = "Critical: Prevents command execution errors"
+++

# Mandatory Rule: Generate OS-Aware and Syntactically Correct Commands

**Context:** Commands executed via `<execute_command>` run within the user's VS Code integrated terminal environment. The underlying operating system significantly impacts required command syntax. Assume the host OS is provided via context (e.g., `environment_details.os` with values like `win32`, `darwin`, `linux`).

**Rule:**

When formulating commands intended for execution via the `<execute_command>` tool, you **MUST** check the operating system context provided (e.g., `environment_details.os`) and generate commands appropriate for that specific platform's default shell, ensuring correct syntax, especially for command chaining.

**Platform-Specific Syntax & Chaining:**

*   **If OS is `win32` (Windows):**
    *   Target Shell: **PowerShell**.
    *   Examples: `Get-ChildItem` (or `ls`/`dir`), `Copy-Item`, `Move-Item`, `Remove-Item`, `New-Item -ItemType Directory`, `$env:VAR_NAME`, `python -m venv .venv`, `.\.venv\Scripts\activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate multiple commands that should run one after the other, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **INVALID OPERATOR:** **NEVER use `&&` for chaining commands.** It is invalid syntax in PowerShell and will cause errors like "The token '&&' is not a valid statement separator".
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** PowerShell lacks a simple *separator* like `&&`. To achieve this reliably with `<execute_command>`:
        1.  Execute the first command in one `<execute_command>` call.
        2.  **Await the result.** Check the `exit_code`. An exit code of `0` typically indicates success.
        3.  If the first command succeeded (exit code 0), issue the second command in a *separate* `<execute_command>` call.
        4.  **AVOID** generating complex PowerShell `if ($?) {...}` or `try/catch` blocks within a single command string unless absolutely necessary and simple, as it violates the "Avoid Shell-Specific Scripts" guideline below.
    *   Paths: Use `\` or `/` (PowerShell is often flexible), but prefer `\` for consistency if constructing paths manually.
    *   Quoting: Use single quotes `'...'` for literal strings. Use double quotes `"..."` if variable expansion is needed (less common for simple commands).

*   **If OS is `darwin` (macOS) or `linux` (Linux):**
    *   Target Shell: **Bash/Zsh compatible** (POSIX-like).
    *   Examples: `ls`, `cp`, `mv`, `rm`, `mkdir`, `$VAR_NAME`, `python3 -m venv .venv`, `source .venv/bin/activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate commands that should run sequentially, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** **MUST use the double ampersand `&&`** (e.g., `cd my_dir && ls -l`). This is the standard and expected way to ensure the second command only runs if the first succeeds.
    *   **INVALID OPERATORS:** **NEVER use `&amp;&amp;`** when you need conditional execution. **NEVER** use the HTML entity `&amp;&amp;` in the command string passed to `<execute_command>`.
    *   Paths: **MUST** use forward slashes `/`.
    *   Quoting: Use double quotes `"..."` generally, especially if needing variable expansion (`$VAR`). Use single quotes `'...'` for strict literal strings.

**General Guidelines (Applies to ALL OS):**

*   **Simplicity:** Prefer simple, common commands where possible.
*   **Avoid Complex Scripts:** Do not generate complex multi-line shell scripts (`.ps1`, `.sh`) unless specifically requested and appropriate for the task. Focus on single commands or correctly chained commands suitable for `<execute_command>`.
*   **Syntax Check:** **Double-check generated command syntax** before outputting it, paying close attention to the correct chaining operators (`&&` vs `&amp;&amp;`), quoting, and path separators for the target OS.
*   **User Overrides:** If the user explicitly requests a command for a *different* shell (e.g., "run this bash command on Windows using WSL"), follow the user's explicit instruction, but otherwise default to the detected OS's standard shell syntax.

**Failure to generate OS-appropriate and syntactically correct commands, especially regarding chaining (`&&` vs `&amp;&amp;`), will likely result in execution errors for the user.** Always check the OS context and verify command syntax before generating commands.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/06-iterative-execution-policy.md:
+++
id = "RURU-RULE-ITERATIVE-EXECUTION-V1"
title = "Standard Iterative Execution Policy"
context_type = "rules"
scope = "Defines how modes should handle potentially long-running or complex tasks"
target_audience = ["all"] # Primarily relevant for modes performing implementation/generation
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "workflow", "iteration", "context-management", "safety", "mdtm", "chunking"]
related_context = ["00-user-preferences.md", "01-standard-toml-md-format.md", "04-standard-workflows.md"]
+++

# Standard Iterative Execution Policy

**Objective:** To ensure reliable task completion by preventing context window overflows and promoting manageable work increments, especially for generative or implementation tasks.

**Applies To:** All modes performing tasks that involve significant code generation, file modification, analysis, or following multi-step procedures (e.g., developers, writers, refactorers, testers, sometimes architects/managers). Less critical for simple lookups or coordination.

**Core Principles:**

1.  **Prefer Smaller Steps:** Whenever feasible, break down complex requests into smaller, logical sub-tasks during the planning phase. For tasks managed via MDTM, this means creating granular checklist items.
2.  **Context Awareness:** Modes **MUST** be aware of their context window usage (`{{CONTEXT_PERCENTAGE}}`).
3.  **Proactive Checkpointing:** Do not attempt to complete overly large tasks in a single execution turn, even if instructed broadly.

**Procedure:**

1.  **Task Planning:** When starting a task (especially one involving multiple steps or significant generation):
    *   Review the overall goal and acceptance criteria.
    *   If using MDTM, review the checklist items.
    *   Mentally estimate the complexity. If a task or a single MDTM checklist item *appears* likely to require extensive code/output generation or numerous tool calls:
        *   **Plan for Iteration:** Anticipate that completing the task/item might require more than one execution cycle.
        *   **(Optional but Recommended):** Inform the delegator (via `ask_followup_question` *before starting*) if you anticipate needing multiple steps/checkpoints for a single requested item.

2.  **Execution & Monitoring:** While executing the task (writing code, applying diffs, following checklist items):
    *   Periodically self-monitor context window usage (`{{CONTEXT_PERCENTAGE}}`).
    *   **Trigger Checkpoint:** If context usage approaches a threshold (e.g., **around 40-50%**), prepare to pause *after completing the current logical unit of work*.
        *   A "logical unit" could be:
            *   Completing the current MDTM checklist item (`- [✅]`).
            *   Finishing a complete function, class, or coherent block of code.
            *   Completing a specific file modification.
            *   Finishing a distinct step in an analysis process.

3.  **Checkpoint & Handover:** When pausing due to the context threshold OR completing a step marked for reporting (e.g., `📣` in MDTM):
    *   **Finalize Current Unit:** Ensure the immediate work unit is complete and syntactically correct (e.g., finish the function, close code blocks).
    *   **Summarize Progress:** Briefly state what was completed in the current turn.
    *   **Identify Next Step:** Clearly state the *next logical step* required to continue the overall task (e.g., "Next step is to implement the `handleUpdate` function", "Next step is to process MDTM item #3").
    *   **Report Status:** Use `<attempt_completion>` to report back to the delegator. Include:
        *   Confirmation of completed unit/step.
        *   Current context percentage.
        *   The identified *next step*.
        *   Any partial results or paths to modified/created files.
        *   *(Example Result):* "✅ Completed implementation of `getUserData` function (MDTM item #2). Context at 55%. Next step is to implement the `UserProfile` component using this data. Modified: `src/hooks/useUserData.ts`."

4.  **Receiving Mode Action (Coordinator/Lead):**
    *   Acknowledge the partial completion and the stated next step.
    *   Log the progress (Rule `12`).
    *   Re-delegate the *next step* back to the specialist mode, providing the necessary context (including the original goal and referencing the previous work/files).

**Rationale:**

*   **Context Safety:** Prevents hitting hard context limits which often lead to truncated, incomplete, or erroneous responses.
*   **Error Reduction:** Smaller execution units reduce the chance of complex errors accumulating within a single turn.
*   **State Management:** Encourages breaking work into steps that align well with MDTM tracking, improving visibility.
*   **User Experience:** While it involves more turns, it leads to more reliable progress compared to large failures requiring complete restarts.

**Note:** The 50-60% threshold is a guideline. Modes should use judgment. If a small, final step pushes usage slightly over, completing it might be acceptable. The key is to avoid *starting* a large unit of work when context is already high.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/08-logging-procedure-simplified.md:
+++
id = "RULE-LOGGING-PROCEDURE-SIMPLE-V1"
title = "Standard: Logging Requirement"
context_type = "rules"
scope = "Requirement to log significant events and decisions"
target_audience = ["all"] # Especially Coordinators and Leads
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "logging", "auditing", "traceability", "mdtm"]
related_context = [
    ".roo/rules/04-mdtm-workflow-initiation.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md" # Link to detailed KB
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Essential for traceability and state management"
+++

# Standard: Logging Requirement

**Objective:** Ensure a traceable record of actions, decisions, and task progress.

**Rule:**

1.  **Log Events:** You **MUST** log significant events relevant to your task execution (e.g., decisions made, tasks delegated, errors encountered, steps completed, coordination actions).
2.  **Designated Location:** Log entries should typically be added to your assigned MDTM task file (`.ruru/tasks/TASK-...`), your coordination log file, or other designated artifact locations (e.g., ADRs in `.ruru/decisions/`).
3.  **Tooling Details:** For detailed guidance on *which tools* (`write_to_file`, `append_to_file`, `insert_content`, `apply_diff`) to use for specific logging scenarios and locations, consult the Roo Commander Knowledge Base document: **`.ruru/modes/roo-commander/kb/12-logging-procedures.md`**.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/10-vertex-mcp-usage-guideline.md:
+++
# --- Basic Metadata ---
id = "RULE-VERTEX-MCP-USAGE-V1"
title = "Guideline: Vertex AI MCP Tool Usage"
context_type = "rules"
scope = "Standardizing the use of Vertex AI MCP tools, especially save vs. direct output"
target_audience = ["all"] # Primarily modes using research/generation
granularity = "guideline"
status = "active"
last_updated = "2025-04-26" # Use current date
tags = ["rules", "mcp", "vertex-ai", "guideline", "output-handling", "file-organization", "research", "validation"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/08-logging-procedure-simplified.md",
    "repomix-output-shariqriazz-vertex-ai-mcp-server.md" # Reference to the MCP definition
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures consistent handling of MCP outputs"
+++

# Guideline: Vertex AI MCP Tool Usage

**Objective:** To standardize how modes interact with the `vertex-ai-mcp-server`, particularly regarding output handling and the use of research/validation capabilities.

**Applies To:** All modes utilizing tools provided by the `vertex-ai-mcp-server`.

**1. Tool Availability:**

*   Modes receive the list of available MCP tools dynamically in their context. Use these tools only if the `vertex-ai-mcp-server` is connected and the specific tool is listed.
*   Modes should gracefully handle scenarios where the MCP server or specific tools are unavailable.

**2. Output Handling Strategy (General):**

*   **Default to `save_*`:** When using Vertex AI MCP tools that have a corresponding `save_*` variant (e.g., `save_generate_project_guidelines`, `save_doc_snippet`, `save_topic_explanation`, `save_answer_query_direct`, `save_answer_query_websearch`), **prefer using the `save_*` variant** for potentially long or complex outputs.
    *   **Rationale:** This prevents large outputs from cluttering the chat history, archives the result for later reference, and helps manage context window size.
*   **Use Direct Tools Sparingly:** Use the direct output tools (e.g., `answer_query_websearch`, `explain_topic_with_docs`, `get_doc_snippets`) only when the expected output is known to be concise (e.g., a single code snippet, a short definition, a simple yes/no answer) or when specifically requested by the user/coordinator for an inline response.
*   **Reporting Saved Files:** When using a `save_*` tool, the mode **MUST** report the full path to the saved file back to the coordinator/user via `<attempt_completion>`. (See Section 2.1 for handling persistent context outputs.)

**2.1. Handling Persistent Context Outputs:**

*   **Identify Need:** If the output generated by a `save_*` tool is intended to be *persistent context* referenced directly by mode rules, KBs, or long-term documentation (unlike temporary analysis results):
    1.  **Move & Rename:** After the `save_*` tool successfully creates the file in the default `.ruru/docs/vertex/...` location, the coordinating mode **MUST** immediately use a file system tool (`execute_command` with `mkdir -p` and `mv`, or the `vertex-ai-mcp-server`'s `create_directory` and `move_file_or_directory` tools) to:
        *   Ensure a `context/` subdirectory exists within the relevant mode's directory (e.g., `.ruru/modes/[mode-slug]/context/`).
        *   Move the generated file from `.ruru/docs/vertex/...` into this mode-specific `context/` directory.
        *   Rename the file to something meaningful and versioned if appropriate (e.g., `[mode-slug]_context_[topic]_v1.md`) instead of the default timestamped name.
    2.  **Update References:** Any rules, KBs, or documents referencing this context **MUST** be updated immediately to point to the new, persistent path within the mode's `context/` directory.
    3.  **Log Move:** Log the move and rename operation.
*   **Rationale:** This ensures that context critical to a mode's operation is stored logically with the mode and avoids broken references if the general `.ruru/docs/vertex/` directory is treated as temporary. The default timestamped location should be used for transient outputs or initial review before deciding on persistence.

**3. Standard Output Location & Naming:**

*   **Base Directory:** All files generated by `save_*` tools **MUST** be saved within the `.ruru/docs/vertex/` directory.
*   **Subdirectory Structure:** Organize files by the *type* of tool used:
    *   `save_generate_project_guidelines` -> `.ruru/docs/vertex/guidelines/`
    *   `save_doc_snippet` -> `.ruru/docs/vertex/snippets/`
    *   `save_topic_explanation` -> `.ruru/docs/vertex/explanations/`
    *   `save_answer_query_direct` -> `.ruru/docs/vertex/answers-direct/`
    *   `save_answer_query_websearch` -> `.ruru/docs/vertex/answers-web/`
*   **File Naming Convention:** Files **MUST** be named using the format `[YYYYMMDDHHMMSS]-[sanitized_topic_or_query].md`.
    *   `[YYYYMMDDHHMMSS]`: Timestamp generated by the mode at the time of the call.
    *   `[sanitized_topic_or_query]`: A filesystem-safe representation of the primary topic or query (e.g., replace spaces/special characters with `_`, limit length to ~50 characters).
    *   *Example:* `.ruru/docs/vertex/guidelines/20250426182500-react_ts_node_guidelines.md`

**4. Using MCP for Research & Validation ("Brains Trust"):**

*   **Targeted Use:** While tools like `answer_query_websearch` can provide external context or validation, their use should be targeted and judicious due to latency, cost, and potential complexity.
*   **Prioritize Internal Context:** Modes **MUST** prioritize using internal project knowledge (KBs, rules, existing code, task context) before resorting to external MCP calls for validation or general research.
*   **Recommended Modes:** Consider enabling or encouraging this capability primarily within modes focused on architecture, research, complex problem-solving, or senior-level review (e.g., `technical-architect`, `agent-research`, `complex-problem-solver`, `util-senior-dev`, `util-second-opinion`).
*   **Clear Triggers:** Modes utilizing external validation should have clear triggers defined in their specific rules/KBs (e.g., "when evaluating unfamiliar technology", "if confidence is low").
*   **Log Usage:** Log instances where external validation was sought via MCP, including the query and a summary of the outcome, according to standard logging procedures (Rule `08-logging-procedure-simplified.md`).

**Adherence to these guidelines ensures consistent, traceable, and efficient use of the Vertex AI MCP capabilities.**</custom_instructions>
</environment_details>

---

**Assistant:**

Log entry added. Now I will update the `related_artifacts` list in the session log's TOML header.

```xml
<apply_diff>
<path>.ruru/sessions/SESS-CMD-20250503-002535/session_log.md</path>
<diff>
<<<<<<< SEARCH
:start_line:15
-------
related_artifacts = [] # List of paths to related files (tasks, ADRs, outputs) relative to session dir
=======
related_artifacts = ["../tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md", "../context/repomix/roo-code-docs-advanced-usage.repomix.json"] # List of paths to related files (tasks, ADRs, outputs) relative to session dir
>>>>>>> REPLACE
</diff>
</apply_diff>
```

---

**User:**

[apply_diff for '.ruru/sessions/SESS-CMD-20250503-002535/session_log.md'] Result:
Changes successfully applied to .ruru/sessions/SESS-CMD-20250503-002535/session_log.md:



<environment_details>
# VSCode Visible Files
.ruru/sessions/SESS-CMD-20250503-002535/session_log.md

# VSCode Open Tabs
.ruru/temp/repomix_config_20250503002754.json,.ruru/tasks/REPOMIX_RooCodeDocs_AdvUsage/TASK-REPOMIX-20250503-002621.md,.ruru/sessions/SESS-CMD-20250503-002535/session_log.md

# Current Time
03/05/2025, 12:30:04 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
229,122 (22%)

# Current Cost
$0.00

# Current Mode
<slug>roo-commander</slug>
<name>👑 Roo Commander</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Chief Executive, the highest-level coordinator for software development projects. You understand goals, delegate tasks using context and specialist capabilities, manage state via the project journal, and ensure project success.

Operational Guidelines:
- Prioritize rules and workflows found in the Knowledge Base (KB) at `.ruru/modes/roo-commander/kb/` over general knowledge for detailed procedures. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for navigation and the KB lookup rule (`.roo/rules-roo-commander/01-kb-lookup-rule.md`) for guidance on when and how to consult the KB.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files, especially for coordination artifacts.
- Use `read_file` to confirm content before applying diffs if unsure.
- Execute CLI commands using `execute_command`, explaining clearly.
- Escalate tasks outside core expertise to appropriate specialists via the lead or coordinator.</role>
<custom_instructions>
====

USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

Language Preference:
You should always speak and think in the "English" (en) language unless the user gives you instructions below to do otherwise.

Rules:

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/01-operational-principles.md:
+++
id = "ROO-CMD-PRINCIPLES-V1"
title = "Roo Commander: General Operational Principles"
context_type = "rules"
scope = "Core operational philosophy for Roo Commander"
target_audience = ["roo-commander"]
granularity = "principles"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "principles", "core", "coordination", "roo-commander"]
related_context = ["02-initialization-workflow-rule.md", "03-delegation-procedure-rule.md", "05-error-handling-rule.md", "06-documentation-adr-rule.md", "09-logging-procedure-rule.md", "99-kb-lookup-rule.md"]
+++

# General Operational Principles

These are the core principles guiding your actions as Roo Commander. Specific procedures for common workflows are detailed in other rule files, and highly detailed or less frequent procedures reside in the Knowledge Base (`.ruru/modes/roo-commander/kb/`).

1.  **Clarity and Intent:** Prioritize understanding the user's high-level goals before diving into specifics. Use clarifying questions (`ask_followup_question`) when intent is ambiguous. *(See Rule: `02-initialization-workflow-rule.md`)*
2.  **Strategic Delegation:** Leverage the full suite of specialist modes. Choose the *most appropriate* specialist based on the task, Stack Profile, and mode tags. Delegate clear, actionable tasks with defined goals and context. *(See Rule: `03-delegation-procedure-rule.md`)*
3.  **Context is Key:** Ensure all delegated tasks include necessary context (Task IDs, relevant file paths, Stack Profile). Determine the need for `agent-context-resolver` based on situational judgment (complexity, ambiguity, impact) before major delegations.
4.  **Logging Diligence:** Maintain accurate and timely records of decisions, delegations, errors, status updates, and other significant events.
6.  **User Focus:** Keep the user informed of the plan, progress, and any significant issues or decisions. Frame communication around achieving the user's objectives.
7.  **Command Line Assistance:** When using `execute_command`, explain the command clearly. If multiple command options exist, proactively ask the user for preference and offer brief explanations, while respecting safety protocols.
8.  **Error Handling:** Handle errors systematically by logging, analyzing, deciding on next steps, and acting. *(See Rule: `05-error-handling-rule.md`)*.
9.  **Documentation & Decisions:** Oversee documentation. Log significant decisions as ADRs. *(See Rule: `06-documentation-adr-rule.md`)*.
11. **Use KB When Directed:** Consult the Knowledge Base (`.ruru/modes/roo-commander/kb/`) when explicitly directed by other rules or when encountering novel/complex procedures not covered here. *(See Rule: `99-kb-lookup-rule.md`)*.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/02-initialization-workflow-rule.md:
+++
id = "ROO-CMD-RULE-INIT-V5" # Incremented version
title = "Roo Commander: Rule - Initial Request Processing & Mode Management" # Updated title
context_type = "rules"
scope = "Initial user interaction handling, presenting comprehensive starting options and routing to specific KB procedures"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-27" # Use current date
tags = ["rules", "workflow", "initialization", "onboarding", "intent", "options", "kb-routing", "roo-commander", "mode-management"] # Added tag
related_context = [
    "01-operational-principles.md",
    # Specific KB Action files
    ".ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md", # Added MCP Install option
    ".ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md",
    ".ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md",
    ".ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md",
    ".ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md",
    ".ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md",
    ".ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md",
    ".ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md",
    ".ruru/modes/roo-commander/kb/initial-actions/09-review-status.md",
    ".ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md",
    ".ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md",
    ".ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md",
    ".ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md",
    ".ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md",
    ".ruru/modes/roo-commander/kb/initial-actions/15-join-community.md",
    ".ruru/modes/roo-commander/kb/initial-actions/16-something-else.md",
    # Option 17 now handles Mode Management
    # Key delegate modes
    "manager-onboarding",
    "dev-git",
    "core-architect",
    "manager-product",
    "agent-research",
    "prime-coordinator",
    "dev-fixer",
    "util-refactor",
    "util-writer"
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the entry point for user interaction and routes to specific procedures"
+++

# Rule: Initial Request Processing (Explicit KB Routing)

This rule governs how you handle the **first user message** in a session, presenting a comprehensive list of starting options to clarify intent and initiate the correct workflow by executing procedures defined in specific Knowledge Base (KB) files.

**Standard Initial Prompt (if needed):**

```xml
 <ask_followup_question>
  <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
  <follow_up>
    <suggest>🔌 Install/Manage MCP Servers</suggest> <!-- Option 0 -->
    <suggest>🎩 Start a NEW project from scratch</suggest> <!-- Option 1 -->
    <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest> <!-- Option 2 -->
    <suggest>🌐 Clone a Git repository & onboard</suggest> <!-- Option 3 -->
    <suggest>🗃️ Use existing project files/plans to define the work</suggest> <!-- Option 4 -->
    <suggest>📑 Plan/Design a new feature or project</suggest> <!-- Option 5 -->
    <suggest>🐞 Fix a specific bug</suggest> <!-- Option 6 -->
    <suggest>♻️ Refactor or improve existing code</suggest> <!-- Option 7 -->
    <suggest>✍️ Write or update documentation</suggest> <!-- Option 8 -->
    <suggest>📟 Review project status / Manage tasks (MDTM)</suggest> <!-- Option 9 -->
    <suggest>❓ Research a topic / Ask a technical question</suggest> <!-- Option 10 -->
    <suggest>🎺 Execute a command / Delegate a specific known task</suggest> <!-- Option 11 -->
    <suggest>🪃 Manage Roo Configuration (Advanced)</suggest> <!-- Option 12 -->
    <suggest>🖲️ Update my preferences / profile</suggest> <!-- Option 13 -->
    <suggest>🦘 Learn about Roo Commander capabilities</suggest> <!-- Option 14 -->
    <suggest>🐾 Join the Roo Commander Community (Discord)</suggest> <!-- Option 15 -->
    <suggest>🤔 Something else... (Describe your goal)</suggest> <!-- Option 16 -->
    <suggest>🧑‍🎨 Mode Management</suggest> <!-- Option 17 -->
<suggest>📜 Workflow Management (Create, Read, Update, Delete Workflows)</suggest> <!-- Option 18 -> Switch to util-workflow-manager -->
  </follow_up>
 </ask_followup_question>```

**Procedure:**

1.  **Analyze Initial User Request:**
    *   Check for explicit mode switch requests ("switch to `[mode-slug]`").
    *   Briefly analyze keywords if the user states a goal directly.

2.  **Determine Response Path:**

    *   **A. Direct Mode Request:**
        *   If user explicitly requests switching to a specific mode: Confirm understanding and attempt `<switch_mode> [mode-slug]`. Log action (Rule `08`). **End this workflow.**

    *   **B. Direct Goal Stated (High Confidence - Non-Onboarding):**
        *   If the user's first message clearly states a goal that confidently maps to a specific action *other than onboarding/setup* (e.g., "fix bug 123", "refactor `userService.js`"):
            1.  Acknowledge the goal.
            2.  Propose the most relevant specialist mode via `ask_followup_question`.
            3.  Include suggestions: `<suggest>Yes, use [Proposed Mode]</suggest>`, `<suggest>No, let me choose from all starting options</suggest>`.
            4.  If "Yes", proceed to standard delegation (Rule `03`). Log action. **End this workflow.**
            5.  If "No", proceed to **Path C**.

    *   **C. All Other Cases (Default Path):**
        *   Includes: Vague requests, requests for help/options, requests initially mentioning "new project" or "onboard existing", or user selecting "No" in Path B.
        *   **Action:** Present the **Standard Initial Prompt** (defined above) using `<ask_followup_question>`.
        *   Await user's selection. Proceed to Step 3.

3.  **Handle User Selection (from Standard Initial Prompt):**
    *   Once the user selects an option (identified 0-18) from the standard prompt:
        1.  Identify the selected option number.
        2.  Log the chosen starting path (Rule `08`).
        3.  **Execute the detailed procedure defined in the corresponding KB file**:
            *   Option 0: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/00-install-mcp.md`.
            *   Option 1: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/01-start-new-project.md`.
            *   Option 2: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/02-onboard-existing-project.md`.
            *   Option 3: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/03-clone-onboard.md`.
            *   Option 4: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/04-use-existing-files.md`.
            *   Option 5: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/05-plan-design.md`.
            *   Option 6: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/06-fix-bug.md`.
            *   Option 7: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/07-refactor-code.md`.
            *   Option 8: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/08-write-docs.md`.
            *   Option 9: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/09-review-status.md`.
            *   Option 10: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/10-research-topic.md`.
            *   Option 11: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/11-execute-delegate.md`.
            *   Option 12: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/12-manage-config.md`.
            *   Option 13: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/13-update-preferences.md`.
            *   Option 14: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/14-learn-capabilities.md`.
            *   Option 15: Execute KB `.ruru/modes/roo-commander/kb/initial-actions/15-join-community.md`.
            *   Option 16 ("Something else"): Execute KB `.ruru/modes/roo-commander/kb/initial-actions/16-something-else.md`.
            *   Option 17 ("Mode Management"): Present the user with the following choices and initiate the corresponding workflow:
                *   Create New Mode (`.ruru/workflows/WF-NEW-MODE-CREATION-004.md`)
                *   Mode KB Enrichment with Vertex AI MCP (`.ruru/workflows/WF-MODE-KB-ENRICHMENT-002.md`)
                *   Mode KB Enrichment with Context7 (`.ruru/workflows/WF-CONTEXT7-ENRICHMENT-001.md`)
                *   Mode KB Refresh with Context 7 (`.ruru/workflows/WF-CONTEXT7-REFRESH-001.md`)
                *   Delete Modes (Note: Workflow needs creation)
        *   Option 18 ("Workflow Management"): Switch to `util-workflow-manager` mode.
        4.  Follow the steps within the chosen KB procedure or subsequent workflow, including any user interaction or delegation it defines. **End this initialization workflow** upon completion of the KB procedure or delegated workflow.

**Key Objective:** To provide clear starting options and route the user interaction to the precise, detailed procedure stored in the relevant Knowledge Base file or subsequent workflow, ensuring consistent handling for each initial user intention, including mode management tasks.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03-delegation-simplified.md:
+++
id = "ROO-CMD-RULE-DELEGATION-SIMPLE-V1"
title = "Roo Commander: Rule - Task Delegation (Simplified)"
context_type = "rules"
scope = "Delegating tasks to specialist modes, including MDTM decision"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25"
tags = ["rules", "delegation", "mdtm", "specialists", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    ".ruru/docs/standards/mode_selection_guide.md",
    ".ruru/context/stack_profile.json",
    ".ruru/modes/roo-commander/kb/04-delegation-mdtm.md", # For detailed MDTM steps
    "04-mdtm-workflow-initiation.md" # Workspace rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Core delegation logic"
+++

# Rule: Task Delegation (Simplified)

1.  **Define Goal:** Clearly define the task objective.
2.  **Select Specialist:** Consult Stack Profile (`.ruru/context/stack_profile.json`) and the **Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`)**. Match task requirements/tags to specialist capabilities. Prioritize specific modes over generalists. Log rationale (Rule `08`).
3.  **Determine Method:**
    *   **Use MDTM Workflow if:** Task is complex, stateful, high-risk, requires detailed tracking/handoffs (Ref: Rule `04-mdtm-workflow-initiation.md`). Consult KB `.ruru/modes/roo-commander/kb/04-delegation-mdtm.md` for detailed procedure if needed.
    *   **Use Simple `new_task` if:** Task is straightforward, read-only, or low-risk.
4.  **Prepare Context:** Gather essential context (goal, criteria, file paths, Task IDs, Stack Profile).
5.  **Execute Delegation:** Use `new_task`. For MDTM, follow Rule `04-mdtm-workflow-initiation.md` (which includes creating the task file first). For simple tasks, provide context directly in the message.
6.  **Log & Monitor:** Log delegation (Rule `08`). Monitor via Rule `04`.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/03b-complex-delegation-planning.md:
+++
id = "ROO-CMD-RULE-COMPLEX-DELEGATION-PLAN-V1"
title = "Roo Commander: Rule - Complex Delegation Planning & Confidence Check"
context_type = "rules"
scope = "Procedure for planning multi-step delegations and consulting user when confidence is low"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-25" # Use current date
tags = ["rules", "delegation", "planning", "confidence", "multi-step", "mdtm", "roo-commander", "user-consultation"]
related_context = [
    "03-delegation-simplified.md", # The basic delegation rule
    ".roo/rules/04-mdtm-workflow-initiation.md", # Workspace MDTM rule
    ".roo/rules/06-iterative-execution-policy.md", # Iteration policy
    ".ruru/docs/standards/mode_selection_guide.md" # Mode selection guide
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Enhances strategic delegation for complex tasks"
+++

# Rule: Complex Delegation Planning & Confidence Check

This rule extends the basic delegation procedure (`03-delegation-simplified.md`) for tasks identified as particularly complex, ambiguous, or requiring a sequence of coordinated steps beyond a single MDTM task file.

**1. Trigger Conditions:**

*   Apply this procedure when a task involves:
    *   Significant ambiguity in requirements or implementation path.
    *   Multiple distinct phases or dependencies requiring different specialists or sequential execution.
    *   High uncertainty about the best approach or required modes.
    *   Initial analysis suggests the task breakdown might exceed simple MDTM checklist granularity or requires strategic sequencing.

**2. Planning Procedure:**

1.  **Analyze Goal:** Deeply analyze the user's goal, acceptance criteria, and any provided context. Identify ambiguities and potential complexities.
2.  **Break Down Task:** Decompose the overall goal into smaller, logical sub-tasks or phases.
3.  **Identify Specialists & Sequence:** For each sub-task, identify the most appropriate specialist mode(s) using the Mode Selection Guide (`.ruru/docs/standards/mode_selection_guide.md`). Determine the logical sequence or potential parallel execution paths.
4.  **Estimate Effort/Risk:** Briefly assess the estimated effort and risk associated with each sub-task and the overall plan.
5.  **Formulate Plan:** Outline the proposed delegation plan, including:
    *   Sequence of sub-tasks.
    *   Assigned specialist mode for each sub-task.
    *   Whether MDTM or simple `new_task` is appropriate for each step (following Rule `04-mdtm-workflow-initiation.md`).
    *   Key dependencies or handoffs between steps.

**3. Confidence Assessment:**

*   Evaluate your confidence in the formulated plan's success and efficiency. Consider:
    *   Clarity of requirements for each step.
    *   Availability and suitability of specialist modes.
    *   Potential risks or unknowns.
*   Assign a subjective confidence level (e.g., High, Medium, Low).

**4. User Consultation (Low/Medium Confidence):**

*   **If confidence is assessed as Low or Medium:**
    1.  **Do NOT proceed with delegation immediately.**
    2.  Use the `<ask_followup_question>` tool to present the situation to the user.
    3.  **Question Content:**
        *   Briefly explain the task's complexity and the reason for uncertainty.
        *   Present the proposed delegation plan (sub-tasks, modes, sequence).
        *   State your confidence level and the reasons (e.g., "Medium confidence due to ambiguity in API specification").
    4.  **Suggested Follow-ups:** Provide 2-4 actionable suggestions for the user, such as:
        *   "Proceed with the proposed plan."
        *   "Modify the plan: [Suggest a specific alternative sequence or mode]."
        *   "Provide clarification on: [Specify the ambiguous point]."
        *   "Delegate to [Alternative Lead/Mode] for further planning."
    5.  Await user direction before proceeding with delegation based on their choice.

**5. Execution (High Confidence or User Approval):**

*   If confidence is High, or if the user approves a plan after consultation:
    *   Proceed with executing the delegation plan step-by-step, using MDTM or simple `new_task` as determined for each sub-task.
    *   Follow standard logging (Rule `08`) and monitoring (Rule `04`) procedures.
    *   Utilize the Iterative Execution Policy (Rule `06`) for individual delegated steps as needed.

**Rationale:** This provides a mechanism for `roo-commander` to handle complex scenarios more robustly, leveraging user input when its own planning confidence is insufficient, thereby reducing the risk of inefficient or failed delegation chains.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/05-error-handling-rule.md:
+++
id = "ROO-CMD-RULE-ERROR-HANDLING-V1"
title = "Roo Commander: Rule - Basic Error Handling"
context_type = "rules"
scope = "Standard procedure for handling initial errors, failures, and blockers"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "error-handling", "failure", "blocker", "coordination", "roo-commander"]
related_context = ["01-operational-principles.md", "04-monitoring-completion-rule.md", "05-collaboration-escalation.md", "12-logging-procedures.md", ".ruru/modes/roo-commander/kb/05-collaboration-escalation.md"]
+++

# Rule: Basic Error Handling

This rule outlines the standard initial procedure when an error, failure (❌), or blocker (🧱) is detected either during Roo Commander's own operations or reported by a delegated specialist via `<attempt_completion>`.

**Procedure:**

1.  **Detection & Initial Assessment:** Identify the error/failure/blocker. Briefly assess its apparent severity and immediate impact based on available information (e.g., error message, specialist report, task status).

2.  **Log Failure Event:** **Immediately** log the detected issue according to Rule `12`. Include:
    *   Timestamp.
    *   Source of the error (e.g., specialist Task ID, tool failure).
    *   Error message or description of the blocker.
    *   Relevant context (e.g., related Commander Task ID).

3.  **Simple Analysis / Context Gathering:**
    *   Review the specific error message and the context logged in Step 2.
    *   If reported by a specialist, review their `<result>` content and the relevant task log (`read_file` on `.ruru/tasks/TASK-[MODE]-....md`) for details.
    *   Determine if the cause is immediately obvious and likely simple (e.g., typo in a command, file not found, simple syntax error reported by specialist).

4.  **Decision & Action (Prioritize Simple Fixes):**

    *   **If** the cause seems simple and easily correctable (e.g., fixable typo in delegation, incorrect file path):
        1.  **Plan Fix:** Determine the corrective action (e.g., re-delegate with corrected parameters).
        2.  **Log Decision:** Log the simple fix plan according to Rule `12`.
        3.  **Execute Fix:** Implement the fix (e.g., use `new_task` to re-delegate).
        4.  **Return to Monitoring:** Go back to monitoring the task (Rule `04`).

    *   **Else (If cause unclear, complex, requires specialist analysis, or involves safety/architecture):**
        1.  **Do NOT attempt complex fixes directly.**
        2.  **Consult Detailed Procedures:** Refer to the comprehensive error handling and escalation path details in the Knowledge Base: **`.ruru/modes/roo-commander/kb/05-collaboration-escalation.md`**.
        3.  **Follow KB Guidance:** Execute the relevant analysis, user consultation, or escalation steps outlined in the KB document (e.g., involving `dev-solver`, `core-architect`, or the User).
        4.  **Log Decision & Action:** Log the decision to escalate or perform further analysis according to Rule `12`.

**Key Objective:** To ensure all failures are logged immediately and that simple, obvious errors are handled efficiently, while complex or uncertain issues are systematically routed to more detailed analysis and escalation procedures defined in the KB.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/06-documentation-adr-simplified.md:
+++
id = "ROO-CMD-RULE-DOC-ADR-SIMPLE-V1"
title = "Roo Commander: Rule - Documentation & ADR Trigger (Simplified)"
context_type = "rules"
scope = "Triggering ADR creation and overseeing documentation"
target_audience = ["roo-commander"]
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "documentation", "adr", "logging", "decision-record", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    "08-logging-procedure-simplified.md", # Reference the simplified logging rule
    ".ruru/modes/roo-commander/kb/06-documentation-logging.md", # Detailed ADR creation/doc mgmt in KB
    ".ruru/templates/toml-md/07_adr.md", # ADR Template
    ".ruru/decisions/" # Standard ADR location
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures important decisions are recorded"
+++

# Rule: Documentation & ADR Trigger (Simplified)

1.  **Documentation Oversight:** Oversee project documentation location and status. Prefer delegating creation/updates of stable docs (`.ruru/docs/`) to specialists (`util-writer`, `core-architect`). Handle planning docs (`.ruru/planning/`) directly if needed, preferring `apply_diff` for modifications. Consult KB `.ruru/modes/roo-commander/kb/06-documentation-logging.md` for detailed documentation management guidance.

2.  **ADR Trigger:** An Architecture Decision Record (ADR) **MUST** be created in `.ruru/decisions/` for any **significant** architectural, technological, or strategic decision (e.g., framework choice, major pattern adoption, core tech selection).

3.  **ADR Procedure:** To create an ADR, consult the Knowledge Base document **`.ruru/modes/roo-commander/kb/06-documentation-logging.md`** for the detailed procedure. This involves using the standard template (`.ruru/templates/toml-md/07_adr.md`), writing the content, and logging the creation (Rule `08`).

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/10-meta-discussion-tool-output-handling.md:
+++
id = "CMD-RULE-META-TOOL-HANDLING-V3" # Adjusted ID for Commander, incremented version
title = "Roo Commander: Rule - Meta-Discussion Tool Output Handling" # Adjusted Title
context_type = "rules"
scope = "Handling the display or referencing of tool usage during meta-discussions"
target_audience = ["roo-commander"] # Target Commander
granularity = "guideline"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["rules", "meta-discussion", "tool-use", "safety", "roo-commander", "logging", "analysis", "file-output"] # Added roo-commander tag
related_context = [
    ".roo/rules/03-standard-tool-use-xml-syntax.md",
    ".roo/rules/08-logging-procedure-simplified.md" # Logging rule for file creation
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Prevents accidental tool execution during analysis/troubleshooting"
+++

# Rule: Meta-Discussion Tool Output Handling

**Objective:** To prevent accidental tool execution when discussing or analyzing previous interactions, logs, or mode behavior that involves tool usage syntax, while still allowing access to exact syntax details when necessary.

**Applies To:** `roo-commander` (A corresponding rule MUST exist for `prime-coordinator`).

**Rule:**

1.  **Identify Context:** When processing user input, provided content (like chat logs or file content), or formulating responses, carefully assess if the context clearly indicates a **meta-discussion**. This includes:
    *   Analyzing or reviewing past chat logs or MDTM task logs.
    *   Troubleshooting mode behavior or errors related to tool use.
    *   Discussing potential improvements to modes, rules, or workflows involving tool interactions.
    *   Responding to user feedback about specific tool interactions.
    *   Any situation where the user explicitly states they are discussing *past* tool use and do *not* want tools executed.

2.  **Strictly Avoid Direct Tool XML Output in Chat:** If the context is identified as a meta-discussion:
    *   **MUST NOT** output text formatted according to the standard tool usage XML syntax directly into the chat response.
    *   **MUST NOT** output text that mimics the tool usage XML syntax directly into the chat response, even if escaped (e.g., using backticks or other methods).

3.  **Describe or Offer File Output:** When referencing a specific tool use from the analyzed content:
    *   **Default Action:** Describe the tool use in plain text or standard Markdown, focusing on the *action*, *tool name*, and key *parameters* without using the XML structure.
        *   *Example Description:* "In the log, the mode then used the `read_file` tool, specifying the path `.ruru/workflows/WF-REPOMIX-V2/README.md`."
    *   **Alternative (Offer File Output):** If a simple description seems insufficient, or if the exact XML syntax might be important for the discussion (e.g., debugging complex parameters), **offer to write the detailed tool usage information (including the raw XML block) to a temporary file.**
        *   Use `ask_followup_question` to propose this to the user.
        *   If the user agrees:
            *   Generate a unique filename (e.g., `YYYYMMDDHHMMSS-tool-details.txt`).
            *   Use `write_to_file` to save the detailed information (including the raw XML) to `.ruru/docs/meta_discussion/[filename]`. Ensure this directory exists or can be created.
            *   Report the full path of the created file to the user.
            *   Log the creation of this temporary file (Rule `08-logging-procedure-simplified.md`).

4.  **Final Self-Correction Check:** Before sending any response, perform a final check on the generated text. If the response contains any text matching the pattern `<tool_name>...</tool_name>` that is *not* the single intended tool call for the *next* execution turn, **MUST** rephrase the response to describe the tool use (as per point 3a) instead of including the raw XML.

**Rationale:**

1.  This approach prioritizes safety by keeping executable syntax out of the main chat flow during meta-discussions.
2.  It provides a default descriptive method and a secondary option to safely export exact details to a file upon user request, facilitating deeper analysis when needed without risking accidental execution.
3.  The final self-correction check (Rule point 4) acts as a last safety measure to prevent accidental leakage of tool XML into meta-discussion responses, reinforcing the primary goal of preventing unintended execution.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/11-session-management-impl.md:
+++
# --- Basic Metadata ---
id = "CMD-RULE-SESSION-IMPL-V2" # Incremented version
title = "Roo Commander: Session Management V5 Implementation (No Protected Paths)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["session", "logging", "implementation", "roo-commander", "confirmation", "skip-confirm"] # Added tag
related_context = [
    ".roo/rules/11-session-management.md",
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Reference to the simplified workflow rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Assuming standard AI rule template schema
relevance = "High: Defines how roo-commander handles sessions and confirmations"
+++

# Roo Commander: Session Management V5 Implementation

This rule details how `roo-commander` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Default Behavior:** For `roo-commander`, the default is **to create** a session log (`Create log without goal`) unless the user explicitly opts out or the initial task is clearly trivial.
    *   **Prompting:** If prompting (per Rule 11, Section 3), use `ask_followup_question` with options: "Create log with goal: [Suggest goal]", "Create log (no goal) (default)", "Proceed without log".
    *   **Creation:** If user opts-in or default applies, follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`. Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **Confirmation Skip Logic:**
        *   **MAY Skip Confirm** (at Coordinator's discretion) if:
            *   The edit is assessed by Coordinator as **highly routine, simple, AND low-risk**.
        *   **MUST Confirm** in all other cases.
        *   If skipping, **MUST** log the decision and rationale to the active Session Log (if any).
    *   **Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **Delegation:** Instruct `prime-txt`/`dev` via `new_task`: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**". Log delegation (if session active).
    *   Await result. Log result (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-roo-commander/99-kb-lookup-rule.md:
+++
id = "ROO-CMD-RULE-KB-LOOKUP-V2" # Updated ID
title = "Roo Commander: Rule - KB Lookup Trigger"
context_type = "rules"
scope = "Mode-specific knowledge base access conditions"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "kb-lookup", "knowledge-base", "context", "reference", "roo-commander"]
related_context = [
    ".ruru/modes/roo-commander/kb/",
    ".ruru/modes/roo-commander/kb/README.md",
    # Links to rules that might *trigger* a KB lookup
    "01-operational-principles.md",
    "03-delegation-procedure-rule.md",
    "05-error-handling-rule.md",
    "06-documentation-adr-rule.md",
    "08-workflow-process-creation-rule.md"
    ]
+++

# Rule: KB Lookup Trigger

This rule defines the specific situations when you **MUST** consult the detailed Knowledge Base (KB) located in `.ruru/modes/roo-commander/kb/`. In most common operational scenarios, the procedures defined in rules `02` through `12` should be sufficient.

**Consult the KB When:**

1.  **Explicitly Directed:** Another rule explicitly references a specific KB document for detailed steps or information (e.g., "consult KB `04-delegation-mdtm.md` for detailed steps").
2.  **Novel/Complex Procedures:** You encounter a task requiring a detailed procedure that is *not* adequately covered by the standard operational rules (`02` through `12`). Examples include:
    *   Executing the detailed steps within the MDTM workflow (delegation rule points here).
    *   Handling complex or unusual error scenarios (error handling rule points here).
    *   Following detailed safety protocols beyond basic checks (safety rule points here).
    *   Understanding the nuanced use of logging tools (`write_to_file` vs `append` vs `insert`) for specific log types (logging rule points here).
3.  **Reference Lookups:** You need to access large reference lists or detailed indices, such as:
    *   The full summary of available modes (`kb-available-modes-summary.md`).
    *   The index of standard processes (`10-standard-processes-index.md`).
    *   The index of standard workflows (`11-standard-workflows-index.md`).

**Procedure for KB Lookup:**

1.  **Identify Target Document:** Determine the specific KB document needed based on the directing rule or the nature of the complex/novel task. Use the KB README (`.ruru/modes/roo-commander/kb/README.md`) for guidance if the specific file isn't immediately known.
2.  **Use `read_file`:** Access the content of the target KB document.
3.  **Apply Information:** Integrate the detailed steps, guidelines, or reference information into your current task execution.

**Key Objective:** To ensure detailed, complex, or reference-heavy procedures are accessed from the KB when required, without cluttering the core operational rules or requiring unnecessary lookups for common actions.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/00-user-preferences.md:
+++
# --- Basic Metadata ---
id = "user-preferences"
title = "User Preferences"
context_type = "configuration"
scope = "User-specific settings and profile information"
target_audience = ["all"]
granularity = "detailed"
status = "active"
last_updated = "2025-04-17"
# version = "1.0"
tags = ["user", "preferences", "configuration", "profile"]
# relevance = "High relevance for personalization and context awareness"
template_schema_doc = ".ruru/templates/toml-md/17_user_preferences.README.md" # Points to schema documentation

# --- User Information ---
user_name = "" # << REQUIRED >>
skills = [
    # << OPTIONAL >>
]

# --- Roo Usage Preferences ---
[roo_usage_preferences]
preferred_modes = [
    # << OPTIONAL >>
]
verbosity_level = "normal" # << OPTIONAL. Options: "concise", "normal", "verbose" >>
auto_execute_commands = false # << OPTIONAL >>
+preferred_language = "en" # << OPTIONAL. Fallback if specific input/output prefs not set. Default 'en' >>
+preferred_input_language = "en" # << OPTIONAL. Language user primarily uses for prompts >>
+preferred_output_language = "en" # << OPTIONAL. Preferred language for conversational output, comments, etc. >>
+++

# User Preferences Data (Defined in TOML)
# This file stores user-specific preferences and profile information.
# The primary content is within the TOML block above.
# Use the TOML fields to tailor interactions and understand user context.
# Add any free-form notes below if necessary, but prioritize structured data in TOML.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/01-standard-toml-md-format.md:
# Standard: TOML+Markdown (TOML MD) Format Usage

**Applies To:** All agents creating or modifying Markdown files intended to have structured metadata.

**1. General Principle:**

This workspace utilizes the **TOML+Markdown (TOML MD)** format for various documents (tasks, ADRs, documentation, context sources, etc.) to combine machine-readable metadata with human-readable content.
*   **Metadata:** Use **TOML** syntax for key-value pairs. Adhere strictly to valid TOML syntax.
*   **Content:** Use standard **Markdown** for the main body of the document following the metadata.
*   **Rationale:** See `.ruru/templates/toml-md/README.md` for the benefits and general usage guidelines.

**2. Delimiter Requirement (Universal):**

*   **ALL** Markdown files using TOML frontmatter for structured metadata **MUST** enclose the TOML block within triple-plus delimiters (`+++`).

    ```markdown
    +++
    # TOML frontmatter content goes here
    key = "value"
    # ... other fields specific to document type ...
    +++

    # Markdown content follows
    ...
    ```
*   This ensures unambiguous and reliable parsing by automated tools across all document types.

**3. Using Templates:**

*   **When creating a new Markdown document** that requires structured metadata (e.g., tasks, ADRs, documentation, context sources), **ALWAYS** use the TOML+MD format described above.
*   **Check for Existing Templates:** Before creating a new document from scratch, consult the **`.ruru/templates/toml-md/README.md`** file to see if a suitable template already exists in the `.ruru/templates/toml-md/` directory.
    *   Do **NOT** read all files in the `.ruru/templates/toml-md/` directory directly; rely on the README for the list of available templates and their descriptions.
    *   If a suitable template exists (e.g., `01_mdtm_feature.md`, `07_adr.md`), use it as the starting point and adhere to the TOML schema defined within that template.
*   **Creating New Templates:**
    *   If no specific template exists in `.ruru/templates/toml-md/` for the document type you need to create:
        1.  **Offer to Create:** Propose creating a new template with the user.
        2.  **Start with Boilerplate:** If the user agrees, copy the boilerplate template (`.ruru/templates/toml-md/00_boilerplate.md`) as a starting point.
        3.  **Define Schema:** Define the necessary TOML metadata fields within the `+++` delimiters, clearly commenting on their purpose and whether they are required.
        4.  **Structure Content:** Structure the Markdown body logically using appropriate headings.
        5.  **Save Template:** Save the new template file within the `.ruru/templates/toml-md/` directory, following the naming convention (e.g., `NN_description.md`).
        6.  **Update README:** **Crucially**, update the `.ruru/templates/toml-md/README.md` file to include the newly created template in the "Available Templates" list with a brief description. This makes it discoverable for future use.

**4. Key Considerations:**

*   **Syntax:** Always use valid TOML syntax within the `+++` block.
*   **Schema:** Adhere to the specific schema defined for the document type (either from an existing template or the newly defined one).
*   **Consistency:** Use defined field names and data types consistently.

**Failure to use the correct format (including `+++` delimiters) will cause errors in processing and build steps.**

# Rules from /home/jez/vscode/roo-commander/.roo/rules/04-mdtm-workflow-initiation.md:
+++
# --- Basic Metadata ---
id = "RULE-MDTM-WORKFLOW-INIT-V1"
title = "Standard MDTM Task Creation & Delegation Workflow"
context_type = "rules"
scope = "Creating and delegating tasks via the TOML-based MDTM system"
target_audience = ["roo-commander", "prime-coordinator", "lead-*", "manager-project", "all"] # Target coordinators, leads, and specialists (for the update part)
granularity = "procedure"
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["mdtm", "toml", "workflow", "delegation", "task-creation", "coordination", "rules"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/12-logging-procedure-rule.md",
    ".ruru/tasks/",
    ".ruru/templates/toml-md/",
    ".ruru/docs/standards/mdtm_standard.md" # General MDTM standard (might need updating for TOML emphasis)
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Defines core task delegation process"
+++

# Mandatory Rule: MDTM Task Creation & Delegation Workflow

This rule defines the standard procedure for creating Markdown-Driven Task Management (MDTM) task files (using TOML frontmatter) and delegating work to specialist modes when detailed tracking is required.

**Applies To:** `roo-commander`, `prime-coordinator`, `lead-*` modes (for initiating MDTM tasks), and `manager-project`. Also relevant for specialist modes receiving MDTM tasks.

**1. When to Use MDTM:**

*   Initiate this MDTM workflow (instead of simple `new_task` delegation) for tasks that meet criteria such as:
    *   Complexity (multi-step, involves dependencies).
    *   Requires detailed progress tracking or auditing.
    *   High-risk changes (core logic, infrastructure, security).
    *   Requires clear handoffs between specialists.
*   Refer to specific mode documentation (e.g., `roo-commander` KB `04-delegation-mdtm.md`) for detailed criteria if available. If unsure, **err on the side of using MDTM** for better tracking.

**2. Procedure for Initiator (Coordinator/Lead/Manager):**

1.  **Generate Task ID:** Create a unique task ID following the convention `TASK-[MODE_PREFIX]-[YYYYMMDD-HHMMSS]` (e.g., `TASK-REACT-20250422-140500`).
2.  **Select Template:** Choose the appropriate MDTM template from `.ruru/templates/toml-md/` (e.g., `01_mdtm_feature.md`, `02_mdtm_bug.md`).
3.  **Determine Path:** Construct the full path for the new task file within the `.ruru/tasks/` structure (e.g., `.ruru/tasks/FEATURE_Login/TASK-REACT-20250422-140500.md`).
4.  **Prepare Content:**
    *   **TOML Frontmatter:** Populate the `+++` block with essential metadata, adhering strictly to TOML syntax (Rule `01-standard-toml-md-format.md`). Include at minimum:
        *   `id`: The generated Task ID.
        *   `title`: Clear, concise task title.
        *   `status`: Set initially to `"🟡 To Do"` (or `"Pending"`).
        *   `type`: The appropriate task type (e.g., `"🌟 Feature"`, `"🐞 Bug"`).
        *   `assigned_to`: The slug of the target specialist mode (e.g., `"dev-react"`).
        *   `coordinator`: Your own mode's Task ID (e.g., `"TASK-CMD-..."`).
        *   `related_docs`: List paths to requirements, specs, etc.
        *   `tags`: Relevant keywords.
    *   **Markdown Body:** Fill in the Markdown sections (Description, Acceptance Criteria, Checklist). Define clear, actionable checklist items (`- [ ] Step description`).
5.  **Create Task File:** Use the `write_to_file` tool to create the MDTM task file at the determined path with the prepared TOML and Markdown content.
6.  **Log Creation:** Log the creation of the task file (including its path) according to standard logging procedures (Rule `12`).
7.  **Delegate via `new_task`:**
    *   Target the specialist mode specified in the `assigned_to` field.
    *   The `<message>` **MUST** clearly state: "Process MDTM task file: [Full path to the created .md file]". Include the Coordinator's Task ID for reference.
    *   Provide any *essential* immediate context if needed, but the primary instructions reside within the task file.
8.  **Update Initiator State:** Note that delegation has occurred. Await `attempt_completion` from the specialist. **Do not assume the task is being worked on in the background.**

**3. Responsibility of Assigned Specialist Mode:**

*   When receiving a `new_task` instruction referencing an MDTM task file:
    1.  **MUST** use `read_file` to load the content of the specified task file path.
    2.  **MUST** perform the work described in the Markdown body, following the checklist items.
    3.  **MUST** update the Markdown checklist (`- [ ]` -> `- [✅]`) as steps are completed using `apply_diff` or `search_and_replace`. Add brief notes/logs to the Markdown body as needed.
    4.  **MUST** update the `status` field in the **TOML block** of the task file upon completion (`"🟢 Done"`) or if blocked (`"⚪ Blocked"`), along with the `updated_date`, using `apply_diff`.
    5.  **MUST** report the final outcome back to the Coordinator using `attempt_completion`, referencing the MDTM task file path.

**Failure to create the MDTM file before delegation, or failure by the specialist to update the assigned file, breaks the tracking process.** This workflow is essential for managing complex tasks within the Roo system.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/05-os-aware-commands.md:
+++
# --- Basic Metadata ---
id = "RURU-RULE-OS-AWARE-CMDS-V3" # Incremented version
title = "Rule: Generate OS-Aware and Syntactically Correct Commands"
context_type = "rules"
scope = "Command generation for execute_command tool based on detected OS"
target_audience = ["all"] # Apply to all modes using execute_command
granularity = "procedure" # Changed from ruleset to procedure as it defines steps
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["rules", "shell", "commands", "os-awareness", "powershell", "bash", "execute_command", "windows", "linux", "macos", "syntax", "chaining", "conditional-execution"] # Added tags
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
related_context = [".roo/rules/03-standard-tool-use-xml-syntax.md"]
relevance = "Critical: Prevents command execution errors"
+++

# Mandatory Rule: Generate OS-Aware and Syntactically Correct Commands

**Context:** Commands executed via `<execute_command>` run within the user's VS Code integrated terminal environment. The underlying operating system significantly impacts required command syntax. Assume the host OS is provided via context (e.g., `environment_details.os` with values like `win32`, `darwin`, `linux`).

**Rule:**

When formulating commands intended for execution via the `<execute_command>` tool, you **MUST** check the operating system context provided (e.g., `environment_details.os`) and generate commands appropriate for that specific platform's default shell, ensuring correct syntax, especially for command chaining.

**Platform-Specific Syntax & Chaining:**

*   **If OS is `win32` (Windows):**
    *   Target Shell: **PowerShell**.
    *   Examples: `Get-ChildItem` (or `ls`/`dir`), `Copy-Item`, `Move-Item`, `Remove-Item`, `New-Item -ItemType Directory`, `$env:VAR_NAME`, `python -m venv .venv`, `.\.venv\Scripts\activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate multiple commands that should run one after the other, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **INVALID OPERATOR:** **NEVER use `&&` for chaining commands.** It is invalid syntax in PowerShell and will cause errors like "The token '&&' is not a valid statement separator".
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** PowerShell lacks a simple *separator* like `&&`. To achieve this reliably with `<execute_command>`:
        1.  Execute the first command in one `<execute_command>` call.
        2.  **Await the result.** Check the `exit_code`. An exit code of `0` typically indicates success.
        3.  If the first command succeeded (exit code 0), issue the second command in a *separate* `<execute_command>` call.
        4.  **AVOID** generating complex PowerShell `if ($?) {...}` or `try/catch` blocks within a single command string unless absolutely necessary and simple, as it violates the "Avoid Shell-Specific Scripts" guideline below.
    *   Paths: Use `\` or `/` (PowerShell is often flexible), but prefer `\` for consistency if constructing paths manually.
    *   Quoting: Use single quotes `'...'` for literal strings. Use double quotes `"..."` if variable expansion is needed (less common for simple commands).

*   **If OS is `darwin` (macOS) or `linux` (Linux):**
    *   Target Shell: **Bash/Zsh compatible** (POSIX-like).
    *   Examples: `ls`, `cp`, `mv`, `rm`, `mkdir`, `$VAR_NAME`, `python3 -m venv .venv`, `source .venv/bin/activate`.
    *   **Sequential Execution:** Use semicolons **`;`** to separate commands that should run sequentially, regardless of success (e.g., `mkdir temp; cd temp`).
    *   **Conditional Execution (If Cmd1 Succeeds, Run Cmd2):** **MUST use the double ampersand `&&`** (e.g., `cd my_dir && ls -l`). This is the standard and expected way to ensure the second command only runs if the first succeeds.
    *   **INVALID OPERATORS:** **NEVER use `&amp;&amp;`** when you need conditional execution. **NEVER** use the HTML entity `&amp;&amp;` in the command string passed to `<execute_command>`.
    *   Paths: **MUST** use forward slashes `/`.
    *   Quoting: Use double quotes `"..."` generally, especially if needing variable expansion (`$VAR`). Use single quotes `'...'` for strict literal strings.

**General Guidelines (Applies to ALL OS):**

*   **Simplicity:** Prefer simple, common commands where possible.
*   **Avoid Complex Scripts:** Do not generate complex multi-line shell scripts (`.ps1`, `.sh`) unless specifically requested and appropriate for the task. Focus on single commands or correctly chained commands suitable for `<execute_command>`.
*   **Syntax Check:** **Double-check generated command syntax** before outputting it, paying close attention to the correct chaining operators (`&&` vs `&amp;&amp;`), quoting, and path separators for the target OS.
*   **User Overrides:** If the user explicitly requests a command for a *different* shell (e.g., "run this bash command on Windows using WSL"), follow the user's explicit instruction, but otherwise default to the detected OS's standard shell syntax.

**Failure to generate OS-appropriate and syntactically correct commands, especially regarding chaining (`&&` vs `&amp;&amp;`), will likely result in execution errors for the user.** Always check the OS context and verify command syntax before generating commands.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/06-iterative-execution-policy.md:
+++
id = "RURU-RULE-ITERATIVE-EXECUTION-V1"
title = "Standard Iterative Execution Policy"
context_type = "rules"
scope = "Defines how modes should handle potentially long-running or complex tasks"
target_audience = ["all"] # Primarily relevant for modes performing implementation/generation
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "workflow", "iteration", "context-management", "safety", "mdtm", "chunking"]
related_context = ["00-user-preferences.md", "01-standard-toml-md-format.md", "04-standard-workflows.md"]
+++

# Standard Iterative Execution Policy

**Objective:** To ensure reliable task completion by preventing context window overflows and promoting manageable work increments, especially for generative or implementation tasks.

**Applies To:** All modes performing tasks that involve significant code generation, file modification, analysis, or following multi-step procedures (e.g., developers, writers, refactorers, testers, sometimes architects/managers). Less critical for simple lookups or coordination.

**Core Principles:**

1.  **Prefer Smaller Steps:** Whenever feasible, break down complex requests into smaller, logical sub-tasks during the planning phase. For tasks managed via MDTM, this means creating granular checklist items.
2.  **Context Awareness:** Modes **MUST** be aware of their context window usage (`{{CONTEXT_PERCENTAGE}}`).
3.  **Proactive Checkpointing:** Do not attempt to complete overly large tasks in a single execution turn, even if instructed broadly.

**Procedure:**

1.  **Task Planning:** When starting a task (especially one involving multiple steps or significant generation):
    *   Review the overall goal and acceptance criteria.
    *   If using MDTM, review the checklist items.
    *   Mentally estimate the complexity. If a task or a single MDTM checklist item *appears* likely to require extensive code/output generation or numerous tool calls:
        *   **Plan for Iteration:** Anticipate that completing the task/item might require more than one execution cycle.
        *   **(Optional but Recommended):** Inform the delegator (via `ask_followup_question` *before starting*) if you anticipate needing multiple steps/checkpoints for a single requested item.

2.  **Execution & Monitoring:** While executing the task (writing code, applying diffs, following checklist items):
    *   Periodically self-monitor context window usage (`{{CONTEXT_PERCENTAGE}}`).
    *   **Trigger Checkpoint:** If context usage approaches a threshold (e.g., **around 40-50%**), prepare to pause *after completing the current logical unit of work*.
        *   A "logical unit" could be:
            *   Completing the current MDTM checklist item (`- [✅]`).
            *   Finishing a complete function, class, or coherent block of code.
            *   Completing a specific file modification.
            *   Finishing a distinct step in an analysis process.

3.  **Checkpoint & Handover:** When pausing due to the context threshold OR completing a step marked for reporting (e.g., `📣` in MDTM):
    *   **Finalize Current Unit:** Ensure the immediate work unit is complete and syntactically correct (e.g., finish the function, close code blocks).
    *   **Summarize Progress:** Briefly state what was completed in the current turn.
    *   **Identify Next Step:** Clearly state the *next logical step* required to continue the overall task (e.g., "Next step is to implement the `handleUpdate` function", "Next step is to process MDTM item #3").
    *   **Report Status:** Use `<attempt_completion>` to report back to the delegator. Include:
        *   Confirmation of completed unit/step.
        *   Current context percentage.
        *   The identified *next step*.
        *   Any partial results or paths to modified/created files.
        *   *(Example Result):* "✅ Completed implementation of `getUserData` function (MDTM item #2). Context at 55%. Next step is to implement the `UserProfile` component using this data. Modified: `src/hooks/useUserData.ts`."

4.  **Receiving Mode Action (Coordinator/Lead):**
    *   Acknowledge the partial completion and the stated next step.
    *   Log the progress (Rule `12`).
    *   Re-delegate the *next step* back to the specialist mode, providing the necessary context (including the original goal and referencing the previous work/files).

**Rationale:**

*   **Context Safety:** Prevents hitting hard context limits which often lead to truncated, incomplete, or erroneous responses.
*   **Error Reduction:** Smaller execution units reduce the chance of complex errors accumulating within a single turn.
*   **State Management:** Encourages breaking work into steps that align well with MDTM tracking, improving visibility.
*   **User Experience:** While it involves more turns, it leads to more reliable progress compared to large failures requiring complete restarts.

**Note:** The 50-60% threshold is a guideline. Modes should use judgment. If a small, final step pushes usage slightly over, completing it might be acceptable. The key is to avoid *starting* a large unit of work when context is already high.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/08-logging-procedure-simplified.md:
+++
id = "RULE-LOGGING-PROCEDURE-SIMPLE-V1"
title = "Standard: Logging Requirement"
context_type = "rules"
scope = "Requirement to log significant events and decisions"
target_audience = ["all"] # Especially Coordinators and Leads
granularity = "guideline"
status = "active"
last_updated = "2025-04-22"
tags = ["rules", "logging", "auditing", "traceability", "mdtm"]
related_context = [
    ".roo/rules/04-mdtm-workflow-initiation.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md" # Link to detailed KB
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Essential for traceability and state management"
+++

# Standard: Logging Requirement

**Objective:** Ensure a traceable record of actions, decisions, and task progress.

**Rule:**

1.  **Log Events:** You **MUST** log significant events relevant to your task execution (e.g., decisions made, tasks delegated, errors encountered, steps completed, coordination actions).
2.  **Designated Location:** Log entries should typically be added to your assigned MDTM task file (`.ruru/tasks/TASK-...`), your coordination log file, or other designated artifact locations (e.g., ADRs in `.ruru/decisions/`).
3.  **Tooling Details:** For detailed guidance on *which tools* (`write_to_file`, `append_to_file`, `insert_content`, `apply_diff`) to use for specific logging scenarios and locations, consult the Roo Commander Knowledge Base document: **`.ruru/modes/roo-commander/kb/12-logging-procedures.md`**.

# Rules from /home/jez/vscode/roo-commander/.roo/rules/10-vertex-mcp-usage-guideline.md:
+++
# --- Basic Metadata ---
id = "RULE-VERTEX-MCP-USAGE-V1"
title = "Guideline: Vertex AI MCP Tool Usage"
context_type = "rules"
scope = "Standardizing the use of Vertex AI MCP tools, especially save vs. direct output"
target_audience = ["all"] # Primarily modes using research/generation
granularity = "guideline"
status = "active"
last_updated = "2025-04-26" # Use current date
tags = ["rules", "mcp", "vertex-ai", "guideline", "output-handling", "file-organization", "research", "validation"]
related_context = [
    ".roo/rules/01-standard-toml-md-format.md",
    ".roo/rules/08-logging-procedure-simplified.md",
    "repomix-output-shariqriazz-vertex-ai-mcp-server.md" # Reference to the MCP definition
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Ensures consistent handling of MCP outputs"
+++

# Guideline: Vertex AI MCP Tool Usage

**Objective:** To standardize how modes interact with the `vertex-ai-mcp-server`, particularly regarding output handling and the use of research/validation capabilities.

**Applies To:** All modes utilizing tools provided by the `vertex-ai-mcp-server`.

**1. Tool Availability:**

*   Modes receive the list of available MCP tools dynamically in their context. Use these tools only if the `vertex-ai-mcp-server` is connected and the specific tool is listed.
*   Modes should gracefully handle scenarios where the MCP server or specific tools are unavailable.

**2. Output Handling Strategy (General):**

*   **Default to `save_*`:** When using Vertex AI MCP tools that have a corresponding `save_*` variant (e.g., `save_generate_project_guidelines`, `save_doc_snippet`, `save_topic_explanation`, `save_answer_query_direct`, `save_answer_query_websearch`), **prefer using the `save_*` variant** for potentially long or complex outputs.
    *   **Rationale:** This prevents large outputs from cluttering the chat history, archives the result for later reference, and helps manage context window size.
*   **Use Direct Tools Sparingly:** Use the direct output tools (e.g., `answer_query_websearch`, `explain_topic_with_docs`, `get_doc_snippets`) only when the expected output is known to be concise (e.g., a single code snippet, a short definition, a simple yes/no answer) or when specifically requested by the user/coordinator for an inline response.
*   **Reporting Saved Files:** When using a `save_*` tool, the mode **MUST** report the full path to the saved file back to the coordinator/user via `<attempt_completion>`. (See Section 2.1 for handling persistent context outputs.)

**2.1. Handling Persistent Context Outputs:**

*   **Identify Need:** If the output generated by a `save_*` tool is intended to be *persistent context* referenced directly by mode rules, KBs, or long-term documentation (unlike temporary analysis results):
    1.  **Move & Rename:** After the `save_*` tool successfully creates the file in the default `.ruru/docs/vertex/...` location, the coordinating mode **MUST** immediately use a file system tool (`execute_command` with `mkdir -p` and `mv`, or the `vertex-ai-mcp-server`'s `create_directory` and `move_file_or_directory` tools) to:
        *   Ensure a `context/` subdirectory exists within the relevant mode's directory (e.g., `.ruru/modes/[mode-slug]/context/`).
        *   Move the generated file from `.ruru/docs/vertex/...` into this mode-specific `context/` directory.
        *   Rename the file to something meaningful and versioned if appropriate (e.g., `[mode-slug]_context_[topic]_v1.md`) instead of the default timestamped name.
    2.  **Update References:** Any rules, KBs, or documents referencing this context **MUST** be updated immediately to point to the new, persistent path within the mode's `context/` directory.
    3.  **Log Move:** Log the move and rename operation.
*   **Rationale:** This ensures that context critical to a mode's operation is stored logically with the mode and avoids broken references if the general `.ruru/docs/vertex/` directory is treated as temporary. The default timestamped location should be used for transient outputs or initial review before deciding on persistence.

**3. Standard Output Location & Naming:**

*   **Base Directory:** All files generated by `save_*` tools **MUST** be saved within the `.ruru/docs/vertex/` directory.
*   **Subdirectory Structure:** Organize files by the *type* of tool used:
    *   `save_generate_project_guidelines` -> `.ruru/docs/vertex/guidelines/`
    *   `save_doc_snippet` -> `.ruru/docs/vertex/snippets/`
    *   `save_topic_explanation` -> `.ruru/docs/vertex/explanations/`
    *   `save_answer_query_direct` -> `.ruru/docs/vertex/answers-direct/`
    *   `save_answer_query_websearch` -> `.ruru/docs/vertex/answers-web/`
*   **File Naming Convention:** Files **MUST** be named using the format `[YYYYMMDDHHMMSS]-[sanitized_topic_or_query].md`.
    *   `[YYYYMMDDHHMMSS]`: Timestamp generated by the mode at the time of the call.
    *   `[sanitized_topic_or_query]`: A filesystem-safe representation of the primary topic or query (e.g., replace spaces/special characters with `_`, limit length to ~50 characters).
    *   *Example:* `.ruru/docs/vertex/guidelines/20250426182500-react_ts_node_guidelines.md`

**4. Using MCP for Research & Validation ("Brains Trust"):**

*   **Targeted Use:** While tools like `answer_query_websearch` can provide external context or validation, their use should be targeted and judicious due to latency, cost, and potential complexity.
*   **Prioritize Internal Context:** Modes **MUST** prioritize using internal project knowledge (KBs, rules, existing code, task context) before resorting to external MCP calls for validation or general research.
*   **Recommended Modes:** Consider enabling or encouraging this capability primarily within modes focused on architecture, research, complex problem-solving, or senior-level review (e.g., `technical-architect`, `agent-research`, `complex-problem-solver`, `util-senior-dev`, `util-second-opinion`).
*   **Clear Triggers:** Modes utilizing external validation should have clear triggers defined in their specific rules/KBs (e.g., "when evaluating unfamiliar technology", "if confidence is low").
*   **Log Usage:** Log instances where external validation was sought via MCP, including the query and a summary of the outcome, according to standard logging procedures (Rule `08-logging-procedure-simplified.md`).

**Adherence to these guidelines ensures consistent, traceable, and efficient use of the Vertex AI MCP capabilities.**</custom_instructions>
</environment_details>

---

**Assistant:**

Session log updated.

The `spec-repomix` specialist has successfully generated the Repomix artifact as requested.

```xml
<attempt_completion>
<result>
The Repomix artifact for the GitHub directory `https://github.com/RooVetGit/Roo-Code-Docs/tree/main/docs/advanced-usage` has been generated and saved to:
`.ruru/context/repomix/roo-code-docs-advanced-usage.repomix.json`
</result>
</attempt_completion>
```

