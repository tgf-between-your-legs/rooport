# Integration Testing: Test Doubles (Mocks, Stubs, Fakes)

Using test doubles to isolate components and control dependencies during integration testing.

## Core Concept: Replacing Real Dependencies

When testing the integration between two components (A and B), you often want to isolate that specific interaction without involving other *real* dependencies that component B might have (e.g., component C, an external API, a complex database). Test doubles are objects or functions that replace these real dependencies during a test, providing controlled behavior.

**Why Use Test Doubles in Integration Tests?**

*   **Isolation:** Focus the test on the specific interaction between A and B, removing noise from other dependencies.
*   **Control:** Force specific scenarios or return values from dependencies (e.g., simulate network errors, specific data responses, empty results).
*   **Speed:** Avoid slow operations like real network calls or complex database setups.
*   **Availability:** Test interactions even when real dependencies are unavailable or unstable (e.g., third-party APIs in a test environment).
*   **Cost:** Avoid costs associated with hitting paid third-party APIs during tests.

## Common Types of Test Doubles

While terms are sometimes used interchangeably, here's a common distinction (based on Gerard Meszaros / Martin Fowler):

1.  **Dummy Objects:** Passed around but never actually used. Usually just satisfy parameter lists. (Rarely used directly in integration tests).
2.  **Stubs:** Provide canned answers to calls made during the test. They return pre-defined data or responses, ignoring anything outside the pre-programmed behavior. Often used to provide specific data needed for a test scenario or to prevent calls to real external services.
    *   *Example:* A stub for a weather service API always returns a specific JSON forecast regardless of the requested location.
3.  **Spies:** Stubs that also record some information about how they were called (e.g., number of calls, arguments passed). Useful for verifying that a component *attempted* to call a dependency, even if the dependency's actual logic is replaced.
    *   *Example:* A spy for an email service records that `send_email` was called with the correct recipient and subject, but doesn't actually send an email.
4.  **Mocks:** Objects pre-programmed with *expectations* about the calls they are expected to receive. They verify that these expected calls are made during the test, often failing the test if the expected interaction doesn't occur. Mocks often incorporate stubbing behavior as well.
    *   *Example:* A mock for a payment gateway expects the `charge` method to be called exactly once with a specific amount and card details. The test fails if `charge` isn't called or is called with different arguments.
5.  **Fakes:** Objects that have working implementations, but are simplified or use a different underlying mechanism compared to the real production object. They provide the same interface but might use an in-memory database, simplified logic, or skip complex operations.
    *   *Example:* An in-memory database implementation used instead of a real database connection for faster testing. A fake payment gateway that approves all transactions without hitting a real API.

## Choosing the Right Double

*   Use **Stubs** when you need to provide specific data or prevent calls to real dependencies (e.g., external APIs, database reads needed for setup).
*   Use **Spies** when you need to verify that a call was made without necessarily dictating the response or failing if it wasn't called (less common than mocks).
*   Use **Mocks** when you want to verify specific *interactions* (that a method was called with certain arguments) as part of the test's assertion. Be cautious, as overusing mocks can lead to tests that are tightly coupled to the implementation details.
*   Use **Fakes** when you need a functional replacement for a complex dependency that is simpler or faster for testing purposes (e.g., in-memory database).

## Implementation (Conceptual Examples)

**Python (`unittest.mock`):**

```python
# Assuming service_b depends on service_c
from unittest.mock import patch, MagicMock

@patch('myapp.service_b.service_c') # Patch service_c where it's imported in service_b
def test_service_a_calls_service_b(mock_service_c):
    # Configure the mock (Stub behavior)
    mock_service_c.get_data.return_value = {"status": "mocked_success"}

    # Call the component under test (service_a might call service_b)
    result = service_a.do_something_that_uses_b()

    # Assert on the result based on the mocked dependency
    assert result["b_status"] == "mocked_success"

    # Assert that the mock was called (Mock/Spy behavior)
    mock_service_c.get_data.assert_called_once_with(expected_argument="some_value")
```

**JavaScript (Jest):**

```javascript
// Assuming serviceB depends on serviceC
import * as serviceC from './serviceC';
import { serviceA } from './serviceA';

// Mock the entire serviceC module
jest.mock('./serviceC');

test('serviceA calls serviceB', async () => {
  // Configure the mock implementation (Stub behavior)
  const mockGetData = jest.fn().mockResolvedValue({ status: 'mocked_success' });
  // If serviceC is a class: jest.spyOn(serviceC.prototype, 'getData').mockResolvedValue(...)
  // If serviceC exports functions: (serviceC as jest.Mocked<typeof serviceC>).getData.mockResolvedValue(...)
  jest.spyOn(serviceC, 'getData').mockImplementation(mockGetData); // More robust way

  const result = await serviceA.doSomethingThatUsesB();

  // Assert on the result
  expect(result.b_status).toBe('mocked_success');

  // Assert that the mock was called (Mock/Spy behavior)
  expect(mockGetData).toHaveBeenCalledTimes(1);
  expect(mockGetData).toHaveBeenCalledWith({ expected_argument: 'some_value' });
});
```

## Considerations

*   **Scope:** Mock dependencies at the boundary of the components you are integrating. Don't mock things *within* the component you are testing.
*   **Maintainability:** Mocks, especially those verifying exact call signatures, can make tests brittle if the implementation details change frequently. Prefer stubbing return values or verifying state changes where possible.
*   **Realism vs. Isolation:** Decide how much realism is needed. Mocking too much might hide real integration problems, while mocking too little makes tests slower and less isolated.

Test doubles are essential tools for effective integration testing, allowing you to isolate interactions, control dependencies, and create more reliable and focused tests. Choose the appropriate type of double based on whether you need to provide data (stub), verify calls (mock/spy), or replace complex logic (fake).