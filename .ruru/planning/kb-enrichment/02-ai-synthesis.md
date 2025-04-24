+++
# --- Metadata ---
id = "PLAN-KB-ENRICH-PHASE2-V1"
title = "KB Enrichment Plan: Phase 2 - AI Synthesis"
status = "draft"
created_date = "2025-04-24"
updated_date = "2025-04-24"
version = "1.0"
tags = ["plan", "kb", "enrichment", "phase2", "synthesis", "ai", "context-generation"]
related_docs = [".ruru/planning/kb-enrichment/00-kb-enrichment-plan.md", ".ruru/modes/agent-context-condenser/agent-context-condenser.mode.md"]
objective = "Define the tasks for an AI agent (`agent-context-condenser`) to read prepared markdown files and generate new, synthesized context documents for a target mode's knowledge base."
scope = "Orchestrating the AI synthesis process, defining inputs and desired outputs."
# --- Plan Specific Fields ---
synthesizer_mode = "agent-context-condenser"
source_directory_template = "kb/{library_name}/"
target_directory_template = ".ruru/modes/{mode_slug}/kb/{library_name}/synthesized/"
synthesis_tasks = [ # List of synthesis types to perform
    { task_id: "core_concepts", description: "Generate overview of core library concepts.", input_categories: ["guide", "concepts", "about"], output_file: "core-concepts.md" },
    { task_id: "api_overview", description: "Generate high-level API surface summary.", input_categories: ["api", "reference"], output_file: "api-overview.md" },
    { task_id: "common_patterns", description: "Extract common usage patterns/best practices.", input_categories: ["guide", "cookbook", "examples"], output_file: "common-patterns.md" },
    { task_id: "setup_guide", description: "Summarize installation and basic setup.", input_categories: ["guide", "config", "start"], output_file: "setup-summary.md" }
    # Add more tasks as needed (e.g., troubleshooting, specific feature deep-dives)
]
+++

# KB Enrichment Plan: Phase 2 - AI Synthesis

**Objective:** Use the `[synthesizer_mode]` to process the structured markdown files from `[source_directory_template]` and generate high-level, synthesized context documents, saving them to `[target_directory_template]`.

**Procedure (for a given `[library_name]` and `[mode_slug]`):**

1.  **Prepare Target Directory (Coordinator Task):**
    *   Tool: `execute_command`
    *   Action: Ensure the target directory `[target_directory_template]` exists. Use `mkdir -p [target_directory_template]` (Check OS Rule 05). Handle errors.

2.  **Execute Synthesis Tasks (Coordinator Task - Looping through `synthesis_tasks`):**
    *   For each `task` defined in the `synthesis_tasks` list above:
        *   **Identify Input Files:** Use `list_files` to find all `.md` files within the relevant `[source_directory_template]/[category]/` directories specified in `task.input_categories`. Create a list of these input file paths `[Input File List]`. If no input files found for the required categories, log a warning and skip this task.
        *   **Delegate Synthesis:**
            *   Tool: `new_task`
            *   Mode: `[synthesizer_mode]`
            *   Message:
                ```
                🧠 Synthesize KB Context:
                Task: [task.description]
                Library: [library_name]
                Target Mode: [mode_slug]
                Input File Paths: [List of input file paths]
                Output File Path: [target_directory_template]/[task.output_file]

                Instructions: Read the content of the input files. Generate a concise, well-structured Markdown document summarizing the requested information ([task.description]). Focus on providing high-level understanding, key takeaways, and connections between concepts relevant to the library. Include relevant keywords and concepts. Format the output as Markdown with a TOML frontmatter block containing 'title', 'summary' (1-2 sentences), and 'tags'. Write the final synthesized content to the specified output file path.
                ```
            *   Action: Delegate the task. Await completion (`attempt_completion`). Handle errors reported by the synthesizer (log, potentially retry or skip).

**Completion:** All defined synthesis tasks have been attempted. Synthesized `.md` files should exist in `[target_directory_template]`. Proceed to Phase 3 (`03-kb-organization-indexing.md`).