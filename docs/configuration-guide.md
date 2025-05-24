# Configuration Guide: Ultimate Agentic Coding Tool

This guide outlines key configuration aspects of the Ultimate Agentic Coding Tool. Most day-to-day operations are autonomous, but understanding these configurations can be helpful for advanced users, administrators, or for troubleshooting.

## Table of Contents
1.  [Core System Configuration](#1-core-system-configuration)
    1.  [MCP Server Configuration (`.roo/mcp.json`)](#11-mcp-server-configuration-roomcpjson)
    2.  [ROOPORT Rules (`.roo/rules/` and subdirectories)](#12-rooport-rules-roorules-and-subdirectories)
2.  [Engine-Specific Configuration (Conceptual)](#2-engine-specific-configuration-conceptual)
    1.  [Proactive Orchestration Engine (POE)](#21-proactive-orchestration-engine-poe)
    2.  [Continuous Learning System (CLS)](#22-continuous-learning-system-cls)
    3.  [Agentic RAG Engine](#23-agentic-rag-engine)
    4.  [Ultimate Agentic Orchestrator](#24-ultimate-agentic-orchestrator)
3.  [ConPort Configuration](#3-conport-configuration)
4.  [Environment Variables](#4-environment-variables)
5.  [Modifying Configurations](#modifying-configurations)

## 1. Core System Configuration

### 1.1. MCP Server Configuration (`.roo/mcp.json`)
This is a critical file for ROOPORT's operation and defines how it connects to Model Context Protocol (MCP) servers like `conport` and `vertex-ai-mcp-server`.

*   **`conport` Server:**
    *   **`command`**: Specifies the full command to start the ConPort server. This includes the Python executable path (often within a virtual environment), the path to ConPort's main script, and arguments like `--mode stdio`, `--workspace_id ${workspaceFolder}`, log file paths, and log levels.
    *   **`startup_timeout_ms`**: Timeout for the server to start.
    *   **`permissions`**: Defines which tools and resources ROOPORT modes can access from this MCP server. Typically, `["*"]` grants full access.
*   **`vertex-ai-mcp-server` (and other AI model servers):**
    *   Similar structure for command, timeout, and permissions.
    *   These servers might require environment variables for API keys (e.g., `GOOGLE_APPLICATION_CREDENTIALS` for Vertex AI, `PERPLEXITY_API_KEY` for Perplexity). These are usually set in the environment where the MCP server process is launched, not directly in `mcp.json`.

### 1.2. ROOPORT Rules (`.roo/rules/` and subdirectories)
These Markdown files with TOML frontmatter define the behavior, permissions, and operational guidelines for all ROOPORT modes, including Roo Commander.

*   **Key Integration Rule:** [`.roo/rules-roo-commander/02-ultimate-agentic-integration.md`](../../../.roo/rules-roo-commander/02-ultimate-agentic-integration.md) dictates how Roo Commander utilizes the AI enrichment engines.
*   **Autonomous Mandate:** [`.roo/rules/23-autonomous-execution-mandate.md`](../../../.roo/rules/23-autonomous-execution-mandate.md) enforces non-interactive operation for this integration.
*   Other rules define ConPort usage, logging, session management, etc. Modifications to these files can significantly alter system behavior and should be done with caution by experienced administrators.

## 2. Engine-Specific Configuration (Conceptual)

While the current Python scripts for the engines ([`proactive-orchestration-engine.py`](../../modes/roo-commander/proactive-orchestration-engine.py), [`continuous-learning-system.py`](../../modes/roo-commander/continuous-learning-system.py), [`agentic-rag-engine.py`](../../modes/roo-commander/agentic-rag-engine.py)) have some hardcoded parameters or simple rule loading, a production-grade system would externalize more configurations.

### 2.1. Proactive Orchestration Engine (POE)
*   **Risk/Opportunity Rules:** Currently defined within `OpportunityRiskIdentifier` in the POE script. Future enhancements could load these from external JSON/YAML files or a ConPort custom data category.
*   **Suggestion Thresholds:** Confidence scores or priority levels for automatically actioning suggestions could be configurable.

### 2.2. Continuous Learning System (CLS)
*   **Feedback Categories & Inference Logic:** Defined in `FeedbackCollector`. Could be made more configurable.
*   **Performance Metric Calculation:** Parameters for calculating trends or defining "good" vs. "bad" performance could be externalized.
*   **Refinement Proposal Triggers:** Thresholds for error rates or low ratings that trigger improvement proposals are currently internal logic.

### 2.3. Agentic RAG Engine
*   **Retrieval Strategy Selection Logic:** The `_select_strategy` method in `AgenticRAGEngine` has logic for choosing strategies. This could be made rule-based or configurable.
*   **Keyword Extraction Stop Words:** `StrategicRetriever._extract_keywords` uses a hardcoded stop word list.
*   **Confidence Thresholds:** Values for HIGH, MEDIUM, LOW confidence in retrieval and synthesis are internal.

### 2.4. Ultimate Agentic Orchestrator
*   **Weighting of Confidence Scores:** `_calculate_overall_confidence` uses fixed weights. These could be configurable.
*   **Limits for Suggestions/Actions:** The number of proactive suggestions or next actions presented is currently hardcoded (e.g., top 5).

## 3. ConPort Configuration

ConPort itself is configured primarily through its startup arguments (see Section 1.1). Its behavior related to data storage (SQLite database at `context_portal/context.db`) and logging is also determined at startup.

*   **Vector Data Storage:** The ADR mentions storing embeddings in `conport_vector_data/`. The specific configuration for embedding models and vector store interaction would reside within the AI Enrichment Engine components that perform these tasks, likely leveraging the `vertex-ai-mcp-server` or similar.

## 4. Environment Variables

*   **General ROOPORT:** May have its own set of environment variables.
*   **AI Model Providers:** As mentioned, MCP servers connecting to external AI services (Vertex AI, OpenAI, Anthropic, Perplexity) will require API keys and potentially other configurations (project IDs, model names) to be set as environment variables in their execution shell. These are **not** stored in version control.

## Modifying Configurations

*   **`mcp.json` and `.roo/rules/`:** These are primary configuration points. Changes here directly impact system operation. **Handle with care.**
*   **Engine Python Scripts:** For current internal configurations, modifications would require code changes in the respective Python files. Future versions should aim to externalize more of these settings.
*   **ConPort Data:** Modifying data directly in ConPort (e.g., deleting `Custom Data` entries) can affect engine behavior, as they rely on this data for context and learning. Use ConPort tools for data management.

Always back up configurations before making significant changes. Consult the [Best Practices Guide](./best-practices.md) for guidance on system maintenance.