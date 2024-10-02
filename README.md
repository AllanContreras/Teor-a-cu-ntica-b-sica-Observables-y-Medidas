# Teoria cuantica basica Observables y Medidas

# Problemas
 - La probabilidad de encontrar una partícula en una posición específica.
 - La probabilidad de transición entre dos estados cuánticos.

# Solución

- Probabilidad de encontrar la partícula en una posición específica:
- Utilizamos el cuadrado del valor absoluto de la amplitud de probabilidad en esa posición.
Fórmula:


``` txt
 P(i)=∣ci​∣2
```

- Probabilidad de transición entre dos estados:
- Calculamos el valor absoluto del producto interno de los dos vectores de estado al cuadrado.
Fórmula:

``` txt
P(ψ→ϕ)=∣⟨ϕ∣ψ⟩∣2=​i∑​di∗​ci​​2
```
 # Implementación en Python
- Usamos Python para implementar estas fórmulas. Aquí están los pasos clave:
 - Definimos una función probabilidad_posicion para calcular la probabilidad de encontrar la partícula en una posición dada.
- Definimos una función probabilidad_transicion para calcular la probabilidad de transición entre dos estados.

# Herramientas utilizadas:

- NumPy: Para realizar operaciones matemáticas y de álgebra lineal, como productos internos y verificación de matrices hermitianas.
