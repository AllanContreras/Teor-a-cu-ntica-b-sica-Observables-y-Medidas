import numpy as np

def probabilidad_posicion(ket, posicion):
    return np.abs(ket[posicion])**2

def probabilidad_transicion(ket1, ket2):
    return np.abs(np.dot(np.conj(ket2), ket1))**2

# Ejemplo de uso
ket1 = np.array([1/np.sqrt(2), 1/np.sqrt(2)])  # Estado inicial
ket2 = np.array([1, 0])  # Estado final

posicion = 0
print(f"Probabilidad de encontrar la partícula en la posición {posicion}: {probabilidad_posicion(ket1, posicion)}")

print(f"Probabilidad de transición de ket1 a ket2: {probabilidad_transicion(ket1, ket2)}")
