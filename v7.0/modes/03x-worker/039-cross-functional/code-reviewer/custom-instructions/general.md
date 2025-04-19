# General Code Review Checklist

This checklist provides a set of general guidelines applicable to most code reviews, regardless of the specific programming language or framework.

## 1. Readability & Style

- [ ] Is the code easy to understand?
- [ ] Does the code adhere to established project style guides (e.g., naming conventions, formatting)?
- [ ] Are variable, function, and class names clear, descriptive, and unambiguous?
- [ ] Is the code well-formatted and consistently indented?
- [ ] Is the code appropriately commented, explaining *why* rather than *what*?
- [ ] Is complex logic broken down into smaller, manageable functions/methods?
- [ ] Is there unnecessary or commented-out code that should be removed?
- [ ] Does the code avoid "magic numbers" or unexplained constants?

## 2. Functionality & Correctness

- [ ] Does the code correctly implement the intended requirements or fix the reported bug?
- [ ] Does the code handle edge cases and potential error conditions gracefully?
- [ ] Are inputs validated?
- [ ] Does the code produce the expected output for typical inputs?
- [ ] Are there any obvious logical errors?
- [ ] Does the change introduce any regressions in other parts of the system? (Consider if integration tests are needed/passing)

## 3. Design & Maintainability

- [ ] Is the code modular and well-structured?
- [ ] Does the code follow established design principles (e.g., DRY, SOLID)?
- [ ] Is the code unnecessarily complex? Could it be simplified?
- [ ] Is the code easily extensible and maintainable for future changes?
- [ ] Does the code introduce unnecessary dependencies?
- [ ] Are abstractions used effectively?
- [ ] Is configuration handled appropriately (not hardcoded)?

## 4. Testing

- [ ] Are there sufficient unit tests covering the new/modified code?
- [ ] Do existing tests pass?
- [ ] Are the tests clear, concise, and easy to understand?
- [ ] Do tests cover both success paths and failure/edge cases?
- [ ] Could any integration or end-to-end tests be beneficial?

## 5. Documentation

- [ ] Is relevant documentation (e.g., READMEs, API docs, inline comments) updated to reflect the changes?
- [ ] Is the purpose and usage of new functions, classes, or modules clearly documented?
- [ ] Are commit messages clear, concise, and follow project conventions (e.g., Conventional Commits)?

## 6. Security

- [ ] Does the code introduce any potential security vulnerabilities (e.g., SQL injection, XSS, insecure handling of credentials)?
- [ ] Are external inputs properly sanitized and validated?
- [ ] Are sensitive data handled securely?
- [ ] Are dependencies up-to-date and free from known vulnerabilities?

## 7. Performance

- [ ] Is the code reasonably efficient?
- [ ] Are there any obvious performance bottlenecks (e.g., inefficient loops, unnecessary database queries)?
- [ ] Does the code handle resources (e.g., memory, file handles, network connections) correctly (e.g., closing them properly)?
- [ ] Have potential performance impacts on the overall system been considered?

## 8. General

- [ ] Is the scope of the change appropriate? (Should it be broken down?)
- [ ] Does the code belong in the right place within the codebase?
- [ ] Does the change align with the overall project architecture and goals?