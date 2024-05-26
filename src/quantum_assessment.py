import tensorflow as tf
import tensorflow_quantum as tfq

def assess_quantum_readiness(task_description):
    # Placeholder for actual machine learning model
    # For demonstration, we will use a simple heuristic
    quantum_ready_tasks = ["optimization", "simulation", "factorization"]
    for keyword in quantum_ready_tasks:
        if keyword in task_description.lower():
            return True
    return False