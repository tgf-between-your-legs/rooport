# Roo Commander

Roo Commander is a VS Code extension designed to enhance developer productivity by providing specialised AI assistants (modes) tailored for various software development tasks. It leverages large language models (LLMs) to offer context-aware support directly within the IDE.

## Purpose

The primary goal of Roo Commander is to streamline workflows by offering intelligent assistance for coding, debugging, documentation, architecture design, project management, and more. Each "mode" acts as a specialised expert, equipped with specific tools and instructions to effectively handle tasks within its domain.

## Setup and Usage

1.  **Installation:** Install Roo Commander from the VS Code Marketplace (link to be added once published).
2.  **Using Modes:**
    *   Access Roo Commander via its sidebar icon or command palette.
    *   Select a mode relevant to your current task (e.g., `code` for writing code, `technical-writer` for documentation, `git-manager` for version control).
    *   Interact with the selected mode through the chat interface, providing instructions or asking questions.
    *   Modes can utilise various tools (file access, terminal execution, web searches, etc.) to accomplish tasks, often requiring user approval for actions.

## Customisation

Roo Commander is highly customisable:

*   **Custom Instructions:** Modify the behaviour of all modes or specific modes by editing the `custom_instructions_*.md` files (e.g., `custom_instructions_for_all_modes.md`, `custom_instructions_for_code_mode.md`). These files allow you to provide global or mode-specific guidelines, preferences, and constraints.
*   **Modes:** The `modes/` directory contains JSON configuration files for each available mode. You can:
    *   Modify existing modes by editing their respective `.json` files.
    *   Create new modes by adding new `.json` files following the established schema. (Refer to `ROO_MODE_SYSTEM.md` for details on mode creation).

## Available Modes (Examples)

Roo Commander comes with a suite of pre-defined modes, including:

*   `code`: General software engineering tasks.
*   `architect`: System design and planning.
*   `ask`: Answering technical questions.
*   `debug`: Diagnosing and fixing issues.
*   `technical-writer`: Creating documentation.
*   `git-manager`: Handling Git operations.
*   `frontend-developer`: UI and client-side logic.
*   `api-developer`: Designing and building APIs.

Explore the `modes/` directory for the full list and their configurations.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please refer to CONTRIBUTING.md (to be created) for guidelines.

## Future Plans

*   Expand the range of available modes.
*   Enhance tool capabilities.
*   Improve context understanding and memory.