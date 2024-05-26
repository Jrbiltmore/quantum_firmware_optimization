# quantum_firmware_optimization/tests/test_hybrid_processing.py

import unittest
from unittest.mock import patch, MagicMock
from quantum_firmware_optimization.src.hybrid_processing import (
    run_quantum_circuit, run_classical_model, hybrid_processing
)

class TestHybridProcessing(unittest.TestCase):

    @patch('quantum_firmware_optimization.src.hybrid_processing.cirq.Simulator')
    def test_run_quantum_circuit(self, mock_simulator):
        """Test the run_quantum_circuit function."""
        mock_simulator_instance = mock_simulator.return_value
        mock_simulator_instance.run.return_value = "Quantum Result"

        circuit = MagicMock()
        parameters = {"param": 1}

        result = run_quantum_circuit(circuit, parameters)
        mock_simulator_instance.run.assert_called_once_with(circuit, param_resolver=MagicMock())
        self.assertEqual(result, "Quantum Result")

    @patch('quantum_firmware_optimization.src.hybrid_processing.tf.keras.Model')
    def test_run_classical_model(self, mock_model):
        """Test the run_classical_model function."""
        mock_model_instance = mock_model.return_value
        mock_model_instance.predict.return_value = "Classical Result"

        model = mock_model_instance
        data = MagicMock()

        result = run_classical_model(model, data)
        mock_model_instance.predict.assert_called_once_with(data)
        self.assertEqual(result, "Classical Result")

    @patch('quantum_firmware_optimization.src.hybrid_processing.assess_quantum_readiness')
    @patch('quantum_firmware_optimization.src.hybrid_processing.run_quantum_circuit')
    @patch('quantum_firmware_optimization.src.hybrid_processing.run_classical_model')
    def test_hybrid_processing_quantum(self, mock_run_classical_model, mock_run_quantum_circuit, mock_assess_quantum_readiness):
        """Test the hybrid_processing function for quantum tasks."""
        mock_assess_quantum_readiness.return_value = True
        mock_run_quantum_circuit.return_value = "Quantum Result"

        task_description = "Optimization task"
        data = MagicMock()
        circuit = MagicMock()
        parameters = {"param": 1}
        model = MagicMock()

        result = hybrid_processing(task_description, data, circuit=circuit, parameters=parameters, model=model)
        mock_assess_quantum_readiness.assert_called_once_with(task_description)
        mock_run_quantum_circuit.assert_called_once_with(circuit, parameters)
        mock_run_classical_model.assert_not_called()
        self.assertEqual(result, "Quantum Result")

    @patch('quantum_firmware_optimization.src.hybrid_processing.assess_quantum_readiness')
    @patch('quantum_firmware_optimization.src.hybrid_processing.run_quantum_circuit')
    @patch('quantum_firmware_optimization.src.hybrid_processing.run_classical_model')
    def test_hybrid_processing_classical(self, mock_run_classical_model, mock_run_quantum_circuit, mock_assess_quantum_readiness):
        """Test the hybrid_processing function for classical tasks."""
        mock_assess_quantum_readiness.return_value = False
        mock_run_classical_model.return_value = "Classical Result"

        task_description = "Simple task"
        data = MagicMock()
        circuit = MagicMock()
        parameters = {"param": 1}
        model = MagicMock()

        result = hybrid_processing(task_description, data, circuit=circuit, parameters=parameters, model=model)
        mock_assess_quantum_readiness.assert_called_once_with(task_description)
        mock_run_classical_model.assert_called_once_with(model, data)
        mock_run_quantum_circuit.assert_not_called()
        self.assertEqual(result, "Classical Result")

if __name__ == "__main__":
    unittest.main()
