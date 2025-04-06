## Angular (Modern) - Condensed Context Index

### Overall Purpose

Angular is a comprehensive, TypeScript-based web framework developed by Google for building scalable single-page applications (SPAs) and complex user interfaces. It utilizes a component-based architecture, dependency injection, and a powerful template system to facilitate development.

### Core Concepts & Capabilities

*   **Components (`@Component`):** Fundamental UI building blocks encapsulating template (HTML), styles (CSS), and logic (TypeScript). Key decorators/properties: `selector`, `template`/`templateUrl`, `styles`/`styleUrl`, `imports`.
*   **Modules (`@NgModule`):** Organize components, directives, pipes, and services. `imports` array links necessary modules (e.g., `ReactiveFormsModule`, `FormsModule`, `RouterModule`). Standalone components reduce reliance on NgModules.
*   **Dependency Injection (DI):** Manages service instances and dependencies. Use `@Injectable({ providedIn: 'root' })` for singleton services or the `inject()` function for flexible injection. Constructor injection is also common.
*   **Templates & Data Binding:** HTML enhanced with Angular syntax. Supports interpolation (`{{ }}`), property binding (`[]`), event binding (`()`), two-way binding (`[()]`), template variables (`#var`).
*   **Directives (`@Directive`):** Modify DOM structure or behavior. Attribute directives change appearance/behavior (e.g., `[ngClass]`, `[ngStyle]`); Structural directives alter layout (e.g., `@if`, `@for`, `@switch`).
*   **Services (`@Injectable`):** Reusable logic/data access classes, typically singletons injected into components/other services.
*   **Routing (`@angular/router`):** Manages navigation between different views/components. Configured via `provideRouter(routes)` and uses `routerLink` directive in templates.
*   **Forms (`@angular/forms`):** Handles user input.
    *   **Reactive Forms:** Explicit control creation in component class (`FormGroup`, `FormControl`), validation (`Validators`), template binding (`[formGroup]`, `formControlName`). Requires `ReactiveFormsModule`.
    *   **Template-Driven Forms:** Logic primarily in the template (`ngModel`, `[(ngModel)]`). Requires `FormsModule`.
*   **Signals (`@angular/core`):** Fine-grained reactive state management. Core functions: `signal()`, `computed()`, `effect()`. Methods: `.set()`, `.update()`.
*   **HttpClient (`@angular/common/http`):** Service for making HTTP requests. Configured via `provideHttpClient()`. Methods: `get()`, `post()`, etc. Supports interceptors (`HttpInterceptorFn`).
*   **Pipes (`@Pipe`):** Transform data within templates (e.g., formatting dates, currency). Custom pipes implement `PipeTransform`.
*   **Lifecycle Hooks:** Methods called during component/directive lifecycle (e.g., `ngOnInit`, `ngOnChanges`). Implement corresponding interfaces (`OnInit`, `OnChanges`).
*   **Angular CLI:** Essential command-line tool (`ng new`, `ng generate`, `ng serve`, `ng build`, `ng test`).

### Key APIs / Components / Configuration / Patterns

*   `@Component({ ... })`: Defines a component with metadata (selector, template, styles, imports).
*   `@Injectable({ providedIn: 'root' })`: Defines a service injectable application-wide.
*   `inject(ServiceType)`: Function for DI, often preferred over constructor injection.
*   `signal(initialValue)`: Creates a writable signal for reactive state.
*   `computed(() => expression)`: Creates a derived signal based on other signals.
*   `effect(() => { /* side effect */ })`: Executes code reactively based on signal changes.
*   `FormControl`, `FormGroup`: Classes for building reactive forms.
*   `Validators`: Provides standard form validation functions (e.g., `required`, `minLength`).
*   `HttpClient`: Service for HTTP requests (`http.get<T>()`, `http.post<T>()`).
*   `provideRouter(routes)`: Configures application routes.
*   `routerLink="/path"`: Navigates to a specified route.
*   `@Input()`, `input.required<T>()`: Defines component input properties.
*   `@Output()`, `output<T>()`: Defines component output event emitters.
*   `@ViewChild('templateVar')`: Accesses template elements/components in the component class.
*   `@if`, `@for`, `@switch`: Built-in template control flow syntax.
*   `ng generate component <name>`: CLI command to scaffold a new component.
*   `provideHttpClient(withInterceptors([loggingInterceptor]))`: Configures HttpClient with interceptors.
*   `provideClientHydration()`: Enables server-side rendering hydration.

### Common Patterns & Best Practices / Pitfalls

*   **Modularity:** Use standalone components or feature modules to organize code.
*   **Services:** Encapsulate business logic and data access in injectable services.
*   **Reactivity:** Leverage Signals for efficient state management and change detection.
*   **Forms:** Prefer Reactive Forms for complex validation and dynamic scenarios. Remember to import `ReactiveFormsModule` or `FormsModule`.
*   **HTTP:** Use `HttpClient` within services. Handle errors and use `async` pipe or `.subscribe()` correctly. Consider interceptors for auth, logging.
*   **Lifecycle:** Understand key hooks like `ngOnInit` (initialization) and `ngOnDestroy` (cleanup).
*   **CLI:** Use `ng generate` for consistency and speed.
*   **Testing:** Write unit tests (`ng test`) and E2E tests. Use `--no-watch --browsers=ChromeHeadless` for CI.
*   **Security:** Angular provides built-in XSS protection (e.g., sanitizing `innerHTML`). Be cautious when bypassing security mechanisms.

---
This index summarizes the core concepts, APIs, and patterns for Angular (Modern) based on the provided snippets. Consult the full official Angular documentation for exhaustive details. Source: `project_journal/context/source_docs/angular-developer-llms-context-20250406.md`