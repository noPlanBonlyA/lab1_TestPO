"""
Integration tests for CalculatorWithHistory class.
Tests the integration between Calculator and History components.
"""

import pytest
from main import CalculatorWithHistory


class TestCalculatorWithHistory:
    """Integration test suite for CalculatorWithHistory class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc_with_history = CalculatorWithHistory()
    
    # Test 1: Basic integration functionality
    def test_operation_with_history_recording(self):
        """Test that operations are recorded in history."""
        # Arrange & Act
        result = self.calc_with_history.add(10, 5)
        
        # Assert
        assert result == 15
        history = self.calc_with_history.get_history(1)
        assert len(history) == 1
        assert history[0]['operation'] == 'add'
        assert history[0]['operands'] == [10, 5]
        assert history[0]['result'] == 15
    
    def test_multiple_operations_history(self):
        """Test multiple operations are properly recorded."""
        # Arrange & Act
        self.calc_with_history.add(5, 3)
        self.calc_with_history.multiply(4, 7)
        self.calc_with_history.divide(20, 4)
        
        # Assert
        history = self.calc_with_history.get_history()
        assert len(history) == 3
        
        # Check operations in reverse chronological order
        assert history[0]['operation'] == 'divide'
        assert history[0]['result'] == 5
        assert history[1]['operation'] == 'multiply'
        assert history[1]['result'] == 28
        assert history[2]['operation'] == 'add'
        assert history[2]['result'] == 8
    
    # Test 2: Error handling with history
    def test_error_not_recorded_in_history(self):
        """Test that failed operations are not recorded in history."""
        # Arrange
        initial_count = len(self.calc_with_history.get_history())
        
        # Act & Assert
        with pytest.raises(ZeroDivisionError):
            self.calc_with_history.divide(10, 0)
        
        # Verify history wasn't updated
        final_count = len(self.calc_with_history.get_history())
        assert final_count == initial_count
    
    # Test 3: Statistics integration
    def test_statistics_integration(self):
        """Test that statistics work correctly with integrated operations."""
        # Arrange & Act
        self.calc_with_history.add(10, 5)      # result: 15
        self.calc_with_history.add(20, 25)     # result: 45
        self.calc_with_history.multiply(3, 4)  # result: 12
        self.calc_with_history.subtract(50, 10) # result: 40
        
        # Assert
        stats = self.calc_with_history.get_statistics()
        assert stats['total_operations'] == 4
        assert stats['operation_types']['add'] == 2
        assert stats['operation_types']['multiply'] == 1
        assert stats['operation_types']['subtract'] == 1
        assert stats['average_result'] == (15 + 45 + 12 + 40) / 4  # 28
        assert stats['max_result'] == 45
        assert stats['min_result'] == 12
    
    # Test 4: Clear history integration
    def test_clear_history_integration(self):
        """Test clearing history in integrated environment."""
        # Arrange
        self.calc_with_history.add(5, 3)
        self.calc_with_history.multiply(2, 4)
        assert len(self.calc_with_history.get_history()) == 2
        
        # Act
        self.calc_with_history.clear_history()
        
        # Assert
        assert len(self.calc_with_history.get_history()) == 0
        stats = self.calc_with_history.get_statistics()
        assert stats['total_operations'] == 0
    
    # Test 5: Complex scenario test
    def test_complex_calculation_scenario(self):
        """Test a complex calculation scenario with full integration."""
        # Arrange & Act - Simulate a series of calculations
        # Calculate: ((10 + 5) * 3) / 2 - 8 = 14.5
        step1 = self.calc_with_history.add(10, 5)        # 15
        step2 = self.calc_with_history.multiply(step1, 3) # 45
        step3 = self.calc_with_history.divide(step2, 2)   # 22.5
        final = self.calc_with_history.subtract(step3, 8) # 14.5
        
        # Assert
        assert final == 14.5
        
        history = self.calc_with_history.get_history()
        assert len(history) == 4
        
        # Verify sequence (most recent first)
        operations = [op['operation'] for op in history]
        assert operations == ['subtract', 'divide', 'multiply', 'add']
        
        results = [op['result'] for op in history]
        assert results == [14.5, 22.5, 45, 15]