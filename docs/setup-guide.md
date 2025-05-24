# Setup Guide: Ultimate Agentic Coding Tool

This guide provides step-by-step instructions for setting up and configuring the Ultimate Agentic Coding Tool.

## Table of Contents
1.  [Prerequisites](#1-prerequisites)
2.  [Installation Steps](#2-installation-steps)
    1.  [Verify Core Engine Files](#21-verify-core-engine-files)
    2.  [Verify Integration Rules](#22-verify-integration-rules)
3.  [Configuration](#3-configuration)
    1.  [ConPort MCP Server Configuration](#31-conport-mcp-server-configuration)
    2.  [Vertex AI MCP Server Configuration (Optional)](#32-vertex-ai-mcp-server-configuration-optional)
    3.  [Environment Variables](#33-environment-variables)
4.  [Initial System Validation](#4-initial-system-validation)
5.  [Autonomous Operation](#5-autonomous-operation)
6.  [Next Steps](#next-steps)

## 1. Prerequisites

Before you begin, ensure your environment meets the following prerequisites:

*   **Python Environment:** Python 3.9 or higher.
*   **ROOPORT Installation:** A working installation of ROOPORT.
*   **ConPort MCP Server:** The ConPort MCP server must be running and accessible. Refer to ConPort documentation for its setup.
*   **Vertex AI MCP Server (Optional but Recommended):** For full capabilities, the Vertex AI MCP server should be configured and running. This may require:
    *   Google Cloud Project with Vertex AI API enabled.
    *   Authentication configured (e.g., `gcloud auth application-default login`).
*   **Git:** Version control system for managing project files.
*   **Required Python Packages:** Ensure all dependencies for the core engines are installed (typically managed via `requirements.txt` or a similar mechanism within the ROOPORT project).

## 2. Installation Steps

The Ultimate Agentic Coding Tool is integrated within the ROOPORT ecosystem. The primary installation involves ensuring all components and configurations are correctly in place.

### 2.1. Verify Core Engine Files

Ensure the following core engine files are present in your ROOPORT installation, typically under `.ruru/modes/roo-commander/`:

*   [`proactive-orchestration-engine.py`](../../modes/roo-commander/proactive-orchestration-engine.py)
*   [`continuous-learning-system.py`](../../modes/roo-commander/continuous-learning-system.py)
*   [`agentic-rag-engine.py`](../../modes/roo-commander/agentic-rag-engine.py)
*   [`ultimate-agentic-orchestrator.py`](../../modes/roo-commander/ultimate-agentic-orchestrator.py)

### 2.2. Verify Integration Rules

Confirm that the necessary integration rules are in place, typically within the `.roo/rules-roo-commander/` directory:

*   **`02-ultimate-agentic-integration.md`**: This file defines how Roo Commander leverages the ultimate agentic capabilities.
*   Ensure that general workspace rules like `23-autonomous-execution-mandate.md` are present in `.roo/rules/` to enable full autonomous operation.

## 3. Configuration

### 3.1. ConPort MCP Server Configuration

*   Ensure your ROOPORT `mcp.json` file (typically in `.roo/mcp.json`) includes a valid configuration for the `conport` server. This configuration should specify the command to start the server and grant necessary tool permissions.
    *   Example snippet for `mcp.json`:
        ```json
        {
          "name": "conport",
          "command": "C:\\Users\\thegr\\OneDrive\\Desktop\\frontendtest\\integration\\context-portal\\.venv\\Scripts\\python.exe C:\\Users\\thegr\\OneDrive\\Desktop\\frontendtest\\integration\\context-portal\\src\\context_portal_mcp\\main.py --mode stdio --workspace_id ${workspaceFolder} --log-file /logs/conport.log --log-level INFO",
          "startup_timeout_ms": 30000,
          "permissions": {
            "tools": ["*"], // Or specify individual tools
            "resources": ["*"]
          }
        }
        ```
*   The `workspace_id` in the ConPort server command must point to the root of your ROOPORT project.

### 3.2. Vertex AI MCP Server Configuration (Optional)

*   If using Vertex AI for enhanced capabilities (e.g., advanced embeddings, generation models):
    *   Ensure the `vertex-ai-mcp-server` is configured in your `mcp.json`.
    *   The server requires appropriate Google Cloud authentication and Vertex AI API enablement.
    *   Refer to the `vertex-ai-mcp-server` documentation for specific setup instructions.

### 3.3. Environment Variables

*   Certain components might require environment variables (e.g., API keys for external services). Refer to the specific documentation for each engine or MCP server if applicable.

## 4. Initial System Validation

After setup and configuration, perform these steps to validate the system:

1.  **Start ROOPORT:** Launch your ROOPORT environment.
2.  **Verify MCP Server Connections:** Check the ROOPORT logs or MCP status indicators to ensure both ConPort and Vertex AI (if used) MCP servers connect successfully.
3.  **Test Basic Interaction:** Engage with Roo Commander with a simple query. Observe if the system responds and if logs indicate activity from the new engines.
    *   Example: "What is the current status of the project?"
4.  **Check ConPort Logging:**
    *   After an interaction, check if ConPort logs new entries (e.g., in `Custom Data` for `UltimateAgenticExecution` or `AgenticRAGExecution`).
    *   This can be done by querying ConPort via Roo Commander or directly inspecting the ConPort database/logs if accessible.

## 5. Autonomous Operation

*   The system is designed for autonomous operation as per rule [`.roo/rules/23-autonomous-execution-mandate.md`](../../../.roo/rules/23-autonomous-execution-mandate.md). This means it will generally not prompt for confirmation for actions it deems high-confidence.
*   Familiarize yourself with this operational paradigm. While it enhances efficiency, it's crucial to have robust logging and monitoring (handled by the CLS and ConPort) to track system behavior.

## Next Steps

Once setup is complete and validated, proceed to the [User Guide](./user-guide.md) to learn about using the Ultimate Agentic Coding Tool's features and workflows.