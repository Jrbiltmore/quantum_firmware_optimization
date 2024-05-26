import cirq

def create_quantum_circuit():
    qubit = cirq.GridQubit(0, 0)
    circuit = cirq.Circuit(cirq.H(qubit))
    return circuit