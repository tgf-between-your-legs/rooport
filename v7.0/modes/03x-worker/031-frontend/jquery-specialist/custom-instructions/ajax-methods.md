# jQuery AJAX Methods Quick Reference

Common methods for making Asynchronous JavaScript and XML (AJAX) requests using jQuery.

## 1. `$.ajax(options)` (Core Method)

*   **Purpose:** The fundamental method for performing AJAX requests. Highly configurable.
*   **Common Options:**
    *   `url`: The URL to request.
    *   `method` or `type`: The HTTP method ('GET', 'POST', 'PUT', 'DELETE', etc. Default: 'GET').
    *   `data`: Data to send to the server (Object, String, or Array). Automatically processed for GET/POST.
    *   `dataType`: The type of data expected back from the server ('json', 'xml', 'html', 'text', 'script'). jQuery attempts to infer if not specified.
    *   `contentType`: Content type when sending data (e.g., `'application/json; charset=utf-8'` for JSON POST). Default is `'application/x-www-form-urlencoded; charset=UTF-8'`.
    *   `headers`: An object of additional header key/value pairs.
    *   `success(data, textStatus, jqXHR)`: Callback function if the request succeeds.
    *   `error(jqXHR, textStatus, errorThrown)`: Callback function if the request fails.
    *   `complete(jqXHR, textStatus)`: Callback function that executes always, after success or error.
    *   `beforeSend(jqXHR, settings)`: A pre-request callback function. Can be used to modify `jqXHR` (e.g., set headers). Return `false` to cancel the request.
*   **Promise Interface:** `$.ajax()` returns a `jqXHR` object which implements the Promise interface. Use `.done()`, `.fail()`, `.always()` (similar to `then`, `catch`, `finally`).
    ```javascript
    // Example using Callbacks
    $.ajax({
      url: '/api/users',
      method: 'POST',
      data: JSON.stringify({ name: 'John Doe', email: 'john@example.com' }),
      contentType: 'application/json; charset=utf-8',
      dataType: 'json', // Expect JSON back
      beforeSend: function(xhr) {
        // Maybe set an auth header
        // xhr.setRequestHeader('Authorization', 'Bearer YOUR_TOKEN');
      },
      success: function(data, textStatus, jqXHR) {
        console.log('User created:', data);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.error('Error creating user:', textStatus, errorThrown, jqXHR.responseText);
      },
      complete: function() {
        console.log('Request finished.');
      }
    });

    // Example using Promises
    $.ajax({
      url: '/api/items/123',
      method: 'GET',
      dataType: 'json'
    })
    .done(function(data) {
      console.log('Item data:', data);
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
      console.error('Error fetching item:', textStatus, errorThrown);
    })
    .always(function() {
      console.log('GET request finished.');
    });
    ```

## 2. Shorthand Methods

*   **`$.get(url, [data], [successCallback], [dataType])`**
    *   Performs a GET request.
    *   `data` is appended to the URL as query parameters.
    ```javascript
    $.get('/api/search', { query: 'jquery', page: 1 }, function(data) {
      console.log('Search results:', data);
    }, 'json');
    ```
*   **`$.post(url, [data], [successCallback], [dataType])`**
    *   Performs a POST request.
    *   `data` is sent in the request body (typically form-encoded).
    ```javascript
    $.post('/api/comments', { comment: 'Great post!', user: 'Jane' }, function(response) {
      console.log('Comment added:', response);
    }, 'json');
    ```
*   **`$.getJSON(url, [data], [successCallback])`**
    *   Performs a GET request and automatically parses the response as JSON.
    ```javascript
    $.getJSON('/api/config', function(configData) {
      console.log('Config loaded:', configData);
    });
    ```
*   **`$(selector).load(url, [data], [completeCallback])`**
    *   Loads HTML from a URL and inserts it into the selected element(s).
    *   If `data` is provided, it makes a POST request; otherwise, GET.
    ```javascript
    $('#results').load('/api/html-fragment #content', function(response, status, xhr) {
      if (status == "error") {
        console.error("Error loading fragment:", xhr.statusText);
      }
    }); // Loads only the #content part of the response
    ```

## Error Handling

*   Use the `error` callback or the `.fail()` promise method.
*   The `jqXHR` object provides details like `status`, `statusText`, `responseText`, `responseJSON` (if applicable).
*   The `textStatus` string indicates the type of error (e.g., "timeout", "error", "abort", "parsererror").
*   The `errorThrown` object (usually a string) provides the textual portion of the error status (e.g., "Not Found", "Internal Server Error").

*(Refer to the jQuery AJAX documentation for full details: https://api.jquery.com/category/ajax/)*