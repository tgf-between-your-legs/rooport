# E2E Testing: Playwright Quick Reference

Common commands, assertions, and patterns for writing E2E tests with Playwright.

## Core Concept: Cross-Browser Automation

Playwright is a modern E2E testing framework developed by Microsoft, designed for reliable testing across multiple browsers (Chromium, Firefox, WebKit) with a single API. It runs tests outside the browser (using Node.js) and communicates via the WebDriver BiDi protocol or Chrome DevTools Protocol.

**Key Features:**

*   **Cross-Browser:** Supports Chromium (Chrome, Edge), Firefox, and WebKit (Safari).
*   **Auto-Waiting:** Automatically waits for elements to be actionable before performing actions, reducing flakiness.
*   **Rich Locators:** Powerful and resilient element selectors (`page.getByRole`, `page.getByText`, `page.getByTestId`, etc.).
*   **Network Interception:** Intercept, modify, or mock network requests (`page.route()`).
*   **Multiple Contexts/Pages:** Supports testing scenarios involving multiple browser tabs, origins, or user contexts within a single test.
*   **Tracing & Debugging:** Excellent debugging tools, including Playwright Inspector and Trace Viewer (generates detailed trace files with DOM snapshots, actions, network logs).
*   **Parallel Execution:** Built-in support for running tests in parallel for faster execution.
*   **TypeScript Support:** First-class TypeScript support.

## Setup & Running Tests

*   **Installation:** `npm init playwright@latest` (Interactive setup) or `npm install --save-dev @playwright/test`
*   **Configuration:** `playwright.config.js` (or `.ts`) in the project root. Configure `baseURL`, browsers (`projects`), viewport, timeouts, trace options, etc.
*   **Test Files:** Typically located in `tests/**/*.spec.{js,ts}`. Uses `@playwright/test` runner syntax (`test`, `expect`).
*   **Running Tests:** `npx playwright test`
    *   `npx playwright test --project=chromium` (Run only for Chromium project defined in config)
    *   `npx playwright test login.spec.ts` (Run specific file)
    *   `npx playwright test -g "Login success"` (Run tests matching title)
    *   `npx playwright test --ui` (Open UI Mode for interactive debugging)
    *   `npx playwright test --headed` (Run with browser window visible)
    *   `npx playwright show-report` (View HTML report after run)
    *   `npx playwright show-trace trace.zip` (View detailed trace file)

## Common Commands & Patterns

```typescript
// tests/login.spec.ts (Example using @playwright/test)
import { test, expect, Page } from '@playwright/test';

// Optional: Define Page Object Model
class LoginPage {
  constructor(private page: Page) {}

  usernameInput = this.page.getByTestId('username-input');
  passwordInput = this.page.getByTestId('password-input');
  submitButton = this.page.getByRole('button', { name: /log in/i });
  errorMessage = this.page.locator('.error-message'); // Example using CSS locator

  async goto() {
    await this.page.goto('/login'); // Assumes baseURL is configured
  }

  async login(username: string, password: string) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }
}

// Test suite
test.describe('Login Flow', () => {
  // Runs before each test in this block
  test.beforeEach(async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
  });

  test('should display login form', async ({ page }) => {
    const loginPage = new LoginPage(page);
    // Assert visibility using built-in locators and expect
    await expect(loginPage.usernameInput).toBeVisible();
    await expect(loginPage.passwordInput).toBeVisible();
    await expect(loginPage.submitButton).toBeVisible();
  });

  test('should show error on invalid credentials', async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.login('wronguser', 'wrongpassword');

    // Assert error message
    await expect(loginPage.errorMessage).toBeVisible();
    await expect(loginPage.errorMessage).toContainText('Invalid credentials');

    // Assert URL
    await expect(page).toHaveURL(/.*login/);
  });

  test('should login successfully with valid credentials', async ({ page }) => {
    const loginPage = new LoginPage(page);
    // Use environment variables (set via .env file or OS)
    const username = process.env.TEST_USERNAME!;
    const password = process.env.TEST_PASSWORD!;

    await loginPage.login(username, password);

    // Assert redirection and content on the next page
    await expect(page).toHaveURL(/.*dashboard/);
    await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
    await expect(page.getByTestId('user-greeting')).toContainText(`Welcome, ${username}`);
  });

  test('should intercept API login request (stubbing)', async ({ page }) => {
    // Intercept POST requests to /api/login
    await page.route('**/api/login', async route => {
      // Optionally check request details: route.request().postData()
      console.log('Intercepted login request:', route.request().postData());
      // Fulfill with a mock response
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ userId: '123', token: 'fake-jwt-token' }),
      });
    });

    const loginPage = new LoginPage(page);
    await loginPage.login('anyuser', 'anypassword');

    // Assert based on the stubbed response outcome
    await expect(page).toHaveURL(/.*dashboard/);
  });
});
```

**Key Playwright Concepts/API:**

*   **`test` function:** Defines a test case. Takes description and an async callback function with fixtures (like `page`).
*   **`test.describe`:** Groups related tests.
*   **`test.beforeEach`/`afterEach`/`beforeAll`/`afterAll`:** Hooks for setup/teardown.
*   **`page` fixture:** The primary object for interacting with a browser page.
*   **Locators:** Objects representing how to find element(s) (`page.getByRole`, `page.getByText`, `page.locator`, etc.). Actions automatically wait for elements matching locators.
*   **Actions:** Methods performed on locators (`.click()`, `.fill(text)`, `.type(text)`, `.check()`, `.uncheck()`, `.selectOption()`, `.press(key)`).
*   **`expect(locator)`:** Used for making assertions on locators.
*   **Web-First Assertions:** Assertions that automatically wait/retry (`.toBeVisible()`, `.toHaveText()`, `.toBeEnabled()`, `.toHaveCount()`, etc.).
*   **`page.goto(url)`:** Navigate to a URL.
*   **`expect(page).toHaveURL(urlOrRegex)`:** Assert the current page URL.
*   **`page.route(urlPattern, handler)`:** Intercept network requests. `handler` can `route.fulfill()` (mock) or `route.continue()` (let it proceed).
*   **`page.waitForLoadState()`, `page.waitForURL()`, `page.waitForSelector()`:** Explicit waits (less common due to auto-waiting, but sometimes needed).

Playwright provides a robust, modern API for reliable cross-browser E2E testing. Leverage its powerful locators and auto-waiting features. Use the `test` runner syntax with `async/await` and `expect` for assertions. Utilize the Trace Viewer for effective debugging.

*(Refer to the official Playwright documentation.)*