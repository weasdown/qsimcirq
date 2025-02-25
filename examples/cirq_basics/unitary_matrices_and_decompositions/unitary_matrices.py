# Copied and modified from https://quantumai.google/cirq/start/basics#unitary_matrices_and_decompositions

import cirq

print('Unitary of the X gate')
print(cirq.unitary(cirq.X))

print('\nUnitary of SWAP operator on two qubits.')
q0, q1 = cirq.LineQubit.range(2)
print(cirq.unitary(cirq.SWAP(q0, q1)))

print('\nUnitary of a sample circuit')
print(cirq.unitary(cirq.Circuit(cirq.X(q0), cirq.SWAP(q0, q1))))
