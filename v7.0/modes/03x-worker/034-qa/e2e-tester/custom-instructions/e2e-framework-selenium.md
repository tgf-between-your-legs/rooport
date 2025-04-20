# E2E Testing: Selenium WebDriver Quick Reference

Basic concepts and patterns for writing E2E tests with Selenium WebDriver.

## Core Concept: Browser Automation Standard

Selenium WebDriver is a long-standing standard and library for automating web browsers. It provides bindings for multiple programming languages (Java, Python, C#, JavaScript, Ruby) and supports various browsers through browser-specific "drivers" (like ChromeDriver, GeckoDriver for Firefox).

**Key Characteristics:**

*   **Language Bindings:** Available in many popular programming languages.
*   **Cross-Browser:** Supports major browsers (Chrome, Firefox, Edge, Safari, IE) via specific WebDriver executables.
*   **W3C Standard:** The WebDriver protocol is a W3C standard.
*   **Explicit Waits:** Unlike Cypress/Playwright, Selenium generally requires *explicit waits* for elements or conditions before interacting, making tests potentially more verbose or prone to timing issues if not implemented carefully.
*   **Runs Outside Browser:** Test scripts run as separate processes and communicate with the browser driver via the WebDriver protocol (usually over HTTP).
*   **Large Ecosystem:** Mature ecosystem with many integrations, helper libraries, and grid solutions (Selenium Grid) for parallel execution.

## Setup & Running Tests (Python Example)

*   **Installation:**
    ```bash
    pip install selenium # Selenium library
    # Download WebDriver executable (e.g., chromedriver) and ensure it's in your system PATH
    # Or use a webdriver manager library: pip install webdriver-manager
    ```
*   **Test Runner:** Often used with standard unit testing frameworks like `unittest` or `pytest`.
*   **Test Files:** Standard Python test files (e.g., `test_login.py`).

```python
# test_login.py (Example using unittest and Selenium WebDriver with Python)
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager # Example using webdriver-manager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Initialize WebDriver (using webdriver-manager to handle driver download/path)
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.base_url = "http://localhost:8000" # Example base URL
        self.driver.implicitly_wait(5) # Implicit wait (use cautiously, explicit waits preferred)

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

    def test_login_form_visible(self):
        self.driver.get(self.base_url + "/login")
        username_input = self.driver.find_element(By.ID, "username") # Find by ID
        password_input = self.driver.find_element(By.NAME, "password") # Find by Name
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']") # Find by XPath

        self.assertTrue(username_input.is_displayed())
        self.assertTrue(password_input.is_displayed())
        self.assertIn("Log In", submit_button.text)

    def test_login_invalid_credentials(self):
        self.driver.get(self.base_url + "/login")
        username_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        username_input.send_keys("wronguser")
        password_input.send_keys("wrongpassword")
        submit_button.click()

        # --- Explicit Wait Example ---
        # Wait up to 10 seconds for the error message element to be visible
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message")) # Find by CSS Selector
        )

        self.assertTrue(error_message.is_displayed())
        self.assertIn("Invalid credentials", error_message.text)
        self.assertIn("/login", self.driver.current_url)

    def test_login_successful(self):
        self.driver.get(self.base_url + "/login")
        username_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        # Use environment variables or a secure method for credentials
        username = "testuser" # os.environ.get("TEST_USERNAME")
        password = "password" # os.environ.get("TEST_PASSWORD")

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()

        # Wait for URL to change or for an element on the next page
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/dashboard")
        )
        # Assert on the new page
        heading = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertIn("Dashboard", heading.text)

if __name__ == "__main__":
    unittest.main()

```

**Key Selenium Concepts/API (Python):**

*   `webdriver.Chrome()`, `webdriver.Firefox()`, etc.: Initialize browser driver.
*   `driver.get(url)`: Navigate to URL.
*   `driver.find_element(By.ID/NAME/XPATH/CSS_SELECTOR/LINK_TEXT/TAG_NAME, value)`: Find a single element. Throws exception if not found.
*   `driver.find_elements(...)`: Find multiple elements (returns a list).
*   `element.click()`: Click the element.
*   `element.send_keys(text)`: Type into an input/textarea.
*   `element.clear()`: Clear input value.
*   `element.text`: Get the visible text content.
*   `element.get_attribute(name)`: Get attribute value.
*   `element.is_displayed()`, `element.is_enabled()`, `element.is_selected()`: Check element state.
*   `driver.current_url`: Get current URL.
*   `driver.title`: Get page title.
*   `driver.quit()`: Close the browser and driver process.
*   **Waits:**
    *   `driver.implicitly_wait(seconds)`: Global wait applied before throwing `NoSuchElementException`. Use cautiously as it can hide performance issues and slow down tests.
    *   `WebDriverWait(driver, timeout).until(expected_condition)`: **Explicit Wait (Recommended)**. Waits for a specific condition (from `expected_conditions` module) before proceeding or timing out.
    *   `expected_conditions (EC)`: Provides conditions like `visibility_of_element_located`, `element_to_be_clickable`, `url_contains`, `text_to_be_present_in_element`.

Selenium is a powerful and versatile browser automation tool. Its main challenge compared to newer frameworks is the need for careful implementation of explicit waits to ensure reliability. Use robust selectors (ID, Name, CSS, XPath - though prioritize less brittle ones) and leverage `WebDriverWait` with `expected_conditions`.

*(Refer to the official Selenium documentation for Python or your chosen language.)*