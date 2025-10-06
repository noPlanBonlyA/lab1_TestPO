"""
Calculator class with basic mathematical operations and error handling.
Supports operations: addition, subtraction, multiplication, division, and power.
"""

import math
from typing import Union

Number = Union[int, float]


class Calculator:
    """A calculator class with basic mathematical operations."""
    
    def __init__(self):
        """Initialize calculator."""
        self.last_result = 0
    
    def add(self, a: Number, b: Number) -> Number:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        result = a + b
        self.last_result = result
        return result
    
    def subtract(self, a: Number, b: Number) -> Number:
        """
        Subtract second number from first.
        
        Args:
            a: First number (minuend)
            b: Second number (subtrahend)
            
        Returns:
            Difference of a and b
        """
        result = a - b
        self.last_result = result
        return result
    
    def multiply(self, a: Number, b: Number) -> Number:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        result = a * b
        self.last_result = result
        return result
    
    def divide(self, a: Number, b: Number) -> Number:
        """
        Divide first number by second.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Quotient of a and b
            
        Raises:
            ZeroDivisionError: If divisor is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        self.last_result = result
        return result
    
    def power(self, base: Number, exponent: Number) -> Number:
        """
        Raise base to the power of exponent.
        
        Args:
            base: Base number
            exponent: Exponent
            
        Returns:
            base raised to the power of exponent
            
        Raises:
            ValueError: If operation results in complex number or overflow
        """
        try:
            if base < 0 and not isinstance(exponent, int):
                raise ValueError("Cannot raise negative number to non-integer power")
            result = base ** exponent
            if math.isnan(result) or math.isinf(result):
                raise ValueError("Operation resulted in invalid number")
            self.last_result = result
            return result
        except OverflowError:
            raise ValueError("Operation resulted in overflow")
    
    def square_root(self, number: Number) -> Number:
        """
        Calculate square root of a number.
        
        Args:
            number: Number to calculate square root of
            
        Returns:
            Square root of the number
            
        Raises:
            ValueError: If number is negative
        """
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(number)
        self.last_result = result
        return result
    
    def get_last_result(self) -> Number:
        """
        Get the result of the last operation.
        
        Returns:
            Last operation result
        """
        return self.last_result
    
    def clear(self) -> None:
        """Reset the last result to zero."""
        self.last_result = 0