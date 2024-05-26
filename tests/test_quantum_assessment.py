# quantum_firmware_optimization/tests/test_quantum_assessment.py

import unittest
from quantum_firmware_optimization.src.quantum_assessment import assess_quantum_readiness

class TestQuantumAssessment(unittest.TestCase):

    def test_assess_quantum_readiness_optimization(self):
        """Test assess_quantum_readiness function with an optimization task."""
        task_description = "Optimize the portfolio using quantum methods"
        result = assess_quantum_readiness(task_description)
        self.assertTrue(result)

    def test_assess_quantum_readiness_simulation(self):
        """Test assess_quantum_readiness function with a simulation task."""
        task_description = "Simulate the molecular structure"
        result = assess_quantum_readiness(task_description)
        self.assertTrue(result)

    def test_assess_quantum_readiness_factorization(self):
        """Test assess_quantum_readiness function with a factorization task."""
        task_description = "Factorize large integers"
        result = assess_quantum_readiness(task_description)
        self.assertTrue(result)

    def test_assess_quantum_readiness_non_quantum_task(self):
        """Test assess_quantum_readiness function with a non-quantum task."""
        task_description = "Sort a list of numbers"
        result = assess_quantum_readiness(task_description)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
