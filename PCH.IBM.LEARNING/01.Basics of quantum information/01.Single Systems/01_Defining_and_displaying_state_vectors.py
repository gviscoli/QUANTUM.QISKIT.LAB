from qiskit.quantum_info import Statevector
from numpy import sqrt

# ==========================================================================================================
#      https://learning.quantum.ibm.com/course/basics-of-quantum-information/single-systems
# ==========================================================================================================
#

u = Statevector([1 / sqrt(2), 1 / sqrt(2)])
v = Statevector([(1 + 2.0j) / 3, -2 / 3])
w = Statevector([1 / 3, 2 / 3])

print("State vectors u, v, and w have been defined.")

print(u.draw("latex"))
print(v.draw("text"))

print()

print(u.is_valid())
print(w.is_valid())