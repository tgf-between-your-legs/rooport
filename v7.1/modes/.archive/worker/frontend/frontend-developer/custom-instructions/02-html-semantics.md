# HTML: Semantic Elements Quick Reference

Using HTML tags that convey meaning and structure, improving accessibility, SEO, and code maintainability.

## Core Concept

Semantic HTML means using HTML elements according to their intended purpose and meaning, rather than just for presentation (like using `<div>` for everything). This helps browsers, assistive technologies (like screen readers), and search engines understand the structure and importance of your content.

**Always choose the HTML element that most accurately describes the content you are marking up.** Avoid using generic `<div>` and `<span>` elements when a more specific semantic tag is appropriate.

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
    *   `<h1>` - `<h6>`: Section headings, defining the document outline. Use them hierarchically (don't skip levels, start with `<h1>`).
    *   `<p>`: A paragraph of text.
    *   `<blockquote>`: A section quoted from another source. Use `cite` attribute for source URL.
    *   `<figure>` &amp; `<figcaption>`: For embedding illustrations, diagrams, photos, code listings, etc., optionally with a caption (`<figcaption>`).
    *   `<address>`: Contact information for the nearest `<article>` or `<body>` ancestor.
    *   `<time>`: Represents a specific period in time. Use `datetime` attribute for machine-readable format (e.g., `<time datetime="2025-12-25">Christmas Day</time>`).
    *   `<em>`: Stress emphasis (changes meaning). Renders as italic by default.
    *   `<strong>`: Strong importance, seriousness, or urgency. Renders as bold by default.
    *   `<mark>`: Text marked or highlighted for reference.
    *   `<abbr>`: Abbreviation or acronym (use `title` attribute for full expansion, e.g., `<abbr title="HyperText Markup Language">HTML</abbr>`).
    *   `<cite>`: Title of a creative work (book, paper, song, etc.). Renders as italic by default.
*   **Lists:**
    *   `<ul>`: Unordered list (bullets).
    *   `<ol>`: Ordered list (numbers/letters). Use `start`, `reversed`, `type` attributes if needed.
    *   `<li>`: List item (must be child of `<ul>` or `<ol>`).
    *   `<dl>`, `<dt>`, `<dd>`: Description list (term/definition pairs).
*   **Forms:**
    *   `<form>`: Contains form controls.
    *   `<label>`: Associates text label with a form control (use `for` attribute matching control's `id`). Crucial for accessibility.
    *   `<input>`: Various input types (`text`, `email`, `password`, `checkbox`, `radio`, `submit`, `date`, `number`, etc.).
    *   `<textarea>`: Multi-line text input.
    *   `<select>` &amp; `<option>`: Dropdown list.
    *   `<button>`: Clickable button (use `type="submit"`, `type="reset"`, or `type="button"`). Generally preferred over `<input type="button">`.
    *   `<fieldset>` &amp; `<legend>`: Group related form controls (like radio buttons), with `<legend>` providing a caption for the group.
*   **Other:**
    *   `<a>`: Anchor/Hyperlink. Use `href` attribute for the destination URL.
    *   `<img>`: Image. Requires `src` (source URL) and `alt` (alternative text) attributes.
    *   `<table>`, `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<th>`, `<td>`: For tabular data.

## Why Use Semantic HTML?

*   **Accessibility:** Screen readers use semantic tags to navigate and understand page structure, making content accessible to visually impaired users and others using assistive tech. Labels are essential for form controls.
*   **SEO:** Search engines use semantic tags to better understand the content and context of your page, potentially improving rankings.
*   **Maintainability:** Code becomes easier to read, understand, and maintain when structure reflects meaning.
*   **Styling:** While not their primary purpose, semantic tags provide default styling and hooks for CSS (though class-based styling is generally preferred for robustness and lower specificity).

When in doubt, consult MDN Web Docs for detailed information on specific HTML elements.