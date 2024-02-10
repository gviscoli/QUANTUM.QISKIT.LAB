from qiskit.quantum_info import Statevector, Operator
from numpy import sqrt

# The Operator class also has a tensor method. In the example below, we create the X and I gates and display their tensor product.

X = Operator([[0, 1], [1, 0]])
I = Operator([[1, 0], [0, 1]])

X.tensor(I)

print(X,I)

