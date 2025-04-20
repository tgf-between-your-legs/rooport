# Angular: Core Concepts

Fundamental building blocks of an Angular application.

## 1. Components (`@Component`)

*   **Concept:** The primary UI building block. Controls a patch of screen called a view. Encapsulates template (HTML), styles (CSS), and logic (TypeScript).
*   **Decorator:** `@Component({...})` provides metadata.
*   **Key Metadata:**
    *   `selector`: CSS selector that identifies this component in a template (e.g., `app-user-profile`).
    *   `template` / `templateUrl`: Inline HTML or path to an external HTML file.
    *   `styles` / `styleUrls`: Inline CSS strings or paths to external CSS/SCSS files (styles are scoped by default).
    *   `standalone: true`: (Modern Angular) Indicates the component manages its own dependencies.
    *   `imports`: (For standalone components) Array of other standalone components, directives, pipes, or NgModules needed by the template.
*   **Class:** Contains properties (data) and methods (logic) used by the template. Implements lifecycle hooks (e.g., `ngOnInit`).

```typescript
// src/app/user-profile/user-profile.component.ts
import { Component, Input, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common'; // Needed for @if, @for etc.
import { UserService } from '../user.service'; // Example service

@Component({
  selector: 'app-user-profile',
  standalone: true,
  imports: [CommonModule], // Import necessary modules/components/pipes
  template: `
    @if (user) {
      <h2>{{ user.name }}</h2>
      <p>Email: {{ user.email }}</p>
    } @else {
      <p>Loading user...</p>
    }
  `,
  styles: [`h2 { color: blue; }`]
})
export class UserProfileComponent implements OnInit {
  @Input() userId!: string; // Input property from parent
  user: { name: string, email: string } | null = null;

  private userService = inject(UserService); // Dependency Injection

  ngOnInit(): void {
    if (this.userId) {
      this.userService.getUser(this.userId).subscribe(userData => {
        this.user = userData;
      });
    }
  }
}
```

## 2. Templates & Data Binding

*   **Concept:** HTML enhanced with Angular syntax to display component data and respond to user events.
*   **Interpolation `{{ }}`:** Display component property values as strings.
    *   `<h1>{{ pageTitle }}</h1>`
*   **Property Binding `[]`:** Bind an element property to a component property.
    *   `<img [src]="imageUrl" [alt]="altText">`
    *   `<button [disabled]="isSaving">Save</button>`
*   **Event Binding `()`:** Execute a component method when an element fires an event.
    *   `<button (click)="save()">Save</button>`
    *   `<input (input)="onInput($event)">`
*   **Two-Way Binding `[()]` ("Banana in a box"):** Combines property and event binding for form inputs (requires `FormsModule` or `ReactiveFormsModule`).
    *   `<input [(ngModel)]="userName">` (Template-driven forms)

## 3. Directives (`@Directive`)

*   **Concept:** Classes that add behavior or transform the DOM.
*   **Attribute Directives:** Change the appearance or behavior of an element (e.g., `[ngClass]`, `[ngStyle]`). Applied as attributes.
*   **Structural Directives:** Change the DOM layout by adding/removing elements (e.g., `@if`, `@for`, `@switch`). Preceded by `@` in modern Angular templates (or `*` in older syntax like `*ngIf`).

```html
<!-- Structural Directives -->
@if (isLoggedIn) {
  <p>Welcome back!</p>
} @else {
  <p>Please log in.</p>
}

<ul>
  @for (item of items; track item.id) {
    <li>{{ item.name }}</li>
  } @empty {
    <li>No items found.</li>
  }
</ul>

<!-- Attribute Directive -->
<p [ngClass]="{ 'active': isActive, 'error': hasError }">Status message</p>
```

## 4. Services (`@Injectable`) & Dependency Injection (DI)

*   **Concept:** Services encapsulate reusable logic or data access (e.g., fetching data, logging, calculations) separate from components. DI is Angular's mechanism for providing instances of services (dependencies) to components/directives/other services.
*   **Decorator:** `@Injectable({...})` marks a class as available for DI.
*   **`providedIn: 'root'`:** Makes the service a singleton available throughout the application. Preferred method.
*   **Injection:**
    *   **`inject()` function (Modern):** Preferred way inside constructors, factory functions, etc.
        ```typescript
        import { Injectable, inject } from '@angular/core';
        import { HttpClient } from '@angular/common/http';

        @Injectable({ providedIn: 'root' })
        export class DataService {
          private http = inject(HttpClient); // Inject HttpClient

          getData() {
            return this.http.get('/api/data');
          }
        }
        ```
    *   **Constructor Injection (Classic):** Type-hint dependencies in the class constructor.
        ```typescript
        // Less common now, inject() is preferred
        // constructor(private http: HttpClient) {}
        ```

## 5. Modules (`@NgModule`) - Less Common with Standalone

*   **Concept (Classic Angular):** Used to group related components, directives, pipes, and services. Configured DI providers and exported functionality.
*   **Standalone Components:** Modern Angular favors standalone components, directives, and pipes which declare their own dependencies via the `imports` array, reducing the need for NgModules for feature organization. NgModules are still used for library organization and some advanced scenarios.

These core concepts form the foundation of building applications with Angular.

*(Refer to the official Angular documentation for Components, Templates, Dependency Injection, etc.)*