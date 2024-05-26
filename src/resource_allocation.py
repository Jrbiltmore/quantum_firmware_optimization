# quantum_firmware_optimization/src/resource_allocation.py

import logging
from quantum_assessment import assess_quantum_readiness

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("resource_allocation.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)

def allocate_resources(task_description):
    """
    Allocate resources based on the task description.

    Args:
        task_description (str): The description of the task.

    Returns:
        str: 'Quantum' if the task requires quantum resources, 'Classical' otherwise.
    """
    try:
        if assess_quantum_readiness(task_description):
            logger.info(f"Allocating quantum resources for task: {task_description}")
            return "Quantum"
        else:
            logger.info(f"Allocating classical resources for task: {task_description}")
            return "Classical"
    except Exception as e:
        logger.error(f"Error allocating resources for task '{task_description}': {e}")
        raise

if __name__ == "__main__":
    # Example usage
    task_description = "Optimize the portfolio using quantum methods"
    allocated_resource = allocate_resources(task_description)
    logger.info(f"Allocated resource: {allocated_resource}")
    print(f"Allocated resource: {allocated_resource}")
