+++
id = "CTX-RURU-REFACTOR-OVERVIEW"
title = "Roo Commander Path Refactor: Overview & Rationale"
context_type = "conceptual"
scope = "High-level explanation of the need for configurable paths"
target_audience = ["ai_dev_team", "roo-commander", "core-architect"]
granularity = "overview"
status = "proposal"
last_updated = "2025-04-21"
tags = ["refactoring", "configuration", "paths", "ruru", "adaptability", "kilocode"]
+++

# Roo Commander Path Refactor: Overview & Rationale

## 1. Problem Statement

The current Roo Commander system relies heavily on hardcoded relative paths (e.g., `.tasks/`, `.modes/`, `.roo/`) within its rules, knowledge base files, mode definitions, templates, workflows, processes, and build scripts. This presents several challenges:

*   **Maintainability:** Changing the location or name of core directories requires manually updating references across potentially hundreds of files, which is time-consuming and error-prone.
*   **Flexibility:** Users cannot easily configure the system to place these directories within a subdirectory (e.g., `.roocom/` or `.ruru/`) for a cleaner workspace root.
*   **Adaptability:** Forks or clones of the system (like a potential "Kilocode" version using `.kilocode/` instead of `.roo/`) require significant manual refactoring to adjust core paths.

## 2. Goal

The primary goal of this refactoring effort is to **centralize path definitions** for the Roo Commander system, making it easily configurable and adaptable to different directory structures and naming conventions without requiring extensive manual code changes.

## 3. Proposed Solution Summary

We will implement a **Central Configuration + Build-Time Substitution** strategy:

1.  **Central Config File (`ruru.config.toml`):** Define all key base paths (for rules, modes, tasks, docs, etc.) in a single TOML file at the workspace root.
2.  **Placeholders:** Replace hardcoded paths within source Markdown files (rules, KB, templates, etc.) with standardized placeholders (e.g., `{{RURU_TASKS_DIR}}`).
3.  **Substitution Script:** Create a build/setup script (`substitute-paths.js` or similar) that reads the config file and generates *processed* versions of the Markdown files, replacing placeholders with the actual configured paths.
4.  **AI Context:** AI modes will interact *only* with the processed files containing concrete paths, ensuring clarity and reliability.
5.  **Build Script Adaptation:** Existing build scripts (`build_roomodes.js`, etc.) will be modified to read paths from the central config file.

## 4. Benefits

*   **Easy Reconfiguration:** Changing directory structures or names (e.g., for forks like Kilocode) primarily involves editing the `ruru.config.toml` file and re-running the substitution script.
*   **Increased Maintainability:** Path definitions are managed in one place.
*   **User Flexibility:** Allows users to optionally nest Roo Commander directories within a subfolder (e.g., `.ruru/`).
*   **Clearer AI Context:** Ensures AI modes receive instructions with unambiguous, concrete paths.