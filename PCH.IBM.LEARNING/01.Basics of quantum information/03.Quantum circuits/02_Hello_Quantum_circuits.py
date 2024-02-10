from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.primitives import Sampler
from qiskit.visualization import plot_histogram

import os
os.system('cls')

X = QuantumRegister(1, "X")
Y = QuantumRegister(1, "Y")
A = ClassicalRegister(1, "A")
B = ClassicalRegister(1, "B")

circuit = QuantumCircuit(Y, X, B, A)
circuit.h(Y)
circuit.cx(Y, X)
circuit.measure(Y, B)
circuit.measure(X, A)


print(circuit.draw())

# The circuit can be simulated using the Sampler primitive.
#
results = Sampler().run(circuit).result()
statistics = results.quasi_dists[0].binary_probabilities()

print()
print()


print(statistics)

print()

print("Value 00: " + str(statistics['00']))
print("Value 11:" + str(statistics['11']))

print()
print()