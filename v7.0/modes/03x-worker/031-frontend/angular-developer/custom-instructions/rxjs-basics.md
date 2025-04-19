# Angular: RxJS Basics

Introduction to RxJS Observables and common operators used in Angular.

## Core Concept: Observables

RxJS (Reactive Extensions for JavaScript) is a library for reactive programming using Observables, which makes it easier to compose asynchronous or callback-based code. Angular uses Observables extensively for handling events, HTTP requests, routing information, and state management.

*   **Observable:** Represents a stream of values over time. It can emit zero or more values, and optionally a completion or error signal. Think of it like a promise that can return multiple values.
*   **Observer:** An object with `next()`, `error()`, and `complete()` methods that defines how to react to values, errors, or completion signals emitted by an Observable.
*   **Subscription:** The execution of an Observable. Created by calling the `subscribe()` method on an Observable, passing an Observer (or just a `next` callback). Subscriptions should usually be cleaned up (unsubscribed) to prevent memory leaks.
*   **Operators:** Pure functions that enable a functional programming style for dealing with Observables. They take an Observable as input and return a new Observable (e.g., `map`, `filter`, `tap`, `switchMap`, `catchError`). Operators are "piped" together.

## Common Use Cases in Angular

*   **`HttpClient`:** Methods like `http.get()` return Observables that emit the HTTP response once and then complete (or error).
*   **`ActivatedRoute`:** Properties like `paramMap`, `queryParamMap`, and `data` are Observables that can emit multiple times if route parameters change.
*   **`EventEmitter` (`@Output`):** Extends RxJS `Subject` (a type of Observable) to emit custom events from child to parent components.
*   **Reactive Forms:** Properties like `valueChanges` and `statusChanges` on `FormControl`, `FormGroup`, `FormArray` are Observables.
*   **State Management:** Libraries like NgRx or NGXS heavily rely on RxJS for managing application state reactively. Even simple service-based state often uses `BehaviorSubject` or `Subject`.

## Creating & Subscribing

```typescript
import { Observable, of, from, interval, Subject, BehaviorSubject } from 'rxjs';
import { map, filter, take, finalize } from 'rxjs/operators';

// Creating Observables
const simpleObservable = of(1, 2, 3); // Emits 1, 2, 3 then completes
const arrayObservable = from(['a', 'b', 'c']); // Emits 'a', 'b', 'c' then completes
const intervalObservable = interval(1000).pipe(take(5)); // Emits 0, 1, 2, 3, 4 every second

// Subject: Multicast - pushes values to multiple observers
const mySubject = new Subject<string>();

// BehaviorSubject: Subject with an initial value, emits last value to new subscribers
const myBehaviorSubject = new BehaviorSubject<number>(0);

// Subscribing
console.log('Subscribing to simpleObservable:');
const subscription1 = simpleObservable.subscribe({
  next: value => console.log('Next:', value),
  error: err => console.error('Error:', err),
  complete: () => console.log('Complete!')
});
// subscription1.unsubscribe(); // Usually unsubscribe in ngOnDestroy

console.log('Subscribing to intervalObservable:');
const subscription2 = intervalObservable
  .pipe(
    map(val => val * 10), // Multiply emitted value by 10
    filter(val => val > 10), // Only pass values greater than 10
    finalize(() => console.log('Interval finalized')) // Runs on complete or error
  )
  .subscribe(value => console.log('Interval Value:', value));

// Using Subjects
mySubject.subscribe(val => console.log('Subject Observer A:', val));
mySubject.next('Hello'); // Both A and B receive 'Hello'
mySubject.subscribe(val => console.log('Subject Observer B:', val));
mySubject.next('World'); // Both A and B receive 'World'

myBehaviorSubject.subscribe(val => console.log('BehaviorSubject Observer C:', val)); // Receives 0 immediately
myBehaviorSubject.next(1); // C receives 1
myBehaviorSubject.subscribe(val => console.log('BehaviorSubject Observer D:', val)); // Receives 1 immediately
myBehaviorSubject.next(2); // C and D receive 2
```

## Common RxJS Operators

*   **Transformation:**
    *   `map(value => ...)`: Transform each emitted value.
    *   `pluck('propertyName')`: Select a nested property from emitted objects.
    *   `scan((acc, value) => ..., seed)`: Accumulate values over time (like `reduce` for streams).
*   **Filtering:**
    *   `filter(value => ...)`: Emit only values that pass a condition.
    *   `take(n)`: Emit only the first `n` values.
    *   `skip(n)`: Skip the first `n` values.
    *   `first()`: Emit only the first value (or first matching a condition).
    *   `last()`: Emit only the last value.
    *   `debounceTime(ms)`: Emit only after a specified time has passed without new emissions (useful for input throttling).
    *   `distinctUntilChanged()`: Emit only if the current value is different from the previous one.
*   **Combination:**
    *   `concat(...observables)`: Subscribe to Observables sequentially, only starting the next when the previous completes.
    *   `merge(...observables)`: Subscribe to all Observables concurrently, emitting values as they arrive from any source.
    *   `combineLatest([...observables])`: Emit an array of the latest values from *each* source Observable whenever *any* source emits.
    *   `forkJoin([...observables])`: Wait for *all* source Observables to complete, then emit an array of their last values. (Like `Promise.all`).
*   **Higher-Order Mapping (Handling inner Observables, e.g., after HTTP calls):**
    *   `switchMap(value => innerObservable)`: Subscribes to `innerObservable`. If the outer Observable emits again, *unsubscribes* from the previous `innerObservable` and switches to the new one. **Common for handling sequential dependent requests where only the latest matters (e.g., search-as-you-type).**
    *   `mergeMap(value => innerObservable)` / `flatMap()`: Subscribes to `innerObservable` for each outer emission. Runs inner Observables concurrently.
    *   `concatMap(value => innerObservable)`: Subscribes to `innerObservable` for each outer emission, but waits for the previous inner Observable to complete before starting the next. Maintains order.
    *   `exhaustMap(value => innerObservable)`: Subscribes to `innerObservable`. Ignores new outer emissions while the current inner Observable is still active. Useful for preventing multiple submissions.
*   **Error Handling:**
    *   `catchError(err => ...)`: Catches errors and returns a new Observable (e.g., `of([])` to provide a default value) or re-throws the error.
*   **Utility:**
    *   `tap(value => ...)`: Perform side effects (like logging) without modifying the stream.
    *   `finalize(() => ...)`: Execute cleanup logic when the Observable completes or errors.

## Async Pipe (`| async`)

*   **Concept:** A built-in Angular pipe that automatically subscribes to an Observable (or Promise) in the template, unwraps the latest emitted value, and automatically unsubscribes when the component is destroyed.
*   **Benefits:** Reduces boilerplate for subscribing/unsubscribing in the component class, handles change detection automatically. **Highly recommended.**

```typescript
// component.ts
data$: Observable<DataType[]> = this.dataService.getData();
```
```html
<!-- template.html -->
@if (data$ | async; as data) { // Subscribe and assign value to 'data' variable
  <ul>
    @for (item of data; track item.id) {
      <li>{{ item.name }}</li>
    }
  </ul>
} @else {
  <p>Loading data...</p> <!-- Shown while waiting for first emission -->
}
```

RxJS and Observables are powerful tools for managing asynchronous operations and state in Angular. Understanding core concepts and common operators is essential.

*(Refer to the official RxJS documentation and Angular's guide on Observables.)*