import psutil
import GPUtil
from qiskit import IBMQ
import cirq
import pennylane as qml

# CPU Monitoring
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# GPU Monitoring
def get_gpu_usage():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return None
    return [(gpu.id, gpu.load) for gpu in gpus]

# Qiskit Quantum Hardware Monitoring
def get_qiskit_backends():
    IBMQ.load_account()  # Load account from disk
    provider = IBMQ.get_provider(hub='ibm-q')
    backends = provider.backends()
    return [(backend.name(), backend.status().pending_jobs) for backend in backends]

# Cirq Quantum Hardware Monitoring
def get_cirq_backends():
    return [device for device in cirq.google.SycamoreProcessor]

# Pennylane Quantum Hardware Monitoring
def get_pennylane_devices():
    return qml.device("default.qubit", wires=1)

if __name__ == "__main__":
    print(f"CPU usage: {get_cpu_usage()}%")
    print(f"GPU usage: {get_gpu_usage()}")
    print(f"Qiskit backends: {get_qiskit_backends()}")
    print(f"Cirq backends: {get_cirq_backends()}")
    print(f"Pennylane devices: {get_pennylane_devices()}")
