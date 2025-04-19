# Angular: Testing Strategies

Overview of testing approaches in Angular applications (Unit, Integration, E2E).

## Core Concept: Testing Pyramid

Angular encourages a balanced testing strategy, often visualized as a pyramid:

1.  **Unit Tests (Largest Base):** Test individual functions, methods, classes (components, services, pipes) in isolation. Fast, cheap, and numerous. Focus on verifying specific logic units. Dependencies are often mocked.
2.  **Integration Tests (Middle Layer):** Test how multiple units (e.g., a component and its template, a component and a service) work together. Slower than unit tests, fewer in number. Focus on interactions between units. May use shallow rendering or test harnesses.
3.  **End-to-End (E2E) Tests (Smallest Top):** Test complete user flows through the application's UI, interacting with it as a user would (clicking buttons, filling forms). Slowest, most brittle, and fewest in number. Focus on verifying critical user journeys. Use tools like Cypress or Protractor (less common now).

## Angular Testing Utilities

*   **Jasmine/Jest:** Default testing frameworks used by Angular CLI for writing test specs (`describe`, `it`, `expect`). Jest is often preferred for its speed and features.
*   **Karma:** Test runner used by default with Jasmine (less common with Jest). Executes tests in real browsers.
*   **Angular Testing Utilities (`@angular/core/testing`):**
    *   `TestBed`: The primary utility for configuring an Angular testing module environment. Allows providing mock services, importing modules/components, etc.
    *   `ComponentFixture`: A wrapper around a tested component instance and its DOM element. Provides methods to interact with the component and its template (`fixture.componentInstance`, `fixture.nativeElement`, `fixture.debugElement`).
    *   `async`, `fakeAsync`, `tick()`: Utilities for handling asynchronous operations within tests.
    *   `inject`: Utility for injecting services within test functions.
*   **`HttpClientTestingModule` (`@angular/common/http/testing`):** Utilities for mocking `HttpClient` requests (`HttpTestingController`, `expectOne`, `flush`).

## 1. Unit Testing

*   **Goal:** Verify the logic of a single class (service, pipe, component logic) in isolation.
*   **Tools:** Jasmine/Jest, `TestBed` (sometimes, often not needed for simple services/pipes), spies (e.g., `jasmine.createSpyObj`, `jest.fn()`).
*   **Focus:** Test public methods, edge cases, return values, and interactions with *mocked* dependencies.

```typescript
// src/app/my.service.spec.ts
import { MyService } from './my.service';
import { HttpClient } from '@angular/common/http'; // Import dependency type

describe('MyService', () => {
  let service: MyService;
  // Create a mock HttpClient using Jasmine spies
  let httpClientSpy: jasmine.SpyObj<HttpClient>;

  beforeEach(() => {
    // Create spy object before each test
    httpClientSpy = jasmine.createSpyObj('HttpClient', ['get']);

    // Provide the mock spy as the HttpClient dependency
    service = new MyService(httpClientSpy);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should return expected data (HttpClient called once)', (done: DoneFn) => {
    const expectedData = [{ id: 1, name: 'Test Data' }];
    // Make the 'get' spy return a predefined value (as an Observable)
    httpClientSpy.get.and.returnValue(of(expectedData)); // 'of' from RxJS

    service.getData().subscribe({
      next: data => {
        expect(data).toEqual(expectedData);
        done(); // Signal async test completion
      },
      error: done.fail // Fail test if error occurs
    });

    // Verify that the spy was called correctly
    expect(httpClientSpy.get.calls.count()).toBe(1);
    expect(httpClientSpy.get.calls.first().args[0]).toBe('/api/data'); // Check URL
  });

  // Add more tests for other methods, error handling, etc.
});
```

## 2. Integration Testing (Component Testing)

*   **Goal:** Verify a component renders correctly, responds to user interaction, and interacts properly with its template and potentially injected services (which might be real or mocked).
*   **Tools:** Jasmine/Jest, `TestBed`, `ComponentFixture`, `By` (for querying DOM), `DebugElement`.
*   **Focus:** Test template binding, event handling, interaction with child components (shallow testing), interaction with injected services, conditional rendering (`@if`), loops (`@for`).

```typescript
// src/app/my-component/my-component.spec.ts
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { MyComponent } from './my-component.component';
import { DataService } from '../data.service'; // Import service dependency
import { of } from 'rxjs'; // For mocking Observable return values
import { By } from '@angular/platform-browser'; // For querying DOM

describe('MyComponent', () => {
  let component: MyComponent;
  let fixture: ComponentFixture<MyComponent>;
  let dataServiceSpy: jasmine.SpyObj<DataService>;

  beforeEach(async () => {
    // Create spy for the service
    dataServiceSpy = jasmine.createSpyObj('DataService', ['getData']);
    // Stub the spy method to return mock data
    dataServiceSpy.getData.and.returnValue(of([{ id: 1, name: 'Mock Item' }]));

    await TestBed.configureTestingModule({
      imports: [MyComponent], // Import the standalone component
      providers: [
        // Provide the mock service instead of the real one
        { provide: DataService, useValue: dataServiceSpy }
      ]
    }).compileComponents(); // Compile template and css (needed for templateUrl/styleUrls)

    fixture = TestBed.createComponent(MyComponent);
    component = fixture.componentInstance;
    // fixture.detectChanges(); // Initial data binding (often called in tests)
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should display items after ngOnInit', () => {
    fixture.detectChanges(); // Trigger ngOnInit and initial change detection

    // Query the DOM using DebugElement and By.css
    const listItems = fixture.debugElement.queryAll(By.css('li'));
    expect(listItems.length).toBe(1);
    expect(listItems[0].nativeElement.textContent).toContain('Mock Item');

    // Verify service method was called
    expect(dataServiceSpy.getData).toHaveBeenCalledTimes(1);
  });

  it('should call addItem method on button click', () => {
    spyOn(component, 'addItem'); // Spy on the component's own method

    const addButton = fixture.debugElement.query(By.css('button.add-item'));
    addButton.triggerEventHandler('click', null); // Simulate click event

    expect(component.addItem).toHaveBeenCalledTimes(1);
  });
});
```

## 3. End-to-End (E2E) Testing

*   **Goal:** Verify complete user flows work as expected from the user's perspective, interacting with the fully built application running in a browser.
*   **Tools:** Cypress (recommended), Protractor (deprecated).
*   **Focus:** Simulate user actions (clicking, typing, navigating), assert UI state changes, check interactions across multiple pages/components. Tests are written against the running application.

```typescript
// cypress/e2e/spec.cy.ts (Example using Cypress)
describe('My App E2E Test', () => {
  it('should display welcome message', () => {
    cy.visit('/'); // Visit the base URL
    cy.contains('Welcome'); // Assert that 'Welcome' text exists on the page
  });

  it('should navigate to users page and show list', () => {
    cy.visit('/');
    cy.contains('Users').click(); // Find and click the 'Users' link
    cy.url().should('include', '/users'); // Assert URL changed
    cy.get('ul li').should('have.length.greaterThan', 0); // Assert list items exist
  });
});
```

A balanced testing strategy using unit, integration, and E2E tests provides confidence in application correctness and helps prevent regressions. Start with unit tests for core logic and component tests for UI interactions.

*(Refer to the official Angular Testing documentation.)*