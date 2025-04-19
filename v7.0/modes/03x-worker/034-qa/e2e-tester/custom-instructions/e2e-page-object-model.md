# E2E Testing: Page Object Model (POM)

Organizing E2E test code using the Page Object Model pattern for better maintainability.

## Core Concept: Encapsulating UI Pages

The Page Object Model (POM) is a design pattern widely used in test automation to create an object repository for UI elements and interactions. It helps reduce code duplication and improves test maintenance by separating test logic from UI interaction details.

**Key Idea:**

*   For each page or significant component of your web application, create a corresponding "Page Object" class or module.
*   This Page Object contains:
    *   **Locators:** Definitions for finding the UI elements on that specific page (e.g., buttons, inputs, links). Uses robust selectors (like `data-testid`).
    *   **Action Methods:** Functions that encapsulate common user interactions on that page (e.g., `login(username, password)`, `searchForItem(term)`, `clickSubmitButton()`). These methods use the defined locators to interact with the elements.
*   **Test Scripts:** The actual test scripts (`it` or `test` blocks) then use these Page Objects to interact with the application. Tests call the action methods on the Page Objects instead of directly using selectors and interaction commands (`cy.get`, `page.locator`, `.click()`, `.type()`).

## Benefits of POM

*   **Maintainability:** If the UI changes (e.g., an element's selector is updated), you only need to update the locator in *one* place (the Page Object) instead of potentially hundreds of test scripts.
*   **Readability:** Test scripts become cleaner and easier to understand because they describe user actions at a higher level (e.g., `loginPage.login(...)`) rather than low-level UI interactions.
*   **Reusability:** Common actions and element locators are defined once in the Page Object and reused across multiple tests.
*   **Reduced Duplication:** Avoids repeating the same selectors and interaction sequences in multiple tests.

## Implementation Example (Conceptual - Playwright/TypeScript)

```typescript
// === Page Object Definition ===
// tests/pom/login.page.ts
import { Page, Locator } from '@playwright/test';

export class LoginPage {
  // Readonly properties for locators
  readonly usernameInput: Locator;
  readonly passwordInput: Locator;
  readonly submitButton: Locator;
  readonly errorMessage: Locator;

  constructor(private readonly page: Page) {
    // Define locators using robust strategies
    this.usernameInput = page.getByTestId('username-input');
    this.passwordInput = page.getByTestId('password-input');
    this.submitButton = page.getByRole('button', { name: /log in/i });
    this.errorMessage = page.locator('.error-message'); // Example fallback
  }

  // Action method to navigate to the page
  async goto() {
    await this.page.goto('/login'); // Assumes baseURL is configured
  }

  // Action method encapsulating the login flow
  async login(username: string, password: string) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }

  // Optional: Getter methods for assertions in tests
  getErrorMessage() {
    return this.errorMessage;
  }
}

// === Test Script Using Page Object ===
// tests/login.spec.ts
import { test, expect } from '@playwright/test';
import { LoginPage } from './pom/login.page'; // Import the Page Object

test.describe('Login Flow with POM', () => {
  let loginPage: LoginPage; // Declare variable for the Page Object instance

  test.beforeEach(async ({ page }) => {
    // Create an instance of the Page Object before each test
    loginPage = new LoginPage(page);
    await loginPage.goto();
  });

  test('should display login form', async () => {
    // Use Page Object locators for assertions
    await expect(loginPage.usernameInput).toBeVisible();
    await expect(loginPage.passwordInput).toBeVisible();
    await expect(loginPage.submitButton).toBeVisible();
  });

  test('should show error on invalid credentials', async () => {
    // Use Page Object action method
    await loginPage.login('wronguser', 'wrongpassword');

    // Use Page Object getter/locator for assertion
    await expect(loginPage.getErrorMessage()).toBeVisible();
    await expect(loginPage.getErrorMessage()).toContainText('Invalid credentials');
  });

  test('should login successfully with valid credentials', async ({ page }) => {
    const username = process.env.TEST_USERNAME!;
    const password = process.env.TEST_PASSWORD!;

    // Use Page Object action method
    await loginPage.login(username, password);

    // Assertions on the next page (could use another Page Object for dashboard)
    await expect(page).toHaveURL(/.*dashboard/);
    await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
  });
});
```

## Key Considerations

*   **Structure:** Organize Page Objects logically (e.g., one file per page or major component, potentially grouped in a `pom` or `pages` directory).
*   **Naming:** Use clear and descriptive names for Page Objects and their methods.
*   **Abstraction Level:** Methods should represent meaningful user actions, not just single clicks or types.
*   **Return Values:** Action methods can return `void`, `this` (for chaining), or instances of other Page Objects (e.g., a `login()` method might return a `DashboardPage` object upon successful login).
*   **Don't Put Assertions in POM:** Page Objects should focus on finding elements and performing actions. Assertions belong in the test scripts (`expect(...)`). Page Objects might occasionally have simple getter methods that return state (like `isErrorMessageVisible()`) which tests can then assert against.

The Page Object Model is a fundamental pattern for writing scalable and maintainable E2E test suites. By separating test logic from page interaction details, it makes tests more robust against UI changes and easier to read.