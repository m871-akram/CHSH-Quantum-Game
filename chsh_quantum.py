from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator
from numpy import pi


def circuit_chsh(x, y):
    qc = QuantumCircuit(2, 2)
    qc.h(0)              # état de Bell
    qc.cx(0, 1)
    if x == 0:
        qc.ry(pi / 4, 0)      # Alice: 45°
    if y == 0:
        qc.ry(pi / 8, 1)      # Bob: 22.5°
    elif y == 1:
        qc.ry(3 * pi / 8, 1)  # Bob: 67.5°
    qc.measure([0, 1], [0, 1])
    return qc


sim = BasicSimulator()
shots = 100000
entrees = [(0, 0), (0, 1), (1, 0), (1, 1)]

succes = total = 0
for x, y in entrees:
    counts = sim.run(circuit_chsh(x, y), shots=shots).result().get_counts()
    print(f"x={x}, y={y}: {counts}")
    for bits, n in counts.items():
        a, b = int(bits[1]), int(bits[0])  # bits[0]=Bob, bits[1]=Alice
        gagne = (a != b) if (x, y) == (1, 1) else (a == b)  # règle: a XOR b == x*y
        if gagne:
            succes += n
        total += n

p = succes / total
print(f"Probabilité de succès : {p:.2f}")
print("Avantage quantique !" if p > 0.75 else "Pas d'avantage quantique.")
