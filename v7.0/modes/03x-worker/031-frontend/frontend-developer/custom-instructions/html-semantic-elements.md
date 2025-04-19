# HTML: Semantic Elements Quick Reference

Using HTML tags that convey meaning and structure, improving accessibility and SEO.

## Core Concept

Semantic HTML means using HTML elements according to their intended purpose and meaning, rather than just for presentation. This helps browsers, assistive technologies (like screen readers), and search engines understand the structure and importance of your content.

Avoid using generic `<div>` and `<span>` elements for everything. Choose tags that best describe the content they contain.

## Key Semantic Elements

*   **Page Structure:**
    *   `<header>`: Introductory content for a page or section (logos, navigation, headings). Can be used multiple times.
    *   `<nav>`: Contains major navigation links (primary site navigation, table of contents, etc.).
    *   `<main>`: The main, unique content of the document. There should only be **one** visible `<main>` element per page.
    *   `<article>`: Self-contained content that could potentially be distributed independently (e.g., blog post, news article, forum post). Often includes its own `<header>` and `<footer>`.
    *   `<section>`: Represents a thematic grouping of content, typically with a heading (`<h1>`-`<h6>`). Use when there isn't a more specific semantic element.
    *   `<aside>`: Content tangentially related to the main content around it (e.g., sidebar, pull quotes, related links).
    *   `<footer>`: Footer content for a page or section (copyright, author info, related links). Can be used multiple times.
*   **Text Content:**
    *   `<h1>` - `<h6>`: Section headings, defining the document outline. Use them hierarchically (don't skip levels).
    *   `<p>`: A paragraph of text.
    *   `<blockquote>`: A section quoted from another source. Use `cite` attribute for source URL.
    *   `<figure>` & `<figcaption>`: For embedding illustrations, diagrams, photos, code listings, etc., optionally with a caption (`<figcaption>`).
    *   `<address>`: Contact information for the nearest `<article>` or `<body>` ancestor.
    *   `<time>`: Represents a specific period in time. Use `datetime` attribute for machine-readable format.
    *   `<em>`: Stress emphasis (changes meaning).
    *   `<strong>`: Strong importance, seriousness, or urgency.
    *   `<mark>`: Text marked or highlighted for reference.
    *   `<abbr>`: Abbreviation or acronym (use `title` attribute for full expansion).
    *   `<cite>`: Title of a creative work (book, paper, song, etc.).
*   **Lists:**
    *   `<ul>`: Unordered list.
    *   `<ol>`: Ordered list (use `start`, `reversed`, `type` attributes if needed).
    *   `<li>`: List item (must be child of `<ul>` or `<ol>`).
    *   `<dl>`, `<dt>`, `<dd>`: Description list (term/definition pairs).
*   **Forms:**
    *   `<form>`: Contains form controls.
    *   `<label>`: Associates text label with a form control (use `for` attribute matching control's `id`). Crucial for accessibility.
    *   `<input>`: Various input types (`text`, `email`, `password`, `checkbox`, `radio`, `submit`, `date`, etc.).
    *   `<textarea>`: Multi-line text input.
    *   `<select>` & `<option>`: Dropdown list.
    *   `<button>`: Clickable button (use `type="submit"`, `type="reset"`, or `type="button"`).
    *   `<fieldset>` & `<legend>`: Group related form controls, with `<legend>` providing a caption.

## Why Use Semantic HTML?

*   **Accessibility:** Screen readers use semantic tags to navigate and understand page structure, making content accessible to visually impaired users. Labels are essential for form controls.
*   **SEO:** Search engines use semantic tags to better understand the content and context of your page, potentially improving rankings.
*   **Maintainability:** Code becomes easier to read and understand when structure reflects meaning.
*   **Styling:** While not their primary purpose, semantic tags provide hooks for CSS styling (though class-based styling is generally preferred for robustness).

Always choose the HTML element that most accurately describes the content you are marking up. When in doubt, consult MDN Web Docs.