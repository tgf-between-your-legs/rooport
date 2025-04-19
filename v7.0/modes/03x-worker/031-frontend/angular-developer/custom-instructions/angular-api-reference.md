# Angular API Quick Reference (Modern / Standalone Focus)

*(Condensed summary - consult official docs at angular.dev for full details)*

## Core Decorators & Functions

*   **`@Component({...})`:** Decorator for defining components.
    *   `selector`: CSS selector for the component (e.g., `'app-user-profile'`).
    *   `template`/`templateUrl`: Inline HTML or path to HTML file.
    *   `styles`/`styleUrls`: Inline CSS strings or paths to CSS files.
    *   `standalone: true`: Marks component as standalone (preferred).
    *   `imports`: Array of other standalone components, directives, pipes, or NgModules needed by the template.
    *   `changeDetection: ChangeDetectionStrategy.OnPush`: Optional strategy for performance.
*   **`@Directive({...})`:** Decorator for attribute or structural directives.
    *   `selector`: CSS selector (e.g., `[appHighlight]`, `*appIf`).
    *   `standalone: true`: Marks directive as standalone.
    *   `host`: Binds host element properties/attributes/events.
*   **`@Injectable({...})`:** Decorator for services.
    *   `providedIn: 'root'`: Makes service available application-wide (singleton).
*   **`@Pipe({...})`:** Decorator for custom pipes.
    *   `name`: Name used in template (e.g., `'customDate'`).
    *   `standalone: true`: Marks pipe as standalone.
*   **`inject(ServiceType)`:** Function used within constructors or factory functions for Dependency Injection.
*   **`input<T>()`, `input.required<T>()`:** Decorator-less way to define component inputs.
*   **`output<T>()`:** Decorator-less way to define component outputs (`EventEmitter`).
*   **`signal(initialValue)`:** Creates a writable signal for state management.
*   **`computed(() => ...)`:** Creates a derived signal based on other signals.
*   **`effect(() => ...)`:** Runs side effects in response to signal changes.

## Common Modules (Less needed with Standalone Components, but good to know)

*   **`CommonModule` (`@angular/common`):** Provides common directives like `@if`, `@for`, `@switch`, `[ngClass]`, `[ngStyle]`, and pipes like `async`, `date`, `currency`. *Often imported via `imports` in standalone components.*
*   **`RouterModule` (`@angular/router`):** Provides routing directives (`routerLink`, `routerOutlet`) and services. Configured via `provideRouter()`.
*   **`FormsModule` (`@angular/forms`):** Enables template-driven forms (`ngModel`).
*   **`ReactiveFormsModule` (`@angular/forms`):** Enables reactive forms (`formControl`, `formGroup`).
*   **`HttpClientModule` (`@angular/common/http`):** Provides `HttpClient` service. Configured via `provideHttpClient()`.

## Routing (`@angular/router`)

*   **`provideRouter(routes)`:** Main function in `app.config.ts` to configure routes.
*   **`Routes` (Type):** Array of route configuration objects.
    *   `{ path: 'users', component: UserListComponent }`
    *   `{ path: 'users/:id', component: UserDetailComponent }`
    *   `{ path: 'admin', loadComponent: () => import('./admin/admin.component').then(m => m.AdminComponent) }` (Lazy loading)
    *   `{ path: '', redirectTo: '/home', pathMatch: 'full' }`
    *   `{ path: '**', component: PageNotFoundComponent }` (Wildcard)
*   **`<router-outlet>`:** Directive marking where routed components should be displayed.
*   **`[routerLink]="['/path', id]"`:** Directive for navigation links.
*   **`Router` Service:** Programmatic navigation (`router.navigate(...)`).
*   **`ActivatedRoute` Service:** Access route parameters, query params, data.

## HttpClient (`@angular/common/http`)

*   **`provideHttpClient(withInterceptors([...]))`:** Main function in `app.config.ts`.
*   **`HttpClient` Service:** Injected into services.
    *   `http.get<User[]>('/api/users')`
    *   `http.post<User>('/api/users', userData)`
    *   `http.put<User>(`/api/users/${id}`, updates)`
    *   `http.delete(`/api/users/${id}`)`
*   **`HttpInterceptorFn` (Type):** Function type for creating interceptors (e.g., adding auth headers).

## Lifecycle Hooks (Common)

*   **`constructor()`:** DI happens here. Basic initialization.
*   **`ngOnInit()`:** Called once after initial data-bound properties are set. Good for initial data fetch.
*   **`ngOnChanges(changes: SimpleChanges)`:** Called before `ngOnInit` and whenever data-bound input properties change.
*   **`ngOnDestroy()`:** Called just before the component/directive is destroyed. Crucial for cleanup (e.g., unsubscribing from Observables).

*(This is a highly condensed view. Always refer to the official Angular documentation for specifics.)*