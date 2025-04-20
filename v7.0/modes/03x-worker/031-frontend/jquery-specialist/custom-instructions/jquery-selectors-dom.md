# jQuery: Selectors & DOM Manipulation

Using jQuery to select and modify HTML elements.

## Core Concept: The jQuery Object `$()`

jQuery simplifies DOM manipulation by providing a powerful function, usually aliased as `$()`, which acts as both a selector and a wrapper for DOM elements.

*   **Selecting:** Pass a CSS selector string to `$()` (e.g., `$('#myId')`, `$('.myClass')`, `$('div p')`). This returns a jQuery object containing *all* matched elements.
*   **Wrapping:** Pass a DOM element or array of elements to `$()` to wrap them in a jQuery object.
*   **Creating:** Pass an HTML string to `$()` to create new elements (e.g., `$('<p>New paragraph</p>')`).

## Selecting Elements

jQuery supports most CSS selectors, plus some custom ones.

*   **Basic:** `#myId`, `.myClass`, `tagName`, `*`
*   **Hierarchy:** `parent > child`, `ancestor descendant`, `prev + next`, `prev ~ siblings`
*   **Attribute:** `[attribute]`, `[attribute="value"]`, `[attribute^="value"]` (starts with), `[attribute$="value"]` (ends with), `[attribute*="value"]` (contains)
*   **Form:** `:input`, `:text`, `:password`, `:radio`, `:checkbox`, `:submit`, `:button`, `:checked`, `:selected`, `:disabled`, `:enabled`
*   **Positional/Filtering:** `:first`, `:last`, `:even`, `:odd`, `:eq(index)`, `:gt(index)`, `:lt(index)`, `:not(selector)`, `:has(selector)`, `:parent` (elements with children), `:empty` (elements with no children)

**Best Practice: Caching Selectors**
If you use the same selector multiple times, store the result in a variable to avoid re-querying the DOM. Prefix jQuery object variables with `$` by convention.

```javascript
// Select elements
const $mainTitle = $('#main-title'); // Select by ID
const $buttons = $('.btn'); // Select by class
const $firstParagraph = $('article p:first'); // Select first p in article
const $emailInput = $('input[type="email"]'); // Select by attribute

// Cache a selection
const $navLinks = $('#main-nav a');
// Now use $navLinks instead of selecting '#main-nav a' again
$navLinks.addClass('nav-item');
```

## DOM Manipulation Methods

jQuery provides concise methods to modify selected elements. Most methods operate on *all* elements in the jQuery object.

*   **Content:**
    *   `.html('<strong>New</strong>')`: Get or set inner HTML.
    *   `.text('New text')`: Get or set text content (safer).
    *   `.val()`: Get or set the value of form elements (`input`, `textarea`, `select`).
*   **Attributes & Properties:**
    *   `.attr('href', 'new-url')`: Get or set HTML attributes.
    *   `.removeAttr('disabled')`: Remove an attribute.
    *   `.prop('checked', true)`: Get or set element properties (like `checked`, `disabled`, `selectedIndex`). Use `.prop()` for boolean attributes/properties.
*   **CSS Classes:**
    *   `.addClass('active')`
    *   `.removeClass('old')`
    *   `.toggleClass('highlight')`
    *   `.hasClass('some-class')`: Returns boolean.
*   **CSS Styles:**
    *   `.css('color', 'red')`: Get or set a single CSS property.
    *   `.css({ color: 'blue', fontWeight: 'bold' })`: Set multiple properties.
*   **Dimensions & Position:**
    *   `.width()`, `.height()`: Get or set CSS width/height.
    *   `.innerWidth()`, `.innerHeight()`: Includes padding.
    *   `.outerWidth()`, `.outerHeight()`: Includes padding & border. `outerWidth(true)` includes margin.
    *   `.offset()`: Get position relative to the document.
    *   `.position()`: Get position relative to the offset parent.
*   **Visibility:**
    *   `.show()`: Displays elements (restores previous `display` value).
    *   `.hide()`: Hides elements (`display: none`).
    *   `.toggle()`: Toggles visibility.
*   **Adding Elements:**
    *   `.append('<span>More</span>')`: Insert content/elements at the end of each selected element.
    *   `.prepend('<span>Start</span>')`: Insert at the beginning.
    *   `.after('<hr>')`: Insert after each selected element.
    *   `.before('<hr>')`: Insert before each selected element.
    *   `.wrap('<div class="wrapper"></div>')`: Wrap each selected element.
*   **Removing Elements:**
    *   `.remove()`: Remove selected elements (and their data/events).
    *   `.empty()`: Remove all child elements from selected elements.
    *   `.unwrap()`: Remove the parent of selected elements.
*   **Traversal:**
    *   `.parent()`, `.parents()`, `.closest(selector)`
    *   `.children([selector])`, `.find(selector)`
    *   `.siblings([selector])`
    *   `.next()`, `.prev()`, `.nextAll()`, `.prevAll()`
    *   `.filter(selector)`, `.not(selector)`, `.has(selector)`

```javascript
// Example Manipulations
$('#user-greeting').text('Welcome Back!');
$('.product-image').attr('alt', 'Updated alt text');
$('input[name="subscribe"]').prop('checked', true);
$('#error-message').addClass('alert alert-danger').text('Invalid input.').show();
$('.item-list').append('<li>New Item</li>');
$('.old-section').remove();
```

jQuery significantly simplifies selecting and manipulating DOM elements compared to vanilla JavaScript's DOM APIs, especially in older browsers. Remember to cache selectors and use efficient selection strategies.