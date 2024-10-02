# Teoria cuantica basica Observables y Medidas

# FUNCIONES 
-  1. Probabilidad de transición
Objetivo: Calcular la probabilidad de transición entre dos vectores (kets) en un sistema cuántico.

# Pasos:

- Amplitud de transición: Utilicé el producto interno (o producto punto conjugado) entre los dos vectores. Esto se hace con np.vdot(ket1, ket2) en NumPy.

- Probabilidad de transición: Tomé el valor absoluto al cuadrado de la amplitud de transición para obtener la probabilidad. Esto se hace con np.abs(amplitud)**2.

  
# 2. Media y varianza de un observable
Objetivo: Verificar si una matriz es hermitiana y calcular la media y la varianza de un observable en un estado dado.

# Pasos:

- Verificación de hermiticidad: Comprobé si la matriz es igual a su conjugada transpuesta usando np.allclose(matriz, matriz.conj().T).
  
- Cálculo de la media: Utilicé el producto interno entre el ket y el observable aplicado al ket, np.vdot(ket, np.dot(observable, ket)).
  
- Cálculo de la varianza: Calculé el valor esperado del observable al cuadrado y resté el cuadrado de la media.



# Herramientas utilizadas:

- NumPy: Para realizar operaciones matemáticas y de álgebra lineal, como productos internos y verificación de matrices hermitianas.
