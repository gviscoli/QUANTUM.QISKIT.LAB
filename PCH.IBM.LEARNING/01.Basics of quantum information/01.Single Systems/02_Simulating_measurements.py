from qiskit.quantum_info import Statevector

# Next we will see one way that measurements of quantum states can be simulated in Qiskit, 
# using the measure method from the Statevector class.
    
v = Statevector([(1 + 2.0j) / 3, -2 / 3])
#v.draw("latex")
print(v.measure())