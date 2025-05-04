+++
# --- Basic Metadata ---
id = "KB-REPOMIX-CAPABILITIES-V2" # Updated version
title = "Repomix Specialist: Comprehensive CLI Options Reference" # Updated title
context_type = "knowledge_base"
scope = "Reference guide for repomix CLI options based on fetched documentation" # Updated scope
target_audience = ["spec-repomix", "roo-commander", "prime-coordinator"] # Expanded audience
status = "active"
last_updated = "2025-05-03" # Updated date
tags = ["repomix", "kb", "cli", "options", "reference", "capabilities", "filters", "output"] # Added tags
related_context = [
    ".roo/rules-spec-repomix/02-repomix-decision-tree.md",
    ".ruru/modes/spec-repomix/kb/02-repomix-github-source-handling.md",
    ".ruru/modes/spec-repomix/kb/03-repomix-local-source-handling.md",
    ".ruru/modes/spec-repomix/kb/configuration-methods.md" # Added related config KB
    ]
template_schema_doc = ".ruru/templates/toml-md/14_kb_article.README.md"
# --- KB Specific ---
source_ref = "Fetched documentation provided in task SESSION-20250503-172525" # Updated source
+++

# Repomix Comprehensive CLI Options Reference

This document provides a comprehensive reference for the `repomix` command-line options, structured according to the fetched documentation provided for audit task `SESSION-20250503-172525`.

**Note:** The `spec-repomix` mode primarily uses the `--config <path>` option, generating temporary JSON configuration files based on templates. However, understanding the underlying CLI options is crucial for generating correct configurations.

## Basic Options

*   `-v, --version`: Show tool version.

## Output Options

*   `-o, --output <file>`: Output file name (default: `repomix-output.txt`).
*   `--style <type>`: Output style (`plain`, `xml`, `markdown`) (default: `xml`).
*   `--parsable-style`: Enable parsable output based on the chosen style schema (default: `false`). Ensures proper escaping for formats like XML.
*   `--compress`: Perform intelligent code extraction, focusing on essential function and class signatures while removing implementation details. See official `repomix` documentation for details. (default: `false`).
*   `--output-show-line-numbers`: Add line numbers (default: `false`).
*   `--copy`: Copy to clipboard (default: `false`).
*   `--no-file-summary`: Disable file summary section (default: `true`). *Note: Default is `true`, meaning the summary is disabled unless explicitly enabled via config.*
*   `--no-directory-structure`: Disable directory structure section (default: `true`). *Note: Default is `true`, meaning the structure is disabled unless explicitly enabled via config.*
*   `--no-files`: Disable files content output (metadata-only mode) (default: `true`). *Note: Default is `true`, meaning content is disabled unless explicitly enabled via config.*
*   `--remove-comments`: Remove comments (default: `false`).
*   `--remove-empty-lines`: Remove empty lines (default: `false`).
*   `--header-text <text>`: Custom text to include in the file header.
*   `--instruction-file-path <path>`: Path to a file containing detailed custom instructions to include in the header.
*   `--include-empty-directories`: Include empty directories in the output structure (default: `false`).

## Filter Options

These options control which files are included when processing the source path (local directory or temporary clone).

*   `--include <patterns>`: Comma-separated list of glob patterns. Only files matching these patterns will be included.
*   `-i, --ignore <patterns>`: Comma-separated list of additional glob patterns to ignore files/directories.
*   `--no-gitignore`: Disable the use of `.gitignore` files for filtering (default: `false`, meaning `.gitignore` is used by default).
*   `--no-default-patterns`: Disable Repomix's built-in default ignore patterns (like `node_modules`, `.git`, etc.) (default: `false`, meaning defaults are used by default).

## Remote Repository Options

**Note:** The `spec-repomix` mode handles remote repositories via a `git clone` workflow. These flags are primarily for understanding the tool's native capability, which this mode bypasses.

*   `--remote <url>`: Process remote repository URL directly (this mode uses `git clone` instead).
*   `--remote-branch <name>`: Specify the remote branch name, tag, or commit hash (this mode uses this info for `git clone`).

## Configuration Options

*   `-c, --config <path>`: Custom config file path. **This is the primary method used by `spec-repomix` mode.**
*   `--init`: Create a default `repomix.config.json` file.
*   `--global`: Use with `--init` to create/use the global config file.

## Security Options

*   `--no-security-check`: Disable security check for sensitive patterns (default: `true`). *Note: Default is `true`, meaning security checks are disabled unless explicitly enabled via config.*

## Token Count Options

*   `--token-count-encoding <encoding>`: Specify token count encoding (e.g., `o200k_base`, `cl100k_base`) (default: `o200k_base`).

## Other Options

*   `--top-files-len <number>`: Number of top files to show in the token count summary (default: `5`).
*   `--verbose`: Enable verbose logging during execution.
*   `--quiet`: Disable all informational output to stdout (errors may still go to stderr).
*   `-h, --help`: Display help message (Standard CLI practice).

---

*This reference is based on fetched documentation provided for audit task `SESSION-20250503-172525`.*