from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
 
import os

circuit = QuantumCircuit(1)

circuit.h(0)
circuit.t(0)
circuit.h(0)
circuit.t(0)
circuit.z(0)

ket0 = Statevector([1, 0])
v = ket0.evolve(circuit)
#v.draw("text")

#print(v)

statistics = v.sample_counts(4000)

os.system('cls')

print("Value ZERO: " + str(statistics['0']))
print("Value ONE:" + str(statistics['1']))
