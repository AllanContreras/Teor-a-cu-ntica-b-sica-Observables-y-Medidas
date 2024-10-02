import numpy as np

# Definimos los eigenvectores (en este caso, asumimos que son ortogonales y normalizados)
eigenvectors = [
    np.array([1, 0]),  # |e0>
    np.array([0, 1])   # |e1>
]

# Definimos el estado inicial normalizado |ψ>
psi = np.array([1/np.sqrt(2), 1/np.sqrt(2)])  # Ejemplo: |ψ> = (1/√2)|e0> + (1/√2)|e1>

# Calculamos las probabilidades de transición
probabilities = []
for e in eigenvectors:
    probability = np.abs(np.dot(e.conj(), psi))**2
    probabilities.append(probability)

# Mostramos los resultados
for i, prob in enumerate(probabilities):
    print(f"Probabilidad de transicionar a |e{i}>: {prob:.2f}")
