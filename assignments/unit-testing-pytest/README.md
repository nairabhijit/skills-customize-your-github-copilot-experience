# 📘 Assignment: Unit Testing with pytest

## 🎯 Objective

In this assignment, you'll learn how to write comprehensive unit tests using the pytest framework. You'll practice test-driven development, create test fixtures, use mocking to isolate code under test, and ensure your code is reliable and maintainable.

## 📝 Tasks

### 🛠️ Task 1: Write Basic Unit Tests

#### Description
Create unit tests for a simple calculator module using pytest. Focus on testing individual functions with various inputs and edge cases.

#### Requirements
Your tests should:

- Test addition, subtraction, multiplication, and division functions
- Include tests for normal inputs and edge cases (e.g., division by zero)
- Use descriptive test function names (e.g., `test_add_positive_numbers`)
- Assert expected results using `assert` statements
- Run tests with `pytest` and ensure all pass

### 🛠️ Task 2: Implement Test Fixtures and Parametrization

#### Description
Enhance your test suite by using pytest fixtures to set up test data and parametrize tests to run multiple scenarios efficiently.

#### Requirements
Your tests should:

- Create a fixture that provides a calculator instance for multiple tests
- Use `@pytest.mark.parametrize` to test multiple input combinations
- Test error handling with `pytest.raises` for exceptions
- Organize tests in a logical structure with setup and teardown if needed
- Achieve high test coverage for the calculator module

### 🛠️ Task 3: Mock External Dependencies

#### Description
Apply mocking techniques to test functions that depend on external services or complex objects, ensuring tests remain fast and isolated.

#### Requirements
Your tests should:

- Use `unittest.mock` or `pytest-mock` to mock external API calls or database connections
- Test a function that processes data from an external source
- Verify that mocked methods are called with correct arguments
- Test both success and failure scenarios of external dependencies
- Maintain test isolation by avoiding real network or database calls

### 🛠️ Task 4 (Stretch Goal): Test-Driven Development

#### Description
Practice test-driven development by writing tests first, then implementing the code to make tests pass. Create a simple application feature using TDD principles.

#### Requirements
Your implementation should:

- Write failing tests first for a new feature (e.g., a user authentication system)
- Implement minimal code to make tests pass
- Refactor code while keeping tests green
- Include integration tests alongside unit tests
- Demonstrate the red-green-refactor cycle