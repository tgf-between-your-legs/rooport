# HTML Elements & CSS Selectors Reference

This document provides a quick reference for common HTML elements and CSS selectors, useful for defining content extraction strategies in `crawl4ai` (though `crawl4ai` often extracts main content automatically, specific selectors might be needed for fine-grained extraction or filtering).

## Common HTML Elements

*   `<h1>`, `<h2>`, ... `<h6>`: Headings
*   `<p>`: Paragraph
*   `<a>`: Anchor (link) - Key attribute: `href`
*   `<img>`: Image - Key attributes: `src`, `alt`
*   `<div>`: Division (generic container)
*   `<span>`: Inline container
*   `<ul>`: Unordered list
*   `<ol>`: Ordered list
*   `<li>`: List item
*   `<table>`: Table
*   `<tr>`: Table row
*   `<th>`: Table header cell
*   `<td>`: Table data cell
*   `<form>`: Input form
*   `<input>`: Input field (text, password, checkbox, radio, submit, etc.) - Key attributes: `type`, `name`, `value`
*   `<textarea>`: Multiline text input
*   `<select>`: Dropdown list - Contains `<option>` elements
*   `<button>`: Button
*   `<header>`, `<footer>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<section>`: Semantic layout elements

## Common CSS Selectors

*   **Tag Name:** Selects all elements of that type.
    *   `p` (selects all paragraphs)
    *   `div` (selects all divs)
*   **Class Name:** Selects elements with a specific class attribute. Uses a dot (`.`).
    *   `.article-content` (selects elements with `class="article-content"`)
    *   `p.highlight` (selects paragraphs with `class="highlight"`)
*   **ID:** Selects a single element with a specific ID attribute. Uses a hash (`#`). Should be unique per page.
    *   `#main-navigation` (selects the element with `id="main-navigation"`)
*   **Attribute Selector:** Selects elements based on attributes and their values.
    *   `a[target="_blank"]` (selects links opening in a new tab)
    *   `input[type="submit"]` (selects submit buttons)
    *   `[data-testid="user-profile"]` (selects elements with a specific data attribute)
*   **Descendant Combinator:** Selects elements nested within another element. Uses a space.
    *   `div p` (selects all paragraphs inside any div)
    *   `.content a` (selects all links inside elements with `class="content"`)
*   **Child Combinator:** Selects direct children of an element. Uses `>`.
    *   `ul > li` (selects list items that are direct children of an unordered list)
*   **Adjacent Sibling Combinator:** Selects an element immediately following another. Uses `+`.
    *   `h2 + p` (selects the first paragraph immediately after an h2 heading)
*   **General Sibling Combinator:** Selects elements that follow another and share the same parent. Uses `~`.
    *   `h2 ~ p` (selects all paragraphs that follow an h2 and share the same parent)
*   **Pseudo-classes:** Select elements based on their state or position.
    *   `a:hover` (link when hovered)
    *   `input:focus` (input field when focused)
    *   `li:first-child` (first list item in a list)
    *   `p:nth-child(2)` (the second paragraph among its siblings)
*   **Pseudo-elements:** Select parts of an element.
    *   `p::first-line`
    *   `::before`, `::after`

*(Refer to MDN Web Docs for a comprehensive guide to CSS Selectors.)*