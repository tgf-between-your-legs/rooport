# jQuery: Performance Patterns & Best Practices

Writing more efficient jQuery code.

## Core Concept

While jQuery simplifies DOM manipulation, inefficient usage can still lead to performance bottlenecks, especially with complex selectors, frequent DOM updates, or numerous event handlers. Applying best practices helps mitigate these issues.

## Key Performance Patterns

1.  **Cache jQuery Selections:**
    *   **Problem:** Repeatedly selecting the same element(s) (e.g., `$('#myElement')`) forces jQuery to re-query the DOM each time, which is inefficient.
    *   **Solution:** Store the result of a selection in a variable (conventionally prefixed with `$`) and reuse that variable.

    ```javascript
    // Inefficient:
    // $('#myList').append('<li>Item 1</li>');
    // $('#myList').addClass('updated');
    // if ($('#myList').children().length > 5) { ... }

    // Efficient:
    const $myList = $('#myList'); // Cache the selection
    $myList.append('<li>Item 1</li>');
    $myList.addClass('updated');
    if ($myList.children().length > 5) { ... }
    ```

2.  **Use Specific Selectors:**
    *   **Problem:** Broad selectors (like tag names `$('div')` or descendant selectors `$('.container p')`) require the browser to traverse more of the DOM.
    *   **Solution:** Be as specific as possible. IDs (`#myId`) are the fastest, followed by classes (`.myClass`), then tag names. Use context for selections where appropriate.

    ```javascript
    // Less efficient:
    // $('p'); // Selects ALL paragraphs on the page

    // More efficient:
    // $('#mainContent p'); // Selects paragraphs only within #mainContent
    const $mainContent = $('#mainContent');
    $mainContent.find('p'); // Even better if $mainContent is cached

    // Fastest (if applicable):
    // $('#specificParagraphId');
    ```

3.  **Use Event Delegation:**
    *   **Problem:** Attaching event handlers directly to many individual elements (e.g., hundreds of list items or table cells) consumes more memory and can be slow, especially if elements are added dynamically after initial setup.
    *   **Solution:** Attach a single event handler to a static parent element. Use the second argument of `.on()` to specify the target child selector. The handler runs only when the event originates from a matching child.

    ```javascript
    // Inefficient (attaches handler to potentially many LIs):
    // $('#myList li').on('click', function() { ... });

    // Efficient (attaches single handler to UL):
    $('#myList').on('click', 'li', function(event) {
      // 'this' refers to the clicked LI element
      const $clickedItem = $(this);
      console.log('Clicked:', $clickedItem.text());
      // ...
    });
    ```

4.  **Minimize DOM Manipulation in Loops:**
    *   **Problem:** Modifying the DOM (appending, changing attributes/styles) inside a loop is often slow because each modification can trigger browser reflows/repaints.
    *   **Solution:** Build HTML strings or create DOM elements in memory within the loop, then append them to the DOM *once* after the loop finishes. Use document fragments for better performance when appending multiple elements.

    ```javascript
    const data = [/* ... large array ... */];
    const $list = $('#targetList');

    // Inefficient:
    // data.forEach(item => {
    //   $list.append(`<li>${item.name}</li>`); // Appends inside loop
    // });

    // More Efficient (String building):
    // let listHtml = '';
    // data.forEach(item => {
    //   listHtml += `<li>${item.name}</li>`;
    // });
    // $list.html(listHtml); // Single DOM update

    // More Efficient (Document Fragment):
    const fragment = document.createDocumentFragment();
    data.forEach(item => {
      const $li = $('<li>').text(item.name); // Create element in memory
      fragment.appendChild($li[0]); // Append raw DOM node to fragment
    });
    $list.append(fragment); // Single DOM append
    ```

5.  **Detach Elements for Complex Updates (Advanced):**
    *   For very complex manipulations on a large DOM subtree, you can temporarily detach it from the main DOM using `.detach()`, perform your updates, and then re-append it. This minimizes reflows during the updates. Use with caution.

6.  **Debounce/Throttle Frequent Events:**
    *   **Problem:** Event handlers attached to frequent events like `scroll`, `resize`, or `mousemove` can fire excessively, causing performance issues if the handler performs complex calculations or DOM manipulations.
    *   **Solution:** Use **debouncing** (wait until events stop firing for a period before executing) or **throttling** (execute the handler at most once per specified interval) utility functions (often from libraries like Lodash/Underscore, or implement simple versions).

    ```javascript
    // Conceptual example using a hypothetical debounce function
    // $(window).on('resize', debounce(function() {
    //   console.log('Window resized (debounced)!');
    //   // Perform expensive layout calculations here
    // }, 250)); // Execute 250ms after the last resize event
    ```

By applying these patterns, you can write jQuery code that is not only functional but also performs well, even in complex applications or legacy systems.