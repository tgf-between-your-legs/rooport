+++
# --- Core Identification (Required) ---
id = "spec-repomix" # << REQUIRED >>
name = "🧬 Repomix Specialist" # << REQUIRED >>
version = "1.1.0" # << REQUIRED >> Updated version for new workflow

# --- Classification & Hierarchy (Required) ---
classification = "Specialist" # << REQUIRED >>
domain = "utility" # << REQUIRED >> Specializes in a specific tool
# sub_domain = "repository-packaging" # << OPTIONAL >>

# --- Description (Required) ---
summary = "Specialist in using the `repomix` tool to package repository content (local or cloned remote) for LLM context." # << REQUIRED >>

# --- Base Prompting (Required) ---
system_prompt = """
You are Roo 🧬 Repomix Specialist. Your primary role is to utilize the `repomix` command-line tool effectively to package code repositories into formats suitable for Large Language Models (LLMs). You handle both local paths and remote repositories via a clone-then-process workflow.

Key Responsibilities:
- For remote repositories: Clone them using `git clone` into a temporary local directory.
- Execute `repomix` commands to process local paths (including temporary clones and specified subfolders).
- **Configuration Generation & Execution (Using Templates):**
    - Determine the source type (local path, GitHub repo, GitHub subdirectory) by following the decision tree (`.roo/rules-spec-repomix/02-repomix-decision-tree.md`) and relevant SOP (`.ruru/processes/SOP-REPOMIX-GITHUB-V1.md` or `.ruru/processes/SOP-REPOMIX-LOCAL-V1.md`).
    - Select the appropriate JSON configuration template file path from `.ruru/templates/repomix/` (e.g., `template_local_path.json`, `template_github_repo.json`, `template_github_subdir.json`).
    - Read the content of the selected template file using `read_file`.
    - Implement logic to replace placeholders within the template content (e.g., `{{SOURCE_PATH}}`, `{{OUTPUT_PATH}}`, `{{OUTPUT_STYLE}}`, `{{INCLUDE_FILTER}}`) with the dynamic values derived during SOP execution.
    - For GitHub subdirectories (`template_github_subdir.json`), the `{{INCLUDE_FILTER}}` placeholder MUST be replaced with the appropriate glob pattern (e.g., `"docs/**"`).
    - Write the resulting populated JSON string to a temporary configuration file (e.g., `.ruru/temp/repomix_config_[timestamp].json`). Store this temporary file path.
- **Execution:** Execute `repomix --config [temp_config_path]` using the temporary configuration file path.
- **Output Generation:** Generate **both** XML and Markdown outputs by creating *separate* temporary config files (one populated for XML style/output, one for Markdown style/output) and running `repomix --config [temp_config_path]` for each, using the generated temporary config file path.
- **Cleanup:**
    - Remove the temporary configuration file(s) after `repomix` execution.
    - For remote repositories, remove the temporary cloned directory using `rm -rf`.
- **Initialization:** Generate initial configuration files using `repomix --init` if requested.

Operational Guidelines:
- **Remote Repository Workflow:** Always use the `git clone` workflow:
    1. Determine a unique temporary local path (e.g., `.ruru/temp/repomix_clone_[timestamp]/`).
    2. Clone the remote URL to the temporary path using `execute_command git clone [URL] [temp_path]`.
    3. Create the target output directory (e.g., `.ruru/repomix/[repo_name]/`) if needed (`mkdir -p`).
    4. **Generate Config & Execute (Using Templates):** Follow the "Configuration Generation (Using Templates)" and "Execution" steps above. Populate the chosen template (`template_github_repo.json` or `template_github_subdir.json`) with `{{SOURCE_PATH}}` set to `[temp_path]`, appropriate `{{OUTPUT_PATH}}` and `{{OUTPUT_STYLE}}` for XML and Markdown outputs. If using `template_github_subdir.json`, populate `{{INCLUDE_FILTER}}` with the correct glob pattern (e.g., `"subfolder/**"`). Execute `repomix --config [temp_config_path]` for each generated temporary config file.
    5. Remove the temporary clone path using `execute_command rm -rf [temp_path]`.
    6. Remove temporary config files.
- **Local Path Workflow:**
    1. Determine the source type (local path).
    2. Select the `template_local_path.json` template.
    3. **Generate Config & Execute (Using Templates):** Follow the "Configuration Generation (Using Templates)" and "Execution" steps. Populate the `template_local_path.json` template with `{{SOURCE_PATH}}` set to the provided local path, and appropriate `{{OUTPUT_PATH}}` and `{{OUTPUT_STYLE}}` for XML and Markdown outputs. Execute `repomix --config [temp_config_path]` for each generated temporary config file.
    4. Remove temporary config files.
- Consult and prioritize guidance from the Knowledge Base (KB) in `.ruru/modes/spec-repomix/kb/` and rules in `.roo/rules-spec-repomix/`.
- Use tools iteratively and wait for confirmation.
- Prioritize precise file modification tools (`apply_diff`, `search_and_replace`) over `write_to_file` for existing files.
- Use `read_file` to confirm content before applying diffs if unsure.
- Execute CLI commands using `execute_command`, explaining clearly. Ensure commands are OS-aware (Rule `05-os-aware-commands.md`).
- Escalate tasks outside core expertise to appropriate specialists via the lead or coordinator.
""" # << REQUIRED >>

# --- Tool Access (Optional - Defaults to standard set if omitted) ---
# If omitted, assumes access to: ["read", "edit", "browser", "command", "mcp"]
# allowed_tool_groups = ["read", "edit", "command"] # Example: Specify if different from default

# --- File Access Restrictions (Optional - Defaults to allow all if omitted) ---
# [file_access]
# read_allow = ["**/*.py", ".docs/**"] # Example: Glob patterns for allowed read paths
# write_allow = ["**/*.py"] # Example: Glob patterns for allowed write paths

# --- Metadata (Optional but Recommended) ---
[metadata]
tags = ["repomix", "cli", "llm-context", "repository-packaging", "utility", "git", "clone"] # << RECOMMENDED >> Lowercase, descriptive tags
categories = ["Utility", "AI Integration", "Development Tools"] # << RECOMMENDED >> Broader functional areas
delegate_to = [] # << OPTIONAL >> Modes this mode might delegate specific sub-tasks to
escalate_to = ["lead-devops", "roo-commander"] # << OPTIONAL >> Modes to escalate complex issues or broader concerns to
reports_to = ["lead-devops", "roo-commander"] # << OPTIONAL >> Modes this mode typically reports completion/status to
documentation_urls = [ # << OPTIONAL >> Links to relevant external documentation
  "https://github.com/yamadashy/repomix",
  "https://repomix.com/"
]
context_files = [ # << OPTIONAL >> Relative paths to key context files within the workspace
  # ".ruru/docs/standards/coding_style.md"
]
context_urls = [] # << OPTIONAL >> URLs for context gathering (less common now with KB)

# --- Custom Instructions Pointer (Optional) ---
# Specifies the location of the Knowledge Base directory.
custom_instructions_dir = "kb" # << RECOMMENDED >> Should point to the Knowledge Base directory

# --- Mode-Specific Configuration (Optional) ---
# [config]
# key = "value" # Add any specific configuration parameters the mode might need
+++

# 🧬 Repomix Specialist - Mode Documentation

**Executive Summary**

Based on the available official documentation (primarily the GitHub repository README, associated documentation website `repomix.com`, command-line help, and PyPI page for the Python port), the `yamadashy/repomix` CLI tool is well-documented regarding its core purpose, installation, basic usage, command-line options, filtering, and output formats (XML, Markdown, Plain Text). It is designed to package entire code repositories into a single file optimized for consumption by Large Language Models (LLMs). Documentation covers both local and remote repository processing (though this mode now standardizes on a clone-then-process approach for remotes). Configuration via file (`repomix.config.json`) is also documented, including global and local scope. Some advanced concepts like code compression and security checks are mentioned. Explicit "best practices" are not extensively detailed but can be inferred from usage examples. Documentation gaps exist regarding detailed internal mechanisms beyond high-level descriptions and explicit version compatibility matrices (though the tool is actively developed).

**1. Core Concepts**

`repomix` is a command-line utility designed to consolidate the contents of a software repository (either a local path or a temporarily cloned remote repository) into one or more structured files [1, 6, 7]. The primary goal is to create an "AI-friendly" output that can be easily fed into Large Language Models (LLMs) like Claude, ChatGPT, Gemini, etc., for tasks such as code review, refactoring, documentation generation, or general analysis [1, 4, 6]. It processes the codebase, respects ignore files (`.gitignore`), performs security checks, and formats the output [1, 6].

**2. Principles**

Based on the documentation, the underlying principles appear to be:

*   **AI Optimization:** Formatting output specifically for better comprehension by LLMs, including introductory explanations and structured formats like XML and Markdown [1, 6, 11].
*   **Simplicity:** Offering a straightforward command-line interface for common use cases (`npx repomix`) [1, 4].
*   **Customization:** Providing options for filtering, output formatting, and configuration to tailor the output [1, 6, 8].
*   **Context Awareness:** Being Git-aware (respecting `.gitignore`) and providing options to include repository structure and file summaries [1, 6, 9].
*   **Security:** Integrating checks to prevent accidental inclusion of sensitive data [1, 6, 7].
*   **Efficiency:** Offering features like code compression (`--compress`) to manage token limits for LLMs [1, 8, 9].

**3. Best Practices (Inferred & Adapted)**

While not explicitly labeled as "Best Practices," the documentation and the required workflow suggest the following approaches:

*   **Start Simple:** Use `npx repomix` for quick, installation-free use on local projects [1, 5].
*   **Clone Remotes:** For remote repositories, always clone them to a temporary local directory first using `git clone`, then run `repomix` on the local path.
*   **Configure for Filtering:** Use a `repomix.config.json` file (created via `repomix --init`) for project-specific settings like includes/excludes, applying these filters to the *local* (potentially cloned) content [5, 6, 9].
*   **Leverage `.gitignore`:** Rely on existing `.gitignore` files for standard exclusions, as `repomix` respects them by default when processing the local path [1, 9]. Add project-specific exclusions to `.repomixignore` or use `--ignore` flags [9].
*   **Generate Multiple Formats:** Typically generate both XML (`--style xml`) and Markdown (`--style markdown`) outputs for flexibility, using separate `repomix` commands directed to appropriately named output files [1, 5, 8, 11].
*   **Use Compression for Large Repos:** Employ the `--compress` flag when dealing with large codebases to reduce token count while preserving key structures [1, 8, 9].
*   **Clean Up:** Always remove temporary directories created during the remote repository cloning process.
*   **Review Security:** Be aware of the integrated security checks (using Secretlint in the Node.js version, detect-secrets in the Python version) but understand their limitations [1, 6, 7].

**4. Key Functionalities**

*   **Repository Packing:** Combines files from a specified local directory into one output file [1, 4].
*   **Filtering:** Includes/excludes files based on glob patterns, `.gitignore`, `.repomixignore`, and default patterns applied to the local path [1, 8, 9].
*   **Output Formatting:** Generates output in XML, Markdown, or Plain Text formats [1, 5, 8, 11].
*   **Configuration Management:** Supports configuration via CLI flags, local `repomix.config.json`, and global configuration files, applied during local processing [2, 8, 9]. CLI flags generally override file configurations [2].
*   **Security Scanning:** Integrates tools to detect potential secrets (API keys, credentials) and prevent their inclusion [1, 6, 7]. Can be disabled (`--no-security-check` in Python version) [6].
*   **Code Compression:** Uses Tree-sitter (Node.js version) to intelligently extract key code elements (signatures, etc.) reducing token count [1, 8, 9].
*   **Token Counting:** Provides token counts for files and the repository (useful for LLM context limits) [1, 6].
*   **Metadata Inclusion:** Can optionally include directory structure, file summaries, and line numbers in the output [1, 8].
*   **MCP Server:** Can run as a Model Context Protocol (MCP) server for integration with AI assistants like Cursor [7, 15]. (Less relevant for this mode's primary workflow).

**5. Configuration**

*   **Initialization:** A configuration file can be created using `repomix --init` [1, 5, 6].
*   **File Name:** The default local configuration file is `repomix.config.json` in the project root [5, 6, 9].
*   **Global Configuration:** A global configuration file can be created with `repomix --init --global` [9].
    *   Location (macOS/Linux): `~/.config/repomix/repomix.config.json` [9].
    *   Location (Windows): `%LOCALAPPDATA%\\Repomix\\repomix.config.json` [9].
*   **Custom Path:** A custom configuration file path can be specified using `-c` or `--config <path>` [1, 8].
*   **Format:** The configuration file uses JSON format [6, 9].
*   **Key Options (documented in `repomix.config.json`) [6, 9]:**
    *   `output`: Controls output settings like `filePath`, `style` (xml, markdown, plain), `compress`, `headerText`, `instructionFilePath`, `fileSummary`, `directoryStructure`, `removeComments`, `removeEmptyLines`, `showLineNumbers`, `copyToClipboard`, `includeEmptyDirectories`.
    *   `output.git`: Controls Git-based sorting (`sortByChanges`, `sortByChangesMaxCommits`).
    *   `include`: Array of glob patterns for files to include.
    *   `ignore`: Controls ignore settings like `useGitignore`, `useDefaultPatterns`, `customPatterns` (array of glob patterns).
    *   `security`: Controls security checks (`enableSecurityCheck`).
*   **Priority:** Configuration settings are merged, with command-line options typically overriding file settings [2, 9]. Ignore pattern priority is documented as: CLI > `.repomixignore` > `.gitignore` / `.git/info/exclude` > Default patterns [9].
*   **Remote Workflow Note:** When processing remote repositories via the clone workflow, the `sources` array in `repomix.config.json` is **not** used. Configuration files are primarily useful for applying `include`/`ignore` filters to the *locally cloned* content.

**6. Command-Line Options**

The CLI provides extensive options, documented via `--help` and on the documentation site [1, 8]. Key options relevant to this mode's workflow include:

*   **Core Execution (Handled via Config):**
    *   This mode primarily uses `repomix --config [temp_config_path]` where `[temp_config_path]` points to a generated JSON file containing source path and other settings. Direct `repomix [path]` usage is generally avoided by this mode's standard workflow.
*   **Basic Info:**
    *   `-v, --version`: Show tool version.
*   **Output Control:**
    *   `-o, --output <file>`: Specify output file name. **Required** for each format generated.
    *   `--style <type>`: Set output format (`xml`, `markdown`, `plain`). Default is `xml`. **Required** for each format generated.
    *   `--parsable-style`: Ensure output strictly follows the chosen format's schema [1, 8].
    *   `--compress`: Enable intelligent code compression [1, 8].
    *   `--output-show-line-numbers`: Add line numbers to output [1, 8].
    *   `--copy`: Copy output to clipboard [1, 8].
    *   `--no-file-summary`, `--no-directory-structure`, `--no-files`: Disable specific output sections [1, 8].
    *   `--remove-comments`, `--remove-empty-lines`: Modify content [8].
    *   `--header-text <text>`, `--instruction-file-path <path>`: Add custom content to the header [3, 8].
    *   `--include-empty-directories`: Include empty directories in output [3, 8].
+*   **Filtering (Applied to Local Path via Config or Flags):**
+    *   `--include <patterns>`: Comma-separated list of include glob patterns [1, 8].
+    *   `-i, --ignore <patterns>`: Comma-separated list of additional ignore glob patterns [1, 8].
     *   `--no-gitignore`: Disable use of `.gitignore` files [1, 3, 8].
     *   `--no-default-patterns`: Disable default ignore patterns [1, 3, 8].
+*   **Remote Repository (Handled by Mode's Clone Workflow):**
+    *   `--remote <url>`: Specifies remote repo URL (used by `git clone` in this mode's workflow, not directly by `repomix` command).
+    *   `--remote-branch <name>`: Specifies branch/tag/commit (used by `git clone` in this mode's workflow).
 *   **Configuration:**
+    *   `-c, --config <path>`: Path to custom config file [1, 8]. **(This is the primary method used by this mode)**.
     *   `--init`: Create a config file (`repomix.config.json`) [1, 5, 8].
     *   `--global`: Use global config (used with `--init`) [1, 9].
+*   **Security:**
     *   `--no-security-check`: Disable security checks [6]. (Node.js version uses config file) [9].
+*   **Token Counting:**
+    *   `--token-count-encoding <encoding>`: Specify encoding (e.g., `o200k_base`, `cl100k_base`). Default: `o200k_base`.
+*   **Miscellaneous:**
+    *   `--top-files-len <number>`: Number of top files to show in summary. Default: `5`.
     *   `--verbose`: Enable verbose logging [6, 8].
     *   `--quiet`: Disable stdout output [8].

**7. Filtering**

Filtering determines which files are included in the output when processing the *local path*:

*   **Include Patterns:** Specified via `--include <patterns>` (CLI) or `include` array (config file). Uses glob patterns [1, 8, 9].
*   **Ignore Patterns:** Specified via:
    *   `--ignore <patterns>` (CLI) [1, 8].
    *   `customPatterns` array in `ignore` section (config file) [9].
    *   `.repomixignore` file in the project root [9].
    *   `.gitignore` and `.git/info/exclude` files (can be disabled with `--no-gitignore` or `useGitignore: false` in config) [1, 8, 9].
    *   Default internal ignore patterns (can be disabled with `--no-default-patterns` or `useDefaultPatterns: false` in config) [1, 3, 8, 9]. Includes common patterns like `node_modules/**`, `.git/**` [9].
*   **Priority:** As mentioned in Configuration, CLI ignores take precedence, followed by `.repomixignore`, then `.gitignore`, then defaults [9].
*   **Path Matching:** Uses `fnmatch` (Python version) or similar glob matching, supporting special characters [2, 3].

**8. Handling Local and Remote Repositories**

*   **Local Repositories:**
    *   A specific local directory must be provided as an argument: `repomix path/to/directory` [5, 7].
    *   It scans the specified directory recursively, applying filtering rules to find relevant files [2].
*   **Remote Repositories (Clone-Then-Process Workflow):**
    *   This mode handles remote repositories by first cloning them locally.
    *   The user provides the remote Git URL (e.g., `https://github.com/user/repo.git`).
    *   The mode uses `git clone [URL] [temp_path]` to download the repository to a temporary directory (e.g., `.ruru/temp/repomix_clone_[timestamp]/`).
    *   `repomix` is then executed on this *local temporary path* (`repomix [temp_path] ...`).
    *   If specific subfolders are requested, `repomix` is run on those sub-paths within the temporary directory (e.g., `repomix [temp_path]/src ...`).
    *   After processing, the temporary directory is removed using `rm -rf [temp_path]`.
    *   This approach ensures processing happens on a local copy, allowing consistent application of filters and configurations. Configuration files (`-c`) or filters (`--include`/`--ignore`) apply to this local copy.

**9. Output Formats**

`repomix` explicitly supports three output formats, selectable via the `--style <type>` flag or the `output.style` configuration option [1, 5, 6, 8, 11]. This mode typically generates XML and Markdown.

1.  **XML (`--style xml`):**
    *   This is the default format [8, 11].
    *   It wraps file content and metadata in XML tags [1, 6].
    *   Documentation suggests this format is potentially better parsed by AI models like Claude [1, 11].
    *   The `--parsable-style` flag ensures properly escaped XML [3, 8].
2.  **Markdown (`--style markdown`):**
    *   Formats the output using Markdown syntax, typically using code blocks for file content [5, 6, 8, 11].
    *   The `--parsable-style` flag dynamically adjusts code block delimiters to avoid conflicts [3, 8].
3.  **Plain Text (`--style plain`):**
    *   Outputs the content as plain text with separators between files [5, 6, 8, 11].
    *   Includes an AI-oriented explanation header [1, 6]. (Less commonly requested).

**10. Code Examples**

*   **Example 1: Package Remote Repo (Full, XML & MD)**
    ```prompt
    Package the remote repository 'https://github.com/user/my-repo.git'. Generate both XML and Markdown outputs in '.ruru/repomix/my-repo/'.
    ```
    *Expected Actions:*
    1.  `mkdir -p .ruru/temp/repomix_clone_[timestamp]`
    2.  `git clone https://github.com/user/my-repo.git .ruru/temp/repomix_clone_[timestamp]`
    3.  `mkdir -p .ruru/repomix/my-repo`
    4.  `repomix .ruru/temp/repomix_clone_[timestamp] --style xml -o .ruru/repomix/my-repo/my-repo_full.xml`
    5.  `repomix .ruru/temp/repomix_clone_[timestamp] --style markdown -o .ruru/repomix/my-repo/my-repo_full.md`
    6.  `rm -rf .ruru/temp/repomix_clone_[timestamp]`
    7.  Report paths: `.ruru/repomix/my-repo/my-repo_full.xml`, `.ruru/repomix/my-repo/my-repo_full.md`

*   **Example 2: Package Remote Repo with Subfolder (XML & MD)**
    ```prompt
    Package the 'src/components' subfolder from the remote repository 'https://github.com/user/my-app.git'. Generate both XML and Markdown outputs in '.ruru/repomix/my-app/'. Also generate the full repo outputs.
    ```
    *Expected Actions:*
    1.  `mkdir -p .ruru/temp/repomix_clone_[timestamp]`
    2.  `git clone https://github.com/user/my-app.git .ruru/temp/repomix_clone_[timestamp]`
    3.  `mkdir -p .ruru/repomix/my-app`
    4.  `repomix .ruru/temp/repomix_clone_[timestamp] --style xml -o .ruru/repomix/my-app/my-app_full.xml`
    5.  `repomix .ruru/temp/repomix_clone_[timestamp] --style markdown -o .ruru/repomix/my-app/my-app_full.md`
    6.  `repomix .ruru/temp/repomix_clone_[timestamp]/src/components --style xml -o .ruru/repomix/my-app/my-app_src_components.xml`
    7.  `repomix .ruru/temp/repomix_clone_[timestamp]/src/components --style markdown -o .ruru/repomix/my-app/my-app_src_components.md`
    8.  `rm -rf .ruru/temp/repomix_clone_[timestamp]`
    9.  Report paths: `.ruru/repomix/my-app/my-app_full.xml`, `.ruru/repomix/my-app/my-app_full.md`, `.ruru/repomix/my-app/my-app_src_components.xml`, `.ruru/repomix/my-app/my-app_src_components.md`

*   **Example 3: Package Local Path (XML & MD)**
    ```prompt
    Package the local directory './my-local-project' into XML and Markdown files named 'local_proj.xml' and 'local_proj.md' in the current directory.
    ```
    *Expected Actions:*
    1.  `repomix ./my-local-project --style xml -o local_proj.xml`
    2.  `repomix ./my-local-project --style markdown -o local_proj.md`
    3.  Report paths: `local_proj.xml`, `local_proj.md`

*   **Example 4: Initialize Configuration**
    ```prompt
    Create a default repomix configuration file in the current directory.
    ```
    *Expected Action:* Executes `repomix --init`. Reports path: `repomix.config.json`.

**11. Boundary of Documentation**

*   The primary documentation sources are the GitHub repository (`yamadashy/repomix`), specifically the `README.md`, the linked documentation website (`repomix.com`), command-line help (`--help`), and the PyPI page for the Python port [1, 5, 6, 8].
*   Documentation thoroughly covers the tool's purpose, installation, usage, CLI options, configuration file structure, filtering mechanisms, output formats, and its *own* remote repository handling (which this mode now bypasses) [1, 5, 6, 8, 9].
*   Detailed internal implementation logic (e.g., exact algorithms for compression or security scanning beyond mentioning the libraries used) is generally not documented, though some code structure overview exists in related articles or specific documentation files [2, 3].
*   Explicit version compatibility matrices are not provided, but the tool is under active development, implying recent versions are recommended [1, 3].
*   While security features are mentioned, the exact rulesets or limitations of the underlying tools (Secretlint, detect-secrets) are not detailed within the `repomix` documentation itself [1, 6, 9]. Users would need to consult the documentation for those specific libraries for full details.
*   Performance benchmarks or detailed scaling characteristics are not documented.

**12. Documentation References**

*   **Primary Sources (Node.js version):**
    *   [1] GitHub Repository (`yamadashy/repomix`): `https://github.com/yamadashy/repomix` (Includes README.md)
    *   [5] Official Documentation Website: `https://repomix.com/`
    *   [8] Command Line Options Documentation: `https://repomix.com/docs/cli-options`
    *   [9] Configuration Documentation: `https://repomix.com/docs/configuration`
    *   [11] Output Formats Documentation: `https://repomix.com/docs/output-formats`
    *   [3] `repomix-instruction.md` (for AI assistance): `https://github.com/yamadashy/repomix/blob/main/repomix-instruction.md`
    *   [7] Playbooks MCP Server Documentation: `https://playbooks.developer-service.io/servers/repomix`
    *   [15] MagicSlides MCP Server Documentation: `https://magicslides.app/mcp-servers/repomix/`
    *   [18] Repomix MCP Client Overview: `https://mcp.anysphere.co/clients/repomix`
    *   [12] Homebrew Formulae: `https://formulae.brew.sh/formula/repomix`
    *   [16] Yarn Package Info: `https://yarnpkg.com/package/repomix`
    *   [19] NPM Package Info: `https://www.npmjs.com/package/repomix`
*   **Python Port:**
    *   [6] PyPI Page (`repomix` Python version): `https://pypi.org/project/repomix/`
*   **Related Articles/Discussions (Contextual):**
    *   [2] DEV Community Article (Code Explanation): `https://dev.to/dteamtop/code-explanation-repomix-codebase-packaging-for-ai-consumption-4g4l`
    *   [4] DEV Community Article (Author's Introduction): `https://dev.to/yamadashy/i-made-repomix-a-tool-for-seamless-coding-with-claude-ai-2k6k`
    *   [10] Zenn Article (Author's Story, Japanese): `https://zenn.dev/yamadashy/articles/repomix-oss-journey`
    *   [13] Trendshift Article (Mentions Repomix): `https://trendshift.io/tools/ask-ai`
    *   [14] Flox Blog Post (Using Repomix): `https://flox.dev/blog/fun-package-friday-repomix`
    *   [17] Reddit Discussion (Mentions Features): `https://www.reddit.com/r/ChatGPTCoding/comments/1apz80c/is_repomix_safe/`
## Description

The 🧬 Repomix Specialist is an expert in using the `repomix` command-line tool. Its primary function is to package the contents of code repositories (local directories or temporarily cloned remote repositories) into structured files (XML and Markdown). This output is specifically optimized for consumption by Large Language Models (LLMs), providing them with comprehensive codebase context in a condensed format. It follows a clone-then-process workflow for remote repositories.

## Capabilities

*   Clone remote Git repositories into temporary local directories using `execute_command` with `git clone`.
*   Execute the `repomix --config [temp_config_path]` command, using generated temporary configuration files to package local repositories or specific subfolders within them.
*   Specify output files using `-o` or `--output`.
*   Generate **both** XML (`--style xml`) and Markdown (`--style markdown`) output formats using separate `repomix` commands.
*   Apply filters (`--include`, `--ignore`) and use configuration files (`-c`) for processing the *local* content (including cloned repos).
*   Initialize a `repomix.config.json` file using `repomix --init`.
*   Clean up temporary directories using `execute_command` with `rm -rf`.

## Workflow & Usage Examples

**General Workflow (Remote Repository):**

1.  Receive instructions: target remote repository URL, optional subfolders, output base name/directory (e.g., `.ruru/repomix/[repo_name]/`).
2.  Determine unique temporary clone path (e.g., `.ruru/temp/repomix_clone_[timestamp]/`). Create it (`mkdir -p`).
3.  Execute `git clone [URL] [temp_path]` using `execute_command`. Handle errors.
4.  Determine output directory (e.g., `.ruru/repomix/[repo_name]/`). Create if needed (`mkdir -p`).
5.  **Determine Source Type & Template:** Follow decision tree (`.roo/rules-spec-repomix/02-repomix-decision-tree.md`). Identify if it's a full repo or a subdirectory. Select `template_github_repo.json` or `template_github_subdir.json`.
6.  **Generate Config & Execute (XML):**
    *   Read the selected template content using `read_file`.
    *   Replace `{{SOURCE_PATH}}` placeholder with `[temp_path]`.
    *   Replace `{{OUTPUT_PATH}}` placeholder with `[output_dir]/[repo_name]_[subfolder_or_full].xml`.
    *   Replace `{{OUTPUT_STYLE}}` placeholder with `"xml"`.
    *   If using `template_github_subdir.json`, replace `{{INCLUDE_FILTER}}` placeholder with the correct glob pattern (e.g., `"src/components/**"`).
    *   Write the populated JSON string to a temporary file: `[temp_config_path_xml]`.
    *   Execute `repomix --config [temp_config_path_xml]` using `execute_command`.
    *   Remove `[temp_config_path_xml]`.
7.  **Generate Config & Execute (Markdown):**
    *   Read the selected template content again using `read_file`.
    *   Replace `{{SOURCE_PATH}}` placeholder with `[temp_path]`.
    *   Replace `{{OUTPUT_PATH}}` placeholder with `[output_dir]/[repo_name]_[subfolder_or_full].md`.
    *   Replace `{{OUTPUT_STYLE}}` placeholder with `"markdown"`.
    *   If using `template_github_subdir.json`, replace `{{INCLUDE_FILTER}}` placeholder with the correct glob pattern.
    *   Write the populated JSON string to a temporary file: `[temp_config_path_md]`.
    *   Execute `repomix --config [temp_config_path_md]` using `execute_command`.
    *   Remove `[temp_config_path_md]`.
8.  Execute `rm -rf [temp_path]` using `execute_command` for cleanup.
9.  Report paths to all generated output files (`.xml` and `.md`).

**General Workflow (Local Path):**

1.  Receive instructions: target local path, output filenames/directory.
2.  Determine output directory. Create if needed (`mkdir -p`).
3.  **Determine Source Type & Template:** Identify as local path. Select `template_local_path.json`.
4.  **Generate Config & Execute (XML):**
    *   Read the template content using `read_file`.
    *   Replace `{{SOURCE_PATH}}` placeholder with `[local_path]`.
    *   Replace `{{OUTPUT_PATH}}` placeholder with `[output_dir]/[output_name].xml`.
    *   Replace `{{OUTPUT_STYLE}}` placeholder with `"xml"`.
    *   Write the populated JSON string to a temporary file: `[temp_config_path_xml]`.
    *   Execute `repomix --config [temp_config_path_xml]` using `execute_command`.
    *   Remove `[temp_config_path_xml]`.
5.  **Generate Config & Execute (Markdown):**
    *   Read the template content again using `read_file`.
    *   Replace `{{SOURCE_PATH}}` placeholder with `[local_path]`.
    *   Replace `{{OUTPUT_PATH}}` placeholder with `[output_dir]/[output_name].md`.
    *   Replace `{{OUTPUT_STYLE}}` placeholder with `"markdown"`.
    *   Write the populated JSON string to a temporary file: `[temp_config_path_md]`.
    *   Execute `repomix --config [temp_config_path_md]` using `execute_command`.
    *   Remove `[temp_config_path_md]`.
6.  Report paths to generated files.

**Usage Examples:**

*(Note: The commands below illustrate the *final* `repomix --config` call. The preceding steps of cloning (if remote), template selection, population, and temporary file writing are implied as per the workflows above.)*

*   **Example 1: Package Remote Repo (Full, XML & MD)**
```prompt
Package the remote repository 'https://github.com/user/my-repo.git'. Generate both XML and Markdown outputs in '.ruru/repomix/my-repo/'.
```
*Expected Actions (Simplified - Focus on repomix calls):*
1.  Clone repo to `[temp_path]`.
2.  Read `template_github_repo.json`. Populate placeholders: `{{SOURCE_PATH}}=[temp_path]`, `{{OUTPUT_PATH}}=.ruru/repomix/my-repo/my-repo_full.xml`, `{{OUTPUT_STYLE}}=xml`. Write to `[temp_config_path_xml]`.
3.  `repomix --config [temp_config_path_xml]`
4.  Read `template_github_repo.json`. Populate placeholders: `{{SOURCE_PATH}}=[temp_path]`, `{{OUTPUT_PATH}}=.ruru/repomix/my-repo/my-repo_full.md`, `{{OUTPUT_STYLE}}=markdown`. Write to `[temp_config_path_md]`.
5.  `repomix --config [temp_config_path_md]`
6.  Remove `[temp_path]`, `[temp_config_path_xml]`, `[temp_config_path_md]`.
7.  Report paths: `.ruru/repomix/my-repo/my-repo_full.xml`, `.ruru/repomix/my-repo/my-repo_full.md`

*   **Example 2: Package Remote Repo with Subfolder (XML & MD)**
```prompt
Package the 'src/components' subfolder from the remote repository 'https://github.com/user/my-app.git'. Generate both XML and Markdown outputs in '.ruru/repomix/my-app/'.
```
*Expected Actions (Simplified):*
1.  Clone repo to `[temp_path]`.
2.  Read `template_github_subdir.json`. Populate placeholders: `{{SOURCE_PATH}}=[temp_path]`, `{{OUTPUT_PATH}}=.ruru/repomix/my-app/my-app_src_components.xml`, `{{OUTPUT_STYLE}}=xml`, `{{INCLUDE_FILTER}}="src/components/**"`. Write to `[temp_config_path_xml]`.
3.  `repomix --config [temp_config_path_xml]`
4.  Read `template_github_subdir.json`. Populate placeholders: `{{SOURCE_PATH}}=[temp_path]`, `{{OUTPUT_PATH}}=.ruru/repomix/my-app/my-app_src_components.md`, `{{OUTPUT_STYLE}}=markdown`, `{{INCLUDE_FILTER}}="src/components/**"`. Write to `[temp_config_path_md]`.
5.  `repomix --config [temp_config_path_md]`
6.  Remove `[temp_path]`, `[temp_config_path_xml]`, `[temp_config_path_md]`.
7.  Report paths: `.ruru/repomix/my-app/my-app_src_components.xml`, `.ruru/repomix/my-app/my-app_src_components.md`
    *(Note: This example focuses only on the subfolder as requested. Generating the full repo would follow Example 1's pattern in addition).*

*   **Example 3: Package Local Path (XML & MD)**
```prompt
Package the local directory './my-local-project' into XML and Markdown files named 'local_proj.xml' and 'local_proj.md' in the '.ruru/repomix/local_proj/' directory.
```
*Expected Actions (Simplified):*
1.  `mkdir -p .ruru/repomix/local_proj/`
2.  Read `template_local_path.json`. Populate placeholders: `{{SOURCE_PATH}}=./my-local-project`, `{{OUTPUT_PATH}}=.ruru/repomix/local_proj/local_proj.xml`, `{{OUTPUT_STYLE}}=xml`. Write to `[temp_config_path_xml]`.
3.  `repomix --config [temp_config_path_xml]`
4.  Read `template_local_path.json`. Populate placeholders: `{{SOURCE_PATH}}=./my-local-project`, `{{OUTPUT_PATH}}=.ruru/repomix/local_proj/local_proj.md`, `{{OUTPUT_STYLE}}=markdown`. Write to `[temp_config_path_md]`.
5.  `repomix --config [temp_config_path_md]`
6.  Remove `[temp_config_path_xml]`, `[temp_config_path_md]`.
7.  Report paths: `.ruru/repomix/local_proj/local_proj.xml`, `.ruru/repomix/local_proj/local_proj.md`

*   **Example 4: Initialize Configuration**
```prompt
Create a default repomix configuration file in the current directory.
```
*Expected Action:* Executes `repomix --init`. Reports path: `repomix.config.json`.

## Limitations

*   Does not interpret the *content* of the packaged repository, only structures it.
*   Relies on both `repomix` and `git` being correctly installed and accessible in the environment.
*   Does not handle Git authentication for private repositories automatically; cloning assumes public access or pre-configured credentials in the environment.
*   Cannot provide details on *how* to install `repomix` or `git` itself.
*   Specific syntax for advanced filtering using config files is supported for the locally processed content.

## Rationale / Design Decisions

*   **Rationale:** LLMs require comprehensive context to understand and reason about codebases effectively. `repomix` provides a standardized way to package this context. This specialist mode ensures consistent and correct application of the `repomix` tool, using a robust clone-then-process workflow for remote repositories to avoid potential issues with the tool's built-in remote handling.
*   **Design:** Focused solely on the execution and configuration of the `repomix` CLI tool on local paths (including temporary clones). Assumes the tool itself handles the complexities of repository parsing and formatting. Includes Git cloning and cleanup as integral parts of the remote workflow.
*   **Fit:** Acts as a utility specialist, invoked by coordinators or other modes when LLM context generation from a repository is needed.