# Typography Guidelines

Recommendations for selecting and pairing fonts, and setting type scales for readability and visual hierarchy.

## Font Selection & Pairing

*   **Limit Fonts:** Use a maximum of 2-3 font families for simplicity and performance.
*   **Choose Purposefully:** Select fonts that match the project's mood and brand identity (e.g., Serif for traditional/formal, Sans-serif for modern/clean, Display for headlines).
*   **Pairing:**
    *   Combine a Serif heading font with a Sans-serif body font (or vice-versa) for contrast.
    *   Use different weights or styles within the *same* font family for hierarchy.
    *   Ensure paired fonts have complementary moods and x-heights.
    *   Test pairings at different sizes.
*   **Readability:** Prioritize readability for body text. Choose fonts with clear letterforms and appropriate x-height.
*   **Licensing:** Ensure fonts used are properly licensed for web use (e.g., Google Fonts, Adobe Fonts, commercially licensed fonts).

## Recommended Pairings (Examples)

*   **Heading:** Playfair Display (Serif) / **Body:** Lato (Sans-serif) - Elegant, readable.
*   **Heading:** Montserrat (Sans-serif) / **Body:** Merriweather (Serif) - Modern, sturdy.
*   **Heading:** Oswald (Sans-serif Condensed) / **Body:** Roboto (Sans-serif) - Strong headlines, clean body.
*   **Monospace (for code):** Fira Code, Source Code Pro

## Type Scale & Hierarchy

*   **Establish a Scale:** Define a consistent scale for font sizes (e.g., using a modular scale like 1.25 or 1.333). This creates rhythm and hierarchy.
    *   Example Scale (Base: 16px): 12px (small), 16px (base), 20px (h4), 25px (h3), 31px (h2), 39px (h1).
*   **Use Size & Weight:** Differentiate headings (h1-h6) and body text using distinct sizes and font weights (e.g., bold headings, regular body).
*   **Line Height:** Set appropriate line height (leading) for readability, typically 1.4-1.6 times the font size for body text.
*   **Line Length:** Aim for comfortable line lengths (around 45-75 characters per line) for body text. Control this with container widths.
*   **Paragraph Spacing:** Use margins or padding between paragraphs for clear separation (often equal to the base line height).

## Implementation (CSS)

*   **Use `rem` or `em`:** Prefer relative units for font sizes to allow user scaling and maintain proportions. Set base font size on `<html>` or `:root`.
*   **Font Loading:** Use `@font-face` correctly or rely on font service providers (Google Fonts) for efficient loading. Consider `font-display: swap;` for better perceived performance.
*   **CSS Variables:** Define type scale, font families, and weights using CSS Custom Properties for easy maintenance.
    ```css
    :root {
      --font-family-heading: 'Playfair Display', serif;
      --font-family-body: 'Lato', sans-serif;
      --font-size-base: 1rem; /* Typically 16px */
      --line-height-base: 1.5;
      --font-size-h1: 2.441rem;
      /* ... other sizes */
    }

    body {
      font-family: var(--font-family-body);
      font-size: var(--font-size-base);
      line-height: var(--line-height-base);
    }

    h1, h2, h3, h4, h5, h6 {
      font-family: var(--font-family-heading);
      margin-bottom: 0.5em; /* Example spacing */
    }

    h1 { font-size: var(--font-size-h1); }
    /* ... other heading sizes */
    ```

*(Consult web typography best practices and resources like Google Fonts for more detailed guidance.)*