# Roo Commander Mode Specification v1.0

This document defines the **source organization standard** for defining custom Roo Commander modes (v7.1+). It aims for clarity, scalability, maintainability, and ease of automation in managing mode definitions. **Note:** This standard describes the source structure; a separate build process is required to generate the runtime files (JSON definitions, `.roo/rules-{modeSlug}/` instruction files) that Roo Code directly consumes.

## 1. Overview

The standard utilizes a combination of:

*   **TOML Frontmatter:** For structured configuration data required by the system (metadata, IDs, prompts, tool access, links).
*   **Markdown:** For human-readable documentation (description, capabilities, usage, rationale).
*   **Standardized Directory Structure:** To organize mode definition files, custom instructions, context files, and examples consistently.

## 2. File Format: `{id}.mode.md`

Each mode is defined by a single Markdown file named after the mode's unique ID (e.g., `aws-architect.mode.md`) located within its dedicated directory. This file contains TOML frontmatter enclosed in `+++` delimiters, followed by standard Markdown content. Using the mode's ID in the filename improves glanceability when browsing multiple mode directories.

```markdown
+++
# TOML Frontmatter Section
# Required and optional configuration fields go here
key = "value"
list = ["item1", "item2"]

[metadata]
tags = ["tag1", "tag2"]
+++

# Markdown Documentation Section

## Description

A clear explanation of the mode's purpose and primary function.

## Capabilities

Details on what the mode can do.

## Usage / Workflow Examples

How to interact with the mode effectively.

## Rationale

Design choices and reasoning behind the mode's structure.
```

## 3. TOML Frontmatter Schema (`+++ ... +++`)

The TOML frontmatter contains the core configuration.

```toml
# --- Core Identification (Required) ---
id = "unique-mode-slug" # kebab-case, unique identifier (e.g., "aws-architect")
name = "Mode Display Name" # Human-friendly name (e.g., "☁️ AWS Architect")
version = "1.0.0" # Semantic version for the mode definition itself

# --- Classification & Hierarchy (Required) ---
# Reflects the directory structure for organizational purposes
classification = "lead" # e.g., "executive", "director", "lead", "worker", "assistant", "footgun"
domain = "devops" # e.g., "design", "frontend", "backend", "devops", "data", "utility", "core"
sub_domain = "cloud" # Optional: Further specialization (e.g., "cloud", "ci-cd", "monitoring")

# --- Description (Required) ---
# Short, concise summary used in listings and selections
summary = "Specialized Lead for designing and managing AWS infrastructure."

# --- Base Prompting (Required) ---
# The core instructions defining the mode's persona and primary directives
# Use multi-line strings for readability.
system_prompt = """
You are the AWS Architect, a specialized Lead within the DevOps domain.
Your responsibilities include:
- Designing scalable, secure, cost-effective AWS solutions based on requirements.
- Providing guidance on AWS best practices (Well-Architected Framework).
- Assisting with Infrastructure as Code (IaC) using tools like Terraform or CloudFormation.
- Troubleshooting complex AWS infrastructure issues.
- Collaborating with other leads and specialists.
You have access to standard tools and potentially specialized AWS-related MCP tools.
Adhere strictly to security best practices and cost optimization principles.
"""

# --- Tool Access (Optional - Defaults to standard set if omitted) ---
# Explicitly define allowed tool groups or specific tools.
# If omitted, assumes access to: ["read", "edit", "browser", "command", "mcp"]
# Tool groups can be defined elsewhere (e.g., in a central config)
allowed_tool_groups = ["read", "edit", "command", "mcp", "aws_tools"]
# OR specify individual tools:
# allowed_tools = ["read_file", "write_to_file", "execute_command", "use_mcp_tool", "access_mcp_resource"]

# --- File Access Restrictions (Optional - Defaults to allow all if omitted) ---
# Restrict which files the mode can read or write using glob patterns.
# Useful for enforcing separation of concerns (e.g., architects only edit .md, .yaml)
[file_access]
read_allow = ["**/*.md", "**/*.yaml", "**/*.yml", "**/*.tf", "**/*.json", ".docs/**", ".decisions/**", ".planning/**"]
write_allow = [".docs/**/*.md", ".decisions/**/*.md", ".planning/**/*.md", "**/*.tf", "**/*.yaml", "**/*.yml"] # Example: Allow editing docs, ADRs, plans, IaC

# --- Metadata (Optional but Recommended) ---
[metadata]
tags = ["aws", "cloud", "infrastructure", "devops", "lead", "architecture", "iac", "terraform", "cloudformation"] # Keywords for searching/filtering
categories = ["Cloud Infrastructure", "DevOps Leadership"] # Broader functional categories
# Pointers for workflow automation/delegation (Mode IDs or Role Types)
delegate_to = ["terraform-specialist", "cloudformation-specialist", "security-specialist", "backend-lead"] # Modes this mode might delegate tasks to
escalate_to = ["technical-architect", "roo-commander"] # Modes to escalate complex issues or decisions
reports_to = ["devops-lead", "technical-architect"] # Reporting structure (optional)
# Links to relevant external documentation or internal context
documentation_urls = [
  "https://aws.amazon.com/documentation/",
  "https://aws.amazon.com/architecture/well-architected/",
  "https://registry.terraform.io/providers/hashicorp/aws/latest/docs",
  "https://docs.aws.amazon.com/cloudformation/index.html"
]
# Pointers to internal context files (paths relative to the workspace root)
context_files = [
  "v7.1/modes/[class]/[domain]/[id]/context/aws_well_architected_summary.md", # Example full path
  "v7.1/modes/[class]/[domain]/[id]/context/common_aws_patterns.md"  # Example full path
]
# URLs for dynamic context fetching (e.g., via Crawl4AI or similar)
context_urls = [
  "https://context7.com/..." # Example placeholder
]

# --- Custom Instructions Pointer (Optional) ---
# Specifies the location of the *source* directory for custom instructions, relative to the main `{id}.mode.md` file.
# This informs the build process where to find instruction source files.
# Conventionally, this should always be "custom-instructions".
custom_instructions_source_dir = "custom-instructions"

# --- Mode-Specific Configuration (Optional) ---
# For modes that require specific parameters
[config]
default_region = "us-east-1"
iac_tool = "terraform" # or "cloudformation"
```

## 4. Markdown Content Structure (`{id}.mode.md` after `+++`)

While flexible, the following sections are recommended for clarity and consistency within the Markdown portion of the `{id}.mode.md` file:

*   **`## Description`**: An expanded explanation of the mode's purpose, goals, and typical use cases.
*   **`## Capabilities`**: A detailed list or description of the mode's skills, knowledge areas, and the types of tasks it excels at.
*   **`## Workflow & Usage Examples`**: Concrete examples of how to interact with the mode, including sample prompts and expected outputs or actions. Illustrate typical workflows.
*   **`## Limitations`**: Clearly state any known limitations or areas where the mode might struggle or require assistance.
*   **`## Rationale / Design Decisions`**: Explain *why* the mode is designed the way it is. Justify key aspects of the system prompt, tool access, or intended workflow. (Optional but helpful).
*   **`## Dependencies / Interactions`**: Describe how this mode interacts with other modes, tools, or system components. (Optional).

## 5. Directory Structure

Each mode resides in its own directory. The path to this directory often reflects the classification/domain structure (e.g., `v7.0/modes/02x-lead/devops/aws-architect/`). Within each mode's directory, the following structure is standard:

```
mode-slug/                  # Directory named after the mode's id (e.g., aws-architect/)
├── {id}.mode.md            # The primary definition file, named after the mode's id (e.g., aws-architect.mode.md).
│
├── custom-instructions/    # Optional: Folder for the source of custom instructions.
│   ├── README.md           # Explains the purpose and order of instructions.
│   ├── 01-core-principles.md # Instructions loaded first (lowest number).
│   ├── 02-security-rules.md
│   └── ...                 # Higher numbers loaded later.
│
├── context/                # Optional: Static context files specific to this mode.
│   ├── aws_well_architected_summary.md # Pre-summarized docs, checklists, etc.
│   └── common_aws_patterns.md
│
├── examples/               # Optional: Concrete usage examples or test cases.
│   ├── create_vpc_scenario.md
│   └── troubleshoot_s3_permissions.md
│
└── assets/                 # Optional: Images, diagrams, or other assets referenced in docs.
    └── architecture_diagram.png
```

*   **`{id}.mode.md`**: Core definition file containing TOML frontmatter and Markdown documentation. Named after the mode's `id`.
*   **`custom-instructions/`**: Contains the *source* Markdown files for custom instructions.
    *   **Purpose:** These files define the detailed operational logic, rules, and guidelines for the mode.
    *   **Build Step:** These source files are intended to be processed by a build step to populate the actual runtime directory (`.roo/rules-{modeSlug}/`) that Roo Code reads from.
    *   **Structure Recommendation:** It is recommended to structure instructions using numbered files based on logical themes. A good baseline includes:
        *   `01-operational-principles.md`: Core identity, goals, high-level rules.
        *   `02-workflow.md`: Step-by-step process, interaction flow.
        *   `03-collaboration-delegation-escalation.md`: How the mode interacts with others.
        *   `04-safety-protocols.md`: Guardrails, constraints, security rules.
        *   `05-error-handling.md`: How to manage errors or unexpected situations.
        *   Additional files (e.g., `06-tool-usage.md`, `07-specific-technique.md`) should be added as needed based on the mode's complexity and function.
    *   **Ordering:** Using numerical prefixes ensures predictable processing order during the build step (lowest number first).
    *   `README.md` should document the purpose and structure of the instruction files within this directory.
*   **`context/`**: Stores static, mode-specific knowledge files (Markdown, text, JSON, YAML, etc.).
    *   **Purpose:** Provides reference material, checklists, data, or pre-summarized documentation that the mode can access *using tools* (e.g., `read_file`).
    *   **Not Auto-Loaded:** These files are *not* automatically loaded into the mode's prompt context.
    *   **Path References:** The `context_files` array in the TOML frontmatter can list key files using paths relative to the workspace root.
*   **`examples/`**: Provides concrete examples of how to use the mode, potentially including sample prompts and expected outputs. Useful for testing and documentation.
*   **`assets/`**: Contains any supporting assets (images, diagrams) referenced in `{id}.mode.md` or other documentation files.
*   **Path Referencing:** Any references between files within a mode's source structure (e.g., an instruction in `custom-instructions/` referring to a file in `context/`) **must use full paths relative to the workspace root** (e.g., `v7.1/modes/[class]/[domain]/[id]/context/file.md`).

## 6. Relationship to Runtime Files & Build Process

This v7.1 source structure is designed for organization and maintainability. It requires a **build process** to generate the actual files Roo Code uses at runtime:

1.  **JSON Mode Definitions:** A build script should traverse the `v7.1/modes/` directory. For each `{id}.mode.md` file found within a mode's directory, it should parse the TOML frontmatter to generate the corresponding JSON object required by Roo Code (e.g., for inclusion in `custom_modes.json` or a `.roomodes` file). Key fields like `id`, `name`, `roleDefinition` (derived from `system_prompt`), and `customInstructions` (potentially pointing to the runtime instruction file/directory) need to be mapped.
2.  **Runtime Custom Instructions:** The build script should process the files found in the `custom-instructions/` source directory (identified by `custom_instructions_source_dir` in the TOML of the `{id}.mode.md` file). It should concatenate these files in the correct order (based on numerical prefixes) and place the combined content into the appropriate runtime location that Roo Code automatically loads, typically within `.roo/rules-{modeSlug}/` (e.g., `.roo/rules-{modeSlug}/00-generated-instructions.md`). The exact mechanism (single concatenated file vs. copying individual files) depends on the build script's implementation and how Roo Code loads from these directories.

**Benefits of Separation:** This separation between source and runtime files allows developers to manage mode definitions using readable TOML/Markdown and structured directories, while the build process handles the generation of the specific formats Roo Code requires, preventing accidental editing of live mode configurations.

## 7. Critique & Alternatives Considered

*   **Filename Convention:** Using `{id}.mode.md` provides better glanceability when browsing multiple mode directories compared to a generic `mode.md`. While `mode.md` offered simpler predictability for tools operating within a known directory, `{id}.mode.md` is preferred for human factors. Build tools will need to identify the file based on the `{id}` pattern.
*   **TOML vs. JSON:** TOML is chosen for frontmatter due to its superior human readability, support for comments, and easier handling of multi-line strings compared to JSON, making mode definition more maintainable. The final bundle is JSON, but the source format prioritizes developer experience.
*   **Custom Instruction Source:** Using a dedicated `custom-instructions/` source directory with numbered files provides a clear, maintainable way to manage complex instructions before they are processed by a build step for runtime use.
*   **Context Files:** The `context/` directory provides a place for static knowledge accessible via tools. Dynamic context fetching (via `context_urls` and tools) is complementary. Listing key files in `context_files` (using workspace-relative paths) aids discoverability.

## 8. Future Considerations

*   **Schema Validation:** Implement robust schema validation during the bundling process.
*   **Tool Definition:** Standardize how tool groups (`allowed_tool_groups`) are defined centrally.
*   **Build Script:** Develop and document the standard build script(s) responsible for transforming the v7.1 source structure into runtime JSON definitions and `.roo/rules-{modeSlug}/` content.
*   **Dynamic Context Loading:** Explore how tools can leverage `context_urls` and `context_files` metadata for automated fetching or RAG.
*   **Mode Dependencies:** Formalize how dependencies between modes are declared and managed in the TOML.
*   **Testing Framework:** Create tools or processes to test modes based on examples in the `examples/` directory, potentially integrating with the build process.