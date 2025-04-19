# JavaScript: Asynchronous Operations & Fetch API

Handling asynchronous operations like fetching data from APIs using Promises and `async/await`.

## 1. Core Concept: Asynchronous JavaScript

JavaScript is single-threaded. Asynchronous operations (network requests, timers) run in the background without blocking the main thread, keeping the UI responsive.

*   **Callbacks (Older):** Functions passed to run on completion. Can lead to "callback hell".
*   **Promises (Modern):** Objects representing the eventual result (success/failure) of an async operation. States: `pending`, `fulfilled`, `rejected`. Use `.then(onFulfilled, onRejected)`, `.catch(onRejected)`, `.finally(onSettled)`.
*   **`async/await` (Modern Syntax for Promises):** Cleaner, synchronous-looking code.
    *   `async function myFunc() {...}`: Declares a function that implicitly returns a Promise.
    *   `await promise`: Pauses execution *inside an `async` function* until the `promise` settles. Returns the resolved value or throws the rejection reason. Requires `try...catch` for error handling.

## 2. Fetch API

Standard browser API for network requests (e.g., calling backend APIs). It's Promise-based.

**Basic `GET` Request:**

```javascript
const apiUrl = 'https://api.example.com/data';

// Using async/await (Recommended)
async function fetchData() {
  console.log('Fetching data...');
  try {
    const response = await fetch(apiUrl); // Send request, wait for response headers

    // Check if HTTP status code is 2xx (e.g., 200 OK)
    if (!response.ok) {
      // If not OK (e.g., 404 Not Found, 500 Server Error), throw an error
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    // Parse response body as JSON (this also returns a Promise)
    const data = await response.json();

    console.log('Data received successfully:', data);
    // Process the data (e.g., update the DOM)
    displayData(data);

  } catch (error) {
    // Catches network errors (e.g., DNS lookup failure) OR errors thrown above
    console.error('Error fetching data:', error);
    displayError(error.message);
  } finally {
    console.log('Fetch attempt finished.');
  }
}

fetchData(); // Call the async function

// Example helper functions
function displayData(data) {
  const container = document.getElementById('data-container');
  if (!container) return;
  container.textContent = JSON.stringify(data, null, 2); // Display formatted JSON
}

function displayError(message) {
  const errorEl = document.getElementById('error-display');
  if (!errorEl) return;
  errorEl.textContent = `Failed to load data: ${message}`;
  errorEl.style.color = 'red';
}
```

**Fetch Options (`POST`, Headers, Body):**

Use the optional second argument (an `options` object) for other methods, headers, or sending data.

*   `method`: `'GET'`, `'POST'`, `'PUT'`, `'DELETE'`, etc.
*   `headers`: Object or `Headers` instance (e.g., `{ 'Content-Type': 'application/json', 'Authorization': 'Bearer YOUR_TOKEN' }`).
*   `body`: Request payload. Must be stringified for JSON (`JSON.stringify(yourDataObject)`).

```javascript
async function postData(url, dataToSend) {
  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        // Add other headers like Authorization if required by the API
        // 'Authorization': `Bearer ${getAuthToken()}`
      },
      body: JSON.stringify(dataToSend) // Convert JS object to JSON string
    });

    if (!response.ok) {
      // Try to get more specific error info from response body if API provides it
      let errorDetails = `HTTP error! Status: ${response.status}`;
      try {
        const errorBody = await response.json(); // Or response.text()
        errorDetails += ` - ${errorBody.message || JSON.stringify(errorBody)}`;
      } catch (parseError) {
        // Ignore if response body isn't helpful JSON/text
      }
      throw new Error(errorDetails);
    }

    // Assuming the API returns the created/updated resource as JSON
    const responseData = await response.json();
    console.log('POST successful:', responseData);
    return responseData; // Return data for further processing

  } catch (error) {
    console.error('Error posting data:', error);
    // Display error to the user
    throw error; // Re-throw for higher-level handling if necessary
  }
}

// Example Usage (e.g., in a form submit handler)
async function submitNewUser(userData) {
    const apiUrl = '/api/users'; // Your backend endpoint
    try {
        const createdUser = await postData(apiUrl, userData);
        alert(`User ${createdUser.name} created successfully!`);
        // Reset form, redirect, etc.
    } catch (error) {
        alert(`Failed to create user: ${error.message}`);
    }
}
```

**Key Points:**

*   Always handle potential errors using `try...catch` with `async/await` or `.catch()` with Promises.
*   Check `response.ok` to verify successful HTTP status codes (200-299).
*   Parse the response body appropriately (`response.json()`, `response.text()`, etc.) - this is also an async operation.
*   Set correct `Content-Type` header when sending data (e.g., `'application/json'`).
*   Stringify your data (`JSON.stringify`) before putting it in the `body` for JSON APIs.
*   Handle authentication (e.g., `Authorization` header) as required by the API.