"""
Unit tests for Calculator class using pytest.
Tests follow AAA (Arrange-Act-Assert) pattern and FIRST principles.
"""

import pytest
import math
from calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method (Arrange)."""
        self.calculator = Calculator()
    
    # Test 1: Basic arithmetic operations (Happy path)
    def test_basic_addition(self):
        """Test addition with positive numbers."""
        # Arrange
        a, b = 5, 3
        expected = 8
        
        # Act
        result = self.calculator.add(a, b)
        
        # Assert
        assert result == expected
        assert self.calculator.get_last_result() == expected
    
    def test_basic_subtraction(self):
        """Test subtraction with positive numbers."""
        # Arrange
        a, b = 10, 4
        expected = 6
        
        # Act
        result = self.calculator.subtract(a, b)
        
        # Assert
        assert result == expected
        assert self.calculator.get_last_result() == expected
    
    def test_basic_multiplication(self):
        """Test multiplication with positive numbers."""
        # Arrange
        a, b = 6, 7
        expected = 42
        
        # Act
        result = self.calculator.multiply(a, b)
        
        # Assert
        assert result == expected
        assert self.calculator.get_last_result() == expected
    
    def test_basic_division(self):
        """Test division with positive numbers."""
        # Arrange
        a, b = 15, 3
        expected = 5.0
        
        # Act
        result = self.calculator.divide(a, b)
        
        # Assert
        assert result == expected
        assert self.calculator.get_last_result() == expected
    
    def test_basic_power(self):
        """Test power operation with positive numbers."""
        # Arrange
        base, exponent = 2, 3
        expected = 8
        
        # Act
        result = self.calculator.power(base, exponent)
        
        # Assert
        assert result == expected
        assert self.calculator.get_last_result() == expected
    
    # Test 2: Edge cases and boundary conditions
    def test_addition_with_zero(self):
        """Test addition with zero (boundary case)."""
        # Arrange
        a, b = 5, 0
        expected = 5
        
        # Act
        result = self.calculator.add(a, b)
        
        # Assert
        assert result == expected
    
    def test_multiplication_by_zero(self):
        """Test multiplication by zero (boundary case)."""
        # Arrange
        a, b = 42, 0
        expected = 0
        
        # Act
        result = self.calculator.multiply(a, b)
        
        # Assert
        assert result == expected
    
    def test_power_to_zero(self):
        """Test raising number to power of zero (boundary case)."""
        # Arrange
        base, exponent = 5, 0
        expected = 1
        
        # Act
        result = self.calculator.power(base, exponent)
        
        # Assert
        assert result == expected
    
    def test_zero_to_power(self):
        """Test raising zero to a power (boundary case)."""
        # Arrange
        base, exponent = 0, 3
        expected = 0
        
        # Act
        result = self.calculator.power(base, exponent)
        
        # Assert
        assert result == expected
    
    # Test 3: Error handling and exceptional cases
    def test_division_by_zero(self):
        """Test division by zero raises ZeroDivisionError."""
        # Arrange
        a, b = 10, 0
        
        # Act & Assert
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            self.calculator.divide(a, b)
    
    def test_negative_square_root(self):
        """Test square root of negative number raises ValueError."""
        # Arrange
        negative_number = -4
        
        # Act & Assert
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calculator.square_root(negative_number)
    
    def test_negative_base_non_integer_exponent(self):
        """Test negative base with non-integer exponent raises ValueError."""
        # Arrange
        base, exponent = -2, 0.5
        
        # Act & Assert
        with pytest.raises(ValueError, match="Cannot raise negative number to non-integer power"):
            self.calculator.power(base, exponent)
    
    # Test 4: Negative numbers operations
    def test_operations_with_negative_numbers(self):
        """Test operations with negative numbers."""
        # Test addition with negatives
        assert self.calculator.add(-5, -3) == -8
        assert self.calculator.add(-5, 3) == -2
        assert self.calculator.add(5, -3) == 2
        
        # Test subtraction with negatives
        assert self.calculator.subtract(-5, -3) == -2
        assert self.calculator.subtract(-5, 3) == -8
        
        # Test multiplication with negatives
        assert self.calculator.multiply(-5, -3) == 15
        assert self.calculator.multiply(-5, 3) == -15
        
        # Test division with negatives
        assert self.calculator.divide(-15, -3) == 5
        assert self.calculator.divide(-15, 3) == -5
    
    # Test 5: Floating point operations
    def test_floating_point_operations(self):
        """Test operations with floating point numbers."""
        # Arrange
        a, b = 3.14, 2.86
        
        # Act & Assert - test with tolerance for floating point precision
        result = self.calculator.add(a, b)
        assert abs(result - 6.0) < 1e-10
        
        result = self.calculator.divide(22, 7)
        assert abs(result - 3.142857142857143) < 1e-10
        
        result = self.calculator.multiply(0.1, 0.2)
        assert abs(result - 0.02) < 1e-10
    
    # Test 6: Square root operations
    def test_square_root_positive(self):
        """Test square root with positive numbers."""
        # Perfect squares
        assert self.calculator.square_root(16) == 4
        assert self.calculator.square_root(25) == 5
        assert self.calculator.square_root(0) == 0
        
        # Non-perfect squares
        result = self.calculator.square_root(2)
        assert abs(result - 1.4142135623730951) < 1e-10
    
    # Test 7: Large numbers and overflow
    def test_large_number_operations(self):
        """Test operations with large numbers."""
        # Large addition
        large_a, large_b = 1e15, 2e15
        result = self.calculator.add(large_a, large_b)
        assert result == 3e15
        
        # Large multiplication
        result = self.calculator.multiply(1e8, 1e8)
        assert result == 1e16
    
    def test_power_overflow(self):
        """Test power operation that causes overflow."""
        # Arrange
        base, exponent = 10, 1000
        
        # Act & Assert
        with pytest.raises(ValueError, match="Operation resulted in overflow"):
            self.calculator.power(base, exponent)
    
    # Test 8: Last result functionality
    def test_last_result_tracking(self):
        """Test that last result is properly tracked."""
        # Arrange
        initial_result = self.calculator.get_last_result()
        
        # Act
        self.calculator.add(5, 3)
        first_result = self.calculator.get_last_result()
        
        self.calculator.multiply(2, 4)
        second_result = self.calculator.get_last_result()
        
        # Assert
        assert initial_result == 0
        assert first_result == 8
        assert second_result == 8  # Should be updated to the multiply result
    
    def test_clear_functionality(self):
        """Test clear functionality resets last result."""
        # Arrange
        self.calculator.add(10, 5)
        assert self.calculator.get_last_result() == 15
        
        # Act
        self.calculator.clear()
        
        # Assert
        assert self.calculator.get_last_result() == 0
    
    # Test 9: Complex power operations
    def test_complex_power_operations(self):
        """Test various power operation scenarios."""
        # Negative base with integer exponent
        assert self.calculator.power(-2, 3) == -8
        assert self.calculator.power(-2, 2) == 4
        
        # Fractional exponents
        assert self.calculator.power(8, 1/3) == 2
        result = self.calculator.power(4, 0.5)
        assert abs(result - 2.0) < 1e-10
    
    # Test 10: Input type validation
    def test_mixed_integer_float_operations(self):
        """Test operations with mixed integer and float inputs."""
        # Integer + Float
        result = self.calculator.add(5, 3.5)
        assert result == 8.5
        
        # Float + Integer
        result = self.calculator.multiply(2.5, 4)
        assert result == 10.0
        
        # Division resulting in float
        result = self.calculator.divide(7, 2)
        assert result == 3.5