# Angular: HttpClient & Interceptors

Making HTTP requests and intercepting them globally using Angular's `HttpClient`.

## Core Concept: `HttpClient`

*   **Purpose:** Angular's built-in service for making HTTP requests to backend APIs or other resources. It leverages RxJS Observables to handle asynchronous responses.
*   **Module:** Part of `@angular/common/http`.
*   **Setup (Standalone Apps):** Use `provideHttpClient()` in the `providers` array when bootstrapping the application (`main.ts`).
    ```typescript
    // src/main.ts
    import { bootstrapApplication } from '@angular/platform-browser';
    import { provideHttpClient, withInterceptors } from '@angular/common/http'; // Import providers
    import { AppComponent } from './app/app.component';
    import { authInterceptor } from './app/auth.interceptor'; // Example interceptor

    bootstrapApplication(AppComponent, {
      providers: [
        provideHttpClient(
          withInterceptors([authInterceptor]) // Register functional interceptors
        )
        // ... other providers
      ]
    }).catch(err => console.error(err));
    ```
*   **Setup (Module-based Apps):** Import `HttpClientModule` into your root `AppModule`.
*   **Usage:** Inject `HttpClient` into your services or components and call methods like `get()`, `post()`, `put()`, `delete()`. These methods return an Observable of the response.

```typescript
// src/app/data.service.ts
import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

interface Item {
  id: number;
  name: string;
}

@Injectable({ providedIn: 'root' })
export class DataService {
  private http = inject(HttpClient);
  private apiUrl = '/api/items'; // Example API endpoint

  getItems(searchTerm?: string): Observable<Item[]> {
    let params = new HttpParams();
    if (searchTerm) {
      params = params.set('search', searchTerm);
    }

    return this.http.get<Item[]>(this.apiUrl, { params }) // Specify expected response type
      .pipe(
        retry(2), // Retry failed requests 2 times
        catchError(this.handleError) // Centralized error handling
      );
  }

  getItem(id: number): Observable<Item> {
    return this.http.get<Item>(`${this.apiUrl}/${id}`)
      .pipe(catchError(this.handleError));
  }

  addItem(item: Omit<Item, 'id'>): Observable<Item> {
    const httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json' })
    };
    return this.http.post<Item>(this.apiUrl, item, httpOptions)
      .pipe(catchError(this.handleError));
  }

  updateItem(item: Item): Observable<any> { // Often returns no body or just status
    const httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json' })
    };
    return this.http.put(`${this.apiUrl}/${item.id}`, item, httpOptions)
      .pipe(catchError(this.handleError));
  }

  deleteItem(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`)
      .pipe(catchError(this.handleError));
  }

  private handleError(error: HttpErrorResponse) {
    // Basic client-side error handling
    console.error('API Error:', error.message);
    // Return an observable with a user-facing error message
    return throwError(() => new Error('Something bad happened; please try again later.'));
  }
}
```

## Interceptors

*   **Concept:** Interceptors allow you to declare code that intercepts outgoing HTTP requests and incoming responses globally. They are useful for tasks like adding authentication tokens, logging, modifying headers, handling errors universally, or caching responses.
*   **Types (Modern Angular - Functional Interceptors):**
    *   **Functional Interceptors:** Simple functions conforming to the `HttpInterceptorFn` type. This is the preferred approach in modern Angular.
    *   **Signature:** `(req: HttpRequest<unknown>, next: HttpHandlerFn) => Observable<HttpEvent<unknown>>`
        *   `req`: The outgoing request object (immutable). Clone it (`req.clone({...})`) to modify.
        *   `next`: A function to call to pass the (potentially modified) request to the next interceptor or the backend. It returns an `Observable<HttpEvent<unknown>>`.
*   **Registration (Functional):** Pass interceptor functions to `withInterceptors([...])` within `provideHttpClient()`. Order matters.
*   **Types (Classic Angular - Class-based Interceptors):**
    *   Classes implementing the `HttpInterceptor` interface with an `intercept()` method.
    *   Registered in `AppModule` providers using `HTTP_INTERCEPTORS` multi-provider token. (Less common now).

**Example: Functional Authentication Interceptor (Adding Bearer Token)**

```typescript
// src/app/auth.interceptor.ts
import { HttpInterceptorFn, HttpRequest, HttpHandlerFn, HttpEvent } from '@angular/common/http';
import { inject } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service'; // Assume an AuthService exists

export const authInterceptor: HttpInterceptorFn = (
  req: HttpRequest<unknown>,
  next: HttpHandlerFn
): Observable<HttpEvent<unknown>> => {

  const authService = inject(AuthService); // Inject services if needed
  const authToken = authService.getToken(); // Get token from service

  // Clone the request and add the authorization header if token exists
  if (authToken) {
    const authReq = req.clone({
      // headers: req.headers.set('Authorization', `Bearer ${authToken}`)
      // Or more robustly:
      setHeaders: {
        Authorization: `Bearer ${authToken}`
      }
    });
    // Pass the cloned request to the next handler
    return next(authReq);
  } else {
    // If no token, pass the original request
    return next(req);
  }
};

// Registration shown in Setup section above
```

**Example: Functional Logging Interceptor**

```typescript
// src/app/logging.interceptor.ts
import { HttpInterceptorFn, HttpRequest, HttpHandlerFn, HttpEvent, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

export const loggingInterceptor: HttpInterceptorFn = (
  req: HttpRequest<unknown>,
  next: HttpHandlerFn
): Observable<HttpEvent<unknown>> => {

  const started = Date.now();
  console.log(`Outgoing Request: ${req.method} ${req.urlWithParams}`);

  return next(req).pipe(
    tap(event => {
      if (event instanceof HttpResponse) {
        const elapsed = Date.now() - started;
        console.log(`Incoming Response: ${event.status} (${elapsed}ms) for ${req.urlWithParams}`);
      }
    }, error => {
        // Error logging handled separately by catchError or another interceptor
        console.error(`Request Error: ${req.method} ${req.urlWithParams}`, error);
    })
  );
};

// Register in main.ts: provideHttpClient(withInterceptors([authInterceptor, loggingInterceptor]))
// Order matters: authInterceptor runs before loggingInterceptor for outgoing requests
```

`HttpClient` provides a robust way to handle HTTP communication, and Interceptors offer a powerful mechanism for globally managing requests and responses.

*(Refer to the official Angular HttpClient and Interceptors documentation.)*