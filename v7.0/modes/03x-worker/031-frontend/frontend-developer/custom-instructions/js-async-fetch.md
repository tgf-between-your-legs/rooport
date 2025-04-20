# JavaScript: Asynchronous Operations & Fetch API

Handling asynchronous operations like fetching data from APIs using Promises and `async/await`.

## Core Concept: Asynchronous JavaScript

JavaScript is single-threaded, meaning it can only do one thing at a time. Asynchronous operations allow tasks (like network requests, timers, file reading) to happen in the background without blocking the main thread, ensuring the user interface remains responsive.

*   **Callbacks (Older):** Functions passed as arguments to be executed when an async operation completes. Can lead to "callback hell" (deeply nested callbacks).
*   **Promises (Modern):** Objects representing the eventual completion (or failure) of an asynchronous operation and its resulting value. They have states: `pending`, `fulfilled` (succeeded), `rejected` (failed). Use `.then()` for success, `.catch()` for errors, and `.finally()` for cleanup.
*   **`async/await` (Syntactic Sugar for Promises):** Provides a cleaner, more synchronous-looking way to work with Promises.
    *   `async` keyword: Placed before a function declaration to indicate it returns a Promise implicitly.
    *   `await` keyword: Used *inside* an `async` function to pause execution until a Promise settles (resolves or rejects). It returns the resolved value or throws the rejection reason. Requires `try...catch` for error handling.

## Fetch API

The standard browser API for making network requests (e.g., to get data from a backend API). It is Promise-based.

**Basic Usage (`GET` request):**

```javascript
const apiUrl = 'https://api.example.com/users';

// Using .then() / .catch()
fetch(apiUrl)
  .then(response => {
    // Check if the request was successful (status code 200-299)
    if (!response.ok) {
      // If not OK, throw an error to be caught by .catch()
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    // Parse the response body as JSON (returns another Promise)
    return response.json();
  })
  .then(data => {
    // Data is the parsed JSON object/array
    console.log('Data received:', data);
    // Update the DOM with the data
    displayUsers(data);
  })
  .catch(error => {
    // Handle network errors or errors thrown from .then()
    console.error('Fetch error:', error);
    displayError(error.message);
  });

// Using async/await (often preferred for readability)
async function getUsers() {
  try {
    const response = await fetch(apiUrl);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json(); // Wait for JSON parsing
    console.log('Data received:', data);
    displayUsers(data);

  } catch (error) {
    console.error('Fetch error:', error);
    displayError(error.message);
  }
}

getUsers(); // Call the async function

// Helper functions for displaying results (example)
function displayUsers(users) {
  const list = document.getElementById('user-list');
  if (!list) return;
  list.innerHTML = ''; // Clear previous list
  users.forEach(user => {
    const li = document.createElement('li');
    li.textContent = user.name;
    list.appendChild(li);
  });
}

function displayError(message) {
  const errorDiv = document.getElementById('error-message');
  if (!errorDiv) return;
  errorDiv.textContent = `Error: ${message}`;
}
```

**Fetch Options (`POST`, Headers, Body):**

The `fetch()` function accepts an optional second argument, an `options` object, to configure the request:

*   `method`: HTTP method (`'GET'`, `'POST'`, `'PUT'`, `'DELETE'`, etc. Defaults to `'GET'`).
*   `headers`: An object or `Headers` instance for request headers (e.g., `Content-Type`, `Authorization`).
*   `body`: The request body (e.g., for `POST` or `PUT`). Must be stringified for JSON data (`JSON.stringify(dataObject)`).

```javascript
async function createUser(userData) {
  try {
    const response = await fetch('/api/users', { // Your API endpoint
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        // Add Authorization header if needed
        // 'Authorization': `Bearer ${yourAuthToken}`
      },
      body: JSON.stringify(userData) // Convert JS object to JSON string
    });

    if (!response.ok) {
      // Try to get error details from response body if possible
      const errorData = await response.json().catch(() => ({})); // Handle cases where body isn't JSON
      throw new Error(`HTTP error! status: ${response.status} - ${errorData.message || 'Failed to create user'}`);
    }

    const createdUser = await response.json();
    console.log('User created:', createdUser);
    return createdUser;

  } catch (error) {
    console.error('Error creating user:', error);
    // Display error to user
    throw error; // Re-throw if needed for higher-level handling
  }
}

// Example usage within a form submit handler
myForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const formData = new FormData(myForm);
  const userData = Object.fromEntries(formData.entries()); // Convert FormData to object

  try {
    await createUser(userData);
    // Handle success (e.g., show message, clear form)
  } catch (error) {
    // Handle error (e.g., show error message)
  }
});
```

Understanding Promises and `async/await` is crucial for working with asynchronous operations like `fetch` in modern JavaScript, enabling non-blocking interactions with APIs and other resources. Always include error handling.