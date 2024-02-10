from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.result import marginal_distribution
from qiskit.circuit.library import UGate
from numpy import pi, random

# ==========================================================================================================
#      https://learning.quantum.ibm.com/course/basics-of-quantum-information/entanglement-in-action
# ==========================================================================================================
#

# The barrier function creates a visual separation making the circuit diagram more readable, 
# and it also prevents Qiskit from performing various simplifications and optimizations across barriers 
# during compilation when circuits are run on real hardware.
#
# The if_test function applies an operation conditionally depending on a classical bit or register.
#

import os
os.system('cls')

random_gate = UGate(
    theta=random.random() * 2 * pi,
    phi=random.random() * 2 * pi,
    lam=random.random() * 2 * pi,
)

print()
print()
print(random_gate.to_matrix())
print()
print()

qubit = QuantumRegister(1, "Q")
ebit0 = QuantumRegister(1, "A")
ebit1 = QuantumRegister(1, "B")
a = ClassicalRegister(1, "a")
b = ClassicalRegister(1, "b")

protocol = QuantumCircuit(qubit, ebit0, ebit1, a, b)

# Prepare ebit used for teleportation
protocol.h(ebit0)
protocol.cx(ebit0, ebit1)
protocol.barrier()

# Alice's operations
protocol.cx(qubit, ebit0)
protocol.h(qubit)
protocol.barrier()

# Alice measures and sends classical bits to Bob
protocol.measure(ebit0, a)
protocol.measure(qubit, b)
protocol.barrier()

# Bob uses the classical bits to conditionally apply gates
with protocol.if_test((a, 1)):
    protocol.x(ebit1)
with protocol.if_test((b, 1)):
    protocol.z(ebit1)

# Create a new circuit including the same bits and qubits used in the
# teleportation protocol.

test = QuantumCircuit(qubit, ebit0, ebit1, a, b)

# Start with the randomly selected gate on Q

test.append(random_gate, qubit)
test.barrier()

# Append the entire teleportation protocol from above.

test = test.compose(protocol)
test.barrier()

# Apply the inverse of the random unitary to B and measure.

test.append(random_gate.inverse(), ebit1)

# Finally let's run the Aer simulator on this circuit and plot a histogram of the outputs. We'll see the statistics for all three classical bits
#
result = ClassicalRegister(1, "Result")
test.add_register(result)
test.measure(ebit1, result)

print(test.draw())

print()
print()

result = AerSimulator().run(test).result()
statistics = result.get_counts()
print(statistics)

print()
print()

# We can also filter the statistics to focus just on the test result qubit if we wish, like this:
#
filtered_statistics = marginal_distribution(statistics, [2])
print(filtered_statistics)