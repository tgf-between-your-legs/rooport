# Angular Performance Optimization Tips

Key areas and techniques for improving Angular application performance.

## 1. Change Detection Strategy

*   **Default:** Angular's default change detection checks the entire component tree on many async events (timers, clicks, HTTP requests).
*   **`OnPush`:**
    *   **What:** `changeDetection: ChangeDetectionStrategy.OnPush` in `@Component`.
    *   **How:** Component only re-checks if:
        *   An `@Input()` reference changes.
        *   An event originates from the component or its children.
        *   `async` pipe receives a new value.
        *   Manually triggered via `ChangeDetectorRef.detectChanges()` or `markForCheck()`.
        *   A bound signal's value changes.
    *   **Benefit:** Significantly reduces the number of checks, improving performance, especially in large applications.
    *   **Requirement:** Requires immutable data patterns (create new object/array references for `@Input()` changes) or explicit triggering.

## 2. Lazy Loading Modules/Components

*   **Concept:** Load code for specific features (routes) only when the user navigates to them, reducing the initial bundle size and improving startup time.
*   **Implementation (Routing):** Use `loadComponent` (for standalone components) or `loadChildren` (for NgModules) in the `Routes` configuration.
    ```typescript
    // Standalone
    { path: 'admin', loadComponent: () => import('./admin/admin.component').then(m => m.AdminComponent) }
    // Module-based (less common now)
    { path: 'customers', loadChildren: () => import('./customers/customers.module').then(m => m.CustomersModule) }
    ```
*   **Benefit:** Smaller initial download, faster perceived load time.

## 3. RxJS Optimization

*   **Unsubscribe:** Always unsubscribe from Observables when a component is destroyed (`ngOnDestroy`) to prevent memory leaks. Use operators like `takeUntil(this.destroy$)` or the `async` pipe.
*   **`async` Pipe:** Handles subscription and unsubscription automatically in templates. `*ngIf="data$ | async as data"`.
*   **Share Operators:** Use `shareReplay(1)` to multicast and cache the last emitted value for multiple subscribers to the same Observable (e.g., multiple `async` pipes using the same HTTP request result).
*   **Avoid Nested Subscriptions:** Use higher-order mapping operators (`switchMap`, `mergeMap`, `concatMap`, `exhaustMap`) instead of subscribing inside another subscription.

## 4. Signals

*   **Fine-Grained Updates:** Signals inherently enable more targeted change detection updates compared to Zone.js-based default strategy. Use them for component state where appropriate.
*   **`computed()`:** Use for derived state; calculations are memoized and only re-run when dependencies change.
*   **`effect()`:** Use for side effects, but be mindful of potential performance implications if the effect triggers frequently or performs heavy computations. Use `manualCleanup` option if needed.

## 5. Build Optimizations (`ng build --configuration=production`)

*   **AOT Compilation:** Ahead-of-Time compilation (default in production builds) compiles HTML templates and components into efficient JavaScript during the build.
*   **Minification & Uglification:** Reduces code size.
*   **Tree Shaking:** Removes unused code.
*   **Differential Loading:** Creates separate bundles for modern and older browsers (less relevant now as support for older browsers like IE is dropped).

## 6. Other Techniques

*   **`trackBy` Function:** For `@for` loops (`*ngFor`), provide a `trackBy` function that returns a unique identifier for each item. This helps Angular optimize DOM updates when the list changes.
*   **Virtual Scrolling (CDK):** Use `@angular/cdk/scrolling` for efficiently rendering large lists by only rendering items visible in the viewport.
*   **Web Workers:** Offload CPU-intensive tasks to background threads.
*   **Optimize Assets:** Compress images, use efficient formats (WebP), lazy-load images below the fold.

*(Consult Angular documentation and web performance best practices for more details.)*