# Roo Commander Modes Repository

This repository contains a collection of specialised AI assistant "modes" designed for use with the Roo Code VS Code extension. These modes enhance developer productivity by providing tailored support for various software development tasks directly within the IDE.

**Important:** This repository provides the *configuration files* for custom modes. It is **not** a VS Code extension to be installed directly. You need to have the Roo Code extension already installed in VS Code to use these modes.

## Purpose

The primary goal of these modes is to streamline workflows by offering intelligent assistance for coding, debugging, documentation, architecture design, project management, and more. Each mode acts as a specialised expert, equipped with specific tools and instructions to effectively handle tasks within its domain.

## Adding These Modes to Roo Code

To use the modes defined in this repository with your Roo Code extension, follow these steps:

1.  **Copy Mode Configuration:** Open the `cline_custom_modes.json` file located in this repository. Select and copy its entire JSON content.
2.  **Open Roo Code Panel:** In VS Code, open the Roo Code panel (usually found in the sidebar).
3.  **Access Prompts View:** Click the 'Prompts' icon within the Roo Code panel (it looks like a book or page icon).
4.  **Edit Global Modes:** In the 'Prompts' view that appears, locate the 'Modes' section and click the 'Edit Global Modes' icon (it looks like curly braces `{}`).
5.  **Paste Configuration:** This action will open your personal `cline_custom_modes.json` configuration file in the VS Code editor. Paste the JSON content you copied in Step 1 into this file.
    *   If your file was empty, you can simply paste the content.
    *   If you already have existing custom modes defined, you will need to carefully merge the copied JSON array with your existing array, ensuring the final structure remains a valid JSON array of mode objects.
6.  **Save:** Save the changes to your `cline_custom_modes.json` file.
7.  **Verify:** The new modes from this repository should now appear in the mode selection dropdown within Roo Code.

## Customisation

You can further customise the behaviour of these modes:

*   **Custom Instructions:** Modify the behaviour of all modes or specific modes by editing the `custom_instructions_*.md` files (e.g., `custom_instructions_for_all_modes.md`, `custom_instructions_for_code_mode.md`). These files allow you to provide global or mode-specific guidelines, preferences, and constraints. *Note: Custom instructions are typically managed within the Roo Code extension settings, but the files here serve as a reference or starting point.*
*   **Modes:** The `modes/` directory contains the individual JSON configuration files for each mode included in `cline_custom_modes.json`. You can:
    *   Modify existing modes by editing their respective `.json` files (remember to update `cline_custom_modes.json` accordingly if you change fundamental properties like the `slug`).
    *   Create new modes by adding new `.json` files following the established schema and including them in the `cline_custom_modes.json` array. (Refer to `ROO_MODE_SYSTEM.md` for details on mode creation).

## Available Modes (Examples)

This repository includes modes such as:

*   `code`: General software engineering tasks.
*   `architect`: System design and planning.
*   `ask`: Answering technical questions.
*   `debug`: Diagnosing and fixing issues.
*   `technical-writer`: Creating documentation.
*   `git-manager`: Handling Git operations.
*   `frontend-developer`: UI and client-side logic.
*   `api-developer`: Designing and building APIs.

Explore the `modes/` directory and `cline_custom_modes.json` for the full list and their configurations.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please refer to CONTRIBUTING.md (to be created) for guidelines.

## Future Plans

*   Expand the range of available modes.
*   Enhance tool capabilities within modes.
*   Refine mode instructions for better performance.