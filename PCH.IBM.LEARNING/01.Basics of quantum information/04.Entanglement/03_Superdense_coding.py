from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer.primitives import Sampler
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# ==========================================================================================================
#      https://learning.quantum.ibm.com/course/basics-of-quantum-information/entanglement-in-action
# ==========================================================================================================
#

# Superdense coding is a protocol that, in some sense, achieves a complementary aim to teleportation. 
# Rather than allowing for the transmission of one qubit using two classical bits of communication (at the cost of one e-bit of entanglement), 
# it allows for the transmission of two classical bits using one qubit of quantum communication (again, at the cost of one e-bit of entanglement).
#
# In greater detail, we have a sender (Alice) and a receiver (Bob) that share one e-bit of entanglement. According to the conventions in place for the lesson, 
# this means that Alice holds a qubit A Bob holds a qubit B and together the pair (A, B) is in the state |pi+>. 
# Alice wishes to transmit two classical bits to Bob, which we'll denoted by c and d and she will accomplish this by sending him one qubit.
#
# It is reasonable to view this feat as being less interesting than the one that teleportation accomplishes. 
# Sending qubits is likely to be so much more difficult than sending classical bits for the foreseeable future that trading one qubit of quantum communication for two bits of classical communication, 
# at the cost of an e-bit no less, hardly seems worth it. However, this does not imply that superdense coding is not interesting, for it most certainly is.
#
# Fitting the theme of the lesson, one reason why superdense coding is interesting is that it demonstrates a concrete and (in the context of information theory) rather striking use of entanglement. 
# A famous theorem in quantum information theory, known as Holevo's theorem, implies that without the use of a shared entangled state, it is impossible to communicate more than one bit of classical information by sending a single qubit. 
# (Holevo's theorem is more general than this. It's precise statement is technical and requires explanation, but this is one consequence of it.) 
# So, through superdense coding, shared entanglement effectively allows for the doubling of the classical information-carrying capacity of sending qubits.
#

import os
os.system('cls')

# Here is a simple implementation of superdense coding where we specify the circuit itself depending on the bits to be transmitted. 
# First let's specify the bits to be transmitted. (Try changing the bits to see that it works correctly.)
# 
c = "1"
d = "0"

# Now we'll build the circuit accordingly. Here we'll just allow Qiskit to use the default names for the qubits: q0 for the top qubit and q1 for the bottom one
#
protocol = QuantumCircuit(2)

# Prepare ebit used for superdense coding
protocol.h(0)
protocol.cx(0, 1)
protocol.barrier()

# Alice's operations
if d == "1":
    protocol.z(0)
if c == "1":
    protocol.x(0)
protocol.barrier()

# Bob's actions
protocol.cx(0, 1)
protocol.h(0)
protocol.measure_all()

print(protocol.draw())

print()
print()

result = Sampler().run(protocol).result()
statistics = result.quasi_dists[0].binary_probabilities()

for outcome, frequency in statistics.items():
    print(f"Measured {outcome} with frequency {frequency}")

print(statistics)

print()
print()
