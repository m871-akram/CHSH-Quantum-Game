from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator
from numpy import pi


def circuit_chsh(x, y):
    qc = QuantumCircuit(2, 2)
    qc.h(0)              # état de Bell
    qc.cx(0, 1)
    if x == 1:
        qc.ry(pi / 2, 0)      # Alice: x=0 -> 0, x=1 -> 90°
    if y == 0:
        qc.ry(pi / 4, 1)      # Bob: y=0 -> 45°
    else:
        qc.ry(-pi / 4, 1)     # Bob: y=1 -> -45°
    qc.measure([0, 1], [0, 1])
    return qc


def main():
    sim = BasicSimulator()
    shots = 100000
    entrees = [(0, 0), (0, 1), (1, 0), (1, 1)]

    succes = 0
    resultats = []
    for x, y in entrees:
        counts = sim.run(circuit_chsh(x, y), shots=shots).result().get_counts()
        print(f"x={x}, y={y}: {counts}")
        gains = 0
        for bits, n in counts.items():
            a, b = int(bits[1]), int(bits[0])  # bits[0]=Bob, bits[1]=Alice
            gagne = (a != b) if (x, y) == (1, 1) else (a == b)  # règle: a XOR b == x*y
            if gagne:
                gains += n
        resultats.append((x, y, gains / shots))
        succes += gains

    print("\n x y | P(gain)")
    for x, y, pg in resultats:
        print(f" {x} {y} | {pg:.4f}")

    p = succes / (len(entrees) * shots)
    print(f"\nProbabilité de succès : {p:.4f}  (théorie cos²(π/8) ≈ 0.8536, classique ≤ 0.75)")
    print("Avantage quantique !" if p > 0.75 else "Pas d'avantage quantique.")


if __name__ == "__main__":
    main()
