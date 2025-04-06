# SOP: Generating Condensed Context Index for Mode Instructions v2.1

**Objective:** To instruct an AI mode (typically `technical-writer`) to generate a dense, structured, and informative summary (Condensed Context Index) from potentially large or multi-file technical documentation sources (provided as file paths, directory paths, or URLs). This index will be embedded into the `customInstructions` of a specialist Roo Code mode to provide essential baseline knowledge about a specific framework, library, or technology, improving its performance and robustness, especially when direct access to the full documentation (via RAG or fetching) is unavailable or fails.

**Target Audience:** AI Mode (e.g., `technical-writer`) executing this SOP.

**Principles:**

1.  **AI-Centric Context:** Structure and word the index for easy parsing and understanding by an LLM acting as a specialist mode. Prioritize keywords, core concepts, API signatures, configuration patterns, relationships, and common usage examples/pitfalls.
2.  **Density & Conciseness:** Maximize relevant information while minimizing token count. Use structured formats (lists, code blocks). Avoid verbose explanations; focus on factual summaries and keywords.
3.  **Structure Reflection:** Mirror the logical organization of the source documentation where possible (e.g., main sections, key APIs, configuration). If analyzing multiple files, synthesize a logical structure.
4.  **Key Information Prioritization:** Focus on foundational concepts, frequently used APIs/components/classes, critical configuration aspects, common pitfalls/solutions, and essential best practices mentioned across the source(s).
5.  **Actionability:** Provide information that helps the specialist mode understand *what* it can do with the technology and *where* (conceptually) to look for details in the full documentation if available.

**Procedure:**

1.  **Input Acquisition & Scope Definition:**
    *   **Input:** Source path(s) (`[source_paths]`), Technology/Framework name (`[tech_name]`), Version (`[tech_version]`, if known). `[source_paths]` can be:
        *   A single file path (e.g., `/path/to/doc.md`).
        *   A directory path (e.g., `/path/to/docs/`).
        *   A list of file paths.
        *   A list of URLs (e.g., `https://context7.com/.../llms.txt`).
    *   **Action:**
        *   **If URLs:** For each URL, use `execute_command` with `curl -L [URL] -o [Local Path] --create-dirs` to download the content. Save to a temporary location or a designated context area (e.g., `project_journal/context/temp_source/`). Treat the list of downloaded file paths as the new `[source_paths]`. Handle download errors gracefully (log warning, proceed with available files).
        *   **If Directory Path:** Use `list_files` (recursive) on the directory path. Filter for relevant text-based files (e.g., `.md`, `.txt`, `README*`, `.rst`; potentially `.js`, `.ts`, `.py` if code examples are primary source). Prioritize reading overview/index/README files first using `read_file`.
        *   **If File Path(s):** Use `read_file` on the provided path(s).
        *   **Analysis:** Read the primary source file(s). Identify the specific `[tech_name]` and `[tech_version]`. Scan introductions/overviews to grasp the core purpose and scope.
    *   **Output (Internal Thought):** Clear understanding of the scope, main purpose, version, and key source files for the technology.

2.  **High-Level Summary:**
    *   **Goal:** Create a concise opening statement for the index.
    *   **Action:** Based on the initial analysis, write a 1-3 sentence summary stating the `[tech_name]`, `[tech_version]`, primary domain (e.g., frontend framework, database, API tool, utility library), and core value proposition or goal.
    *   **Output:** The introductory sentence(s) for the index.
    *   *Example:* "Condensed Context Index for **[Tech Name] v[Version]**. A [Primary Domain] designed for [Core Value Proposition]."

3.  **Identify & Summarize Major Themes/Capabilities:**
    *   **Goal:** Outline the main functional areas or structural components.
    *   **Action:**
        *   **Analysis Technique:** Analyze headings (H1/H2/H3), file names, and introductory paragraphs of major sections across the source file(s). Perform *concept clustering* to group related functionalities.
        *   Identify the key themes or capability areas.
        *   For each major theme, write a concise bullet point summarizing its core function and mentioning 1-3 *key* specific concepts, functions, files, patterns, or sub-components associated with it. Synthesize across sources if necessary.
    *   **Output:** A bulleted list under a heading like "Core Concepts & Capabilities:".
    *   *Example (Database Library):*
        *   `Connection Management:` Handles pooling, credentials, connection strings. Key function: `connect()`.
        *   `Query Execution:` Methods for running raw SQL (`execute_sql`) and parameterized queries (`query`). Supports transactions.
        *   `Object-Relational Mapper (ORM):` Defines models mapping to tables, handles relationships (one-to-one, one-to-many), provides CRUD methods on models.
        *   `Migrations:` System for versioning database schema changes (e.g., using migration files, CLI commands).

4.  **Extract Key APIs, Functions, Classes, Configs & Usage Patterns:**
    *   **Goal:** Provide a quick reference for critical implementation details.
    *   **Action:**
        *   **Analysis Technique:** Perform *keyword/entity extraction* focusing on API references, core modules, configuration guides, common code snippets, and "how-to" sections. Look for frequently repeated terms or central classes/functions.
        *   Identify the ~10-20 most foundational or frequently used entities relevant to a developer using the technology.
        *   Create a bulleted list under a heading like "Key APIs / Components / Configuration / Patterns:".
        *   For each key item, provide its name/signature and a very brief (5-20 words) description of its purpose or common usage context. Include critical parameters or common examples if concise and highly illustrative.
    *   **Output:** A bulleted list of key technical details.
    *   *Example (API Framework):*
        *   `@app.route('/path', methods=['GET', 'POST'])`: Decorator to define URL routes and allowed HTTP methods.
        *   `request.get_json()` / `request.form`: Accessing incoming request body data (JSON or form-encoded).
        *   `jsonify({'key': 'value'})`: Function to create a JSON response.
        *   `app.config['SECRET_KEY']`: Accessing configuration values. Common file: `config.py`.
        *   `Middleware`: Pattern for processing requests/responses globally (e.g., authentication, logging).
        *   `Blueprint`: Organizing routes into modular components.

5.  **Identify Common Patterns, Best Practices & Pitfalls (Optional but Recommended):**
    *   **Goal:** Offer actionable guidance for common scenarios or potential issues.
    *   **Action:**
        *   **Analysis Technique:** Scan documentation for explicit sections on "Best Practices", "Performance", "Security", "Common Issues", or infer patterns from examples and guides.
        *   Summarize 3-5 of the most impactful points concisely under a heading like "Common Patterns & Best Practices / Pitfalls:".
    *   **Output:** A short bulleted list.
    *   *Example (General):*
        *   Pattern: Use dependency injection for services.
        *   Best Practice: Validate all user input server-side.
        *   Performance: Add database indexes for frequently queried columns.
        *   Pitfall: Beware of N+1 query problems when using ORMs with loops.
        *   Security: Sanitize output to prevent XSS attacks.

6.  **Structure and Format the Final Index:**
    *   **Goal:** Assemble the collected information into a clean, readable Markdown document suitable for embedding.
    *   **Action:**
        *   Combine the outputs from steps 2-5 under clear Markdown headings (e.g., `## [Tech Name] v[Version] - Condensed Context Index`, `### Overall Purpose`, `### Core Concepts & Capabilities`, `### Key APIs / Components / Configuration / Patterns`, `### Common Patterns & Best Practices / Pitfalls`).
        *   Use lists and `code` formatting consistently.
        *   Keep descriptions brief, focusing on keywords and core function.
        *   Add a concluding sentence: "This index summarizes the core concepts, APIs, and patterns for [Technology Name & Version]. Consult the full source documentation ([path/URL to source]) for exhaustive details."
        *   Review for clarity, conciseness, accuracy, and logical flow. Remove redundancy.

7.  **Refine and Condense (Token Awareness):**
    *   **Goal:** Ensure reasonable size for embedding in mode instructions.
    *   **Action:**
        *   Review the total length. If excessive (subjective, but aim for density over completeness), prioritize ruthlessly: remove less critical entities/examples, shorten descriptions, potentially omit Step 5. Focus on the absolute essentials for the target mode's function. Rely on judgment for appropriate length based on source complexity.

**Output:** A single Markdown string containing the complete Condensed Context Index, ready to be saved.