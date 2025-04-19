# Angular: Standalone Components, Directives, and Pipes

Using the modern standalone API for building Angular applications without NgModules.

## Core Concept

Introduced as stable in Angular 15 and becoming the default in Angular 17+, the standalone API allows components, directives, and pipes to manage their own dependencies directly, without needing to be declared in an `NgModule`. This simplifies the architecture, reduces boilerplate, and improves tree-shakability.

## Standalone Components

*   **Declaration:** Add `standalone: true` to the `@Component` decorator metadata.
*   **Dependencies:** Declare dependencies (other standalone components, directives, pipes, or even NgModules) directly in the component's `imports` array.
*   **Bootstrapping:** Bootstrap a standalone component directly in `main.ts` using `bootstrapApplication`.
*   **Routing:** Configure routes using `provideRouter` and lazy load standalone components using `loadComponent`.

```typescript
// src/app/app.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { UserProfileComponent } from './user-profile/user-profile.component'; // Import standalone component

@Component({
  selector: 'app-root',
  standalone: true, // Mark as standalone
  imports: [
    CommonModule,
    RouterOutlet,
    UserProfileComponent // Import needed standalone components/directives/pipes
  ],
  template: `
    <h1>Welcome</h1>
    <nav>...</nav>
    <router-outlet></router-outlet>
    <app-user-profile userId="123"></app-user-profile>
  `
})
export class AppComponent {
  // ...
}

// src/main.ts (Bootstrapping)
import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter } from '@angular/router';
import { AppComponent } from './app/app.component';
import { appRoutes } from './app/app.routes'; // Define routes separately
import { provideHttpClient } from '@angular/common/http'; // Import providers

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(appRoutes), // Provide router configuration
    provideHttpClient() // Provide HttpClient globally
    // Other application-wide providers
  ]
}).catch(err => console.error(err));

// src/app/app.routes.ts (Routing)
import { Routes } from '@angular/router';

export const appRoutes: Routes = [
  {
    path: 'dashboard',
    // Lazy load a standalone component
    loadComponent: () => import('./dashboard/dashboard.component').then(m => m.DashboardComponent)
  },
  {
    path: 'users/:id',
    loadComponent: () => import('./user-profile/user-profile.component').then(m => m.UserProfileComponent)
  },
  // ... other routes
];
```

## Standalone Directives and Pipes

*   **Declaration:** Add `standalone: true` to the `@Directive` or `@Pipe` decorator metadata.
*   **Usage:** Import them directly into the `imports` array of the standalone component(s) where they are needed.

```typescript
// src/app/shared/highlight.directive.ts
import { Directive, ElementRef, inject } from '@angular/core';

@Directive({
  selector: '[appHighlight]',
  standalone: true // Mark as standalone
})
export class HighlightDirective {
  private el = inject(ElementRef);
  constructor() {
    this.el.nativeElement.style.backgroundColor = 'yellow';
  }
}

// src/app/shared/initials.pipe.ts
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'initials',
  standalone: true // Mark as standalone
})
export class InitialsPipe implements PipeTransform {
  transform(value: string): string {
    if (!value) return '';
    return value.split(' ').map(n => n[0]).join('').toUpperCase();
  }
}

// src/app/some-component/some-component.component.ts
import { Component } from '@angular/core';
import { HighlightDirective } from '../shared/highlight.directive'; // Import directive
import { InitialsPipe } from '../shared/initials.pipe'; // Import pipe

@Component({
  selector: 'app-some-component',
  standalone: true,
  imports: [HighlightDirective, InitialsPipe], // Import dependencies
  template: `
    <p appHighlight>This text is highlighted.</p>
    <p>User: {{ userName | initials }}</p>
  `
})
export class SomeComponent {
  userName = "Alice Wonderland";
}
```

## Benefits of Standalone API

*   **Simplified Structure:** Reduces the need for `NgModule` boilerplate, making the application structure flatter and easier to understand.
*   **Improved Tree-Shaking:** Allows build tools to more effectively remove unused code, potentially resulting in smaller bundle sizes.
*   **Clearer Dependencies:** Each component/directive/pipe explicitly declares its own dependencies in the `imports` array.
*   **Easier Lazy Loading:** Simplified API (`loadComponent`) for lazy loading components and their dependencies.

The standalone API is the recommended approach for new Angular applications, offering a more streamlined and potentially more performant development experience. While NgModules remain supported, standalone is the future direction.

*(Refer to the official Angular Standalone Components documentation.)*