**User:**

<task>
Please commit the newly created Standard Operating Procedure file.

1.  Stage the file: `git add .ruru/processes/SOP-GIT-COMMIT-CHANGES-V1.md`
2.  Commit the staged file with the message: `docs: Add SOP for committing specific changes`

Execute the necessary `git add` and `git commit` commands.
</task>
<environment_details>
# VSCode Visible Files
.ruru/processes/SOP-GIT-COMMIT-CHANGES-V1.md

# VSCode Open Tabs
.ruru/temp/repomix_config_20250502060602.json,.ruru/modes/spec-repomix/kb/02-repomix-github-source-handling.md,.ruru/modes/spec-repomix/kb/03-repomix-local-source-handling.md,.ruru/processes/SOP-GIT-COMMIT-CHANGES-V1.md,.ruru/repomix/x1xhlol_system-prompts-and-models-of-ai-tools/system-prompts-and-models-of-ai-tools_full.md

# Current Time
02/05/2025, 10:07:27 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
(Not available)

# Current Cost
$0.00

# Current Mode
<slug>dev-git</slug>
<name>🦕 Git Manager</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Git Manager. Your primary role and expertise is executing Git commands safely and accurately based on instructions, primarily within the project's current working directory.

Key Responsibilities:
- Execute specific Git commands provided by other modes or the user (e.g., `git add`, `git commit`, `git push`, `git pull`, `git branch`, `git checkout`, `git merge`, `git rebase`, `git log`, `git status`).
- Ensure commands are executed in the correct working directory (usually the project root, but respect `cwd` if specified).
- Clearly report the outcome (success or failure) and any relevant output from the Git command.
- Handle potential errors gracefully (e.g., merge conflicts, authentication issues) by reporting them clearly. Do *not* attempt to resolve complex issues like merge conflicts automatically unless specifically instructed with a clear strategy.
- Prioritize safety: Avoid destructive commands (`git reset --hard`, `git push --force`) unless explicitly confirmed with strong warnings.

Operational Guidelines:
- Consult and prioritize guidance, best practices, and project-specific information found in the Knowledge Base (KB) located in `.ruru/modes/dev-git/kb/`. Use the KB README to assess relevance and the KB lookup rule for guidance on context ingestion. # << REFINED KB GUIDANCE >>
- Use the `execute_command` tool for all Git operations.
- Always confirm the exact command and target directory before execution.
- If a command is ambiguous or potentially dangerous, ask for clarification using `ask_followup_question`.
- Report results concisely.
- Do not perform complex Git workflows (e.g., multi-step rebases, intricate branch management) without detailed, step-by-step instructions. Escalate complex workflow requests to a Lead or Architect if necessary.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files.
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

# Rules from /home/jez/vscode/roo-commander/.roo/rules-dev-git/.placeholder:
# Placeholder file to ensure directory creation.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-dev-git/01-kb-lookup-rule.md:
# Rule: Consult Knowledge Base

Before proceeding with the task, review the KB README (`.ruru/modes/dev-git/kb/README.md`) which summarizes available documents and their size (line count).
Assess the relevance of each listed document to the current task based on its summary.
Estimate the potential benefit vs. the context cost (line count) of reading relevant documents.
**Limit:** If the total estimated lines to read for *multiple* relevant files exceeds ~1000 lines (adjust threshold as needed), consider if all are truly necessary. If unsure, use `ask_followup_question` to confirm with the user which specific files to read or suggest refining the task.
If you are confident a document is highly relevant and the cost is acceptable (or confirmed by user), read it using `read_file`.
Incorporate information from read documents into your response or actions.
If no relevant documents are found or deemed worth the cost, proceed using your general knowledge.

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
build_collections.log
build_kilocode.log
build_main.log
bun.lock
CHANGELOG.md
LICENSE
package-lock.json
package.json
README.md
mcp-servers/
mcp-servers/vertex-ai/.env.example
mcp-servers/vertex-ai/README.md
scripts/
scripts/sync-wiki.ts
</environment_details>

---

**Assistant:**

Okay, I will execute the Git commands as requested.

First, I need to check the Knowledge Base README as per the rules.
<tool_use>
<tool_name>read_file</tool_name>
<parameters>
<path>.ruru/modes/dev-git/kb/README.md</path>
</parameters>
</tool_use>

---

**User:**

[ERROR] You did not use a tool in your previous response! Please retry with a tool use.

# Reminder: Instructions for Tool Use

Tool uses are formatted using XML-style tags. The tool name is enclosed in opening and closing tags, and each parameter is similarly enclosed within its own set of tags. Here's the structure:

<tool_name>
<parameter1_name>value1</parameter1_name>
<parameter2_name>value2</parameter2_name>
...
</tool_name>

For example:

<attempt_completion>
<result>
I have completed the task...
</result>
</attempt_completion>

Always adhere to this format for all tool uses to ensure proper parsing and execution.

# Next Steps

If you have completed the user's task, use the attempt_completion tool. 
If you require additional information from the user, use the ask_followup_question tool. 
Otherwise, if you have not completed the task and do not need additional information, then proceed with the next step of the task. 
(This is an automated message, so do not respond to it conversationally.)
<environment_details>
# VSCode Visible Files
.ruru/repomix/x1xhlol_system-prompts-and-models-of-ai-tools/system-prompts-and-models-of-ai-tools_full.md

# VSCode Open Tabs
.ruru/temp/repomix_config_20250502060602.json,.ruru/modes/spec-repomix/kb/02-repomix-github-source-handling.md,.ruru/modes/spec-repomix/kb/03-repomix-local-source-handling.md,.ruru/processes/SOP-GIT-COMMIT-CHANGES-V1.md,.ruru/repomix/x1xhlol_system-prompts-and-models-of-ai-tools/system-prompts-and-models-of-ai-tools_full.md

# Current Time
02/05/2025, 10:07:34 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
48,007 (5%)

# Current Cost
$0.00

# Current Mode
<slug>dev-git</slug>
<name>🦕 Git Manager</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Git Manager. Your primary role and expertise is executing Git commands safely and accurately based on instructions, primarily within the project's current working directory.

Key Responsibilities:
- Execute specific Git commands provided by other modes or the user (e.g., `git add`, `git commit`, `git push`, `git pull`, `git branch`, `git checkout`, `git merge`, `git rebase`, `git log`, `git status`).
- Ensure commands are executed in the correct working directory (usually the project root, but respect `cwd` if specified).
- Clearly report the outcome (success or failure) and any relevant output from the Git command.
- Handle potential errors gracefully (e.g., merge conflicts, authentication issues) by reporting them clearly. Do *not* attempt to resolve complex issues like merge conflicts automatically unless specifically instructed with a clear strategy.
- Prioritize safety: Avoid destructive commands (`git reset --hard`, `git push --force`) unless explicitly confirmed with strong warnings.

Operational Guidelines:
- Consult and prioritize guidance, best practices, and project-specific information found in the Knowledge Base (KB) located in `.ruru/modes/dev-git/kb/`. Use the KB README to assess relevance and the KB lookup rule for guidance on context ingestion. # << REFINED KB GUIDANCE >>
- Use the `execute_command` tool for all Git operations.
- Always confirm the exact command and target directory before execution.
- If a command is ambiguous or potentially dangerous, ask for clarification using `ask_followup_question`.
- Report results concisely.
- Do not perform complex Git workflows (e.g., multi-step rebases, intricate branch management) without detailed, step-by-step instructions. Escalate complex workflow requests to a Lead or Architect if necessary.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files.
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

# Rules from /home/jez/vscode/roo-commander/.roo/rules-dev-git/.placeholder:
# Placeholder file to ensure directory creation.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-dev-git/01-kb-lookup-rule.md:
# Rule: Consult Knowledge Base

Before proceeding with the task, review the KB README (`.ruru/modes/dev-git/kb/README.md`) which summarizes available documents and their size (line count).
Assess the relevance of each listed document to the current task based on its summary.
Estimate the potential benefit vs. the context cost (line count) of reading relevant documents.
**Limit:** If the total estimated lines to read for *multiple* relevant files exceeds ~1000 lines (adjust threshold as needed), consider if all are truly necessary. If unsure, use `ask_followup_question` to confirm with the user which specific files to read or suggest refining the task.
If you are confident a document is highly relevant and the cost is acceptable (or confirmed by user), read it using `read_file`.
Incorporate information from read documents into your response or actions.
If no relevant documents are found or deemed worth the cost, proceed using your general knowledge.

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

Okay, I will first check the Knowledge Base README as required.
<tool_use>
<tool_name>read_file</tool_name>
<parameters>
<path>.ruru/modes/dev-git/kb/README.md</path>
</parameters>
</tool_use>

---

**User:**

[ERROR] You did not use a tool in your previous response! Please retry with a tool use.

# Reminder: Instructions for Tool Use

Tool uses are formatted using XML-style tags. The tool name is enclosed in opening and closing tags, and each parameter is similarly enclosed within its own set of tags. Here's the structure:

<tool_name>
<parameter1_name>value1</parameter1_name>
<parameter2_name>value2</parameter2_name>
...
</tool_name>

For example:

<attempt_completion>
<result>
I have completed the task...
</result>
</attempt_completion>

Always adhere to this format for all tool uses to ensure proper parsing and execution.

# Next Steps

If you have completed the user's task, use the attempt_completion tool. 
If you require additional information from the user, use the ask_followup_question tool. 
Otherwise, if you have not completed the task and do not need additional information, then proceed with the next step of the task. 
(This is an automated message, so do not respond to it conversationally.)
<environment_details>
# VSCode Visible Files
.ruru/repomix/x1xhlol_system-prompts-and-models-of-ai-tools/system-prompts-and-models-of-ai-tools_full.md

# VSCode Open Tabs
.ruru/temp/repomix_config_20250502060602.json,.ruru/modes/spec-repomix/kb/02-repomix-github-source-handling.md,.ruru/modes/spec-repomix/kb/03-repomix-local-source-handling.md,.ruru/processes/SOP-GIT-COMMIT-CHANGES-V1.md,.ruru/repomix/x1xhlol_system-prompts-and-models-of-ai-tools/system-prompts-and-models-of-ai-tools_full.md

# Current Time
02/05/2025, 10:07:44 am (Australia/Sydney, UTC+10:00)

# Current Context Size (Tokens)
57,025 (5%)

# Current Cost
$0.00

# Current Mode
<slug>dev-git</slug>
<name>🦕 Git Manager</name>
<model>gemini-2.5-pro-exp-03-25</model>
<role>You are Roo Git Manager. Your primary role and expertise is executing Git commands safely and accurately based on instructions, primarily within the project's current working directory.

Key Responsibilities:
- Execute specific Git commands provided by other modes or the user (e.g., `git add`, `git commit`, `git push`, `git pull`, `git branch`, `git checkout`, `git merge`, `git rebase`, `git log`, `git status`).
- Ensure commands are executed in the correct working directory (usually the project root, but respect `cwd` if specified).
- Clearly report the outcome (success or failure) and any relevant output from the Git command.
- Handle potential errors gracefully (e.g., merge conflicts, authentication issues) by reporting them clearly. Do *not* attempt to resolve complex issues like merge conflicts automatically unless specifically instructed with a clear strategy.
- Prioritize safety: Avoid destructive commands (`git reset --hard`, `git push --force`) unless explicitly confirmed with strong warnings.

Operational Guidelines:
- Consult and prioritize guidance, best practices, and project-specific information found in the Knowledge Base (KB) located in `.ruru/modes/dev-git/kb/`. Use the KB README to assess relevance and the KB lookup rule for guidance on context ingestion. # << REFINED KB GUIDANCE >>
- Use the `execute_command` tool for all Git operations.
- Always confirm the exact command and target directory before execution.
- If a command is ambiguous or potentially dangerous, ask for clarification using `ask_followup_question`.
- Report results concisely.
- Do not perform complex Git workflows (e.g., multi-step rebases, intricate branch management) without detailed, step-by-step instructions. Escalate complex workflow requests to a Lead or Architect if necessary.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files.
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

# Rules from /home/jez/vscode/roo-commander/.roo/rules-dev-git/.placeholder:
# Placeholder file to ensure directory creation.

# Rules from /home/jez/vscode/roo-commander/.roo/rules-dev-git/01-kb-lookup-rule.md:
# Rule: Consult Knowledge Base

Before proceeding with the task, review the KB README (`.ruru/modes/dev-git/kb/README.md`) which summarizes available documents and their size (line count).
Assess the relevance of each listed document to the current task based on its summary.
Estimate the potential benefit vs. the context cost (line count) of reading relevant documents.
**Limit:** If the total estimated lines to read for *multiple* relevant files exceeds ~1000 lines (adjust threshold as needed), consider if all are truly necessary. If unsure, use `ask_followup_question` to confirm with the user which specific files to read or suggest refining the task.
If you are confident a document is highly relevant and the cost is acceptable (or confirmed by user), read it using `read_file`.
Incorporate information from read documents into your response or actions.
If no relevant documents are found or deemed worth the cost, proceed using your general knowledge.

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

Okay, I will first check the Knowledge Base README as required.
<tool_use>
<tool_name>read_file</tool_name>
<parameters>
<path>.ruru/modes/dev-git/kb/README.md</path>
</parameters>
</tool_use>

