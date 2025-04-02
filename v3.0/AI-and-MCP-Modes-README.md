# 🧠🤖📦 AI & MCP Specialist Modes for Roo Commander

Extend your Roo Code capabilities! This repository contains a set of specialized **Custom Modes** designed for AI, RAG, LLM, and MCP development tasks. These modes are built to seamlessly integrate with the core [Roo Commander Multi-Agent Workflow](link-to-your-main-repo-if-available).

Think of this as adding an AI/ML engineering division and an MCP tools team to your existing virtual development team orchestrated by **👑 Roo Commander**.

## ✨ Prerequisites

This mode set assumes you already have the **main Roo Commander mode set installed and functional** in your Roo Code environment. Key dependencies include:

*   **👑 Roo Commander** (for top-level orchestration)
*   **📋 Project Manager** / **🏗️ Technical Architect** (for delegating tasks to these specialists)
*   **📝 Secretary** (Absolutely crucial for the standardized logging protocol used by these modes)
*   The core `project_journal` directory structure established by `🚦 Project Onboarding` or `✨ Project Initializer`.

## 🧩 How These Modes Integrate

These AI/MCP modes function as **specialists** within the established Roo Commander workflow:

1.  **Delegation:** Tasks related to AI model integration, agent development, RAG setup, or MCP server creation/installation will be delegated by `👑 Roo Commander`, `📋 Project Manager`, or `🏗️ Technical Architect` to the appropriate specialist mode using the `new_task` tool.
2.  **Context:** Delegation messages **must** include clear requirements and reference relevant context files within the `project_journal` (e.g., `project_journal/planning/requirements.md`, `project_journal/planning/architecture.md`).
3.  **Logging Protocol:** These specialists follow the **exact same** technical note logging protocol as the main mode set. They log their work, decisions, and findings into their dedicated, timestamped files within `project_journal/technical_notes/[mode_slug]/YYYY-MM-DD/` by **delegating the write task** to the `📝 Secretary` mode.
4.  **Completion:** Upon task completion, they use `attempt_completion`, providing a summary and **referencing the path(s)** to their saved technical notes, allowing the calling mode to track progress and access details.

Essentially, you plug these specialists into your existing team structure, and they follow the established communication and documentation rules.

## 🛠️ Included AI & MCP Specialist Modes

| Mode                             | Emoji | Role                         | Key Function                                                                 |
| :------------------------------- | :---- | :--------------------------- | :--------------------------------------------------------------------------- |
| `agentic-ai-developer`         | 🧠    | Agentic AI Dev             | Designs & builds AI agents/multi-agent systems (LangChain, AutoGen, etc.)  |
| `rag-database-developer`       | 💾    | RAG Database Dev           | Implements RAG retrieval: vector DBs, embedding, indexing, querying        |
| `openai-api-developer`         | 🤖    | OpenAI API Dev             | Integrates OpenAI models (GPT, DALL-E, Whisper)                            |
| `google-gemini-api-developer`  | 💎    | Google Gemini API Dev      | Integrates Google Gemini models (Pro, Vision)                              |
| `vertex-ai-developer`          | ☁️    | Vertex AI Dev              | Builds/deploys/manages ML solutions on Google Vertex AI                  |
| `mcp-installer`                | 📦    | MCP Server Installer       | Guides installation & setup of community MCP servers                       |
| `prompt-engineer`              | ✍️    | Prompt Engineer            | Designs, refines, and evaluates LLM prompts                                |
| `evaluation-specialist`        | 📊    | AI Evaluation Specialist   | Designs & runs evaluations for AI systems (RAG, Agents, LLMs), defines metrics |

## 📓 Core Principles Remain Consistent

*   **Project Journal:** The `project_journal/` directory remains the central hub for context, planning, and detailed technical history.
*   **Secretary:** The `📝 Secretary` mode is still the designated writer for all technical notes and formal documents within the journal, ensuring structure and consistency.

## 🚀 Installation

1.  **Obtain JSON:** Download the `ai_mcp_modes.json` file (or copy its content) from this repository.
2.  **Locate Existing Config:** Find your main Roo Commander configuration file (either `custom_modes.json` in your global Roo Code settings directory or `.roomodes` in your project root).
3.  **Merge Modes:**
    *   Open your existing configuration file.
    *   Find the main `"customModes": [` array.
    *   Copy **all** the mode objects `{...}` from the `ai_mcp_modes.json` file's `"customModes"` array.
    *   Paste these copied mode objects **inside** your existing `"customModes": [...]` array, ensuring you add a comma `,` after the last existing mode object if needed.
    *   **Do NOT overwrite** your existing modes; you are *adding* these new modes to the list.
4.  **Save:** Save the modified configuration file.
5.  **Reload Roo Code:** Restarting VS Code or using the Roo Code "Reload Custom Modes" command (if available) should make the new modes accessible.

## ▶️ Example Usage

Imagine the `📋 Project Manager` needs to add a RAG component:

> **Project Manager -> `new_task` -> `rag-database-developer`:**
>
> `Task: Implement RAG retrieval for project documentation.`
> `Requirements: Use ChromaDB, sentence-transformer embeddings. Index all markdown files in ./docs/. Provide retrieval function.`
> `Context Refs: project_journal/planning/requirements.md#section-3, project_journal/planning/architecture.md#rag-component`

The `rag-database-developer` would then perform the task, log its progress/findings by delegating writes to `secretary` (e.g., `project_journal/technical_notes/rag-database-developer/2025-04-02/2025-04-02_14-15-00_rag-database-developer_indexing-setup.md`), and finally report completion via `attempt_completion` referencing that notes file.

## ⚠️ Important Considerations

*   **Complexity:** Adding more specialized agents increases the complexity of the overall system orchestration.
*   **LLM Capabilities:** The success of these modes relies heavily on the underlying LLM's ability to understand specific AI/ML concepts, follow detailed instructions, and use tools effectively.
*   **Tooling:** Some modes may benefit significantly from specific `mcp` tools (e.g., for interacting with cloud platforms, specific databases, or ML frameworks). Ensure relevant MCP servers are running if needed.
*   **Token Usage:** As with the main set, detailed instructions and logging consume tokens. Monitor usage.
*   **Dynamic Paths:** Ensure the LLM reliably generates the correct timestamped file paths when delegating writes to the `secretary`.

---

Enhance your Roo Commander workflow with these specialized AI and MCP modes to tackle more advanced development challenges!
