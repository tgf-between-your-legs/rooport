# Character Encoding Reference

A brief guide to common character encodings and related issues relevant to file repair.

## Common Encodings

*   **UTF-8:**
    *   **Description:** The dominant encoding on the web. Variable-width (1-4 bytes per character). Backwards compatible with ASCII for the first 128 characters. Can represent characters from virtually all languages.
    *   **Identification:** Often the default. Files starting with a Byte Order Mark (BOM) `EF BB BF` are explicitly UTF-8. Absence of BOM doesn't rule it out.
*   **ASCII:**
    *   **Description:** 7-bit encoding, representing 128 characters (English letters, numbers, basic punctuation, control codes). Cannot represent accented characters or characters from other languages.
    *   **Identification:** If a file only contains characters with code points 0-127, it's ASCII-compatible (and valid UTF-8).
*   **Latin-1 (ISO-8859-1):**
    *   **Description:** 8-bit single-byte encoding. Covers ASCII plus accented characters and symbols used in Western European languages.
    *   **Identification:** Often a default in older systems/protocols. Common source of Mojibake when UTF-8 is expected (e.g., `Ã©` instead of `é`).
*   **Windows-1252 (CP-1252):**
    *   **Description:** Microsoft's 8-bit extension of Latin-1. Includes additional characters like curly quotes (`“”`), em dash (`—`), euro sign (`€`) in the 0x80-0x9F range (which is reserved for control codes in Latin-1).
    *   **Identification:** Very common on Windows. Another frequent source of Mojibake if misinterpreted as UTF-8 or Latin-1.

## Common Issues & Repair

*   **Mojibake (Garbled Text):**
    *   **Cause:** File saved in one encoding (e.g., UTF-8) but read/interpreted using another (e.g., Latin-1, Windows-1252).
    *   **Repair:**
        1.  Identify the likely *actual* encoding (often UTF-8 if multi-byte sequences like `Ã©` appear).
        2.  Identify the encoding it was *incorrectly read as* (often Latin-1 or Windows-1252).
        3.  Attempt to reverse the process: Read the file using the *incorrect* encoding, then encode the resulting (garbled) string back into bytes using that same incorrect encoding, and *finally* decode those bytes using the *correct* original encoding (e.g., UTF-8).
        4.  Alternatively, try reading the original file directly with different common encodings (`utf-8`, `latin-1`, `windows-1252`) until the text looks correct.
        5.  Once correct content is obtained, save it explicitly as UTF-8 using `write_to_file`.
*   **Invalid Characters:**
    *   **Cause:** Characters present that are not valid within the declared or assumed encoding (e.g., bytes > 127 in a file declared as ASCII, invalid byte sequences in UTF-8). Could also be binary data mixed with text.
    *   **Repair:**
        1.  Attempt to identify and remove the invalid characters. Be cautious not to remove valid multi-byte UTF-8 sequences.
        2.  If binary data is suspected, repair might be impossible without understanding the format. Removal might be the only option, leading to data loss.

## Tools & Techniques

*   **`read_file`:** Use this first to inspect the raw content. Look for Mojibake patterns or obviously invalid bytes.
*   **Encoding Detection Libraries (Conceptual):** Libraries like Python's `chardet` can *guess* the encoding, but are not always accurate. This mode typically relies on pattern matching and trial-and-error with common encodings.
*   **Text Editors:** Many text editors allow trying different encodings to view a file or explicitly saving with a specific encoding.

*(Always aim to save repaired files as UTF-8 unless there's a strong reason otherwise.)*