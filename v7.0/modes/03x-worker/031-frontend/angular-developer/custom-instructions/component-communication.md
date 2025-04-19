# Angular: Component Communication Patterns

Methods for sharing data and events between Angular components.

## Core Concept

Components often need to interact with each other. Angular provides several mechanisms for parent-child communication and communication between unrelated components.

## 1. Parent-to-Child: `@Input()` Decorator

*   **Purpose:** Allows a parent component to pass data *down* to a child component.
*   **Mechanism:**
    1.  In the child component, declare a property decorated with `@Input()`. This property can now receive values from the parent.
    2.  In the parent component's template, use property binding `[]` on the child component's selector to pass data to the child's input property.
*   **`input.required<T>()` (Angular 16+):** A modern way to define required inputs, providing compile-time checks.

```typescript
// src/app/child/child.component.ts
import { Component, Input, input } from '@angular/core'; // Import Input or input

@Component({
  selector: 'app-child',
  standalone: true,
  template: `
    <p>Message from parent: {{ message }}</p>
    <p>User ID (required): {{ userId() }}</p> <!-- Read required input signal -->
  `
})
export class ChildComponent {
  // Classic @Input()
  @Input() message: string = 'Default message'; // Optional input with default

  // Modern required input signal (Angular 16+)
  userId = input.required<string>(); // Required input
}

// src/app/parent/parent.component.ts
import { Component } from '@angular/core';
import { ChildComponent } from '../child/child.component'; // Import child

@Component({
  selector: 'app-parent',
  standalone: true,
  imports: [ChildComponent], // Import child
  template: `
    <h2>Parent Component</h2>
    <app-child
      message="Hello from Parent!"
      userId="user-456"> <!-- Bind to child's input properties -->
    </app-child>
  `
})
export class ParentComponent { }
```

## 2. Child-to-Parent: `@Output()` Decorator & `EventEmitter`

*   **Purpose:** Allows a child component to emit events *up* to its parent component.
*   **Mechanism:**
    1.  In the child component, declare a property decorated with `@Output()`. Initialize it with a new `EventEmitter<T>()`, where `T` is the type of data to be emitted.
    2.  In the child component's logic, call the `.emit(data)` method on the `EventEmitter` property to send data upwards.
    3.  In the parent component's template, use event binding `()` on the child component's selector, binding the child's output property to a method in the parent component. The emitted data is available via the `$event` object.
*   **`output<T>()` (Angular 17.1+):** A modern, signal-based alternative to `@Output()` and `EventEmitter`.

```typescript
// src/app/child-emitter/child-emitter.component.ts
import { Component, Output, EventEmitter, output } from '@angular/core'; // Import Output, EventEmitter or output

@Component({
  selector: 'app-child-emitter',
  standalone: true,
  template: `
    <button (click)="sendMessage()">Send Message to Parent</button>
    <button (click)="sendSignalData()">Send Signal Data</button>
  `
})
export class ChildEmitterComponent {
  // Classic @Output()
  @Output() messageEvent = new EventEmitter<string>();

  // Modern output signal (Angular 17.1+)
  dataEvent = output<number>(); // Emits numbers

  sendMessage() {
    this.messageEvent.emit("Message from Child!");
  }

  sendSignalData() {
    this.dataEvent.emit(Math.random());
  }
}

// src/app/parent-listener/parent-listener.component.ts
import { Component } from '@angular/core';
import { ChildEmitterComponent } from '../child-emitter/child-emitter.component';

@Component({
  selector: 'app-parent-listener',
  standalone: true,
  imports: [ChildEmitterComponent],
  template: `
    <h2>Parent Listener</h2>
    <p>Message Received: {{ receivedMessage }}</p>
    <p>Data Received: {{ receivedData }}</p>
    <app-child-emitter
      (messageEvent)="receiveMessage($event)"
      (dataEvent)="receiveData($event)"> <!-- Bind to child's output properties -->
    </app-child-emitter>
  `
})
export class ParentListenerComponent {
  receivedMessage: string = '';
  receivedData: number | null = null;

  receiveMessage(message: string) {
    console.log('Parent received message:', message);
    this.receivedMessage = message;
  }

  receiveData(data: number) {
    console.log('Parent received data:', data);
    this.receivedData = data;
  }
}
```

## 3. Parent Interaction with Child: ViewChild/ViewChildren

*   **Purpose:** Allows a parent component to get a reference to a child component instance (or directive) within its template and call its public methods or access its public properties.
*   **Decorators:** `@ViewChild()` (for single instance), `@ViewChildren()` (for multiple instances, returns `QueryList`).
*   **Usage:** Decorate a property in the parent component class. Pass a selector (component class or template reference variable name) to the decorator. The reference is typically available in the `ngAfterViewInit` lifecycle hook.

```typescript
// src/app/parent-caller/parent-caller.component.ts
import { Component, ViewChild, AfterViewInit } from '@angular/core';
import { ChildActionComponent } from '../child-action/child-action.component'; // Assume ChildActionComponent has a public doSomething() method

@Component({
  selector: 'app-parent-caller',
  standalone: true,
  imports: [ChildActionComponent],
  template: `
    <h2>Parent Caller</h2>
    <button (click)="callChildMethod()">Call Child Method</button>
    <app-child-action #childRef></app-child-action> <!-- Template ref variable -->
  `
})
export class ParentCallerComponent implements AfterViewInit {
  // Access child using template reference variable '#childRef'
  @ViewChild('childRef') childComponent!: ChildActionComponent;
  // Or access child by component type (if only one instance)
  // @ViewChild(ChildActionComponent) childComponent!: ChildActionComponent;

  ngAfterViewInit() {
    // childComponent is now available
    console.log('Child component reference acquired.');
  }

  callChildMethod() {
    if (this.childComponent) {
      this.childComponent.doSomething(); // Call public method on child
    }
  }
}
```

## 4. Unrelated Components: Service-Based Communication

*   **Purpose:** Share data or coordinate actions between components that don't have a direct parent-child relationship.
*   **Mechanism:**
    1.  Create a shared service (`@Injectable({ providedIn: 'root' })`).
    2.  Use RxJS Subjects (`Subject` or `BehaviorSubject`) within the service to act as event buses or state holders.
    3.  Components inject the service.
    4.  One component calls a service method to emit a value/event using the Subject's `.next()` method.
    5.  Other components subscribe to the Subject's Observable (`subject.asObservable()`) in the service to receive the value/event.

```typescript
// src/app/shared/communication.service.ts
import { Injectable } from '@angular/core';
import { Subject, BehaviorSubject } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class CommunicationService {
  // Use Subject for events without initial state
  private messageSource = new Subject<string>();
  message$ = this.messageSource.asObservable(); // Expose as Observable

  // Use BehaviorSubject for state that needs an initial value and emits last value to new subscribers
  private countSource = new BehaviorSubject<number>(0);
  count$ = this.countSource.asObservable();

  sendMessage(message: string) {
    this.messageSource.next(message);
  }

  updateCount(newCount: number) {
    this.countSource.next(newCount);
  }

  getCurrentCount(): number {
    return this.countSource.value;
  }
}

// src/app/component-a/component-a.component.ts
import { Component, inject } from '@angular/core';
import { CommunicationService } from '../shared/communication.service';

@Component({ /* ... */ })
export class ComponentA {
  private commService = inject(CommunicationService);

  send() {
    this.commService.sendMessage('Hello from Component A');
    this.commService.updateCount(this.commService.getCurrentCount() + 1);
  }
}

// src/app/component-b/component-b.component.ts
import { Component, inject, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { CommunicationService } from '../shared/communication.service';
import { AsyncPipe } from '@angular/common'; // For async pipe

@Component({
  selector: 'app-component-b',
  standalone: true,
  imports: [AsyncPipe], // Import AsyncPipe
  template: `
    <p>Received Message: {{ message }}</p>
    <p>Current Count (Async Pipe): {{ commService.count$ | async }}</p>
    <p>Current Count (Manual Sub): {{ currentCount }}</p>
  `
})
export class ComponentB implements OnInit, OnDestroy {
  commService = inject(CommunicationService); // Make public for async pipe
  message: string = '';
  currentCount: number = 0;
  private messageSub?: Subscription;
  private countSub?: Subscription;

  ngOnInit() {
    this.messageSub = this.commService.message$.subscribe(msg => this.message = msg);
    this.countSub = this.commService.count$.subscribe(count => this.currentCount = count);
  }

  ngOnDestroy() {
    // Unsubscribe manually to prevent memory leaks if not using async pipe
    this.messageSub?.unsubscribe();
    this.countSub?.unsubscribe();
  }
}
```

Choose the communication pattern that best fits the relationship between the components involved. Prefer `@Input`/`@Output` for direct parent-child interaction and services for unrelated components. Use `@ViewChild` sparingly.