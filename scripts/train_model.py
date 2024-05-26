import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("train_model.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)

def load_data(data_path):
    """Load the dataset from the specified CSV file."""
    try:
        data = pd.read_csv(data_path)
        logger.info(f"Data loaded from {data_path}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from {data_path}: {e}")
        raise

def preprocess_data(data):
    """Preprocess the dataset and split it into features and labels."""
    try:
        data['memory'] = data['memory'].str.replace('GB', '').astype(float)
        
        # Convert 'total_storage' column to numerical values
        data['total_storage'] = data['total_storage'].apply(lambda x: float(x.replace('GB', '')) if 'GB' in x else float(x.replace('TB', '')) * 1024)
        
        features = data[['clock_speed', 'cores', 'logical_cores', 'memory', 'total_storage']]
        labels = data['brand']
        logger.info("Data preprocessing completed")
        return features, labels
    except Exception as e:
        logger.error(f"Error preprocessing data: {e}")
        raise

def split_data(features, labels, test_size=0.2, random_state=42):
    """Split the data into training and testing sets."""
    try:
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=test_size, random_state=random_state)
        logger.info("Data split into training and testing sets")
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logger.error(f"Error splitting data: {e}")
        raise

def train_model(X_train, y_train):
    """Train the RandomForest model with the training data."""
    try:
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        logger.info("Model training completed")
        return model
    except Exception as e:
        logger.error(f"Error training model: {e}")
        raise

def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model using the test data."""
    try:
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions)

        logger.info(f"Model accuracy: {accuracy}")
        logger.info(f"Classification report:\n{report}")

        return accuracy, report
    except Exception as e:
        logger.error(f"Error evaluating model: {e}")
        raise

def save_model(model, model_path):
    """Save the trained model to a file."""
    try:
        joblib.dump(model, model_path)
        logger.info(f"Model saved to {model_path}")
    except Exception as e:
        logger.error(f"Error saving model to {model_path}: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a machine learning model with the given dataset.")
    parser.add_argument('--data_path', type=str, required=True, help='Path to the dataset CSV file')
    parser.add_argument('--model_path', type=str, default='../models/model.h5', help='Path to save the trained model')
    args = parser.parse_args()

    logger.info("Starting model training...")

    data = load_data(args.data_path)
    features, labels = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(features, labels)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model, args.model_path)

    logger.info("Model training and evaluation completed.")
