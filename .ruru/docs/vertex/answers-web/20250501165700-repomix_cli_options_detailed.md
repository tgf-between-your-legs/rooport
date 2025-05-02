Okay, here is a comprehensive overview of the command-line options for the `repomix` CLI tool, based on the provided search results.

**Executive Summary**

Repomix is a CLI tool available in both Node.js and Python versions, designed to package code repositories into a single file optimized for AI language models [1, 3, 7, 12]. It offers numerous command-line options to control output format, file inclusion/exclusion, remote repository processing, code compression, and configuration [1, 5]. While both versions share core functionality, the Node.js version appears to have a more extensive set of documented CLI flags based on the search results [1, 5, 7, 12].

**Introduction**

Repomix (formerly known as Repopack [4]) helps developers feed entire codebases to Large Language Models (LLMs) like Claude, ChatGPT, Gemini, and others by consolidating project files into one structured output [1, 11]. It respects `.gitignore` rules, can perform security checks, count tokens, and even process remote repositories directly [1, 10, 11].

**Node.js vs. Python Versions**

The search results indicate two primary versions:

1.  **Node.js Version:** The original and seemingly more feature-rich version, actively developed on GitHub (yamadashy/repomix) [1, 2]. It uses Secretlint for security checks [10, 11, 13].
2.  **Python Version:** A port of the original tool, available on PyPI [7, 12]. It uses `detect-secrets` for security checks [12] and may have fewer CLI options exposed compared to the Node.js version, based on the documentation found [7, 12].

The following list focuses primarily on the **Node.js version** due to more detailed documentation in the search results [1, 5], with Python-specific details noted where available.

**Node.js `repomix` CLI Options**

The options are categorized based on the official documentation structure [5]:

**Basic Options**

*   `-v`, `--version`
    *   **Purpose:** Display the installed `repomix` tool version [5].
    *   **Syntax:** `repomix --version`

**Output Options**

*   `-o <file>`, `--output <file>`
    *   **Purpose:** Specify the name for the output file [1, 5].
    *   **Argument:** `<file>` - The desired path/filename for the output.
    *   **Default:** `repomix-output.txt` [5]. *Note: Some sources mention `repomix-output.xml` as the default [11, 13], while others mention `.txt` [2, 5, 10, 14, 25]. The official documentation page [5] lists `.txt` as the default, but it's wise to verify or explicitly set the filename.*
*   `--style <type>`
    *   **Purpose:** Define the format of the output file [1, 5].
    *   **Argument:** `<type>` - Can be `xml`, `markdown`, or `plain` [5, 19].
    *   **Default:** `xml` [5, 19]. XML is noted as potentially better for AI parsing, especially with models like Claude [19].
*   `--parsable-style`
    *   **Purpose:** Ensures the output strictly adheres to the chosen style's schema, including proper escaping (e.g., for XML) [5, 6]. This can increase token count [14].
    *   **Default:** `false` [5].
*   `--compress`
    *   **Purpose:** Enables intelligent code compression. It uses Tree-sitter to extract essential structures (like function signatures, class definitions) while removing implementation details, aiming to reduce token count while preserving structural context [1, 5, 8, 11]. This is considered an experimental feature [8].
    *   **Default:** `false` [9].
*   `--output-show-line-numbers`
    *   **Purpose:** Adds line numbers to the code snippets in the output file [1, 5].
    *   **Default:** `false` [5].
*   `--copy`
    *   **Purpose:** Copies the generated output content to the system clipboard in addition to writing the file [1, 5].
    *   **Default:** `false` [5].
*   `--no-file-summary`
    *   **Purpose:** Disables the inclusion of the file summary section (metadata, token counts) in the output [1, 5].
    *   **Default:** `true` (meaning the summary is disabled by default) [5].
*   `--no-directory-structure`
    *   **Purpose:** Disables the inclusion of the directory structure overview in the output [1, 5].
    *   **Default:** `true` (meaning the directory structure is disabled by default) [5].
*   `--no-files`
    *   **Purpose:** Disables the output of actual file contents, creating a metadata-only output (useful for analyzing structure without content) [5].
    *   **Default:** `true` (meaning file content output is disabled by default) [5]. *Note: This default seems counter-intuitive for the primary use case; users likely need to ensure this is implicitly or explicitly false if they want file contents.*
*   `--remove-comments`
    *   **Purpose:** Removes comments from the code in the output [5].
    *   **Default:** `false` [5].
*   `--remove-empty-lines`
    *   **Purpose:** Removes empty lines from the code in the output [5].
    *   **Default:** `false` [5].
*   `--header-text <text>`
    *   **Purpose:** Includes custom text provided by the user in the header section of the output file [5].
    *   **Argument:** `<text>` - The custom string to add.
*   `--instruction-file-path <path>`
    *   **Purpose:** Specifies a path to a file containing detailed custom instructions to be included in the output header, guiding the AI on how to process the content [5].
    *   **Argument:** `<path>` - Path to the instruction file.
*   `--include-empty-directories`
    *   **Purpose:** Includes empty directories in the directory structure output [5].
    *   **Default:** `false` [5].

**Filter Options**

*   `--include <patterns>`
    *   **Purpose:** Specifies glob patterns for files/directories to *include*. Only matching items will be processed [5, 11]. Multiple patterns are comma-separated [5].
    *   **Argument:** `<patterns>` - Comma-separated glob patterns (e.g., `"src/**/*.ts,*.md"`).
*   `-i <patterns>`, `--ignore <patterns>`
    *   **Purpose:** Specifies additional glob patterns for files/directories to *ignore* [1, 5, 11]. These are added to patterns from `.gitignore` and default ignores unless disabled. Multiple patterns are comma-separated [5].
    *   **Argument:** `<patterns>` - Comma-separated glob patterns (e.g., `"**/*.log,tmp/"`).
*   `--no-gitignore`
    *   **Purpose:** Disables the automatic use of ignore patterns found in `.gitignore` and `.git/info/exclude` files [1, 5, 11].
    *   **Default:** `false` (meaning `.gitignore` is used by default).
*   `--no-default-patterns`
    *   **Purpose:** Disables the use of Repomix's built-in default ignore patterns (e.g., `node_modules`, `.git`, common binary files) [1, 5, 11].
    *   **Default:** `false` (meaning default patterns are used by default).
*   **Ignore Pattern Priority:** CLI (`--ignore`) > `.repomixignore` file > `.gitignore` / `.git/info/exclude` > Default patterns [9, 11].

**Remote Repository Options**

*   `--remote <url>`
    *   **Purpose:** Processes a remote Git repository directly without needing a local clone [1, 5]. Supports full HTTPS URLs and GitHub shorthand (`user/repo`) [1].
    *   **Argument:** `<url>` - The URL or shorthand for the remote repository.
*   `--remote-branch <name>`
    *   **Purpose:** Specifies the branch name, tag, or commit hash to check out and process from the remote repository [1, 5].
    *   **Argument:** `<name>` - The branch, tag, or commit hash.
    *   **Default:** The repository's default branch [1, 5].

**Configuration Options**

*   `-c <path>`, `--config <path>`
    *   **Purpose:** Specifies the path to a custom configuration file (`repomix.config.json`) to load settings from [1, 5]. CLI options override config file settings [9].
    *   **Argument:** `<path>` - Path to the configuration file.
*   `--init`
    *   **Purpose:** Creates a default `repomix.config.json` configuration file in the current directory [1, 5].
*   `--global`
    *   **Purpose:** Used with `--init` to create or manage the global configuration file instead of a local one [1, 5]. Global config is located in a platform-specific user config directory (e.g., `~/.config/repomix/repomix.config.json` on Linux/macOS) [9].

**Security Options**

*   `--no-security-check`
    *   **Purpose:** Disables the built-in security check (using Secretlint) which scans for potential secrets like API keys before including files in the output [1, 5].
    *   **Default:** `true` (meaning the security check is disabled by default) [5]. *Users concerned about secrets should ensure this is false or configure it via the config file.*

**Token Count Options**

*   `--token-count-encoding <encoding>`
    *   **Purpose:** Specifies the encoding model to use for token counting via OpenAI's `tiktoken` library (e.g., `o200k_base` for GPT-4o, `cl100k_base` for GPT-4/3.5) [1, 5].
    *   **Argument:** `<encoding>` - The name of the tiktoken encoding.
    *   **Default:** `o200k_base` [5].

**MCP Options**

*   `--mcp`
    *   **Purpose:** Runs Repomix as a Model Context Protocol (MCP) server, allowing compatible AI assistants (like Claude via extensions) to interact with the tool programmatically to pack local or remote repositories [1, 15, 21]. This is considered an experimental feature [21].

**Other Options**

*   `--top-files-len <number>`
    *   **Purpose:** Specifies the number of top files (by character/token count) to display in the summary output [1, 5].
    *   **Argument:** `<number>` - The number of files to show.
    *   **Default:** `5` [5].
*   `--verbose`
    *   **Purpose:** Enables verbose logging output, showing more details about the process [1, 5].
*   `--quiet`
    *   **Purpose:** Suppresses all output to stdout, running silently except for errors [1, 5].

**Python `repomix` CLI Options**

Based on the PyPI page and Python version's GitHub README [7, 12]:

*   `[directory]`
    *   **Purpose:** Specifies the target directory to process.
    *   **Argument:** `<directory>` - Path to the directory.
    *   **Default:** Current working directory.
*   `-v`, `--version`
    *   **Purpose:** Show the tool version.
*   `-o <file>`, `--output <file>`
    *   **Purpose:** Specify the output file name.
    *   **Default:** `repomix-output.md` [7].
*   `--style <style>`
    *   **Purpose:** Specify the output style.
    *   **Argument:** `<style>` - Options likely include `plain`, `xml`, `markdown` [12] (similar to Node.js version).
*   `--remote <url>`
    *   **Purpose:** Process a remote Git repository.
*   `--remote-branch <name>`
    *   **Purpose:** Specify the remote branch, tag, or commit hash.
*   `--init`
    *   **Purpose:** Initialize a local `repomix.config.json` file.
*   `--global`
    *   **Purpose:** Use with `--init` to manage the global configuration file.

**Examples (Node.js Version)**

*   **Basic Usage (process current directory):**
    ```bash
    npx repomix
    # or if installed globally
    repomix
    ```
    *(Generates default output, e.g., `repomix-output.txt` or `repomix-output.xml`)* [5, 10, 11]

*   **Specify Output File and Style:**
    ```bash
    repomix -o my_project.md --style markdown
    ```
    [1, 5]

*   **Include Specific Files and Ignore Others:**
    ```bash
    repomix --include "src/**/*.js,docs/**/*.md" -i "**/node_modules/**,*.log,build/"
    ```
    [5, 10, 11]

*   **Process a Remote GitHub Repository (specific branch):**
    ```bash
    repomix --remote yamadashy/repomix --remote-branch main
    ```
    [1, 5]

*   **Process Remote Repository using Full URL:**
    ```bash
    repomix --remote https://github.com/yamadashy/repomix/tree/develop
    ```
    [1, 10]

*   **Enable Code Compression:**
    ```bash
    repomix --compress
    ```
    [5, 8]

*   **Compress a Remote Repository:**
    ```bash
    repomix --remote user/repo --compress
    ```
    [8]

*   **Initialize Configuration File:**
    ```bash
    repomix --init
    ```
    [1, 5, 10]

**Sources and Limitations**

*   **Sources:** Information is primarily drawn from the official `repomix` GitHub repository (Node.js version) [1, 6, 11], the official documentation website [5, 8, 9, 19, 20, 21], the Python version's PyPI page and GitHub repository [7, 12], DEV Community articles [2, 3], and other technical blogs/forums [4, 10, 16, 17, 25].
*   **Node.js Default Output File:** There is conflicting information regarding the default output filename for the Node.js version. The official command-line options documentation [5] and several examples [2, 10, 14, 25] state `repomix-output.txt`, while the main README [11], other examples [1, 13], and the default style being `xml` [5, 19] suggest `repomix-output.xml`. Users should verify the default or explicitly set the output file using `-o`.
*   **Python Version Documentation:** The search results provided less detailed CLI documentation for the Python version compared to the Node.js version. The Python version might have more options configurable via its `repomix.config.json` file [7, 12].
*   **Experimental Features:** Features like Code Compression (`--compress`) [8] and the MCP Server (`--mcp`) [15, 21] are noted as experimental and may change.
*   **`--no-files` Default:** The default value `true` for `--no-files` [5] seems unusual for the tool's main purpose (packaging file content). Users should be aware of this and may need to ensure file contents are included, possibly by the flag being implicitly false when not specified or by setting it via config.