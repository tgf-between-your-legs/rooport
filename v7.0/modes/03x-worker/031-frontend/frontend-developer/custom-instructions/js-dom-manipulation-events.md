# JavaScript: DOM Manipulation & Events

Using Vanilla JavaScript to interact with the HTML Document Object Model (DOM).

## Core Concept

The DOM represents the HTML document as a tree structure of objects (nodes). JavaScript allows you to find, create, change, or remove elements and attributes within this tree, and to react to user interactions (events).

## Selecting Elements

*   **`document.getElementById(id)`:** Selects the single element with the specified `id`. Returns `null` if not found.
*   **`document.querySelector(cssSelector)`:** Selects the *first* element matching the CSS selector. Returns `null` if not found. Very versatile.
*   **`document.querySelectorAll(cssSelector)`:** Selects *all* elements matching the CSS selector. Returns a **`NodeList`** (which is like an array, but not exactly - use `Array.from()` or spread syntax `[...]` to convert if needed). Returns an empty `NodeList` if none found.
*   **Relative Selection:** You can also use `querySelector` and `querySelectorAll` on an existing element reference to search within its descendants.

```javascript
// Get elements
const mainTitle = document.getElementById('main-title');
const firstButton = document.querySelector('.btn-primary');
const allButtons = document.querySelectorAll('button');
const specificInput = document.querySelector('form input[name="email"]');

// Iterate over a NodeList
allButtons.forEach(button => {
  console.log(button.textContent);
});

// Convert NodeList to Array
const buttonArray = Array.from(allButtons);
// const buttonArray = [...allButtons]; // Alternative using spread syntax
```

## Modifying Elements

Once you have an element reference:

*   **Content:**
    *   `element.textContent = 'New text'`: Sets the text content (safer, ignores HTML).
    *   `element.innerHTML = '<strong>New</strong> HTML'`: Sets the inner HTML content (use with caution if content includes user input due to XSS risk).
*   **Attributes:**
    *   `element.setAttribute('attributeName', 'value')`: Sets any HTML attribute.
    *   `element.getAttribute('attributeName')`: Gets the value of an attribute.
    *   `element.removeAttribute('attributeName')`: Removes an attribute.
    *   `element.id`, `element.src`, `element.href`, `element.value`: Direct property access for common attributes.
*   **Classes:**
    *   `element.classList.add('new-class')`
    *   `element.classList.remove('old-class')`
    *   `element.classList.toggle('active-class')`
    *   `element.classList.contains('some-class')`: Returns `true` or `false`.
*   **Styles:**
    *   `element.style.propertyName = 'value'`: Sets inline styles (e.g., `element.style.color = 'red'`, `element.style.backgroundColor = '#eee'`). Note camelCase for CSS properties with hyphens. Best practice is usually to toggle classes instead of setting many inline styles.

```javascript
const title = document.getElementById('page-title');
if (title) {
  title.textContent = 'Updated Page Title';
  title.style.color = 'blue';
}

const submitButton = document.querySelector('button[type="submit"]');
if (submitButton) {
  submitButton.setAttribute('disabled', 'true'); // Disable button
  submitButton.classList.add('btn-disabled');
}
```

## Creating & Adding Elements

1.  **Create:** `const newElement = document.createElement('tagName');` (e.g., `document.createElement('div')`)
2.  **Configure:** Set attributes, text content, styles, classes on `newElement`.
3.  **Append:** Add the new element to the DOM.
    *   `parentElement.appendChild(newElement)`: Adds as the last child of `parentElement`.
    *   `parentElement.insertBefore(newElement, referenceElement)`: Inserts before `referenceElement`.
    *   `parentElement.prepend(newElement)`: Adds as the first child.

```javascript
const list = document.querySelector('#my-list');
if (list) {
  const newItem = document.createElement('li');
  newItem.textContent = 'New Item';
  newItem.classList.add('list-item');
  list.appendChild(newItem); // Add to the end of the list
}
```

## Removing Elements

*   `elementToRemove.remove()`: Removes the element directly.
*   `parentElement.removeChild(elementToRemove)`: Older method.

## Event Handling (`addEventListener`)

React to user actions (clicks, input changes, mouse movements, etc.).

*   **`element.addEventListener(eventName, eventHandlerFn, [options])`:** Attaches a function (`eventHandlerFn`) to run when the specified `eventName` occurs on the `element`.
*   **`eventName`:** String like `'click'`, `'mouseover'`, `'mouseout'`, `'keydown'`, `'keyup'`, `'submit'`, `'change'`, `'input'`, `'focus'`, `'blur'`.
*   **`eventHandlerFn(event)`:** The function to execute. It receives an `event` object containing details about the event (e.g., `event.target` - the element that triggered the event, `event.preventDefault()` - stop default browser action, `event.stopPropagation()` - stop event bubbling).
*   **`options` (Optional):** Object, e.g., `{ once: true }` (run handler only once).

```javascript
const myButton = document.getElementById('my-button');
const myForm = document.getElementById('my-form');
const myInput = document.getElementById('my-input');

function handleButtonClick(event) {
  console.log('Button clicked!', event.target);
  // 'this' inside the handler also refers to the element
  this.textContent = 'Clicked!';
}

function handleFormSubmit(event) {
  event.preventDefault(); // IMPORTANT: Prevent default form submission (page reload)
  console.log('Form submitted!');
  const formData = new FormData(myForm);
  const name = formData.get('name'); // Get value by input name
  console.log('Name:', name);
  // Process form data (e.g., send via fetch)
}

function handleInputChange(event) {
    console.log('Input value changed:', event.target.value);
}

if (myButton) {
  myButton.addEventListener('click', handleButtonClick);
}
if (myForm) {
  myForm.addEventListener('submit', handleFormSubmit);
}
if (myInput) {
    myInput.addEventListener('input', handleInputChange); // Fires on every keystroke
    // myInput.addEventListener('change', handleInputChange); // Fires when focus leaves
}

// Removing an event listener (requires the exact same function reference)
// myButton.removeEventListener('click', handleButtonClick);
```

*   **Event Bubbling:** Events typically "bubble" up from the target element through its ancestors. You can handle an event on a parent element (event delegation) instead of attaching listeners to many children. Check `event.target` inside the handler to see which child triggered the event.
*   **Event Capturing:** Less common phase where events travel *down* the DOM tree. Set `useCapture` to `true` in `addEventListener` options.

These core DOM manipulation and event handling techniques are the foundation for creating interactive web pages with Vanilla JavaScript.