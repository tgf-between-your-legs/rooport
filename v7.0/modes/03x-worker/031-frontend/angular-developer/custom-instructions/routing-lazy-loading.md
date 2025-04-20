# Angular: Routing & Lazy Loading

Configuring navigation between views and implementing lazy loading for feature modules or standalone components.

## Core Concept: Angular Router

The `@angular/router` module enables navigation between different views (components) in an Angular application. It interprets browser URL changes and displays the corresponding component hierarchy.

**Key Components & Concepts:**

*   **`Routes`:** An array defining the mapping between URL paths and components.
*   **`provideRouter(routes, ...options)`:** Function used in `main.ts` (for standalone apps) or `AppRoutingModule` (`imports: [RouterModule.forRoot(routes)]` in classic apps) to configure the router with the defined routes.
*   **`<router-outlet>`:** A directive acting as a placeholder in a component's template where the router should render the matched component for the current route.
*   **`routerLink` Directive:** Used on anchor (`<a>`) or other elements to create navigation links without causing a full page reload.
    *   `<a routerLink="/users">Users</a>`
    *   `<a [routerLink]="['/users', userId]">User Profile</a>` (With parameters)
*   **`routerLinkActive` Directive:** Adds CSS classes to an active `routerLink` element, useful for styling active navigation items.
    *   `<a routerLink="/users" routerLinkActive="active-link">Users</a>`
*   **Route Parameters:** Capture values from the URL path (e.g., `/users/:id`). Accessed via `ActivatedRoute` service.
*   **ActivatedRoute Service:** Injected service providing access to information about the currently activated route (parameters, query parameters, data).
*   **Router Service:** Injected service for imperative navigation (`router.navigate(['/path'])`, `router.navigateByUrl('/path')`).

## Basic Routing Configuration (Standalone)

```typescript
// src/app/app.routes.ts
import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component'; // Assume standalone
import { UserListComponent } from './user-list/user-list.component'; // Assume standalone
import { UserProfileComponent } from './user-profile/user-profile.component'; // Assume standalone
import { NotFoundComponent } from './not-found/not-found.component'; // Assume standalone

export const appRoutes: Routes = [
  { path: '', component: HomeComponent, pathMatch: 'full' }, // Default route
  { path: 'users', component: UserListComponent },
  { path: 'users/:id', component: UserProfileComponent }, // Route with parameter ':id'
  // ... other routes
  { path: '**', component: NotFoundComponent } // Wildcard route (must be last)
];

// src/main.ts
import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter } from '@angular/router';
import { AppComponent } from './app/app.component';
import { appRoutes } from './app/app.routes';

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(appRoutes) // Provide the routes
    // Other providers like provideHttpClient()
  ]
}).catch(err => console.error(err));

// src/app/app.component.ts (Template needs <router-outlet>)
import { Component } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive], // Import router directives
  template: `
    <nav>
      <a routerLink="/" routerLinkActive="active" [routerLinkActiveOptions]="{exact: true}">Home</a> |
      <a routerLink="/users" routerLinkActive="active">Users</a>
    </nav>
    <hr>
    <router-outlet></router-outlet> <!-- Where routed components render -->
  `
})
export class AppComponent {}

// src/app/user-profile/user-profile.component.ts (Accessing route params)
import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { map, switchMap } from 'rxjs/operators'; // Import RxJS operators

@Component({ /* ... */ })
export class UserProfileComponent implements OnInit {
  private route = inject(ActivatedRoute);
  userId$: Observable<string | null> = this.route.paramMap.pipe(
    map(params => params.get('id'))
  );
  // Or snapshot (less reactive): const userId = this.route.snapshot.paramMap.get('id');

  ngOnInit() {
    this.userId$.subscribe(id => {
      console.log('User ID:', id);
      // Fetch user data based on id
    });
  }
}
```

## Lazy Loading

*   **Concept:** Defers loading the code for certain parts of the application (feature areas) until the user navigates to them. Improves initial load time and performance by reducing the initial bundle size.
*   **Standalone Components:** Use `loadComponent` in the route definition.
*   **NgModules (Classic):** Use `loadChildren` in the route definition, pointing to a feature module file.

```typescript
// src/app/app.routes.ts (Lazy Loading Standalone Component)
import { Routes } from '@angular/router';

export const appRoutes: Routes = [
  { path: '', loadComponent: () => import('./home/home.component').then(m => m.HomeComponent), pathMatch: 'full' },
  {
    path: 'admin', // Lazy load the whole admin section
    loadChildren: () => import('./admin/admin.routes').then(m => m.ADMIN_ROUTES) // Lazy load child routes
  },
  {
    path: 'products',
    loadComponent: () => import('./products/product-list.component').then(m => m.ProductListComponent)
  },
  // ... other routes
];

// src/app/admin/admin.routes.ts (Child routes for lazy-loaded section)
import { Routes } from '@angular/router';

export const ADMIN_ROUTES: Routes = [
    { path: '', loadComponent: () => import('./dashboard/admin-dashboard.component').then(m => m.AdminDashboardComponent) },
    { path: 'settings', loadComponent: () => import('./settings/admin-settings.component').then(m => m.AdminSettingsComponent) },
    // ... other admin routes
];
```

*   **How it works:** When the user navigates to a lazy-loaded route for the first time, the Angular Router downloads the required JavaScript chunk(s) for that component/module and its dependencies.

Routing is fundamental for structuring SPAs, and lazy loading is essential for optimizing the performance of larger Angular applications.

*(Refer to the official Angular Routing & Navigation documentation.)*