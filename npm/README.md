# 🚀 roocommander

[![npm version](https://badge.fury.io/js/roocommander.svg)](https://badge.fury.io/js/roocommander)

Command Line Interface (CLI) tool for initializing and managing [Roo Commander](https://github.com/jezweb/roo-commander) workspace configurations within your projects.

## What is Roo Commander?

Roo Commander is an advanced configuration layer and opinionated workflow system built specifically for the [Roo Code](https://github.com/RooVetGit/Roo-Code) VS Code extension. It transforms your Roo Code experience by implementing a sophisticated framework for managing software development projects using a structured, **multi-agent approach**. It brings specialized AI agents, structured task management (MDTM), and enhanced context handling directly into your VS Code environment.

Learn more about the core concepts and features in the main [Roo Commander README](https://github.com/jezweb/roo-commander/blob/main/README.md).

## Purpose of `roocommander`

This CLI tool (`roo`) is the **essential starting point** for integrating the Roo Commander framework into your projects. It sets up the necessary directory structures and configuration files required by Roo Code to activate and manage the specialized AI agents and workflows.

## Prerequisites

*   Node.js >= 18.0.0
*   [Roo Code](https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline) VS Code extension installed and configured.

## Installation

You don't need to install this package globally. Use `npx` to run it directly within your project directory:

```bash
# Example: Initialize Roo Commander in the current project
npx roocommander init
```

If you prefer a global installation (less common):

```bash
npm install -g roocommander
```

## Key Features Enabled by the CLI

Using `roocommander` enables the core functionalities of the Roo Commander system:

*   **🚀 Workspace Initialization:** Creates the foundational `.roo/` and `.ruru/` directories and the `.roomodes` file, activating the multi-agent system within Roo Code.
*   **🧠 Structured Artifacts Setup:** Prepares the ground for structured project artifacts (like tasks in `.ruru/tasks/` and decisions in `.ruru/decisions/`) used for context management and traceability (MDTM).
*   **🧩 MCP Server Integration:** Provides commands to easily install and configure Model Context Protocol (MCP) servers, granting Roo Commander agents extended capabilities (e.g., web search via `vertex-ai`, repository interactions via `github`).
*   **⚙️ Agent Configuration:** Ensures Roo Code recognizes the specialized roles (modes), rules, and knowledge bases defined by Roo Commander.

## Commands

Here are the primary commands available:

### `init`

Initializes the Roo Commander configuration files (`.roomodes`) and directory structure (`.roo/`, `.ruru/`) within your current project workspace. This command is the **first step** to prepare your project for the Roo Commander multi-agent framework.

If configuration files or directories already exist, you will be prompted interactively whether to overwrite them.

**Usage:**

```bash
# Navigate to your project's root directory
cd /path/to/your/project

# Initialize Roo Commander configuration
npx roocommander init
```

**Options:**

*   `--help`: Display help for the `init` command.

*(Note: Template functionality (`--template <name>`) is planned for a future release.)*

### `install-mcp`

Installs and configures a specified Model Context Protocol (MCP) server by updating the `.roo/mcp.json` and `.roomodes` files. MCP servers provide Roo Commander agents with additional tools and capabilities beyond standard LLM functions.

*(Note: This command is currently under development. It will set up the basic configuration entries but may require manual steps for full server setup.)*

**Usage:**

```bash
# Install the Vertex AI MCP server (provides web search, file system tools, etc.)
npx roocommander install-mcp vertex-ai

# Install the GitHub MCP server (provides GitHub API tools)
npx roocommander install-mcp github

# Install the basic Fetch MCP server (provides URL fetching)
npx roocommander install-mcp fetch
```

**Arguments:**

*   `server-name`: The identifier of the MCP server to install (e.g., `vertex-ai`, `github`, `fetch`). Check the Roo Commander documentation or use `roo-commander` mode in Roo Code for available servers.

**Options:**

*   `--help`: Display help for the `install-mcp` command.

### `help`

Displays help information for the CLI or a specific command.

**Usage:**

```bash
# Display general help for the CLI
npx roocommander --help

# Display help specifically for the 'init' command
npx roocommander init --help

# Display help specifically for the 'install-mcp' command
npx roocommander install-mcp --help
```

## Basic Workflow Example

1.  **Navigate to your project directory:**
    ```bash
    cd /path/to/your/project
    ```
2.  **Initialize Roo Commander:**
    Run the `init` command. This creates the necessary configuration for Roo Code.
    ```bash
    npx roocommander init
    ```
3.  **(Recommended) Install MCP Servers:**
    Install key MCP servers to enhance agent capabilities. `vertex-ai` is highly recommended.
    ```bash
    npx roocommander install-mcp vertex-ai
    npx roocommander install-mcp github
    ```
4.  **Reload VS Code:**
    Ensure Roo Code picks up the new configuration by reloading your VS Code window (`Ctrl+Shift+P` or `Cmd+Shift+P` -> `"Developer: Reload Window"`).
5.  **Start Using Roo Commander in Roo Code:**
    Select the `"👑 Roo Commander"` mode in the Roo Code chat interface. State your high-level development goal (e.g., "Plan and implement a user authentication feature using Supabase"). Commander will then orchestrate the task using its specialized agents.

## Contributing

Contributions are welcome! Please refer to the main [Roo Commander repository](https://github.com/jezweb/roo-commander) for contribution guidelines, issue tracking, and discussions.

## License

This project is licensed under the MIT License - see the [`LICENSE`](./LICENSE) file for details.