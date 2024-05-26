# quantum/quantum_circuit.py

import cirq
import sympy
import logging
import json
import argparse

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

# Configure logging
logging.basicConfig(level=getattr(logging, config['logging']['level']),
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(config['logging']['file']),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger(__name__)

# Create separate loggers for different parts of the application
circuit_logger = logging.getLogger('quantum_circuit.circuit')
simulation_logger = logging.getLogger('quantum_circuit.simulation')

def create_qubit():
    """Create a single qubit."""
    circuit_logger.debug("Creating a single qubit.")
    return cirq.GridQubit(0, 0)

def create_hadamard_gate(qubit):
    """Apply a Hadamard gate to a qubit."""
    circuit_logger.debug(f"Applying Hadamard gate to qubit: {qubit}.")
    return cirq.H(qubit)

def create_quantum_circuit():
    """
    Create a simple quantum circuit.
    This circuit applies a Hadamard gate to a single qubit.
    """
    circuit_logger.info("Creating a simple quantum circuit.")
    qubit = create_qubit()
    circuit = cirq.Circuit()
    circuit.append(create_hadamard_gate(qubit))
    return circuit

def create_parametric_circuit():
    """
    Create a parametric quantum circuit.
    This circuit applies a parametrized rotation around the Y axis followed by a Hadamard gate.
    """
    circuit_logger.info("Creating a parametric quantum circuit.")
    qubit = create_qubit()
    symbol = sympy.Symbol('theta')
    circuit = cirq.Circuit()
    circuit.append(cirq.ry(symbol).on(qubit))
    circuit.append(create_hadamard_gate(qubit))
    return circuit

def measure_qubit(circuit, qubit):
    """
    Add a measurement to the circuit.
    """
    circuit_logger.debug(f"Adding measurement to qubit: {qubit}.")
    circuit.append(cirq.measure(qubit, key='result'))
    return circuit

def simulate_circuit(circuit):
    """
    Simulate the given quantum circuit.
    """
    simulation_logger.info("Simulating the quantum circuit.")
    simulator = cirq.Simulator()
    try:
        result = simulator.run(circuit)
        simulation_logger.info(f"Simulation result: {result}")
        return result
    except Exception as e:
        simulation_logger.error(f"Error during simulation: {e}")
        return None

def create_and_simulate():
    """
    Create and simulate a quantum circuit.
    """
    circuit_logger.info("Creating and simulating a quantum circuit.")
    qubit = create_qubit()
    circuit = create_quantum_circuit()
    circuit = measure_qubit(circuit, qubit)
    return simulate_circuit(circuit)

def create_parametric_and_simulate(theta_value):
    """
    Create and simulate a parametric quantum circuit.
    """
    circuit_logger.info(f"Creating and simulating a parametric quantum circuit with theta={theta_value}.")
    qubit = create_qubit()
    circuit = create_parametric_circuit()
    circuit = measure_qubit(circuit, qubit)
    simulator = cirq.Simulator()
    param_resolver = cirq.ParamResolver({'theta': theta_value})
    try:
        result = simulator.run(circuit, param_resolver=param_resolver)
        simulation_logger.info(f"Parametric simulation result: {result}")
        return result
    except Exception as e:
        simulation_logger.error(f"Error during parametric simulation: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quantum Circuit Simulator")
    parser.add_argument("--theta", type=float, default=config['quantum_circuit']['theta'], help="Parameter value for the parametric circuit")
    args = parser.parse_args()

    logger.info("Starting the Quantum Circuit Simulator")

    logger.info("Creating and simulating a simple quantum circuit...")
    create_and_simulate()

    logger.info("Creating and simulating a parametric quantum circuit...")
    create_parametric_and_simulate(args.theta)

    logger.info("Quantum Circuit Simulator finished.")
