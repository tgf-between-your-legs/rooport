# API Reference: Ultimate Agentic Coding Tool

This document provides a reference for key integration points and programmatic interactions with the Ultimate Agentic Coding Tool, primarily focusing on how its components might be invoked or extended. Direct API access for end-users is typically abstracted through Roo Commander.

## 1. Core Engine Integration (Conceptual)

The Ultimate Agentic Coding Tool's core engines (POE, CLS, Agentic RAG, Orchestrator) are primarily integrated and utilized internally by Roo Commander. Programmatic interaction from external scripts or tools would generally occur via Roo Commander's own command-line interface or APIs, if available.

However, understanding their Python module interfaces can be useful for advanced users or developers extending the system.

### 1.1. Ultimate Agentic Orchestrator
*   **Module:** [`ultimate-agentic-orchestrator.py`](../../modes/roo-commander/ultimate-agentic-orchestrator.py)
*   **Main Function:** `async def integrate_ultimate_agentic_system(workspace_id: str, user_query: str, conport_client, vertex_ai_client=None) -> UltimateAgenticResponse:`
    *   **Purpose:** Main entry point to process a user query using the full suite of agentic capabilities.
    *   **Arguments:**
        *   `workspace_id (str)`: Absolute path to the current ROOPORT workspace.
        *   `user_query (str)`: The user's request or query.
        *   `conport_client`: An initialized ConPort MCP client instance.
        *   `vertex_ai_client` (Optional): An initialized Vertex AI MCP client instance.
    *   **Returns:** `UltimateAgenticResponse` dataclass object containing the synthesized answer, suggestions, insights, etc.
*   **Optimization Cycle:** `async def run_ultimate_system_optimization(workspace_id: str, conport_client) -> Dict[str, Any]:`
    *   **Purpose:** Triggers a full system optimization cycle, including learning and performance analysis.
    *   **Returns:** A dictionary summarizing the optimization cycle results.

### 1.2. Proactive Orchestration Engine (POE)
*   **Module:** [`proactive-orchestration-engine.py`](../../modes/roo-commander/proactive-orchestration-engine.py)
*   **Main Function:** `async def integrate_with_roo_commander(workspace_id: str, conport_client):` (This is an example integration point)
    *   Internally uses `ProactiveOrchestrationEngine.generate_suggestions(workspace_id)`.
    *   **Purpose:** Analyzes project state via ConPort and generates actionable suggestions (risks, opportunities).
    *   **Returns:** A list of `Suggestion` dataclass objects.

### 1.3. Continuous Learning System (CLS)
*   **Module:** [`continuous-learning-system.py`](../../modes/roo-commander/continuous-learning-system.py)
*   **Main Function:** `async def integrate_continuous_learning(workspace_id: str, conport_client) -> Dict[str, Any]:` (Example integration point)
    *   Internally uses `ContinuousLearningSystem.run_learning_cycle(workspace_id, target_agents)`.
    *   **Purpose:** Runs a learning cycle involving feedback collection, performance analysis, and improvement proposal generation.
    *   **Returns:** A dictionary summarizing the learning cycle results.
*   **Feedback Logging:** `FeedbackCollector.log_agent_feedback(workspace_id: str, feedback: AgentFeedback)`
    *   Used to log structured feedback about agent performance to ConPort.

### 1.4. Agentic RAG Engine
*   **Module:** [`agentic-rag-engine.py`](../../modes/roo-commander/agentic-rag-engine.py)
*   **Main Function:** `async def integrate_agentic_rag(workspace_id: str, query: str, conport_client) -> AgenticRAGResponse:` (Example integration point)
    *   Internally uses `AgenticRAGEngine.process_query(query, workspace_id)`.
    *   **Purpose:** Processes a query using advanced RAG techniques (decomposition, iterative retrieval, synthesis).
    *   **Returns:** `AgenticRAGResponse` dataclass object.

## 2. ConPort MCP Server API (via `use_mcp_tool`)

Interaction with ConPort data, which is fundamental to the Ultimate Agentic Coding Tool, occurs via the `conport` MCP server. All ConPort tool calls require `workspace_id`.

**Key ConPort Tools Used by the System:**

*   **Data Retrieval:**
    *   `get_product_context`: Retrieves overall project goals.
    *   `get_active_context`: Gets current working focus.
    *   `get_decisions`: Retrieves logged architectural decisions.
    *   `get_progress`: Fetches progress entries/tasks.
    *   `get_system_patterns`: Gets defined system/coding patterns.
    *   `get_custom_data`: Retrieves custom key-value data (used for feedback, analysis reports, etc.).
    *   `get_linked_items`: Finds items linked to a specific item.
    *   `search_decisions_fts`: Full-text search in decisions.
    *   `search_custom_data_value_fts`: Full-text search in custom data.
*   **Data Logging:**
    *   `update_product_context`: Updates project goals.
    *   `update_active_context`: Updates current focus.
    *   `log_decision`: Logs a new decision.
    *   `log_progress`: Logs a task status or progress.
    *   `log_system_pattern`: Logs a new system pattern.
    *   `log_custom_data`: Stores various types of data, including:
        *   `AgentInteractionFeedback` category for CLS.
        *   `PerformanceAnalysisReport` category for CLS.
        *   `AgentRefinementProposal` category for CLS.
        *   `POE_Activity` category for POE.
        *   `AgenticRAGExecution` category for RAG engine.
        *   `UltimateAgenticExecution` category for the orchestrator.
        *   `SystemOptimizationCycle` category for the orchestrator.
    *   `link_conport_items`: Creates relationships between ConPort items.

**Example `use_mcp_tool` call for ConPort:**
```xml
<use_mcp_tool>
  <server_name>conport</server_name>
  <tool_name>get_decisions</tool_name>
  <arguments>
    {
      "workspace_id": "c:/Users/thegr/OneDrive/Desktop/frontendtest/integration",
      "limit": 5
    }
  </arguments>
</use_mcp_tool>
```
Refer to the ConPort MCP server's schema (accessible via `get_conport_schema` tool if available, or its documentation) for detailed arguments for each tool.

## 3. Configuration Files

While not direct APIs, understanding key configuration files is important for advanced customization or troubleshooting.

*   **`.roo/mcp.json`**: Defines available MCP servers and their startup commands, including `conport` and `vertex-ai-mcp-server`.
*   **`.roo/rules/` directory (and subdirectories like `.roo/rules-roo-commander/`)**: Contains Markdown-based rule files that govern agent behavior, including how they integrate the AI enrichment engines.
    *   **Key Rule:** [`.roo/rules-roo-commander/02-ultimate-agentic-integration.md`](../../../.roo/rules-roo-commander/02-ultimate-agentic-integration.md)
*   **ConPort Database (`context_portal/context.db`):** SQLite database storing all project context. Direct interaction is generally not recommended; use ConPort MCP tools.

## 4. Extending the System

Extending the system might involve:

*   **Creating New Specialist Modes:** Develop new Python-based modes that can leverage the Ultimate Agentic Orchestrator or individual engines.
*   **Adding New Rules:** Define new rules in `.roo/rules/` to modify or guide agent behavior.
*   **Customizing ConPort Data Categories:** Log new types of structured data to ConPort using `log_custom_data` to expand the system's knowledge base.
*   **Developing New ConPort Tools:** If new low-level data access patterns are needed, the ConPort MCP server itself could be extended with new tools.

Always refer to the specific documentation for each component and follow established development practices within the ROOPORT ecosystem when extending the system.
