# Common File Corruption Patterns & Repair Strategies

This document outlines common types of corruption found in text files and potential strategies for repair.

## 1. Encoding Errors (Mojibake)

*   **Symptoms:** Strange characters replacing expected text (e.g., `â€œ` instead of `"`, `Ã©` instead of `é`). Often happens when a file saved in one encoding (like UTF-8) is read using a different one (like Latin-1 or Windows-1252).
*   **Analysis:** Look for characteristic multi-byte sequences misinterpreted as single-byte characters.
*   **Repair Strategy:**
    1.  Attempt to read the file using common alternative encodings (e.g., `latin-1`, `windows-1252`).
    2.  If successful, re-encode the content correctly, usually to UTF-8.
    3.  Use `write_to_file` with the correctly encoded content.
    *   *(Note: Requires careful identification of the original and target encodings. May need trial-and-error.)*

## 2. Syntax Errors (Basic)

*   **Symptoms:** Mismatched brackets (`{}`, `[]`, `()`), unclosed quotes (`"` or `'`), unterminated comments (`/* ...`), invalid characters within strings, incorrect indentation (YAML).
*   **Analysis:** Scan for common syntax markers. Basic validation for JSON/YAML structure.
*   **Repair Strategy:**
    1.  Attempt to identify the mismatched pair or missing character.
    2.  Add/remove the necessary character(s) to restore basic structure.
    3.  For JSON/YAML, try adding missing commas, closing brackets/braces.
    4.  For indentation errors (YAML), attempt to fix based on surrounding lines (risky).
    *   *(Note: Complex syntax errors often require domain-specific knowledge and should be escalated.)*

## 3. Truncation / Incomplete Files

*   **Symptoms:** File ends abruptly, often mid-structure (e.g., unclosed JSON object, incomplete HTML tag).
*   **Analysis:** Check the end of the file for signs of being cut off. Compare with expected structure if possible.
*   **Repair Strategy:**
    1.  Attempt to add necessary closing syntax (e.g., `}`, `]`, `</tag>`) based on the start of the structure.
    2.  If content is clearly missing, this cannot be fully repaired, but closing the structure might make it partially parsable.
    *   *(Note: Report as partial success at best. Data loss is likely.)*

## 4. Extraneous Characters / Tags

*   **Symptoms:** Unexpected characters, control codes, or markup (like HTML tags) appearing within plain text, code, or data files. Often caused by copy-paste errors or incorrect file conversions.
*   **Analysis:** Look for characters outside the expected set for the file type, or markup in unexpected places.
*   **Repair Strategy:**
    1.  Identify and remove the extraneous characters or tags.
    *   *(Note: Be cautious not to remove valid syntax or content.)*

## 5. Mixed Line Endings

*   **Symptoms:** Inconsistent line endings (CRLF vs. LF) causing issues in some tools or environments.
*   **Analysis:** Difficult to see directly, but may be suspected if tools complain about line endings.
*   **Repair Strategy:**
    1.  Normalize all line endings to a consistent format (usually LF for Linux/macOS, CRLF for Windows). Replace `\r\n` with `\n` or vice-versa.
    *   *(Note: Usually a less critical repair, but can resolve compatibility issues.)*

*(This list provides basic patterns. Complex corruption may require more advanced tools or manual intervention.)*