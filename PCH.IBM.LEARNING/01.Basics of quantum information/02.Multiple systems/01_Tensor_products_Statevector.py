from qiskit.quantum_info import Statevector, Operator
from numpy import sqrt

# ==========================================================================================================
#      https://learning.quantum.ibm.com/course/basics-of-quantum-information/multiple-systems
# ==========================================================================================================
#

# The Statevector class has a tensor method which returns the tensor product of itself and another Statevector

zero, one = Statevector.from_label("0"), Statevector.from_label("1")
zero.tensor(one).draw("latex")

print(zero.tensor(one))

