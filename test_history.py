"""
Unit tests for History class using pytest.
Tests follow AAA (Arrange-Act-Assert) pattern and FIRST principles.
"""

import pytest
from datetime import datetime, timedelta
from history import History


class TestHistory:
    """Test suite for History class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method (Arrange)."""
        self.history = History()
    
    # Test 1: Basic history functionality
    def test_add_single_operation(self):
        """Test adding a single operation to history."""
        # Arrange
        operation = "add"
        operands = [5.0, 3.0]
        result = 8.0
        
        # Act
        self.history.add_operation(operation, operands, result)
        
        # Assert
        assert self.history.get_operation_count() == 1
        operations = self.history.get_all_operations()
        assert len(operations) == 1
        assert operations[0]['operation'] == operation
        assert operations[0]['operands'] == operands
        assert operations[0]['result'] == result
        assert isinstance(operations[0]['timestamp'], datetime)
    
    def test_add_multiple_operations(self):
        """Test adding multiple operations to history."""
        # Arrange
        operations_data = [
            ("add", [1.0, 2.0], 3.0),
            ("multiply", [4.0, 5.0], 20.0),
            ("divide", [10.0, 2.0], 5.0)
        ]
        
        # Act
        for op, operands, result in operations_data:
            self.history.add_operation(op, operands, result)
        
        # Assert
        assert self.history.get_operation_count() == 3
        all_ops = self.history.get_all_operations()
        assert len(all_ops) == 3
        # Most recent should be first
        assert all_ops[0]['operation'] == "divide"
        assert all_ops[1]['operation'] == "multiply"
        assert all_ops[2]['operation'] == "add"
    
    # Test 2: History size limits
    def test_max_size_limit(self):
        """Test that history respects maximum size limit."""
        # Arrange
        small_history = History(max_size=3)
        
        # Act - add more operations than max_size
        for i in range(5):
            small_history.add_operation("add", [i, 1], i + 1)
        
        # Assert
        assert small_history.get_operation_count() == 3
        operations = small_history.get_all_operations()
        # Should contain only the last 3 operations (most recent first)
        assert operations[0]['result'] == 5  # 4 + 1
        assert operations[1]['result'] == 4  # 3 + 1
        assert operations[2]['result'] == 3  # 2 + 1
    
    def test_default_max_size(self):
        """Test that default max size is 100."""
        # Arrange & Act
        default_history = History()
        
        # Add 150 operations
        for i in range(150):
            default_history.add_operation("add", [i, 1], i + 1)
        
        # Assert
        assert default_history.get_operation_count() == 100
    
    # Test 3: Retrieving operations
    def test_get_last_operations(self):
        """Test retrieving last N operations."""
        # Arrange
        for i in range(10):
            self.history.add_operation("add", [i, 1], i + 1)
        
        # Act
        last_3 = self.history.get_last_operations(3)
        last_5 = self.history.get_last_operations(5)
        
        # Assert
        assert len(last_3) == 3
        assert len(last_5) == 5
        # Most recent first
        assert last_3[0]['result'] == 10  # 9 + 1
        assert last_3[1]['result'] == 9   # 8 + 1
        assert last_3[2]['result'] == 8   # 7 + 1
    
    def test_get_last_operations_boundary_cases(self):
        """Test boundary cases for get_last_operations."""
        # Arrange
        for i in range(3):
            self.history.add_operation("add", [i, 1], i + 1)
        
        # Act & Assert
        # Request more than available
        result = self.history.get_last_operations(10)
        assert len(result) == 3
        
        # Request zero or negative
        assert self.history.get_last_operations(0) == []
        assert self.history.get_last_operations(-1) == []
        
        # Empty history
        empty_history = History()
        assert empty_history.get_last_operations(5) == []
    
    # Test 4: Search functionality
    def test_search_operations_by_type(self):
        """Test searching operations by type."""
        # Arrange
        operations_data = [
            ("add", [1, 2], 3),
            ("multiply", [2, 3], 6),
            ("add", [4, 5], 9),
            ("divide", [10, 2], 5),
            ("add", [7, 8], 15)
        ]
        
        for op, operands, result in operations_data:
            self.history.add_operation(op, operands, result)
        
        # Act
        add_operations = self.history.search_operations("add")
        multiply_operations = self.history.search_operations("multiply")
        subtract_operations = self.history.search_operations("subtract")
        
        # Assert
        assert len(add_operations) == 3
        assert len(multiply_operations) == 1
        assert len(subtract_operations) == 0
        
        # Check that results are in reverse chronological order (most recent first)
        add_results = [op['result'] for op in add_operations]
        assert add_results == [15, 9, 3]
    
    # Test 5: Clear functionality
    def test_clear_history(self):
        """Test clearing history."""
        # Arrange
        for i in range(5):
            self.history.add_operation("add", [i, 1], i + 1)
        assert self.history.get_operation_count() == 5
        
        # Act
        self.history.clear_history()
        
        # Assert
        assert self.history.get_operation_count() == 0
        assert self.history.get_all_operations() == []
        assert self.history.get_last_operations(10) == []
    
    # Test 6: Statistics functionality
    def test_statistics_empty_history(self):
        """Test statistics with empty history."""
        # Arrange & Act
        stats = self.history.get_statistics()
        
        # Assert
        expected_stats = {
            'total_operations': 0,
            'operation_types': {},
            'average_result': None,
            'max_result': None,
            'min_result': None
        }
        assert stats == expected_stats
    
    def test_statistics_with_operations(self):
        """Test statistics with multiple operations."""
        # Arrange
        operations_data = [
            ("add", [1, 2], 3),
            ("add", [4, 5], 9),
            ("multiply", [2, 3], 6),
            ("divide", [20, 4], 5),
            ("subtract", [10, 7], 3)
        ]
        
        for op, operands, result in operations_data:
            self.history.add_operation(op, operands, result)
        
        # Act
        stats = self.history.get_statistics()
        
        # Assert
        assert stats['total_operations'] == 5
        assert stats['operation_types'] == {
            'add': 2,
            'multiply': 1,
            'divide': 1,
            'subtract': 1
        }
        assert stats['average_result'] == (3 + 9 + 6 + 5 + 3) / 5  # 5.2
        assert stats['max_result'] == 9
        assert stats['min_result'] == 3
    
    # Test 7: Data integrity and isolation
    def test_operands_list_isolation(self):
        """Test that operands list is properly copied and isolated."""
        # Arrange
        original_operands = [1.0, 2.0]
        
        # Act
        self.history.add_operation("add", original_operands, 3.0)
        original_operands[0] = 999.0  # Modify original list
        
        # Assert
        stored_operation = self.history.get_all_operations()[0]
        assert stored_operation['operands'] == [1.0, 2.0]  # Should be unchanged
    
    def test_multiple_history_instances(self):
        """Test that multiple History instances are independent."""
        # Arrange
        history1 = History()
        history2 = History()
        
        # Act
        history1.add_operation("add", [1, 2], 3)
        history2.add_operation("multiply", [4, 5], 20)
        
        # Assert
        assert history1.get_operation_count() == 1
        assert history2.get_operation_count() == 1
        assert history1.get_all_operations()[0]['operation'] == "add"
        assert history2.get_all_operations()[0]['operation'] == "multiply"
    
    # Test 8: Timestamp validation
    def test_timestamp_ordering(self):
        """Test that timestamps are properly ordered."""
        # Arrange & Act
        start_time = datetime.now()
        
        self.history.add_operation("add", [1, 2], 3)
        # Small delay to ensure different timestamps
        import time
        time.sleep(0.001)
        self.history.add_operation("multiply", [3, 4], 12)
        
        end_time = datetime.now()
        
        # Assert
        operations = self.history.get_all_operations()
        first_timestamp = operations[1]['timestamp']  # Earlier operation (reversed order)
        second_timestamp = operations[0]['timestamp']  # Later operation
        
        assert start_time <= first_timestamp <= end_time
        assert start_time <= second_timestamp <= end_time
        assert first_timestamp <= second_timestamp
    
    # Test 9: Edge cases with custom max_size
    def test_custom_max_size_edge_cases(self):
        """Test edge cases with custom max_size values."""
        # Test with max_size = 1
        tiny_history = History(max_size=1)
        tiny_history.add_operation("add", [1, 2], 3)
        tiny_history.add_operation("multiply", [4, 5], 20)
        
        assert tiny_history.get_operation_count() == 1
        assert tiny_history.get_all_operations()[0]['operation'] == "multiply"
        
        # Test with max_size = 0
        zero_history = History(max_size=0)
        zero_history.add_operation("add", [1, 2], 3)
        
        assert zero_history.get_operation_count() == 0
    
    # Test 10: Complex scenarios
    def test_mixed_operations_scenario(self):
        """Test a complex scenario with mixed operations."""
        # Arrange
        operations = [
            ("add", [10, 5], 15),
            ("subtract", [15, 3], 12),
            ("multiply", [12, 2], 24),
            ("divide", [24, 4], 6),
            ("power", [6, 2], 36),
            ("square_root", [36], 6)
        ]
        
        # Act
        for op, operands, result in operations:
            self.history.add_operation(op, operands, result)
        
        # Assert
        assert self.history.get_operation_count() == 6
        
        # Test search for power operations
        power_ops = self.history.search_operations("power")
        assert len(power_ops) == 1
        assert power_ops[0]['operands'] == [6, 2]
        
        # Test statistics
        stats = self.history.get_statistics()
        assert stats['total_operations'] == 6
        assert "power" in stats['operation_types']
        assert "square_root" in stats['operation_types']
        
        # Test getting recent operations
        recent = self.history.get_last_operations(3)
        assert len(recent) == 3
        expected_operations = ["square_root", "power", "divide"]
        actual_operations = [op['operation'] for op in recent]
        assert actual_operations == expected_operations