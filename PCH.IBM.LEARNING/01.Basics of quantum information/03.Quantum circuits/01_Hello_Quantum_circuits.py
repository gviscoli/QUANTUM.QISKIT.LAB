from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.primitives import Sampler
from qiskit.visualization import plot_histogram

import os
os.system('cls')

# ==========================================================================================================
#      https://learning.quantum.ibm.com/course/basics-of-quantum-information/quantum-circuits
# ==========================================================================================================
#

# In the quantum circuit model, wires represent qubits and gates represent operations acting on these qubits. 
# We'll focus for now on operations we've encountered so far, namely unitary operations and standard basis measurements. 
# As we learn about other sorts of quantum operations and measurements, we'll enhance our model accordingly.


q1 = QuantumRegister(1, "q1")
measureQ1 = ClassicalRegister(1, "measureQ1")

circuit = QuantumCircuit(q1, measureQ1)

circuit.h(q1)
circuit.s(q1)
circuit.h(q1)
circuit.t(q1)

circuit.measure(q1, measureQ1)

print(circuit.draw())

# The circuit can be simulated using the Sampler primitive.
#
results = Sampler().run(circuit).result()
statistics = results.quasi_dists[0].binary_probabilities()

print()
print()


print(statistics)

print()

print("Value 0: " + str(statistics['0']))
print("Value 1:" + str(statistics['1']))

print()
print()

