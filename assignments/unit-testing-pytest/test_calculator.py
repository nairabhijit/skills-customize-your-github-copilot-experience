"""
Unit Tests for Calculator Module

Use this file as a starting point for your pytest tests.
Complete each task by implementing the required tests.
"""

import pytest
from calculator import Calculator, get_weather_data

# TODO: Task 1 - Write basic unit tests for Calculator class methods

class TestCalculator:
    """Test cases for the Calculator class."""

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        calc = Calculator()
        assert calc.add(2, 3) == 5

    # TODO: Add more test methods for add, subtract, multiply, divide
    # Include edge cases like negative numbers, zero, and division by zero

# TODO: Task 2 - Implement test fixtures and parametrization

# @pytest.fixture
# def calculator():
#     return Calculator()

# @pytest.mark.parametrize("a,b,expected", [
#     (2, 3, 5),
#     (-1, 1, 0),
#     (0, 0, 0),
# ])
# def test_add_parametrized(calculator, a, b, expected):
#     assert calculator.add(a, b) == expected

# TODO: Task 3 - Mock external dependencies

# def test_get_weather_data_success(mocker):
#     # Mock the external API call
#     pass

# def test_get_weather_data_failure(mocker):
#     # Test error handling
#     pass

# TODO: Task 4 - Test-Driven Development
# Write tests first, then implement the authentication functions

# def test_authenticate_user_success():
#     pass

# def test_authenticate_user_failure():
#     pass

# def test_register_user():
#     pass

# def test_validate_password():
#     pass