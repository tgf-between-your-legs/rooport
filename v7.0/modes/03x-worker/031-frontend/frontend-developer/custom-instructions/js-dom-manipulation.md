# Vanilla JavaScript DOM Manipulation Quick Reference

Common methods for selecting and manipulating HTML elements using standard browser APIs.

## Selecting Elements

*   **`document.getElementById('elementId')`**
    *   Selects a single element by its unique ID.
    *   Returns the element object or `null`.
*   **`document.querySelector('cssSelector')`**
    *   Selects the **first** element matching the specified CSS selector.
    *   Returns the element object or `null`.
    *   *Example:* `document.querySelector('.my-class')`, `document.querySelector('nav ul li')`
*   **`document.querySelectorAll('cssSelector')`**
    *   Selects **all** elements matching the specified CSS selector.
    *   Returns a **static `NodeList`** (array-like, can be iterated with `forEach`). Returns an empty `NodeList` if no matches.
    *   *Example:* `document.querySelectorAll('p.highlight')`
*   **`element.querySelector()` / `element.querySelectorAll()`**
    *   Same as above, but searches only within the specified `element`.

## Modifying Elements

*   **Content:**
    *   `element.textContent = 'New text content'`: Sets the text content, ignoring HTML tags. Safer for user input.
    *   `element.innerHTML = 'New <strong>HTML</strong> content'`: Sets the HTML content. **Use with caution**, especially with user-provided content, due to XSS risks. Sanitize input if necessary.
*   **Attributes:**
    *   `element.getAttribute('attributeName')`: Gets the value of an attribute.
    *   `element.setAttribute('attributeName', 'newValue')`: Sets the value of an attribute. Creates it if it doesn't exist.
    *   `element.removeAttribute('attributeName')`: Removes an attribute.
    *   `element.hasAttribute('attributeName')`: Checks if an attribute exists.
    *   Direct property access for common attributes: `element.id`, `element.src`, `element.href`, `element.value`, etc.
*   **Classes (`element.classList`):**
    *   `element.classList.add('new-class')`: Adds a class.
    *   `element.classList.remove('old-class')`: Removes a class.
    *   `element.classList.toggle('active-class')`: Adds the class if absent, removes it if present. Returns `true` if class was added, `false` if removed.
    *   `element.classList.contains('some-class')`: Checks if the class exists. Returns `true` or `false`.
    *   `element.classList.replace('old-class', 'new-class')`: Replaces an existing class with a new one.
*   **Styles (`element.style`):**
    *   Sets **inline** styles. Use camelCase for CSS properties (e.g., `backgroundColor`).
    *   `element.style.color = 'red';`
    *   `element.style.backgroundColor = '#eee';`
    *   `element.style.display = 'none';`
    *   **Note:** Prefer adding/removing CSS classes for styling changes over manipulating inline styles directly for better maintainability and separation of concerns.

## Creating & Adding Elements

*   **`document.createElement('tagName')`**: Creates a new element (e.g., `document.createElement('div')`).
*   **`parentNode.appendChild(newElement)`**: Adds `newElement` as the last child of `parentNode`.
*   **`parentNode.insertBefore(newElement, referenceElement)`**: Inserts `newElement` before `referenceElement` within `parentNode`.
*   **`element.remove()`**: Removes the element from the DOM.

```javascript
// Example: Create and add a list item
const newLi = document.createElement('li');
newLi.textContent = 'New Item';
newLi.classList.add('list-item');

const parentUl = document.querySelector('#my-list');
parentUl.appendChild(newLi);
```

## Event Handling

*   **`element.addEventListener('eventName', eventHandlerFunction)`**: Attaches an event listener.
    *   `eventName`: String like `'click'`, `'mouseover'`, `'keydown'`, `'submit'`.
    *   `eventHandlerFunction`: Function to execute when the event occurs. Receives an `event` object as an argument.
*   **`element.removeEventListener('eventName', eventHandlerFunction)`**: Removes a previously attached listener. **Important:** Requires a reference to the *exact same function* used in `addEventListener`.
*   **`event` Object:** Contains information about the event (e.g., `event.target`, `event.preventDefault()`, `event.stopPropagation()`, `event.key`).

```javascript
const myButton = document.getElementById('myButton');

function handleClick(event) {
  console.log('Button clicked!', event.target);
  event.preventDefault(); // Prevent default form submission, if applicable
}

myButton.addEventListener('click', handleClick);

// To remove later:
// myButton.removeEventListener('click', handleClick);
```

*(Refer to MDN Web Docs for detailed API information.)*