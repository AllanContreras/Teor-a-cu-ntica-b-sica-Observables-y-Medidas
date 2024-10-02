import numpy as np

def probabilidad_transicion(ket1, ket2):
    # Calcula la amplitud de transición
    amplitud = np.vdot(ket1, ket2)
    # Calcula la probabilidad de transición
    probabilidad = np.abs(amplitud)**2
    return probabilidad

# Ejemplo de uso
ket1 = np.array([1, 0])
ket2 = np.array([0, 1])
print(probabilidad_transicion(ket1, ket2))



def es_hermitiana(matriz):
    return np.allclose(matriz, matriz.conj().T)

def media_y_varianza(observable, ket):
    if not es_hermitiana(observable):
        raise ValueError("La matriz no es hermitiana")
    
    # Calcula la media
    media = np.vdot(ket, np.dot(observable, ket))
    
    # Calcula la varianza
    media_cuadrado = np.vdot(ket, np.dot(observable @ observable, ket))
    varianza = media_cuadrado - media**2
    
    return media, varianza

# Ejemplo de uso
observable = np.array([[1, 0], [0, -1]])
ket = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
print(media_y_varianza(observable, ket))
