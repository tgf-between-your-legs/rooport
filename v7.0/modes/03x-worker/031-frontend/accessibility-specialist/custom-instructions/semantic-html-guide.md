# Semantic HTML Guide for Accessibility

Using HTML elements according to their meaning to improve accessibility and structure.

## Core Concept

Semantic HTML means using HTML elements for their intended purpose, conveying meaning about the structure and type of content they contain. This provides essential context for assistive technologies (like screen readers) and search engines, improving accessibility and SEO beyond just visual presentation.

**Why Use Semantic HTML?**

*   **Accessibility:** Screen readers and other AT rely on semantic elements to understand page structure, announce content types (headings, lists, tables, forms), and enable navigation (e.g., jumping between headings or landmarks).
*   **Maintainability:** Code becomes more readable and easier to understand and style.
*   **SEO:** Search engines use semantic structure to better understand content relevance.
*   **Browser Functionality:** Some elements have built-in browser behaviors (e.g., form validation, keyboard handling for `<button>`).

**Avoid `<div>` and `<span>` Soup:** Don't use generic `<div>` or `<span>` elements when a more specific semantic element exists. Use ARIA roles only as a fallback when no suitable native HTML element is available or when enhancing existing semantics.

## Key Semantic Elements

**1. Document Structure & Landmarks:**

*   **`<header>`:** Introductory content for a page or section (often contains site branding, navigation). Can be used multiple times (e.g., page header, article header). Maps to `role="banner"` if it's the top-level site header.
*   **`<nav>`:** Contains major navigation links (primary site navigation, table of contents, breadcrumbs). Maps to `role="navigation"`.
*   **`<main>`:** The main, unique content of the document. There should only be **one** visible `<main>` element per page. Maps to `role="main"`.
*   **`<article>`:** Self-contained content that could potentially be distributed independently (e.g., blog post, news article, forum comment). Can be nested.
*   **`<section>`:** Represents a thematic grouping of content, typically with a heading. Use when there isn't a more specific semantic element. Don't use just for styling hooks (use `<div>` for that).
*   **`<aside>`:** Content tangentially related to the main content around it (e.g., sidebar, pull quotes, related links). Maps to `role="complementary"` if not nested within an `<article>`.
*   **`<footer>`:** Footer for a page or section (often contains copyright, author info, related links). Maps to `role="contentinfo"` if it's the top-level site footer.
*   **`<h1>` - `<h6>`:** Headings define the structure and hierarchy of content. Use them in logical order (don't skip levels, e.g., `<h1>` followed by `<h3>`). `<h1>` is typically the main page title.

**2. Text Content:**

*   **`<p>`:** Paragraph of text.
*   **`<ul>`, `<ol>`, `<li>`:** Unordered and ordered lists. Use for groups of related items.
*   **`<dl>`, `<dt>`, `<dd>`:** Description lists (term/definition pairs).
*   **`<blockquote>`:** Represents a block of quoted content from another source. Use `<cite>` for the source.
*   **`<em>`:** Stress emphasis (changes meaning). Often rendered as italics.
*   **`<strong>`:** Strong importance, seriousness, or urgency. Often rendered as bold.
*   **`<cite>`:** Title of a creative work (book, article, song).
*   **`<q>`:** Short inline quotation.
*   **`<code>`:** Inline code snippet.
*   **`<pre>`:** Preformatted text block (preserves whitespace), often used with `<code>`.
*   **`<time>`:** Represents a specific period in time. Use `datetime` attribute for machine-readable format.
*   **`<address>`:** Contact information for the nearest `<article>` or `<body>` ancestor.

**3. Interactive Elements & Forms:**

*   **`<button>`:** Represents a clickable button used for actions within an interface (submitting forms, triggering JS actions). Natively keyboard accessible and focusable.
*   **`<a>`:** Hyperlink to another resource (URL). Use `href` attribute. Natively keyboard accessible and focusable. Use `<button>` if the element performs an action *within* the current page rather than navigating.
*   **`<form>`:** Represents a form for user submission.
*   **`<label>`:** Represents a caption for an item in a user interface. Crucial for associating text labels with form controls using the `for` attribute (`<label for="id_of_input">`). Clicking the label focuses the input.
*   **`<input>`:** Various types of input fields (`type="text"`, `"email"`, `"password"`, `"checkbox"`, `"radio"`, `"number"`, `"date"`, `"submit"`, `"button"`, etc.). Use appropriate types.
*   **`<textarea>`:** Multi-line text input.
*   **`<select>`, `<option>`, `<optgroup>`:** Dropdown list.
*   **`<fieldset>`, `<legend>`:** Group related form controls, with `<legend>` providing a caption for the group.

**4. Embedded Content:**

*   **`<img>`:** Embeds an image. **Requires `alt` attribute** for accessibility (provide descriptive text or `alt=""` for decorative images).
*   **`<figure>`, `<figcaption>`:** Embed self-contained content (like an image, chart, code block) optionally with a caption (`<figcaption>`).
*   **`<audio>`, `<video>`:** Embed audio or video. Provide captions/subtitles and transcripts for accessibility. Use `<track>` element.
*   **`<iframe>`:** Embed another HTML document. Ensure the `title` attribute describes the frame's content.

By prioritizing semantic HTML, you build a more robust, maintainable, and accessible foundation for web content and applications.

*(Refer to MDN Web Docs for detailed information on HTML elements.)*