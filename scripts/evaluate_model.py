# quantum_firmware_optimization/scripts/evaluate_model.py

import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("evaluate_model.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)

def load_model(model_path):
    """Load the pre-trained model from the specified path."""
    try:
        model = joblib.load(model_path)
        logger.info(f"Model loaded from {model_path}")
        return model
    except Exception as e:
        logger.error(f"Error loading model from {model_path}: {e}")
        raise

def load_test_data(data_path):
    """Load the test data from the specified CSV file."""
    try:
        data = pd.read_csv(data_path)
        logger.info(f"Test data loaded from {data_path}")
        return data
    except Exception as e:
        logger.error(f"Error loading test data from {data_path}: {e}")
        raise

def evaluate_model(model, test_data):
    """Evaluate the model using the test data."""
    try:
        features = test_data[['clock_speed', 'cores', 'logical_cores', 'memory', 'total_storage']]
        labels = test_data['brand']
        predictions = model.predict(features)

        accuracy = accuracy_score(labels, predictions)
        report = classification_report(labels, predictions)
        confusion = confusion_matrix(labels, predictions)

        logger.info(f"Model accuracy: {accuracy}")
        logger.info(f"Classification report:\n{report}")
        logger.info(f"Confusion matrix:\n{confusion}")

        return accuracy, report, confusion
    except Exception as e:
        logger.error(f"Error during model evaluation: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate the pre-trained model using test data.")
    parser.add_argument('--model_path', type=str, required=True, help='Path to the pre-trained model file')
    parser.add_argument('--data_path', type=str, required=True, help='Path to the test data CSV file')
    args = parser.parse_args()

    logger.info("Starting model evaluation...")

    model = load_model(args.model_path)
    test_data = load_test_data(args.data_path)
    evaluate_model(model, test_data)

    logger.info("Model evaluation completed.")
