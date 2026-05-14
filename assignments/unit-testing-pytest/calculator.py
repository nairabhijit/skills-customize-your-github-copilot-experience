"""
Calculator Module - Code to Test

This module contains basic calculator functions that you'll write unit tests for.
"""

class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide a by b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# TODO: Add more functions for Tasks 3 and 4
# For Task 3: Add a function that calls an external API
# For Task 4: Add functions for a user authentication system

def get_weather_data(city: str) -> dict:
    """
    Simulate fetching weather data from an external API.
    In a real scenario, this would make an HTTP request.
    """
    # This is a mock implementation - in tests, you'll mock the actual API call
    if city == "New York":
        return {"temperature": 22, "humidity": 65}
    elif city == "London":
        return {"temperature": 15, "humidity": 80}
    else:
        raise ValueError(f"Weather data not available for {city}")

# TODO: Implement user authentication functions for Task 4
# def authenticate_user(username: str, password: str) -> bool:
# def register_user(username: str, password: str) -> bool:
# def validate_password(password: str) -> bool: