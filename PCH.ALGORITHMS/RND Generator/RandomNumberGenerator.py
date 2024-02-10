from qiskit import QuantumCircuit
import qiskit

qr = qiskit.QuantumRegister(1)
cr = qiskit.ClassicalRegister(1)
program = qiskit.QuantumCircuit(qr, cr)

program.measure(qr,cr)

job = qiskit.execute( program, qiskit.BasicAer.get_backend('qasm_simulator') )

print( job.result().get_counts() )
