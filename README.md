# CHSH Quantum Game Simulation

A quantum simulation of the CHSH (Clauser-Horne-Shimony-Holt) game using Qiskit, a Python-based quantum computing framework. The CHSH game is a well-known demonstration of quantum entanglement and Bell's theorem, showcasing the advantage of quantum strategies over classical ones. The simulation creates a quantum circuit to prepare an entangled Bell state, applies measurement settings for Alice and Bob, and evaluates the probability of winning the game based on predefined conditions.

The code simulates the game for different input pairs (x, y) and calculates the success probability, comparing it to the classical limit of 0.75 to demonstrate the quantum advantage (achieving a success probability up to approximately 0.85) :


- **Quantum Circuit Construction**: Builds a quantum circuit with two qubits to create an entangled Bell state using Hadamard and CNOT gates.
- **Measurement Settings**: Applies specific rotations (Ry gates) to Alice's and Bob's qubits based on input values (x, y).
- **Simulation**: Uses Qiskit's AerSimulator to run the quantum circuit with 100,000 shots for statistical accuracy.

Install the required packages using pip:
```bash
pip install qiskit qiskit-aer numpy
```

## Usage

1. Run the script:
   ```bash
   python chsh_quantum.py
   ```

2. The script will:
   - Simulate the CHSH game for input pairs (x, y) = (0,0), (0,1), (1,0), (1,1).
   - Output the measurement counts for each input pair.
   - Calculate and display the overall success probability.
   - Indicate whether the quantum advantage (probability > 0.75) is achieved.

## Results
The simulation typically yields a success probability of approximately 0.85, surpassing the classical limit of 0.75. This demonstrates the power of quantum entanglement in achieving outcomes unattainable by classical strategies.

## Limitations
- The simulation assumes ideal quantum conditions (no noise or decoherence).
- The number of shots (100,000) is set for high statistical accuracy but can be adjusted for faster execution at the cost of precision.
- The code uses Qiskit's AerSimulator, which is suitable for small-scale simulations but may not reflect real quantum hardware behavior.
