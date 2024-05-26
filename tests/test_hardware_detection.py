# quantum_firmware_optimization/tests/test_hardware_detection.py

import unittest
from quantum_firmware_optimization.src.hardware_detection import (
    get_cpu_info, get_memory_info, get_disk_info, get_firmware_version, get_hardware_info
)

class TestHardwareDetection(unittest.TestCase):

    def test_get_cpu_info(self):
        """Test the get_cpu_info function."""
        cpu_info = get_cpu_info()
        self.assertIsInstance(cpu_info, dict)
        self.assertIn("brand", cpu_info)
        self.assertIn("hz_actual", cpu_info)
        self.assertIn("arch", cpu_info)
        self.assertIn("bits", cpu_info)
        self.assertIn("count", cpu_info)
        self.assertIn("logical_count", cpu_info)

    def test_get_memory_info(self):
        """Test the get_memory_info function."""
        memory_info = get_memory_info()
        self.assertIsInstance(memory_info, dict)
        self.assertIn("total", memory_info)
        self.assertIn("available", memory_info)
        self.assertIn("percent", memory_info)
        self.assertIn("used", memory_info)
        self.assertIn("free", memory_info)

    def test_get_disk_info(self):
        """Test the get_disk_info function."""
        disk_info = get_disk_info()
        self.assertIsInstance(disk_info, dict)
        self.assertTrue(len(disk_info) > 0)  # Ensure there is at least one partition
        for partition, info in disk_info.items():
            self.assertIn("total", info)
            self.assertIn("used", info)
            self.assertIn("free", info)
            self.assertIn("percent", info)

    def test_get_firmware_version(self):
        """Test the get_firmware_version function."""
        firmware_version = get_firmware_version()
        self.assertIsInstance(firmware_version, str)
        self.assertTrue(len(firmware_version) > 0)  # Ensure firmware version is not empty

    def test_get_hardware_info(self):
        """Test the get_hardware_info function."""
        hardware_info = get_hardware_info()
        self.assertIsInstance(hardware_info, dict)
        self.assertIn("cpu", hardware_info)
        self.assertIn("memory", hardware_info)
        self.assertIn("disk", hardware_info)
        self.assertIn("firmware", hardware_info)

if __name__ == "__main__":
    unittest.main()
