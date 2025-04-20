# E2E Testing: Cypress Quick Reference

Common commands, assertions, and patterns for writing E2E tests with Cypress.

## Core Concept: All-in-One Testing Framework

Cypress is a popular JavaScript-based E2E testing framework known for its developer experience, interactive test runner, and automatic waiting capabilities. It runs tests directly *within* the browser alongside your application.

**Key Features:**

*   **Interactive Test Runner:** Provides a visual interface to see commands execute, inspect DOM snapshots, debug, and view network requests.
*   **Automatic Waiting:** Cypress automatically waits for elements to exist and become actionable before interacting with them, reducing the need for explicit waits and making tests less flaky.
*   **Time Travel:** Debug tests by stepping back through command snapshots in the Test Runner.
*   **Network Stubbing:** Control and stub network requests (`cy.intercept()`).
*   **Rich Command Set:** Provides commands for querying elements (`cy.get()`), interacting (`.click()`, `.type()`), making assertions (`.should()`), and more.
*   **Extensible:** Supports plugins and custom commands.

## Setup & Running Tests

*   **Installation:** `npm install cypress --save-dev`
*   **Configuration:** `cypress.config.js` (or `.ts`) in the project root. Configure `baseUrl`, viewport size, timeouts, etc.
*   **Test Files:** Typically located in `cypress/e2e/**/*.cy.{js,ts,jsx,tsx}`.
*   **Opening Test Runner:** `npx cypress open`
*   **Running Headless:** `npx cypress run` (often used in CI)
    *   `npx cypress run --browser chrome` (Specify browser)
    *   `npx cypress run --spec "cypress/e2e/login.cy.js"` (Run specific file)

## Common Commands & Patterns

```typescript
// cypress/e2e/login.cy.ts (Example)
describe('Login Flow', () => {
  beforeEach(() => {
    // Visit the login page before each test in this block
    cy.visit('/login'); // Assumes baseUrl is configured
  });

  it('should display login form', () => {
    // Query elements using CSS selectors or data attributes
    cy.get('[data-testid="username-input"]').should('be.visible');
    cy.get('[data-testid="password-input"]').should('be.visible');
    cy.get('button[type="submit"]').should('contain.text', 'Log In');
  });

  it('should show error on invalid credentials', () => {
    // Interact with elements
    cy.get('[data-testid="username-input"]').type('wronguser');
    cy.get('[data-testid="password-input"]').type('wrongpassword{enter}'); // Type and press Enter

    // Assert error message visibility and content
    cy.get('.error-message').should('be.visible').and('contain.text', 'Invalid credentials');

    // Assert URL hasn't changed
    cy.url().should('include', '/login');
  });

  it('should login successfully with valid credentials', () => {
    // Use environment variables for credentials (set via cypress.env.json or OS env vars)
    const username = Cypress.env('TEST_USERNAME');
    const password = Cypress.env('TEST_PASSWORD');

    cy.get('[data-testid="username-input"]').type(username);
    cy.get('[data-testid="password-input"]').type(password);
    cy.get('button[type="submit"]').click();

    // Assert redirection to dashboard (example)
    cy.url().should('include', '/dashboard');
    cy.get('h1').should('contain.text', 'Dashboard');

    // Assert user element is visible
    cy.get('[data-testid="user-greeting"]').should('contain.text', `Welcome, ${username}`);
  });

  it('should intercept API login request (stubbing)', () => {
    // Intercept POST requests to /api/login
    cy.intercept('POST', '/api/login', {
      statusCode: 200,
      body: { userId: '123', token: 'fake-jwt-token' },
    }).as('loginRequest'); // Alias the intercept

    cy.get('[data-testid="username-input"]').type('anyuser');
    cy.get('[data-testid="password-input"]').type('anypassword');
    cy.get('button[type="submit"]').click();

    // Wait for the intercepted request and assert on it
    cy.wait('@loginRequest').its('request.body').should('deep.equal', {
      username: 'anyuser',
      password: 'anypassword',
    });

    // Assert based on the stubbed response
    cy.url().should('include', '/dashboard'); // Assuming redirect happens on success
  });

  // Example using Page Object Model (POM)
  // loginPage.visit();
  // loginPage.getUsernameInput().type(username);
  // loginPage.getPasswordInput().type(password);
  // loginPage.getSubmitButton().click();
  // dashboardPage.getTitle().should('contain.text', 'Dashboard');

});
```

**Key Commands:**

*   `cy.visit(url)`: Navigate to a page.
*   `cy.get(selector)`: Select one or more DOM elements.
*   `.click()`: Click an element.
*   `.type(text)`: Type into an input/textarea. Can include special keys like `{enter}`.
*   `.clear()`: Clear input value.
*   `.select(value)`: Select an option in a `<select>`.
*   `.check()` / `.uncheck()`: Check/uncheck checkboxes/radio buttons.
*   `.should(assertion, value?)`: Make assertions about the selected element(s).
*   `.and()`: Chain assertions.
*   `cy.contains(text)` / `.contains(selector, text)`: Find element containing specific text.
*   `cy.url()`: Get the current URL.
*   `cy.intercept(method, url, response?)`: Stub or spy on network requests.
*   `cy.wait(aliasOrTime)`: Wait for an aliased route/intercept or a fixed time (avoid fixed time).
*   `cy.wrap(object)`: Wrap a non-Cypress object to use Cypress commands/assertions.
*   `cy.log(message)`: Print messages to the Cypress command log.
*   `.its(propertyName)`: Access a property of the current subject.
*   `.then(callback)`: Execute custom code with access to the current subject.

**Common Assertions (`.should()`):**

*   `'be.visible'`, `'not.be.visible'`
*   `'exist'`, `'not.exist'`
*   `'have.length'`, `'have.length.gt'`
*   `'have.class'`, `'not.have.class'`
*   `'have.value'`, `'not.have.value'`
*   `'contain.text'`, `'not.contain.text'` (Cypress-specific, use `contain` for partial text)
*   `'be.disabled'`, `'be.enabled'`
*   `'equal'`, `'deep.equal'` (for values/objects)
*   `'match', regex`

Cypress provides a rich set of commands and automatic waiting, making E2E test writing more efficient. Focus on robust selectors, clear assertions, and organizing tests logically using `describe` and `it` blocks. Leverage the interactive Test Runner for debugging.

*(Refer to the official Cypress documentation for detailed API references.)*