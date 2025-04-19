# Common File Format Syntax & Validation (Basic Reference)

This provides basic syntax rules for common text-based formats to aid in repair attempts.

## JSON (JavaScript Object Notation)

*   **Structure:** Key-value pairs. Objects enclosed in `{}`. Arrays enclosed in `[]`.
*   **Keys:** Must be strings in double quotes (`"`).
*   **Values:** Can be strings (`"`), numbers (`123`, `1.23`), booleans (`true`, `false`), arrays (`[]`), or other JSON objects (`{}`). `null` is also valid.
*   **Separators:** Keys and values separated by colon (`:`). Key-value pairs and array elements separated by comma (`,`). No trailing commas allowed.
*   **Validation:** Check for balanced brackets/braces, correctly quoted keys/strings, valid value types, and correct use of commas. Many online validators exist.

## YAML (YAML Ain't Markup Language)

*   **Structure:** Key-value pairs. Structure defined by **indentation** (spaces, not tabs).
*   **Keys:** Typically strings, colon (`:`) follows the key.
*   **Values:** Can be strings (often unquoted), numbers, booleans (`true`, `false`, `yes`, `no`), lists/sequences, dictionaries/mappings.
*   **Lists/Sequences:** Items start with a hyphen and space (`- `) at the same indentation level.
*   **Dictionaries/Mappings:** Key-value pairs indented under a parent key.
*   **Comments:** Start with `#`.
*   **Validation:** Primarily check for consistent indentation. Mismatched indentation is the most common error. Also check for correct list/mapping syntax.

## XML (Extensible Markup Language)

*   **Structure:** Tree structure defined by tags. Elements enclosed in opening (`<tag>`) and closing (`</tag>`) tags. Self-closing tags (`<tag/>`) are possible.
*   **Tags:** Case-sensitive. Must be properly nested.
*   **Root Element:** Must have exactly one top-level root element.
*   **Attributes:** Key-value pairs within the opening tag (`<tag attribute="value">`). Values usually in quotes (`"` or `'`).
*   **Content:** Text content appears between opening and closing tags.
*   **Special Characters:** Characters like `<`, `>`, `&` must be escaped (`<`, `>`, `&amp;`).
*   **Comments:** Enclosed in `<!-- ... -->`.
*   **Validation:** Check for balanced tags, proper nesting, a single root element, correctly quoted attributes, and proper escaping.

## Markdown

*   **Structure:** Primarily plain text with formatting conventions.
*   **Headings:** `# H1`, `## H2`, etc.
*   **Lists:** `* item` or `- item` (unordered), `1. item` (ordered). Indentation creates nested lists.
*   **Emphasis:** `*italic*` or `_italic_`, `**bold**` or `__bold__`.
*   **Links:** `[text](url)`.
*   **Images:** `![alt text](url)`.
*   **Code:** Inline `code`, fenced code blocks ``` ```.
*   **Blockquotes:** `> quote`.
*   **Validation:** Less strict than data formats. Look for broken link syntax, incorrect list indentation, unclosed code fences or emphasis markers.

*(This is a very basic overview. Refer to official specifications for complete details.)*