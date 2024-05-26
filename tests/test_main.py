# quantum_firmware_optimization/tests/test_main.py

import unittest
from unittest.mock import patch, MagicMock
from quantum_firmware_optimization.src.main import main

class TestMain(unittest.TestCase):

    @patch('quantum_firmware_optimization.src.main.get_hardware_info')
    @patch('quantum_firmware_optimization.src.main.allocate_resources')
    @patch('quantum_firmware_optimization.src.main.hybrid_processing')
    def test_main(self, mock_hybrid_processing, mock_allocate_resources, mock_get_hardware_info):
        """Test the main function."""
        # Mock return values
        mock_get_hardware_info.return_value = {"cpu": "Intel", "memory": "16GB"}
        mock_allocate_resources.return_value = "Quantum"
        mock_hybrid_processing.return_value = "Quantum Result"

        # Define test inputs
        task_description = "Optimize the portfolio using quantum methods"
        data = MagicMock()
        circuit = MagicMock()
        parameters = {"param": 1}
        model = MagicMock()

        # Call the main function
        with patch('builtins.print') as mocked_print:
            main(task_description, data, circuit=circuit, parameters=parameters, model=model)
        
            # Assert calls
            mock_get_hardware_info.assert_called_once()
            mock_allocate_resources.assert_called_once_with(task_description)
            mock_hybrid_processing.assert_called_once_with(task_description, data, circuit=circuit, parameters=parameters, model=model)
            mocked_print.assert_called_once_with("Processing result: Quantum Result")

if __name__ == "__main__":
    unittest.main()
