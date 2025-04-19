# Angular: Signals Basics

Introduction to Angular Signals for state management and reactivity.

## Core Concept: Signals

Introduced in Angular 16 and becoming more central, Signals offer a fine-grained reactivity system. They provide a way to track state changes and automatically update only the parts of the application that depend on that state, potentially leading to performance improvements over zone.js-based change detection in some scenarios.

*   **Signal:** A wrapper around a value that notifies interested consumers when the value changes. Signals can contain any value, from primitives to complex data structures.
*   **`signal(initialValue)`:** Creates a new writable signal with an initial value.
*   **`computed(computationFn)`:** Creates a computed signal whose value is derived from other signals. It recalculates its value only when its dependencies change and only when read.
*   **`effect(effectFn)`:** Registers a side effect that runs whenever any signal read inside its function changes. Useful for logging, analytics, or interacting with browser APIs, but **not** for updating other state (use `computed` for derived state). Effects run asynchronously during the change detection cycle.

## Using Signals

**1. Creating Signals:**

```typescript
import { Component, signal, computed, effect, Injector, runInInjectionContext } from '@angular/core';

@Component({ /* ... */ })
export class CounterComponent {
  count = signal(0); // Create a writable signal with initial value 0
  doubleCount = computed(() => this.count() * 2); // Create a computed signal

  // Injector needed if effect created outside injection context (like constructor/field initializer)
  constructor(private injector: Injector) {
    // Effect runs whenever 'count' changes
    effect(() => {
      console.log(`The count is: ${this.count()}`);
    });

    // Example: Effect needing injection context
    // runInInjectionContext(this.injector, () => {
    //   effect(() => {
    //     const service = inject(MyService); // Can inject here
    //     console.log(`Count from service perspective: ${this.count()}`);
    //   });
    // });
  }
}
```

**2. Reading Signal Values:**

*   Read a signal's current value by calling it like a function: `this.count()`, `this.doubleCount()`.
*   Reading a signal within a `computed` or `effect` function automatically tracks it as a dependency.

**3. Updating Writable Signals:**

*   **`.set(newValue)`:** Directly set a new value, replacing the old one.
    ```typescript
    increment() {
      this.count.set(this.count() + 1);
    }
    ```
*   **`.update(updateFn)`:** Update the value based on the current value. Preferred for complex updates.
    ```typescript
    decrement() {
      this.count.update(currentValue => currentValue - 1);
    }
    ```
*   **`.mutate(mutateFn)`:** (For signals holding objects/arrays) Mutate the *current* value directly within the function. Use less often than `set` or `update`.
    ```typescript
    // Assuming user = signal({ name: 'A', details: {...} })
    updateUserName(newName: string) {
      this.user.mutate(currentUser => {
        currentUser.name = newName; // Mutate the object directly
      });
    }
    ```

**4. Using Signals in Templates:**

*   Read signal values directly in the template using the function call syntax. Angular's change detection automatically tracks signal dependencies used in the template.

```html
<!-- counter.component.html -->
<p>Count: {{ count() }}</p>
<p>Double Count: {{ doubleCount() }}</p>
<button (click)="increment()">Increment</button>
<button (click)="decrement()">Decrement</button>
```

## Signals vs. RxJS Observables

*   **Signals:**
    *   Synchronous: Value is always available immediately on read (`signal()`).
    *   Glitch-free: Computed signals update atomically based on consistent state.
    *   Fine-grained tracking: Only components/effects using a changed signal are updated.
    *   Designed primarily for synchronous state management within Angular.
*   **RxJS Observables:**
    *   Asynchronous: Represent streams of values over time (zero or more).
    *   Powerful Operators: Extensive library for complex event handling, async coordination, transformations.
    *   Better suited for handling asynchronous events (HTTP requests, user input events, WebSockets).

**Interop:**

*   Angular provides functions to convert between Signals and Observables:
    *   `toSignal(observable$, options?)`: Converts an Observable to a Signal. Requires an injection context or specifying `requireSync: true` if you know the Observable emits synchronously.
    *   `toObservable(signal)`: Converts a Signal to an Observable, emitting the signal's value whenever it changes.

```typescript
import { toSignal, toObservable } from '@angular/core/rxjs-interop';
import { interval } from 'rxjs';
import { signal, computed } from '@angular/core';

// Observable to Signal
const counter$ = interval(1000);
const counterSignal = toSignal(counter$, { initialValue: 0 }); // Requires initial value for async source

// Signal to Observable
const mySig = signal('initial');
const myObs$ = toObservable(mySig);
myObs$.subscribe(value => console.log('Signal changed:', value));
mySig.set('new value');
```

Signals offer a simpler mental model for synchronous state management and enable more fine-grained reactivity, potentially improving performance. They work alongside RxJS, which remains the tool of choice for complex asynchronous event handling.

*(Refer to the official Angular Signals documentation.)*