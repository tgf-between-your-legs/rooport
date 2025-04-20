# Common Angular Component Patterns

Examples of common patterns for structuring Angular components.

## 1. Smart vs. Dumb Components (Container/Presentational)

*   **Smart Components (Containers):**
    *   **Purpose:** Manage state, fetch data (often via injected services), handle complex logic, and pass data down to child components. Often correspond to routed components.
    *   **Characteristics:** Inject services, manage state (Signals/RxJS), use `async` pipe, minimal presentation logic in template.
    *   *Example:* `UserProfileContainerComponent` fetches user data and passes it to `UserProfileDisplayComponent`.
*   **Dumb Components (Presentational):**
    *   **Purpose:** Display data received via `@Input()` and emit events via `@Output()`. Focus solely on the UI and presentation logic. Highly reusable.
    *   **Characteristics:** Primarily use `@Input()` and `@Output()`, minimal injected services (often none), stateless or minimal internal UI state, use `ChangeDetectionStrategy.OnPush`.
    *   *Example:* `ButtonComponent`, `DataGridComponent`, `UserProfileDisplayComponent`.

## 2. Content Projection (`<ng-content>`)

*   **Purpose:** Allows parent components to pass content (HTML, other components) *into* a child component's template, making the child more flexible and reusable.
*   **Implementation:**
    *   Child Component Template: Use `<ng-content></ng-content>` (single slot) or `<ng-content select="[css-selector]"></ng-content>` (multi-slot) where projected content should appear.
    *   Parent Component Template: Place content inside the child component's tags: `<app-child><p>Projected Content</p></app-child>`. For multi-slot, use attributes matching the `select` selector: `<app-child><h2 header>Title</h2><p content>Body</p></app-child>`.
*   **Use Case:** Creating reusable layout components (cards, modals, sidebars) where the internal content varies.

## 3. Template Outlet (`<ng-container *ngTemplateOutlet="...">`)

*   **Purpose:** Renders a template defined by `<ng-template>` dynamically, potentially passing context data. More flexible than simple content projection for complex conditional rendering or reusable template definitions.
*   **Implementation:**
    *   Define a template: `<ng-template #myTemplate let-data="contextData">...</ng-template>`
    *   Render it: `<ng-container *ngTemplateOutlet="myTemplate; context: {$implicit: defaultData, contextData: otherData}"></ng-container>`
*   **Use Case:** Dynamic rendering based on conditions, creating highly configurable components where parts of the template can be provided externally.

## 4. Control Value Accessor (`ControlValueAccessor`)

*   **Purpose:** Allows custom components to integrate seamlessly with Angular Forms (both Reactive and Template-driven), acting like native form controls (`ngModel`, `formControlName`).
*   **Implementation:** Implement the `ControlValueAccessor` interface (`writeValue`, `registerOnChange`, `registerOnTouched`, `setDisabledState`) on the custom form component. Provide the component using `NG_VALUE_ACCESSOR`.
*   **Use Case:** Creating custom form inputs (e.g., star rating, custom slider, rich text editor) that work with standard Angular form directives.

## 5. Standalone Components

*   **Purpose:** Simplifies Angular architecture by allowing components, directives, and pipes to manage their own dependencies directly via the `imports` array, reducing reliance on `NgModule`. **This is the preferred approach in modern Angular.**
*   **Implementation:** Add `standalone: true` and the `imports: [...]` array to the `@Component`, `@Directive`, or `@Pipe` decorator. Import necessary standalone components, directives, pipes, or `NgModule`s directly.
*   **Benefit:** Improved modularity, easier refactoring, better tree-shaking potential.

*(These are foundational patterns. Explore Angular documentation and community resources for more advanced techniques like dynamic component loading, custom structural directives, etc.)*