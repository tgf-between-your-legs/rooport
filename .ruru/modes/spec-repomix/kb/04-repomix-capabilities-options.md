+++
# --- Basic Metadata ---
id = "KB-REPOMIX-CAPABILITIES-V1"
title = "Repomix Specialist: Capabilities and Command-Line Options"
context_type = "knowledge_base"
scope = "Reference guide for repomix CLI options"
target_audience = ["spec-repomix"]
status = "active"
last_updated = "2025-05-01"
tags = ["repomix", "kb", "cli", "options", "reference", "capabilities"]
related_context = [".roo/rules-spec-repomix/02-repomix-decision-tree.md", ".ruru/modes/spec-repomix/kb/02-repomix-github-source-handling.md", ".ruru/modes/spec-repomix/kb/03-repomix-local-source-handling.md"]
template_schema_doc = ".ruru/templates/toml-md/14_kb_article.README.md" # Points to schema documentation
# --- KB Specific ---
# version = "1.0" # Optional: Semantic version for the KB article itself
# relevance = "High" # Optional: Qualitative relevance score
# confidence = "High" # Optional: Confidence in the accuracy of the information
# source_type = "Derived" # Optional: e.g., "Derived", "Empirical", "External", "Speculative"
# source_ref = "repomix --help" # Optional: Specific source (URL, command, document)
+++

# Repomix Capabilities and Command-Line Options

This document summarizes the command-line arguments and options available for the `repomix` tool, based on its `--help` output.

## Usage

```
repomix [options] [directories...]
```

## Arguments

-   `directories`: List of local directories to process. Defaults to the current directory (`.`) if no other source (remote or config) is specified.

## Options

### Input/Source Specification

-   `--remote <url>`: Process a remote Git repository URL instead of local directories.
-   `--remote-branch <name>`: Specify a branch, tag, or commit hash for the remote repository. Defaults to the repository's default branch.
-   `-c, --config <path>`: Use a JSON configuration file to specify sources, output, and other options. **(Preferred method for complex or multiple sources)**.
-   `directories...` (Argument): Specify one or more local directories directly.

### Output Configuration

-   `-o, --output <file>`: Specify the output file name.
-   `--style <type>`: Set the output format. Options: `xml`, `markdown`, `plain`.
-   `--parsable-style`: Ensure output is valid and parsable for the chosen style (e.g., proper XML escaping).
-   `--header-text <text>`: Add custom text to the beginning of the output file.
-   `--instruction-file-path <path>`: Include content from a specified file as instructions within the output header.

### Content Filtering and Formatting

-   `--compress`: Apply code compression techniques (potentially lossy) to reduce token count.
-   `--output-show-line-numbers`: Prepend line numbers to each line of code in the output.
-   `--no-file-summary`: Disable the summary section listing processed files.
-   `--no-directory-structure`: Disable the section showing the directory tree.
-   `--remove-comments`: Strip comments from the code.
-   `--remove-empty-lines`: Remove blank lines from the code.
-   `--include-empty-directories`: Include directories that contain no files in the structure output.

### File Inclusion/Exclusion (Ignoring)

-   `--include <patterns>`: Comma-separated list of glob patterns. Only files matching these patterns will be included.
-   `-i, --ignore <patterns>`: Comma-separated list of additional glob patterns to ignore files/directories.
-   `--no-gitignore`: Do not respect rules found in `.gitignore` files.
-   `--no-default-patterns`: Do not use Repomix's built-in default ignore patterns (like `node_modules`, `.git`, etc.).

### Git Integration

-   `--no-git-sort-by-changes`: Disable the default behavior of sorting files based on Git commit frequency.

### Tool Behavior & Meta

-   `-v, --version`: Show the installed `repomix` version.
-   `--init`: Create a default `repomix.config.json` file in the current directory.
-   `--global`: Use with `--init` to create the config file in the global user configuration location instead of the current directory.
-   `--no-security-check`: Disable the check for potentially sensitive file patterns.
-   `--token-count-encoding <encoding>`: Specify the encoding used for token counting (e.g., `o200k_base`, `cl100k_base`). Affects the reported token count.
-   `--mcp`: Run `repomix` as an MCP (Model Context Protocol) server (Advanced usage).
-   `--top-files-len <number>`: Control how many files are listed in the "Top N files by token count" summary.
-   `--verbose`: Show more detailed logging during execution.
-   `--quiet`: Suppress all informational output to standard out (errors may still go to standard error).
-   `-h, --help`: Display this help message.

### Utility

-   `--copy`: Copy the final generated output directly to the system clipboard.

---

*This summary is based on `repomix --help` output.*