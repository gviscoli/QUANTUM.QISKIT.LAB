from qiskit.quantum_info import Statevector

v = Statevector([(1 + 2.0j) / 3, -2 / 3])
#v.draw("latex")
print(v.measure())