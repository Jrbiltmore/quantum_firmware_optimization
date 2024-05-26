import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
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
        # Identify columns that should be numeric
        potential_numeric_columns = ['Price', 'TDP', 'Boost Clock', 'Base Clock', 'Turbo Clock', 'Watt', 'Capacity', 'Memory', 'Size']
        
        for column in data.columns:
            if column in potential_numeric_columns:
                # Remove non-numeric characters
                data[column] = data[column].replace('[^0-9.]', '', regex=True)
                # Convert to numeric
                data[column] = pd.to_numeric(data[column], errors='coerce')
        
        features = data.drop(columns=['Producer'])
        labels = data['Producer']
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

def train_model(X_train, y_train, algorithm='random_forest'):
    """Train the model with the training data using the specified algorithm."""
    try:
        if algorithm == 'random_forest':
            model = RandomForestClassifier(random_state=42)
            param_grid = {
                'n_estimators': [50, 100],
                'max_depth': [10, 20],
                'min_samples_split': [5, 10]
            }
        elif algorithm == 'gradient_boosting':
            model = GradientBoostingClassifier(random_state=42)
            param_grid = {
                'n_estimators': [50, 100],
                'learning_rate': [0.01, 0.1],
                'max_depth': [3, 4]
            }
        elif algorithm == 'svm':
            model = SVC(kernel='linear', random_state=42)
            param_grid = {
                'C': [0.1, 1, 10]
            }
        elif algorithm == 'knn':
            model = KNeighborsClassifier()
            param_grid = {
                'n_neighbors': [3, 5, 7]
            }
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        
        logger.info("Starting grid search...")
        grid_search = GridSearchCV(model, param_grid, cv=3, scoring='accuracy')
        grid_search.fit(X_train, y_train)
        
        best_model = grid_search.best_estimator_
        logger.info(f"Model training completed using {algorithm} with best parameters: {grid_search.best_params_}")
        return best_model
    except Exception as e:
        logger.error(f"Error training model with {algorithm}: {e}")
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
    parser.add_argument('--algorithm', type=str, default='random_forest', choices=['random_forest', 'gradient_boosting', 'svm', 'knn'], help='Algorithm to use for training the model')
    args = parser.parse_args()

    logger.info("Starting model training...")

    data = load_data(args.data_path)
    features, labels = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(features, labels)
    model = train_model(X_train, y_train, algorithm=args.algorithm)
    evaluate_model(model, X_test, y_test)
    save_model(model, args.model_path)

    logger.info("Model training and evaluation completed.")

