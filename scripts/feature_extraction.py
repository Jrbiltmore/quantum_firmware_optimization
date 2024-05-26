def extract_features(task):
    feature_map = {
        "matrix_multiplication": [1000, 50000, 3, 1, 1],
        "image_processing": [5000, 100000, 2, 2, 1],
        "optimization": [50, 1000000, 1, 3, 5],
        # Add more task types as needed
    }
    return feature_map[task["Task Type"]]

if __name__ == "__main__":
    tasks = [
        {"Task Type": "matrix_multiplication"},
        {"Task Type": "image_processing"},
        {"Task Type": "optimization"}
    ]
    
    for task in tasks:
        features = extract_features(task)
        print(f"Features for {task['Task Type']}: {features}")
