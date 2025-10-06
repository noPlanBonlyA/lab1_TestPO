"""Unit tests for Calculator class using pytest."""

import pytest
import math
from calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""
    
    def setup_method(self):
        self.calculator = Calculator()
    
    def test_basic_addition(self):
        """Test addition with positive numbers."""
        result = self.calculator.add(5, 3)
        assert result == 8
        assert self.calculator.get_last_result() == 8
    
    def test_basic_subtraction(self):
        """Test subtraction with positive numbers."""
        result = self.calculator.subtract(10, 4)
        assert result == 6
        assert self.calculator.get_last_result() == 6
    
    def test_basic_multiplication(self):
        """Test multiplication with positive numbers."""
        result = self.calculator.multiply(6, 7)
        assert result == 42
        assert self.calculator.get_last_result() == 42
    
    def test_basic_division(self):
        """Test division with positive numbers."""
        result = self.calculator.divide(15, 3)
        assert result == 5.0
        assert self.calculator.get_last_result() == 5.0
    
    def test_basic_power(self):
        """Test power operation with positive numbers."""
        result = self.calculator.power(2, 3)
        assert result == 8
        assert self.calculator.get_last_result() == 8
    
    def test_addition_with_zero(self):
        """Test addition with zero (boundary case)."""
        result = self.calculator.add(5, 0)
        assert result == 5
    
    def test_multiplication_by_zero(self):
        """Test multiplication by zero (boundary case)."""
        result = self.calculator.multiply(42, 0)
        assert result == 0
    
    def test_power_to_zero(self):
        """Test raising number to power of zero (boundary case)."""
        result = self.calculator.power(5, 0)
        assert result == 1
    
    def test_zero_to_power(self):
        """Test raising zero to a power (boundary case)."""
        result = self.calculator.power(0, 3)
        assert result == 0
    
    def test_division_by_zero(self):
        """Test division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            self.calculator.divide(10, 0)
    
    def test_negative_square_root(self):
        """Test square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calculator.square_root(-4)
    
    def test_negative_base_non_integer_exponent(self):
        """Test negative base with non-integer exponent raises ValueError."""
        with pytest.raises(ValueError, match="Cannot raise negative number to non-integer power"):
            self.calculator.power(-2, 0.5)
    
    def test_operations_with_negative_numbers(self):
        """Test operations with negative numbers."""
        assert self.calculator.add(-5, -3) == -8
        assert self.calculator.add(-5, 3) == -2
        assert self.calculator.add(5, -3) == 2
        assert self.calculator.subtract(-5, -3) == -2
        assert self.calculator.subtract(-5, 3) == -8
        assert self.calculator.multiply(-5, -3) == 15
        assert self.calculator.multiply(-5, 3) == -15
        assert self.calculator.divide(-15, -3) == 5
        assert self.calculator.divide(-15, 3) == -5
    
    def test_floating_point_operations(self):
        """Test operations with floating point numbers."""
        result = self.calculator.add(3.14, 2.86)
        assert abs(result - 6.0) < 1e-10
        
        result = self.calculator.divide(22, 7)
        assert abs(result - 3.142857142857143) < 1e-10
        
        result = self.calculator.multiply(0.1, 0.2)
        assert abs(result - 0.02) < 1e-10
    
    def test_square_root_positive(self):
        """Test square root with positive numbers."""
        assert self.calculator.square_root(16) == 4
        assert self.calculator.square_root(25) == 5
        assert self.calculator.square_root(0) == 0
        
        result = self.calculator.square_root(2)
        assert abs(result - 1.4142135623730951) < 1e-10
    
    def test_large_number_operations(self):
        """Test operations with large numbers."""
        result = self.calculator.add(1e15, 2e15)
        assert result == 3e15
        
        result = self.calculator.multiply(1e8, 1e8)
        assert result == 1e16
    
    def test_power_overflow(self):
        """Test power operation that causes overflow."""
        with pytest.raises(ValueError, match="Operation resulted in overflow"):
            self.calculator.power(10, 1000)
    
    def test_last_result_tracking(self):
        """Test that last result is properly tracked."""
        initial_result = self.calculator.get_last_result()
        
        self.calculator.add(5, 3)
        first_result = self.calculator.get_last_result()
        
        self.calculator.multiply(2, 4)
        second_result = self.calculator.get_last_result()
        
        assert initial_result == 0
        assert first_result == 8
        assert second_result == 8
    
    def test_clear_functionality(self):
        """Test clear functionality resets last result."""
        self.calculator.add(10, 5)
        assert self.calculator.get_last_result() == 15
        
        self.calculator.clear()
        assert self.calculator.get_last_result() == 0
    
    def test_complex_power_operations(self):
        """Test various power operation scenarios."""
        assert self.calculator.power(-2, 3) == -8
        assert self.calculator.power(-2, 2) == 4
        assert self.calculator.power(8, 1/3) == 2
        
        result = self.calculator.power(4, 0.5)
        assert abs(result - 2.0) < 1e-10
    
    def test_mixed_integer_float_operations(self):
        """Test operations with mixed integer and float inputs."""
        result = self.calculator.add(5, 3.5)
        assert result == 8.5
        
        result = self.calculator.multiply(2.5, 4)
        assert result == 10.0
        
        result = self.calculator.divide(7, 2)
        assert result == 3.5