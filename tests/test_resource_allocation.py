# quantum_firmware_optimization/tests/test_resource_allocation.py

import unittest
from unittest.mock import patch
from quantum_firmware_optimization.src.resource_allocation import allocate_resources

class TestResourceAllocation(unittest.TestCase):

    @patch('quantum_firmware_optimization.src.resource_allocation.assess_quantum_readiness')
    def test_allocate_resources_quantum(self, mock_assess_quantum_readiness):
        """Test allocate_resources function when quantum resources are needed."""
        mock_assess_quantum_readiness.return_value = True
        task_description = "Optimize the portfolio using quantum methods"
        
        result = allocate_resources(task_description)
        mock_assess_quantum_readiness.assert_called_once_with(task_description)
        self.assertEqual(result, "Quantum")

    @patch('quantum_firmware_optimization.src.resource_allocation.assess_quantum_readiness')
    def test_allocate_resources_classical(self, mock_assess_quantum_readiness):
        """Test allocate_resources function when classical resources are needed."""
        mock_assess_quantum_readiness.return_value = False
        task_description = "Sort a list of numbers"
        
        result = allocate_resources(task_description)
        mock_assess_quantum_readiness.assert_called_once_with(task_description)
        self.assertEqual(result, "Classical")

if __name__ == "__main__":
    unittest.main()
