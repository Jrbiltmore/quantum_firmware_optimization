# quantum_firmware_optimization/utils/helper_functions.py

import logging
import os
import json
import yaml

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("helper_functions.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)

def load_json(file_path):
    """
    Load a JSON file and return the data.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The data from the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logger.info(f"Loaded JSON file: {file_path}")
            return data
    except Exception as e:
        logger.error(f"Error loading JSON file '{file_path}': {e}")
        raise

def save_json(data, file_path):
    """
    Save data to a JSON file.

    Args:
        data (dict): The data to save.
        file_path (str): The path to the JSON file.

    Returns:
        bool: True if the save was successful, False otherwise.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            logger.info(f"Saved data to JSON file: {file_path}")
            return True
    except Exception as e:
        logger.error(f"Error saving data to JSON file '{file_path}': {e}")
        return False

def load_yaml(file_path):
    """
    Load a YAML file and return the data.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The data from the YAML file.
    """
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            logger.info(f"Loaded YAML file: {file_path}")
            return data
    except Exception as e:
        logger.error(f"Error loading YAML file '{file_path}': {e}")
        raise

def save_yaml(data, file_path):
    """
    Save data to a YAML file.

    Args:
        data (dict): The data to save.
        file_path (str): The path to the YAML file.

    Returns:
        bool: True if the save was successful, False otherwise.
    """
    try:
        with open(file_path, 'w') as file:
            yaml.safe_dump(data, file)
            logger.info(f"Saved data to YAML file: {file_path}")
            return True
    except Exception as e:
        logger.error(f"Error saving data to YAML file '{file_path}': {e}")
        return False

def create_directory(dir_path):
    """
    Create a directory if it does not exist.

    Args:
        dir_path (str): The path to the directory.

    Returns:
        bool: True if the directory was created or already exists, False otherwise.
    """
    try:
        os.makedirs(dir_path, exist_ok=True)
        logger.info(f"Directory created or already exists: {dir_path}")
        return True
    except Exception as e:
        logger.error(f"Error creating directory '{dir_path}': {e}")
        return False

if __name__ == "__main__":
    # Example usage
    test_json_path = "test.json"
    test_yaml_path = "test.yaml"
    test_data = {"key": "value"}

    # JSON operations
    save_json(test_data, test_json_path)
    loaded_json_data = load_json(test_json_path)
    logger.info(f"Loaded JSON data: {loaded_json_data}")

    # YAML operations
    save_yaml(test_data, test_yaml_path)
    loaded_yaml_data = load_yaml(test_yaml_path)
    logger.info(f"Loaded YAML data: {loaded_yaml_data}")

    # Directory creation
    test_dir_path = "test_directory"
    create_directory(test_dir_path)
