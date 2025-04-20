# jQuery: Event Handling

Responding to user interactions and browser events using jQuery.

## Core Concept: `.on()`

The primary method for attaching event handlers in modern jQuery is `.on()`. It provides a flexible way to handle events directly on selected elements or use event delegation.

**Syntax:**

*   **Direct Binding:** `$(selector).on(eventName, handlerFn);`
    *   Attaches the `handlerFn` directly to the element(s) matched by `selector`.
*   **Delegated Binding:** `$(ancestorSelector).on(eventName, childSelector, handlerFn);`
    *   Attaches the `handlerFn` to the `ancestorSelector`.
    *   The handler only executes if the event originated from an element matching `childSelector` *within* the ancestor.
    *   **Performance Benefit:** Attaches only one listener to the ancestor, efficient for handling events on many dynamically added or existing child elements. **Generally preferred over direct binding for lists, tables, or containers with many interactive children.**

**Common Event Names (`eventName`):**

*   **Mouse:** `click`, `dblclick`, `mouseenter`, `mouseleave`, `mouseover`, `mouseout`, `mousemove`, `mousedown`, `mouseup`
*   **Keyboard:** `keydown`, `keyup`, `keypress`
*   **Form:** `submit`, `change` (for `<input>`, `<select>`, `<textarea>` when value changes and element loses focus), `input` (fires immediately on value change), `focus`, `blur`
*   **Document/Window:** `load` (often used on `window`), `ready` (specific to jQuery, see below), `scroll`, `resize`

**Event Handler Function (`handlerFn(event)`):**

*   Receives an `event` object (a normalized jQuery event object).
*   `event.target`: The DOM element where the event originated.
*   `event.currentTarget`: The DOM element the handler is attached to (useful in delegation).
*   `this`: Inside the handler, `this` usually refers to the DOM element the handler is attached to (`event.currentTarget`).
*   `event.preventDefault()`: Stops the browser's default action for the event (e.g., stops form submission, stops link navigation).
*   `event.stopPropagation()`: Stops the event from bubbling up the DOM tree to ancestor elements.
*   `event.pageX`, `event.pageY`: Mouse coordinates relative to the document.
*   `event.which`: Key code for keyboard events.

## Examples

```javascript
$(document).ready(function() { // Ensure DOM is ready before attaching handlers

  // --- Direct Binding ---
  $('#myButton').on('click', function(event) {
    console.log('Button clicked!');
    $(this).text('Clicked!'); // 'this' refers to the button element
  });

  $('input[name="username"]').on('focus', function() {
    $(this).addClass('focused');
  });

  $('input[name="username"]').on('blur', function() {
    $(this).removeClass('focused');
  });

  // --- Event Delegation ---
  // Handle clicks on any '.list-item' inside the '#myList' ul
  $('#myList').on('click', '.list-item', function(event) {
    const $item = $(this); // Wrap 'this' (the clicked .list-item) in jQuery object
    console.log('List item clicked:', $item.text());
    $item.toggleClass('selected');
  });

  // Handle form submission
  $('#myForm').on('submit', function(event) {
    event.preventDefault(); // Prevent default page reload
    console.log('Form submitting via jQuery...');
    // Perform validation or AJAX submission
    const $form = $(this);
    // const formData = $form.serialize(); // Helper to get form data as query string
    // $.post('/api/submit', formData) ...
  });

  // --- Multiple Events ---
  $('.hover-effect').on('mouseenter mouseleave', function() {
    $(this).toggleClass('hovered');
  });

  // --- Namespaced Events (for easier removal) ---
  $(window).on('scroll.myFeature', function() {
    console.log('Scrolling...');
  });

  // --- Removing Event Handlers ---
  // Remove specific handler
  // $('#myButton').off('click', specificHandlerFunction);

  // Remove all click handlers from button
  // $('#myButton').off('click');

  // Remove namespaced event
  // $(window).off('scroll.myFeature');

  // Remove all handlers delegated to '.list-item' within '#myList'
  // $('#myList').off('click', '.list-item');

}); // End document ready
```

## Document Ready

It's crucial to wait until the DOM is fully loaded and parsed before trying to select elements or attach handlers. jQuery provides the `$(document).ready()` function (or its shorthand `$(function() { ... });`) for this.

```javascript
// Long form
$(document).ready(function() {
  // Your jQuery code here...
  console.log('DOM is ready!');
});

// Shorthand
$(function() {
  // Your jQuery code here...
  console.log('DOM is ready (shorthand)!');
});
```

jQuery's event handling simplifies cross-browser event management and provides powerful delegation capabilities. Use `.on()` for attaching events and prefer delegation for performance when dealing with multiple child elements.