
# LINK: https://cloud.ibm.com/docs/quantum-computing?topic=quantum-computing-example-sampler
#
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Options, Sampler

service = QiskitRuntimeService(channel="ibm_cloud", token="XfQy3yrTr1-Y54exSFPTHoIJwocJNbGhcoUzWXRi_YYC", instance="crn:v1:bluemix:public:quantum-computing:us-east:a/e6bb54879eac78ddeaf1d5d298c6dd1c:5c575744-4e31-4aae-9fde-d26398b25380::")
options = Options(optimization_level=1)

with Session(service=service, backend="ibmq_qasm_simulator"):
    sampler = Sampler(options=options)


# Prepare the input circuit.

from qiskit import QuantumCircuit

bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)
bell.measure_all()

# Execute the Bell circuit
with Session(service=service, backend="ibmq_qasm_simulator"):
    sampler = Sampler(options=options)
    job = sampler.run(circuits=bell)
    print(job.result())

    # You can invoke run() multiple times.
    job = sampler.run(circuits=bell)
    print(job.result())