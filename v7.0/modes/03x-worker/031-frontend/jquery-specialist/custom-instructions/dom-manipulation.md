# jQuery DOM Manipulation Quick Reference

Common methods for selecting and manipulating HTML elements using jQuery.

## Selecting Elements (`$()`)

*   **By ID:** `$('#myElement')` (Fastest)
*   **By Class:** `$('.myClass')`
*   **By Tag Name:** `$('div')`
*   **By Attribute:** `$('input[type="text"]')`, `$('a[target="_blank"]')`
*   **Hierarchy:**
    *   Descendant: `$('#container p')` (Selects `<p>` inside `#container`)
    *   Child: `$('#container > p')` (Selects direct child `<p>` of `#container`)
    *   Adjacent Sibling: `$('h2 + div')` (Selects `<div>` immediately following `<h2>`)
    *   General Sibling: `$('h2 ~ p')` (Selects all `<p>` siblings following `<h2>`)
*   **Filtering:**
    *   `.first()`: Selects the first matched element.
    *   `.last()`: Selects the last matched element.
    *   `.eq(index)`: Selects the element at a specific index.
    *   `.filter('.active')`: Filters the selection to elements with the `.active` class.
    *   `.not('.disabled')`: Removes elements with the `.disabled` class from the selection.
    *   `.has('span')`: Selects elements that contain a `<span>`.
*   **Traversal:**
    *   `.find('.child')`: Finds descendants matching the selector.
    *   `.children('.child')`: Finds direct children matching the selector.
    *   `.parent()`: Gets the direct parent.
    *   `.parents('.ancestor')`: Gets all ancestors matching the selector.
    *   `.siblings('.sibling')`: Gets siblings matching the selector.
    *   `.next()`, `.prev()`: Gets the next/previous sibling.
    *   `.closest('.ancestor')`: Finds the first ancestor matching the selector.

**Tip:** Cache jQuery objects: `var $myElement = $('#myElement');` then use `$myElement` instead of re-selecting.

## Modifying Elements

*   **Content:**
    *   `.html('New <strong>HTML</strong>')`: Sets the inner HTML. **Caution with untrusted content (XSS).**
    *   `.text('New text')`: Sets the text content (HTML tags are treated as text). Safer.
    *   `.val('New value')`: Gets or sets the value of form elements (`<input>`, `<select>`, `<textarea>`).
*   **Attributes:**
    *   `.attr('attributeName')`: Gets the value of the first element's attribute.
    *   `.attr('attributeName', 'newValue')`: Sets the attribute value for all matched elements.
    *   `.removeAttr('attributeName')`: Removes the attribute.
    *   `.prop('propertyName')`: Gets or sets DOM properties (like `checked`, `disabled`, `selectedIndex`). Use `.prop()` for boolean attributes/properties.
*   **Classes:**
    *   `.addClass('new-class')`
    *   `.removeClass('old-class')`
    *   `.toggleClass('active-class')`
    *   `.hasClass('some-class')`: Returns `true` or `false`.
*   **CSS Styles:**
    *   `.css('propertyName')`: Gets the style value of the first element.
    *   `.css('propertyName', 'newValue')`: Sets one style property.
    *   `.css({ property1: 'value1', property2: 'value2' })`: Sets multiple style properties.
*   **Dimensions:**
    *   `.width()`, `.height()`: Get/set CSS width/height (excluding padding, border, margin).
    *   `.innerWidth()`, `.innerHeight()`: Includes padding.
    *   `.outerWidth()`, `.outerHeight()`: Includes padding and border.
    *   `.outerWidth(true)`, `.outerHeight(true)`: Includes padding, border, and margin.

## Adding & Removing Elements

*   **Adding:**
    *   `.append('content')`: Inserts content at the end of each matched element.
    *   `.prepend('content')`: Inserts content at the beginning of each matched element.
    *   `.after('content')`: Inserts content after each matched element.
    *   `.before('content')`: Inserts content before each matched element.
    *   `$('content').appendTo('#target')`: Appends created content to the target.
    *   `$('content').prependTo('#target')`: Prepends created content to the target.
    *   `$('content').insertAfter('#target')`
    *   `$('content').insertBefore('#target')`
    *   *(Content can be HTML string, DOM element, or jQuery object)*
*   **Removing:**
    *   `.remove()`: Removes the selected elements (and their children) from the DOM.
    *   `.empty()`: Removes all child elements from the selected elements.
    *   `.detach()`: Removes elements but keeps data/event handlers (useful for re-inserting later).
*   **Wrapping:**
    *   `.wrap('<div class="wrapper"></div>')`: Wraps each matched element individually.
    *   `.wrapAll('<div class="wrapper"></div>')`: Wraps all matched elements with a single wrapper.
    *   `.wrapInner('<div class="inner"></div>')`: Wraps the inner content of each matched element.
    *   `.unwrap()`: Removes the parent of the selected elements.

## Effects (Basic)

*   `.show()`, `.hide()`, `.toggle()`
*   `.fadeIn()`, `.fadeOut()`, `.fadeToggle()`, `.fadeTo(duration, opacity)`
*   `.slideDown()`, `.slideUp()`, `.slideToggle()`
*   `.animate({ property1: 'value1' }, duration, easing, callback)`: Custom animations (use CSS transitions/animations for better performance if possible).

*(Refer to the jQuery API documentation for full details: https://api.jquery.com/)*