# JavaScript: DOM Manipulation & Events

Using Vanilla JavaScript to interact with the HTML Document Object Model (DOM) - selecting, modifying, creating elements, and handling user events.

## 1. Selecting Elements

*   **`document.getElementById(id)`:** Selects the single element with the specified `id`. Returns the element or `null`.
*   **`document.querySelector(cssSelector)`:** Selects the *first* element matching the CSS selector. Returns the element or `null`. Very versatile (e.g., `.class`, `tag[attribute="value"]`).
*   **`document.querySelectorAll(cssSelector)`:** Selects *all* elements matching the CSS selector. Returns a **static `NodeList`** (array-like, use `forEach` or `Array.from()`/`[...]` to convert to a true array). Returns an empty `NodeList` if none found.
*   **Relative Selection:** Use `element.querySelector()` and `element.querySelectorAll()` to search within an existing element's descendants.

```javascript
const mainTitle = document.getElementById('main-title');
const firstButton = document.querySelector('.btn-primary');
const allButtons = document.querySelectorAll('button');
const formEmailInput = document.querySelector('form input[name="email"]');

// Iterate NodeList
allButtons.forEach(button => {
  console.log(button.textContent);
});
```

## 2. Modifying Elements

*   **Content:**
    *   `element.textContent = 'New text'`: Sets text content (safer, ignores HTML). **Preferred for non-HTML content.**
    *   `element.innerHTML = '<strong>HTML</strong>'`: Sets inner HTML (use with caution if content includes user input due to XSS risk - see `07-security-basics.md`).
*   **Attributes:**
    *   `element.setAttribute('name', 'value')`: Sets any HTML attribute.
    *   `element.getAttribute('name')`: Gets attribute value.
    *   `element.removeAttribute('name')`: Removes attribute.
    *   `element.hasAttribute('name')`: Checks if attribute exists.
    *   Direct properties: `element.id`, `element.src`, `element.href`, `element.value` (for form inputs).
*   **Classes (`element.classList`):**
    *   `.add('class')`
    *   `.remove('class')`
    *   `.toggle('class')` (returns `true` if added, `false` if removed)
    *   `.contains('class')` (returns `true`/`false`)
    *   `.replace('old', 'new')`
*   **Styles (`element.style`):**
    *   Sets *inline* styles (e.g., `element.style.color = 'red'`, `element.style.backgroundColor = '#eee'`). Use camelCase for CSS properties.
    *   **Note:** Prefer toggling CSS classes for styling changes over manipulating many inline styles directly.

```javascript
const title = document.getElementById('page-title');
if (title) {
  title.textContent = 'Updated Title';
  title.classList.add('highlight');
  title.style.fontSize = '2rem'; // Example inline style
}
```

## 3. Creating & Adding Elements

1.  **Create:** `const newEl = document.createElement('tagName');` (e.g., `'div'`, `'li'`)
2.  **Configure:** Set `textContent`, `classList`, attributes, etc. on `newEl`.
3.  **Append:** Add to the DOM.
    *   `parentElement.appendChild(newEl)`: Adds as the last child.
    *   `parentElement.insertBefore(newEl, referenceElement)`: Inserts before `referenceElement`.
    *   `parentElement.prepend(newEl)`: Adds as the first child.

```javascript
const list = document.querySelector('#my-list');
if (list) {
  const newItem = document.createElement('li');
  newItem.textContent = 'Dynamically Added Item';
  newItem.classList.add('list-item', 'new');
  list.appendChild(newItem);
}
```

## 4. Removing Elements

*   `elementToRemove.remove()`: Removes the element directly (modern).
*   `parentElement.removeChild(elementToRemove)`: Older method.

## 5. Event Handling (`addEventListener`)

React to user actions or browser events.

*   **Attach:** `element.addEventListener(eventName, eventHandlerFn, [options])`
    *   `eventName`: String like `'click'`, `'mouseover'`, `'keydown'`, `'submit'`, `'change'`, `'input'`, `'focus'`, `'blur'`, `'load'`, `'DOMContentLoaded'`.
    *   `eventHandlerFn(event)`: Function to run. Receives an `event` object. `this` inside the handler refers to the `element`.
    *   `options` (Optional): Object, e.g., `{ once: true }` (run once), `{ capture: true }` (use capture phase).
*   **Remove:** `element.removeEventListener(eventName, eventHandlerFn)` (Requires the *exact same function reference*).
*   **`event` Object:** Contains event details.
    *   `event.target`: The element that triggered the event.
    *   `event.currentTarget`: The element the listener is attached to (`this`).
    *   `event.preventDefault()`: Stop the browser's default action (e.g., form submission, link navigation). **Crucial for form submissions handled by JS.**
    *   `event.stopPropagation()`: Stop the event from bubbling up to parent elements.
    *   `event.key` (for keyboard events), `event.clientX`/`clientY` (for mouse events), etc.

```javascript
const myButton = document.getElementById('action-button');
const myForm = document.getElementById('data-form');

function handleButtonClick(event) {
  console.log(`Button "${event.target.textContent}" clicked!`);
  // 'this' also refers to myButton here
  this.disabled = true; // Disable button after click
}

function handleFormSubmit(event) {
  event.preventDefault(); // Stop page reload
  console.log('Form submitted via JS');
  const formData = new FormData(myForm);
  const email = formData.get('email'); // Get by input 'name' attribute
  console.log('Email submitted:', email);
  // Process data (e.g., call fetch - see 05-js-async-fetch.md)
}

if (myButton) {
  myButton.addEventListener('click', handleButtonClick);
}
if (myForm) {
  myForm.addEventListener('submit', handleFormSubmit);
}

// Event Delegation Example (handling clicks on list items via the parent UL)
const myList = document.getElementById('clickable-list');
if (myList) {
    myList.addEventListener('click', (event) => {
        // Check if the clicked element was an LI
        if (event.target && event.target.tagName === 'LI') {
            console.log('List item clicked:', event.target.textContent);
            event.target.classList.toggle('selected');
        }
    });
}
```

*   **Event Bubbling (Default):** Events travel up from target to ancestors. Allows *event delegation* (handling events on a parent).
*   **Event Capturing:** Events travel down from window to target (use `{ capture: true }`). Less common.

Mastering these DOM methods is fundamental for creating interactive web experiences.