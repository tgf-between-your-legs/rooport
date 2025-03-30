Ensure what we are making is modular and easy to extend the functionality. include commenting and description in each file about how it works, its purpose and how it relates to other files and components. keep component size reasonably small for easier management and editing. use SOLID development principles. Use EN-AU spelling and grammar. When using the terminal just send one command a time. You can use the terminal for file management as normal for linux and connecting to firebase. Unless told otherwise you will be using the most recent version of Material UI (MUI).


--- CRITICAL INSTRUCTION FOR SHELL COMMAND GENERATION ---

**Mandatory Rule:** When generating *any* command string intended for execution in a standard Linux/Unix shell terminal (like bash, zsh, etc.), you **MUST** output **raw, literal special characters**. You **MUST NEVER** use their HTML-encoded equivalents (HTML entities).

**Reason:** Using HTML entities (e.g., `&amp;&amp;`, `>`, `<`, `&#124;`) instead of literal characters (`&&`, `>`, `<`, `|`) will cause **critical syntax errors** and complete command failure when executed in the terminal.

**Explicit Character Mapping (Examples - Follow STRICTLY):**

*   Use literal `&&` (for logical AND), **NEVER** `&amp;&amp;`
*   Use literal `|` (for pipe), **NEVER** `&#124;` or `&vert;`
*   Use literal `>` (for output redirection), **NEVER** `>`
*   Use literal `<` (for input redirection), **NEVER** `<`
*   Use literal `;` (for command separation), **NEVER** `&semi;`
*   Use literal `"` (double quote), **NEVER** `"`
*   Use literal `'` (single quote), **NEVER** `&apos;` or `&#39;`
*   Use literal `$` (for variable expansion), **NEVER** `&#36;`
*   (Apply this principle to *all* non-alphanumeric characters used as shell operators or syntax).

**Contextual Application:** This rule is **absolute** and applies *especially* when generating commands within interactive coding tools or assistants like the 'Roo code editor', particularly in fields or blocks labeled 'Run Command', 'Execute Command', 'Terminal Command', or where the obvious intent is direct shell execution.

**Final Check:** Before outputting any command string, verify it contains only **literal shell syntax characters**, suitable for direct copy-pasting and execution in a standard terminal. Assume the target environment **cannot** interpret HTML entities.

--- END CRITICAL INSTRUCTION ---