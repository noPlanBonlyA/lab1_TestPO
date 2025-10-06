"""
History class for storing and managing calculator operation history.
"""

from datetime import datetime
from typing import List, Dict, Any


class History:
    """Manages history of calculator operations."""
    
    def __init__(self, max_size: int = 100):
        """
        Initialize history with maximum size.
        
        Args:
            max_size: Maximum number of operations to store
        """
        self.max_size = max_size
        self.operations: List[Dict[str, Any]] = []
    
    def add_operation(self, operation: str, operands: List[float], result: float) -> None:
        """
        Add an operation to history.
        
        Args:
            operation: Name of the operation (e.g., 'add', 'multiply')
            operands: List of numbers used in the operation
            result: Result of the operation
        """
        entry = {
            'timestamp': datetime.now(),
            'operation': operation,
            'operands': operands.copy(),
            'result': result
        }
        
        self.operations.append(entry)
        
        # Remove oldest entries if we exceed max_size
        if len(self.operations) > self.max_size:
            self.operations.pop(0)
    
    def get_last_operations(self, count: int = 10) -> List[Dict[str, Any]]:
        """
        Get the last N operations.
        
        Args:
            count: Number of operations to retrieve
            
        Returns:
            List of operation dictionaries, most recent first
        """
        if count <= 0:
            return []
        return self.operations[-count:][::-1]  # Reverse to get most recent first
    
    def get_all_operations(self) -> List[Dict[str, Any]]:
        """
        Get all operations in history.
        
        Returns:
            List of all operation dictionaries, most recent first
        """
        return self.operations[::-1]
    
    def clear_history(self) -> None:
        """Clear all operations from history."""
        self.operations.clear()
    
    def get_operation_count(self) -> int:
        """
        Get the total number of operations in history.
        
        Returns:
            Number of operations in history
        """
        return len(self.operations)
    
    def search_operations(self, operation_type: str) -> List[Dict[str, Any]]:
        """
        Search for operations by type.
        
        Args:
            operation_type: Type of operation to search for
            
        Returns:
            List of matching operations, most recent first
        """
        matching_ops = [op for op in self.operations if op['operation'] == operation_type]
        return matching_ops[::-1]
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about the operations history.
        
        Returns:
            Dictionary with statistics about operations
        """
        if not self.operations:
            return {
                'total_operations': 0,
                'operation_types': {},
                'average_result': None,
                'max_result': None,
                'min_result': None
            }
        
        operation_types = {}
        results = []
        
        for op in self.operations:
            op_type = op['operation']
            operation_types[op_type] = operation_types.get(op_type, 0) + 1
            results.append(op['result'])
        
        return {
            'total_operations': len(self.operations),
            'operation_types': operation_types,
            'average_result': sum(results) / len(results),
            'max_result': max(results),
            'min_result': min(results)
        }