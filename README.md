# CHSH Quantum Game

A small simulation of the **CHSH game** (Clauser–Horne–Shimony–Holt) built with [Qiskit](https://www.qiskit.org/). The CHSH game is a classic demonstration of quantum entanglement and Bell's theorem: two players who share an entangled pair can win more often than any classical strategy allows.

This project builds the quantum circuit, plays the game for every input pair, and measures the success probability — showing that it beats the classical ceiling of **0.75**.

## The game

Two players, Alice and Bob, are placed in separate rooms and can't communicate. A referee sends each of them a random bit:

- Alice receives `x ∈ {0, 1}`
- Bob receives `y ∈ {0, 1}`

Each replies with a bit (`a` for Alice, `b` for Bob). They **win** the round when:

```
a ⊕ b = x · y
```

In words: their answers must be **equal** unless both inputs are `1`, in which case the answers must **differ**.

| Limit | Best win probability |
|-------|----------------------|
| Best classical strategy | 0.75 |
| Quantum strategy (theoretical max) | ≈ 0.853 |

## How the quantum strategy works

1. **Entanglement** — a Bell state is prepared on two qubits with a Hadamard gate followed by a CNOT.
2. **Measurement settings** — depending on their input, Alice and Bob rotate their qubit (`Ry` gates) before measuring. The angles are chosen so that correlated measurements line up with the winning condition.
3. **Simulation** — the circuit is run for each input pair `(x, y)` with 100,000 shots, and the wins are counted.

```bash
pip install qiskit numpy
```

```bash
python chsh_quantum.py
```

The simulation reaches a success probability of about **0.80**, comfortably above the classical limit of 0.75 — entanglement gives a measurable edge. With optimal measurement angles the quantum strategy can reach ≈ 0.853; the angles used here trade a little of that headroom for simplicity.

## Limitations

- Assumes ideal quantum conditions — no noise or decoherence.
- `BasicSimulator` is fine for this two-qubit circuit but is not a model of real quantum hardware.
- 100,000 shots are used for statistical accuracy; lowering this speeds up the run at the cost of precision.
