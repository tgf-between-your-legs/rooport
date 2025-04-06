TITLE: Importing ReactiveFormsModule in Angular
DESCRIPTION: Imports the ReactiveFormsModule from @angular/forms and adds it to the NgModule imports array to enable reactive forms functionality.

LANGUAGE: TypeScript
CODE:
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  imports: [
    // other imports ...
    ReactiveFormsModule
  ],
})
export class AppModule { }

----------------------------------------

TITLE: Creating and Using Signals in Angular
DESCRIPTION: Demonstrates how to create a signal, read its value, and update it using the set and update methods. This snippet introduces the basic operations on signals.

LANGUAGE: typescript
CODE:
import {signal} from '@angular/core';

// Create a signal with the `signal` function.
const firstName = signal('Morgan');

// Read a signal value by calling it— signals are functions.
console.log(firstName());

// Change the value of this signal by calling its `set` method with a new value.
firstName.set('Jaime');

// You can also use the `update` method to change the value
// based on the previous value.
firstName.update(name => name.toUpperCase());

----------------------------------------

TITLE: Creating Injectable Calculator Service in Angular
DESCRIPTION: Demonstrates how to create a basic injectable service in Angular using the @Injectable decorator. The service provides a simple calculator functionality with an add method.

LANGUAGE: typescript
CODE:
import {Injectable} from '@angular/core';

@Injectable({providedIn: 'root'})
export class Calculator {
  add(x: number, y: number) {
    return x + y;
  }
}

----------------------------------------

TITLE: Implementing HeroService with Mock Data in Angular
DESCRIPTION: Extends the HeroService to include a getHeroes method that returns mock hero data, demonstrating a basic service implementation.

LANGUAGE: typescript
CODE:
import { Injectable } from '@angular/core';
import { HEROES } from './mock-heroes';

@Injectable({
  // declares that this service should be created
  // by the root application injector.
  providedIn: 'root',
})
export class HeroService {
  getHeroes() {
    return HEROES;
  }
}

----------------------------------------

TITLE: Installing Angular CLI
DESCRIPTION: Commands to install Angular CLI globally using different package managers

LANGUAGE: shell
CODE:
npm install -g @angular/cli

LANGUAGE: shell
CODE:
pnpm install -g @angular/cli

LANGUAGE: shell
CODE:
yarn global add @angular/cli

LANGUAGE: shell
CODE:
bun install -g @angular/cli

----------------------------------------

TITLE: Importing and Using Angular Components
DESCRIPTION: Shows how to import and use child components within a parent component, demonstrating component composition.

LANGUAGE: typescript
CODE:
import {ProfilePhoto} from 'profile-photo.ts';

@Component({
  selector: 'user-profile',
  imports: [ProfilePhoto],
  template: `
    <h1>User profile</h1>
    <profile-photo />
    <p>This is the user profile page</p>
  `,
})
export class UserProfile {
  // Component behavior is defined in here
}

----------------------------------------

TITLE: Inject Method Usage in TypeScript
DESCRIPTION: Demonstrates how to use the inject method to request dependencies.

LANGUAGE: typescript
CODE:
@Component({ … })
class HeroListComponent {
  private service = inject(HeroService);
}

----------------------------------------

TITLE: Creating a New Angular Workspace and App
DESCRIPTION: Command to create a new Angular workspace and initial starter app named 'my-app'. This will prompt for additional feature selections.

LANGUAGE: shell
CODE:
ng new my-app

----------------------------------------

TITLE: Binding FormGroup to Template
DESCRIPTION: Shows how to connect the FormGroup and FormControls to the HTML template using formGroup and formControlName directives.

LANGUAGE: html
CODE:
<form [formGroup]="profileForm">
  <label>
    Name
    <input type="text" formControlName="name" />
  </label>
  <label>
    Email
    <input type="email" formControlName="email" />
  </label>
  <button type="submit">Submit</button>
</form>

----------------------------------------

TITLE: Angular Core API Type Definitions
DESCRIPTION: Defines the core Angular APIs including imports from rxjs, signal primitives, and core Angular components. Contains type definitions and interfaces that form the foundation of Angular's DI and component systems.

LANGUAGE: typescript
CODE:
import * as _angular_core from '@angular/core';
import { Observable } from 'rxjs';
import { SIGNAL } from '@angular/core/primitives/signals';
import { SignalNode } from '@angular/core/primitives/signals';
import { Subject } from 'rxjs';
import { Subscription } from 'rxjs';

----------------------------------------

TITLE: Component Import and Usage Example
DESCRIPTION: Shows how to import and use a component within another component using the imports array.

LANGUAGE: angular-ts
CODE:
import {ProfilePhoto} from './profile-photo';

@Component({
  imports: [ProfilePhoto],
  /* ... */
})
export class UserProfile { }

----------------------------------------

TITLE: Creating Basic Angular Component
DESCRIPTION: Demonstrates the basic structure of an Angular component with a simple user profile example using inline template.

LANGUAGE: typescript
CODE:
@Component({
  selector: 'user-profile',
  template: `
    <h1>User profile</h1>
    <p>This is the user profile page</p>
  `,
})
export class UserProfile { /* Your component code goes here */ }

----------------------------------------

TITLE: Creating a FormControl in Angular Component
DESCRIPTION: Demonstrates how to create a FormControl instance in an Angular component class.

LANGUAGE: TypeScript
CODE:
import { FormControl } from '@angular/forms';

export class NameEditorComponent {
  name = new FormControl('');
}

----------------------------------------

TITLE: Implementing OnInit Interface in Angular TypeScript
DESCRIPTION: Shows how to implement the OnInit interface to ensure correct implementation of the ngOnInit lifecycle hook.

LANGUAGE: typescript
CODE:
@Component({
  /* ... */
})
export class UserProfile implements OnInit {
  ngOnInit() {
    /* ... */
  }
}

----------------------------------------

TITLE: Template Variables with ViewChild Queries
DESCRIPTION: Example of using template reference variables with ViewChild decorator for querying elements in the component class.

LANGUAGE: angular-html
CODE:
<input #description value="Original description">

LANGUAGE: angular-ts
CODE:
@Component({
  /* ... */,
  template: `<input #description value="Original description">`,
})
export class AppComponent {
  // Query for the input element based on the template variable name.
  @ViewChild('description') input: ElementRef | undefined;
}

----------------------------------------

TITLE: Required Input Declaration
DESCRIPTION: Shows how to declare a required input using input.required with explicit type specification.

LANGUAGE: typescript
CODE:
@Component({/*...*/})
export class CustomSlider {
  // Declare a required input named value. Returns an `InputSignal<number>`.
  value = input.required<number>();
}

----------------------------------------

TITLE: Basic Angular Component Structure
DESCRIPTION: Demonstrates the fundamental structure of an Angular component with a decorator, selector, and template definition.

LANGUAGE: angular-ts
CODE:
@Component({
  selector: 'profile-photo',
  template: `<img src="profile-photo.jpg" alt="Your profile photo">`,
})
export class ProfilePhoto { }

----------------------------------------

TITLE: Implementing Two-way Binding with Form Controls in Angular
DESCRIPTION: This snippet demonstrates how to use two-way binding with form controls in Angular. It imports FormsModule, uses ngModel directive with two-way binding syntax, and updates the firstName attribute dynamically.

LANGUAGE: angular-ts
CODE:
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  imports: [FormsModule],
  template: `
    <main>
      <h2>Hello {{ firstName }}!</h2>
      <input type="text" [(ngModel)]="firstName" />
    </main>
  `
})
export class AppComponent {
  firstName = 'Ada';
}

----------------------------------------

TITLE: Conditional Rendering with @switch in Angular Templates
DESCRIPTION: Demonstrates how to use the @switch block for conditional rendering based on multiple cases. It includes @case and @default blocks for handling different conditions.

LANGUAGE: angular-html
CODE:
@switch (userPermissions) {
  @case ('admin') {
    <app-admin-dashboard />
  }
  @case ('reviewer') {
    <app-reviewer-dashboard />
  }
  @case ('editor') {
    <app-editor-dashboard />
  }
  @default {
    <app-viewer-dashboard />
  }
}

----------------------------------------

TITLE: Defining Angular DI Core Types and Functions
DESCRIPTION: Defines the core types and functions for Angular's dependency injection system, including InjectionToken interface, Injector interface, and utility functions for managing the current injector and handling not found cases.

LANGUAGE: typescript
CODE:
// @public (undocumented)
export function getCurrentInjector(): Injector | undefined | null;

// @public
export interface InjectionToken<T> {
    // (undocumented)
    ɵprov: ɵɵInjectableDeclaration<T>;
}

// @public (undocumented)
export interface Injector {
    // (undocumented)
    retrieve<T>(token: InjectionToken<T>, options?: unknown): T | NotFound;
}

// @public
export function isNotFound(e: unknown): e is NotFound;

// @public
export const NOT_FOUND: unique symbol;

// @public
export type NotFound = typeof NOT_FOUND | NotFoundError;

// @public
export class NotFoundError extends Error {
    constructor(message: string);
}

// @public (undocumented)
export function setCurrentInjector(injector: Injector | null | undefined): Injector | undefined | null;

----------------------------------------

TITLE: Angular Component with External Files
DESCRIPTION: Demonstrates using separate files for template and styles using templateUrl and styleUrl properties.

LANGUAGE: angular-ts
CODE:
@Component({
  selector: 'profile-photo',
  templateUrl: 'profile-photo.html',
  styleUrl: 'profile-photo.css',
})
export class ProfilePhoto { }

----------------------------------------

TITLE: Reactive Form Validation Configuration
DESCRIPTION: TypeScript code demonstrating how to set up form validation in a reactive form using built-in and custom validators.

LANGUAGE: typescript
CODE:
const actorForm = new FormGroup({
  'name': new FormControl('', [
    Validators.required,
    Validators.minLength(4),
    forbiddenNameValidator(/bob/i)
  ])
});

----------------------------------------

TITLE: Creating Writable Signals in TypeScript
DESCRIPTION: Demonstrates how to create and use writable signals in Angular, including reading values and using set/update operations.

LANGUAGE: typescript
CODE:
const count = signal(0);

// Signals are getter functions - calling them reads their value.
console.log('The count is: ' + count());

LANGUAGE: typescript
CODE:
count.set(3);

LANGUAGE: typescript
CODE:
// Increment the count by 1.
count.update(value => value + 1);

----------------------------------------

TITLE: Binding FormGroup to Template in Angular
DESCRIPTION: Demonstrates how to bind a FormGroup to a form element in the component template and use formControlName for individual controls.

LANGUAGE: HTML
CODE:
<form [formGroup]="profileForm" (ngSubmit)="onSubmit()">
  <label for="first-name">First Name: </label>
  <input id="first-name" type="text" formControlName="firstName">

  <label for="last-name">Last Name: </label>
  <input id="last-name" type="text" formControlName="lastName">
</form>

----------------------------------------

TITLE: Creating Actor Form Component in TypeScript
DESCRIPTION: Implements the ActorFormComponent class with form handling logic including model initialization and form submission.

LANGUAGE: typescript
CODE:
export class ActorFormComponent {
  model = new Actor('Marilyn Monroe', 'Universal', 'Method Acting');
  submitted = false;

  onSubmit() { this.submitted = true; }

  newActor() {
    this.model = new Actor('', '', '');
  }
}

----------------------------------------

TITLE: Reactive Forms Component Implementation
DESCRIPTION: Example showing how to implement a single form control using reactive forms approach. Creates a FormControl instance explicitly in the component class.

LANGUAGE: typescript
CODE:
import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-reactive-favorite-color',
  template: `
    Favorite Color: <input type="text" [formControl]="favoriteColorControl">
  `
})
export class FavoriteColorComponent {
  favoriteColorControl = new FormControl('');
}

----------------------------------------

TITLE: Configuring Application Routes
DESCRIPTION: Defines the application routes configuration with Angular Router.

LANGUAGE: typescript
CODE:
export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes)]
};

----------------------------------------

TITLE: Creating New Angular Project
DESCRIPTION: Command to create a new Angular project using the Angular CLI

LANGUAGE: shell
CODE:
ng new <project-name>

----------------------------------------

TITLE: Implementing Dynamic Form Question Component Template
DESCRIPTION: Defines the template for rendering individual questions in the dynamic form. It uses ngSwitch to determine the question type and applies appropriate form controls and validation.

LANGUAGE: HTML
CODE:
<div [formGroup]="form">
  <label [attr.for]="question.key">{{question.label}}</label>

  <div [ngSwitch]="question.controlType">

    <input *ngSwitchCase="'textbox'" [formControlName]="question.key"
            [id]="question.key" [type]="question.type">

    <select [id]="question.key" *ngSwitchCase="'dropdown'" [formControlName]="question.key">
      <option *ngFor="let opt of question.options" [value]="opt.key">{{opt.value}}</option>
    </select>

  </div>

  <div class="errorMessage" *ngIf="!isValid">{{question.label}} is required</div>
</div>


----------------------------------------

TITLE: Input Transform Configuration
DESCRIPTION: Demonstrates how to use input transforms to modify input values before they're set.

LANGUAGE: typescript
CODE:
@Component({
  selector: 'custom-slider',
  /*...*/
})
export class CustomSlider {
  label = input('', {transform: trimString});
}

function trimString(value: string | undefined): string {
  return value?.trim() ?? '';
}

----------------------------------------

TITLE: Sanitizing HTML Binding in Angular Template
DESCRIPTION: Demonstrates binding a potentially unsafe HTML snippet to the innerHTML property, which Angular automatically sanitizes to prevent XSS attacks.

LANGUAGE: html
CODE:
<h3>Binding innerHTML</h3>
<p>Bound Value:</p>
<p class="e2e-inner-html-interpolated">{{htmlSnippet}}</p>
<p>Result of binding to innerHTML:</p>
<p class="e2e-inner-html-bound" [innerHTML]="htmlSnippet"></p>

----------------------------------------

TITLE: Generating Angular Components
DESCRIPTION: CLI commands for generating new Angular artifacts including components, directives, pipes, services, classes, guards, interfaces, enums, and modules.

LANGUAGE: bash
CODE:
ng generate component component-name

----------------------------------------

TITLE: Adding navigation links with routerLink in Angular
DESCRIPTION: Update the app.component.html file to include navigation links using the routerLink directive.

LANGUAGE: html
CODE:
<nav>
  <a routerLink="/crisis-list">Crisis Center</a>
  <a routerLink="/heroes-list">Heroes</a>
</nav>

----------------------------------------

TITLE: Installing Angular CLI Globally
DESCRIPTION: This command installs the latest version of the Angular CLI globally on the system. The Angular CLI provides tooling for effective Angular development.

LANGUAGE: bash
CODE:
npm install -g @angular/cli

----------------------------------------

TITLE: Mutating Server State with HttpClient POST in Angular
DESCRIPTION: Illustrates how to use HttpClient.post() method to send data to the server and update server state. The example shows sending a new configuration object to an API endpoint.

LANGUAGE: typescript
CODE:
http.post<Config>('/api/config', newConfig).subscribe(config => {
  console.log('Updated config:', config);
});

----------------------------------------

TITLE: Implementing Basic Logging Interceptor in Angular
DESCRIPTION: Simple interceptor function that logs outgoing request URLs before forwarding the request through the interceptor chain.

LANGUAGE: typescript
CODE:
export function loggingInterceptor(req: HttpRequest<unknown>, next: HttpHandlerFn): Observable<HttpEvent<unknown>> {
  console.log(req.url);
  return next(req);
}

----------------------------------------

TITLE: Bootstrapping Application with Config in TypeScript
DESCRIPTION: Demonstrates how to bootstrap an Angular application with configuration.

LANGUAGE: typescript
CODE:
bootstrapApplication(AppComponent, appConfig)

----------------------------------------

TITLE: Advanced linkedSignal with Previous State Handling
DESCRIPTION: Shows how to implement linkedSignal with separate source and computation functions to preserve selections when options change.

LANGUAGE: typescript
CODE:
@Component({/* ... */})
export class ShippingMethodPicker {
  shippingOptions: Signal<ShippingMethod[]> = getShippingOptions();

  selectedOption = linkedSignal<ShippingMethod[], ShippingMethod>({
    source: this.shippingOptions,
    computation: (newOptions, previous) => {
      return newOptions.find(opt => opt.id === previous?.value?.id) ?? newOptions[0];
    }
  });

  changeShipping(newOptionIndex: number) {
    this.selectedOption.set(this.shippingOptions()[newOptionIndex]);
  }
}

----------------------------------------

TITLE: Implementing Basic Highlight Functionality
DESCRIPTION: Adds logic to the HighlightDirective to set the background color of the host element to yellow.

LANGUAGE: typescript
CODE:
import { Directive, ElementRef } from '@angular/core';

@Directive({
  selector: '[appHighlight]'
})
export class HighlightDirective {
  constructor(el: ElementRef) {
    el.nativeElement.style.backgroundColor = 'yellow';
  }
}

----------------------------------------

TITLE: Injecting HeroService into HeroListComponent Using Constructor
DESCRIPTION: Shows how to inject a service into a component using the traditional constructor-based dependency injection method in Angular.

LANGUAGE: typescript
CODE:
  constructor(private heroService: HeroService)

----------------------------------------

TITLE: Form Validation CSS Classes
DESCRIPTION: CSS styling for form validation states using Angular's automatically applied CSS classes.

LANGUAGE: css
CODE:
.ng-valid[required], .ng-valid.required {
  border-left: 5px solid #42A948;
}
.ng-invalid:not(form) {
  border-left: 5px solid #a94442;
}

----------------------------------------

TITLE: Fetching JSON Data with HttpClient in Angular
DESCRIPTION: Demonstrates how to use HttpClient.get() method to fetch JSON data from an API endpoint. The example shows how to specify the expected return type using a generic type argument.

LANGUAGE: typescript
CODE:
http.get<Config>('/api/config').subscribe(config => {
  // process the configuration.
});

----------------------------------------

TITLE: Conditional Rendering with @if in Angular Templates
DESCRIPTION: Demonstrates how to use the @if block to conditionally display content based on a truthy expression. It also shows how to use @else if and @else for alternative content.

LANGUAGE: angular-html
CODE:
@if (a > b) {
  <p>{{a}} is greater than {{b}}</p>
}

LANGUAGE: angular-html
CODE:
@if (a > b) {
  {{a}} is greater than {{b}}
} @else if (b > a) {
  {{a}} is less than {{b}}
} @else {
  {{a}} is equal to {{b}}
}

----------------------------------------

TITLE: Using Control Flow with @if in Angular Templates
DESCRIPTION: Demonstrates the use of Angular's @if block for conditional rendering in templates. The example shows conditional rendering of admin settings based on a user's admin status.

LANGUAGE: html
CODE:
<h1>User profile</h1>

@if (isAdmin()) {
  <h2>Admin settings</h2>
  <!-- ... -->
} @else {
  <h2>User settings</h2>
  <!-- ... -->  
}

----------------------------------------

TITLE: Implementing ngOnChanges in Angular TypeScript
DESCRIPTION: Demonstrates how to implement the ngOnChanges lifecycle hook to inspect changes to component inputs. It uses SimpleChanges to access previous and current values of inputs.

LANGUAGE: typescript
CODE:
@Component({
  /* ... */
})
export class UserProfile {
  @Input() name: string = '';

  ngOnChanges(changes: SimpleChanges) {
    for (const inputName in changes) {
      const inputValues = changes[inputName];
      console.log(`Previous ${inputName} == ${inputValues.previousValue}`);
      console.log(`Current ${inputName} == ${inputValues.currentValue}`);
      console.log(`Is first ${inputName} change == ${inputValues.firstChange}`);
    }
  }
}

----------------------------------------

TITLE: Configuring Hydration with bootstrapApplication in Angular
DESCRIPTION: Shows how to enable hydration in a standalone Angular application using provideClientHydration with bootstrapApplication.

LANGUAGE: typescript
CODE:
import {
  bootstrapApplication,
  provideClientHydration,
} from '@angular/platform-browser';
...

bootstrapApplication(AppComponent, {
  providers: [provideClientHydration()]
});

----------------------------------------

TITLE: Custom Validator Implementation
DESCRIPTION: Implementation of a custom validator function that checks for forbidden names using regular expressions.

LANGUAGE: typescript
CODE:
export function forbiddenNameValidator(nameRe: RegExp): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    const forbidden = nameRe.test(control.value);
    return forbidden ? {'forbiddenName': {value: control.value}} : null;
  };
}

----------------------------------------

TITLE: Injecting HttpClient in Angular Service
DESCRIPTION: This snippet illustrates how to inject the HttpClient service as a dependency in an Angular service class.

LANGUAGE: typescript
CODE:
@Injectable({providedIn: 'root'})
export class ConfigService {
  constructor(private http: HttpClient) {
    // This service can now make HTTP requests via `this.http`.
  }
}

----------------------------------------

TITLE: Referencing Conditional Expression Results in Angular @if Blocks
DESCRIPTION: Shows how to save and reuse the result of a conditional expression within an @if block using the 'as' keyword.

LANGUAGE: angular-html
CODE:
@if (user.profile.settings.startDate; as startDate) {
  {{ startDate }}
}

----------------------------------------

TITLE: Providing a Service in Root with @Injectable
DESCRIPTION: Shows how to provide a service at the root level using the @Injectable decorator with providedIn: 'root'.

LANGUAGE: typescript
CODE:
@Injectable({
  providedIn: 'root'  // <--provides this service in the root EnvironmentInjector
})
export class ItemService {
  name = 'telephone';
}

----------------------------------------

TITLE: Adding RouterModule to Angular Component Imports
DESCRIPTION: This code snippet shows how to add the RouterModule to the imports array in the @Component decorator of an Angular component.

LANGUAGE: typescript
CODE:
imports: [RouterModule],

----------------------------------------

TITLE: Implementing HeroService with Logger Dependency in Angular
DESCRIPTION: Demonstrates how to inject and use the Logger service within the HeroService, showcasing service-to-service dependency injection.

LANGUAGE: typescript
CODE:
import { inject, Injectable } from '@angular/core';
import { HEROES } from './mock-heroes';
import { Logger } from '../logger.service';

@Injectable({
  providedIn: 'root',
})
export class HeroService {
  private logger = inject(Logger);

  getHeroes() {
    this.logger.log('Getting heroes.');
    return HEROES;
  }
}

----------------------------------------

TITLE: Setting Current Classes with NgClass in Angular Component
DESCRIPTION: Shows how to define a method in the component to set multiple CSS classes conditionally using NgClass.

LANGUAGE: TypeScript
CODE:
setCurrentClasses() {
  this.currentClasses = {
    'saveable': this.canSave,
    'modified': !this.isUnchanged,
    'special': this.isSpecial
  };
}

----------------------------------------

TITLE: Configuring HttpClient with provideHttpClient in Angular
DESCRIPTION: This snippet demonstrates how to set up HttpClient using the provideHttpClient function in the application configuration.

LANGUAGE: typescript
CODE:
export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(),
  ]
};

----------------------------------------

TITLE: Using Signals in Angular Components
DESCRIPTION: Demonstrates how to use signals and computed signals within an Angular component. This snippet shows practical application of signals in component state management.

LANGUAGE: typescript
CODE:
@Component({/* ... */})
export class UserProfile {
  isTrial = signal(false);
  isTrialExpired = signal(false);
  showTrialDuration = computed(() => this.isTrial() && !this.isTrialExpired());

  activateTrial() {
    this.isTrial.set(true);
  }
}

----------------------------------------

TITLE: Component Composition Example
DESCRIPTION: Demonstrates how components can be composed together in a parent-child relationship.

LANGUAGE: angular-ts
CODE:
@Component({
  selector: 'profile-photo',
})
export class ProfilePhoto { }

@Component({
  imports: [ProfilePhoto],
  template: `<profile-photo />`
})
export class UserProfile { }

----------------------------------------

TITLE: Inline Styles in Angular Component
DESCRIPTION: Demonstrates how to define inline CSS styles directly within the @Component decorator using the styles property. The example shows styling a profile photo with border-radius.

LANGUAGE: angular-ts
CODE:
@Component({
  selector: 'profile-photo',
  template: `<img src="profile-photo.jpg" alt="Your profile photo">`,
  styles: ` img { border-radius: 50%; } `,
})
export class ProfilePhoto { }

----------------------------------------

TITLE: Iterating Collections with @for in Angular Templates
DESCRIPTION: Demonstrates how to use the @for block to loop through a collection and render content repeatedly. It includes the 'track' expression for performance optimization.

LANGUAGE: angular-html
CODE:
@for (item of items; track item.id) {
  {{ item.name }}
}

----------------------------------------

TITLE: HttpClient Class Definition
DESCRIPTION: The main class for making HTTP requests in Angular applications. Provides methods for GET, POST, PUT, DELETE, HEAD, PATCH, JSONP and generic requests with full type support and configuration options.

LANGUAGE: typescript
CODE:
export class HttpClient {
    constructor(handler: HttpHandler);
    get<T>(url: string, options?: {
        headers?: HttpHeaders;
        observe?: 'body';
        params?: HttpParams;
        reportProgress?: boolean;
        responseType?: 'json';
        withCredentials?: boolean;
    }): Observable<T>;
    // Additional methods not shown for brevity
}

----------------------------------------

TITLE: Creating a Reusable UserService with HttpClient in Angular
DESCRIPTION: Demonstrates the creation of a reusable, injectable UserService that encapsulates data access logic using HttpClient. The service provides a method to fetch user data by ID.

LANGUAGE: typescript
CODE:
@Injectable({providedIn: 'root'})
export class UserService {
  constructor(private http: HttpClient) {}

  getUser(id: string): Observable<User> {
    return this.http.get<User>(`/api/user/${id}`);
  }
}

----------------------------------------

TITLE: Custom Kebab Case Pipe Implementation
DESCRIPTION: Shows how to create a custom pipe that transforms strings to kebab case format. Demonstrates pipe decorator usage and transform method implementation.

LANGUAGE: typescript
CODE:
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'kebabCase',
})
export class KebabCasePipe implements PipeTransform {
  transform(value: string): string {
    return value.toLowerCase().replace(/ /g, '-');
  }
}

----------------------------------------

TITLE: Running Angular Tests in Continuous Integration
DESCRIPTION: Demonstrates how to run Angular tests in a Continuous Integration environment. This command runs tests without watch mode, progress reporting, and uses a headless Chrome browser.

LANGUAGE: shell
CODE:
ng test --no-watch --no-progress --browsers=ChromeHeadless

----------------------------------------

TITLE: Creating Effects in Angular Signals
DESCRIPTION: Shows how to create effects that automatically run when dependent signals change, with examples in component context.

LANGUAGE: typescript
CODE:
effect(() => {
  console.log(`The current count is: ${count()}`);
});

----------------------------------------

TITLE: Importing Router Module in Angular
DESCRIPTION: Demonstrates how to import the Router module from @angular/router package.

LANGUAGE: typescript
CODE:
import { provideRouter } from '@angular/router';