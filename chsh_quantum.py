from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
from numpy import pi

# Fonction pour créer le circuit CHSH
def creer_circuit_chsh(x, y):
    # Définir les registres quantiques et classiques
    registre_quantique = QuantumRegister(2, 'q')  # 2 qubits
    registre_classique = ClassicalRegister(2, 'c')  # 2 bits classiques
    circuit = QuantumCircuit(registre_quantique, registre_classique)

    # Préparer l'état de Bell (état intriqué)
    circuit.h(registre_quantique[0])  # Porte Hadamard sur le premier qubit
    circuit.cx(registre_quantique[0], registre_quantique[1])  # Porte CNOT

    # Appliquer les réglages de mesure d'Alice et Bob
    if x == 0:
        circuit.ry(pi / 4, registre_quantique[0])  # Rotation de 45° pour x = 0
    # x = 1 : pas de rotation (base de calcul)

    if y == 0:
        circuit.ry(pi / 8, registre_quantique[1])  # Rotation de 22.5° pour y = 0
    elif y == 1:
        circuit.ry(3 * pi / 8, registre_quantique[1])  # Rotation de 67.5° pour y = 1

    # Mesurer les deux qubits
    circuit.measure(registre_quantique[0], registre_classique[0])  # Mesure qubit 0
    circuit.measure(registre_quantique[1], registre_classique[1])  # Mesure qubit 1

    return circuit

# Paramètres de la simulation
simulateur = AerSimulator()  # Simulateur quantique
nombre_tirs = 100000  # Nombre d'exécutions pour plus de précision

# Définir les entrées et les conditions de victoire
entrees = [(0, 0), (0, 1), (1, 0), (1, 1)]
conditions_victoire = {
    (0, 0): [(0, 0), (1, 1)],  # a doit égaler b
    (0, 1): [(0, 0), (1, 1)],  # a doit égaler b
    (1, 0): [(0, 0), (1, 1)],  # a doit égaler b
    (1, 1): [(0, 1), (1, 0)]   # a doit être différent de b
}

# Exécuter la simulation et calculer la probabilité de succès
compteur_succes = 0
compteur_total = 0

for x, y in entrees:
    # Créer le circuit pour les valeurs x et y
    circuit = creer_circuit_chsh(x, y)
    
    # Exécuter le circuit avec le simulateur
    tache = simulateur.run(circuit, shots=nombre_tirs)
    resultat = tache.result()
    comptages = resultat.get_counts()

    # Débogage : Afficher les comptages pour vérification
    print(f"x={x}, y={y}: {comptages}")

    # Évaluer les résultats
    for resultat_mesure, nombre in comptages.items():
        # Le résultat est une chaîne binaire (ex: "01"), [0] = Bob, [1] = Alice
        a, b = int(resultat_mesure[1]), int(resultat_mesure[0])  # Ajustement format
        if (a, b) in conditions_victoire[(x, y)]:
            compteur_succes += nombre
        compteur_total += nombre

# Calculer et afficher la probabilité de succès
probabilite_succes = compteur_succes / compteur_total
print(f"Probabilité de succès : {probabilite_succes:.2f}")

# Vérifier l'avantage quantique
if probabilite_succes > 0.75:
    print("Avantage quantique atteint ! La probabilité dépasse la limite classique.")
else:
    print("Pas d'avantage quantique. La probabilité est sous la limite classique.")