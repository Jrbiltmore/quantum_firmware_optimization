import joblib
from resource_monitoring import get_cpu_usage, get_gpu_usage, get_qiskit_backends, get_cirq_backends, get_pennylane_devices
from feature_extraction import extract_features

# Load the trained model
model = joblib.load('../models/combined_model.joblib')

def decide_computation_method(task_features):
    prediction = model.predict([task_features])[0]
    
    cpu_usage = get_cpu_usage()
    gpu_usage = get_gpu_usage()
    qiskit_backends = get_qiskit_backends()
    cirq_backends = get_cirq_backends()
    pennylane_devices = get_pennylane_devices()
    
    if prediction == 'CPU' and cpu_usage < 80:
        return 'CPU'
    elif prediction == 'GPU' and gpu_usage and all(load < 80 for _, load in gpu_usage):
        return 'GPU'
    elif prediction == 'QPU':
        if qiskit_backends or cirq_backends or pennylane_devices:
            return 'QPU'
    return 'Hybrid'

if __name__ == "__main__":
    task = {"Task Type": "optimization"}
    task_features = extract_features(task)
    method = decide_computation_method(task_features)
    print(f"Selected computation method: {method}")
