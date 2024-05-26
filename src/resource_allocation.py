def allocate_resources(task_description):
    if assess_quantum_readiness(task_description):
        return "Quantum"
    else:
        return "Classical"