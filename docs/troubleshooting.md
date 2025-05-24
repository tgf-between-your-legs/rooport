# Troubleshooting Guide: Ultimate Agentic Coding Tool

This guide helps you diagnose and resolve common issues you might encounter while using the Ultimate Agentic Coding Tool.

## Table of Contents
1.  [Common Setup Issues](#1-common-setup-issues)
    1.  [MCP Server Connection Failures](#11-mcp-server-connection-failures)
    2.  [Python Environment Issues for ConPort](#12-python-environment-issues-for-conport)
    3.  [Incorrect Workspace ID](#13-incorrect-workspace-id)
2.  [Performance Problems](#2-performance-problems)
    1.  [Slow Responses from Roo Commander](#21-slow-responses-from-roo-commander)
    2.  [High Token Usage (If Applicable)](#22-high-token-usage-if-applicable)
3.  [Integration Failures & Unexpected Behavior](#3-integration-failures--unexpected-behavior)
    1.  [AI Engines Not Behaving as Expected](#31-ai-engines-not-behaving-as-expected)
    2.  [Autonomous Actions Are Not Optimal](#32-autonomous-actions-are-not-optimal)
4.  [Error Message Interpretation](#4-error-message-interpretation)
5.  [Diagnostic Procedures](#5-diagnostic-procedures)
6.  [Support Resources and Contacts](#6-support-resources-and-contacts)

## 1. Common Setup Issues

### 1.1. MCP Server Connection Failures
*   **Symptom:** Roo Commander reports errors connecting to `conport` or `vertex-ai-mcp-server`. Errors in ROOPORT logs indicating MCP connection timeouts or failures.
*   **Possible Causes & Solutions:**
    *   **ConPort Server Not Running:**
        *   Ensure the ConPort MCP server process is active. You may need to start it manually based on its setup instructions (e.g., running its Python script in its virtual environment).
        *   Verify the command in your `.roo/mcp.json` for the `conport` server is correct and executable from your ROOPORT environment.
    *   **Vertex AI MCP Server Not Running/Configured:**
        *   Ensure the `vertex-ai-mcp-server` process is active.
        *   Verify Google Cloud authentication (`gcloud auth application-default login`) is correctly set up in the environment where the server runs.
        *   Ensure the Google Cloud Project has Vertex AI API enabled.
        *   Check the server's own logs for specific startup errors.
    *   **Incorrect `mcp.json` Configuration:**
        *   Double-check the `command` path and arguments for each MCP server in `.roo/mcp.json`. Ensure `${workspaceFolder}` resolves correctly if used.
        *   Verify `startup_timeout_ms` is sufficient.
    *   **Firewall or Network Issues:** Ensure no firewall is blocking communication between ROOPORT and the MCP server processes, especially if they are on different network interfaces or containers.

### 1.2. Python Environment Issues for ConPort
*   **Symptom:** ConPort server fails to start, citing missing Python packages or incorrect Python version.
*   **Possible Causes & Solutions:**
    *   **Virtual Environment Not Activated:** If ConPort runs in a Python virtual environment (e.g., `.venv`), ensure it's activated before starting the server script.
    *   **Missing Dependencies:** Ensure all Python packages listed in ConPort's `requirements.txt` (or equivalent) are installed within its execution environment. Run `pip install -r requirements.txt`.

### 1.3. Incorrect Workspace ID
*   **Symptom:** ConPort tools report errors related to not finding data or being unable to write to expected paths.
*   **Possible Causes & Solutions:**
    *   The `workspace_id` argument passed to the ConPort MCP server on startup (configured in `.roo/mcp.json`) must be the absolute path to your ROOPORT project's root directory. Verify this path.

## 2. Performance Problems

### 2.1. Slow Responses from Roo Commander
*   **Symptom:** Roo Commander takes an unusually long time to respond to queries or commands.
*   **Possible Causes & Solutions:**
    *   **MCP Server Latency:**
        *   The ConPort or Vertex AI MCP servers might be slow. Check their logs for performance issues or high load.
        *   Network latency between ROOPORT and MCP servers.
    *   **Complex RAG Queries:** Very complex queries requiring extensive data retrieval and synthesis by the Agentic RAG Engine can take time. Try simplifying the query.
    *   **Resource Constraints:** The machine running ROOPORT or the MCP servers might be under-resourced (CPU, memory). Monitor system resource usage.
    *   **Inefficient ConPort Queries (Internal):** This would be an issue for system developers to investigate if ConPort's internal database queries are slow.
*   **Diagnostics:**
    *   Check the `execution_time` reported in `UltimateAgenticResponse` or ConPort logs for `AgenticRAGExecution` to pinpoint RAG-related slowness.
    *   Enable more verbose logging in ROOPORT and MCP servers if possible.

### 2.2. High Token Usage (If Applicable)
*   **Symptom:** Notifications or logs indicating high token consumption for LLM API calls.
*   **Possible Causes & Solutions:**
    *   **Verbose Prompts/Context:** The system might be sending very large contexts to LLMs.
    *   **Frequent Complex RAG Operations:** Agentic RAG can be token-intensive.
*   **Mitigation:**
    *   The system includes prompt caching strategies (see [`.roo/rules/21-prompt-caching-strategy.md`](../../../.roo/rules/21-prompt-caching-strategy.md)). Ensure these are active.
    *   Review the [Best Practices Guide](./best-practices.md) for tips on efficient querying.

## 3. Integration Failures & Unexpected Behavior

### 3.1. AI Engines Not Behaving as Expected
*   **Symptom:** POE not providing relevant suggestions, CLS not showing learning improvements, RAG providing irrelevant answers.
*   **Possible Causes & Solutions:**
    *   **Insufficient ConPort Data:** The AI engines heavily rely on rich, accurate data in ConPort. If ConPort is sparsely populated or contains outdated information, engine performance will suffer.
        *   *Solution:* Ensure consistent logging of decisions, progress, and other contextual information to ConPort.
    *   **Misconfiguration of Rules:** Check the relevant integration rules (e.g., [`.roo/rules-roo-commander/02-ultimate-agentic-integration.md`](../../../.roo/rules-roo-commander/02-ultimate-agentic-integration.md)) and engine-specific rules.
    *   **Feedback Loop Issues (CLS):** Ensure feedback mechanisms are working and that the CLS can process this feedback to generate improvement proposals.
    *   **RAG Engine Strategy:** The RAG engine uses dynamic strategies. If results are consistently poor for certain query types, it might indicate a need to refine these strategies (an advanced CLS task).
*   **Diagnostics:**
    *   Review ConPort logs for `POE_Activity`, `ContinuousLearningCycle`, `AgenticRAGExecution`, and `UltimateAgenticExecution` entries. These can provide insights into what the engines are doing.
    *   Check the `reasoning_chain` and `validation_checks` in `AgenticRAGResponse` objects for clues.

### 3.2. Autonomous Actions Are Not Optimal
*   **Symptom:** The system takes autonomous actions that are incorrect or not what you intended.
*   **Possible Causes & Solutions:**
    *   **Context Misinterpretation:** The agent may have misinterpreted the available context.
    *   **Overconfidence:** The agent's confidence score for an action might have been inappropriately high.
    *   **Gaps in Knowledge/Rules:** The underlying rules or knowledge base (KB) might lack the necessary information to guide the agent correctly in a specific scenario.
*   **Response:**
    *   **Correct the Action:** Manually undo or correct the agent's action.
    *   **Provide Feedback:** This corrective action itself serves as implicit feedback to the CLS. If an explicit feedback mechanism is available, use it to report the issue.
    *   **Update ConPort/Rules:** If the issue stems from missing or incorrect information in ConPort or agent rules, update them accordingly (this might be a task for a system administrator or lead).

## 4. Error Message Interpretation

*   **`MCP Server [server_name] not responding or timed out.`**
    *   Indicates the specified MCP server is unreachable or not starting correctly. See Section 1.1.
*   **`ConPort Error: Could not find item [item_id].`**
    *   The requested data item does not exist in ConPort. Verify IDs or data logging processes.
*   **`AgenticRAGResponse: Confidence INSUFFICIENT.`**
    *   The RAG engine could not find enough relevant information or had low confidence in its answer. Try rephrasing the query or ensuring relevant context exists in ConPort.
*   **`POE Suggestion Confidence Low.`**
    *   A suggestion from the Proactive Orchestration Engine has low confidence. It may still be useful but warrants careful consideration.

## 5. Diagnostic Procedures

1.  **Check ROOPORT Logs:** These are often the first place to look for general errors or activity logs.
2.  **Check MCP Server Logs:**
    *   **ConPort:** The log file specified in its startup command (e.g., `/logs/conport.log` relative to the workspace).
    *   **Vertex AI MCP Server:** Check its console output or configured log file.
3.  **Inspect ConPort Data:**
    *   Use Roo Commander to query ConPort for recent decisions, progress, or custom data relevant to the issue.
    *   Example: "Show me the latest POE activity logs from ConPort."
4.  **Review Relevant Rules:** Consult the integration rules in `.roo/rules-roo-commander/` and general rules in `.roo/rules/` to understand expected behavior.
5.  **Isolate Components:** If possible, try to determine which AI engine or component might be causing the issue (POE, CLS, RAG, or the Orchestrator itself). Log entries in ConPort can help with this.

## 6. Support Resources and Contacts

*   **Project Documentation:** This documentation suite is your primary resource.
*   **Internal Team/Leads:** Consult with your team lead or members familiar with the ROOPORT and Ultimate Agentic Coding Tool setup.
*   **System Administrators:** For issues related to server configurations, deployments, or access to cloud services (like Vertex AI).
*   **Issue Tracker:** If your project uses an issue tracker (e.g., Jira, GitHub Issues), check for known issues or report new ones.

If you encounter persistent issues not covered here, gather as much information as possible (logs, steps to reproduce, error messages) before seeking further assistance.