# quantum_firmware_optimization/src/__init__.py

import logging

# Configure package-level logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("quantum_firmware_optimization.log"),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger(__name__)
logger.info("Quantum Firmware Optimization package initialized.")
