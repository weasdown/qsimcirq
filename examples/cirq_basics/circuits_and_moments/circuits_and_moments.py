# Copied from https://quantumai.google/cirq/start/basics#circuits_and_moments
import cirq


def appending_operations_one_by_one():
    print('\nAppending Operations one by one:')
    circuit = cirq.Circuit()
    qubits = cirq.LineQubit.range(3)
    circuit.append(cirq.H(qubits[0]))
    circuit.append(cirq.H(qubits[1]))
    circuit.append(cirq.H(qubits[2]))
    print(circuit)


def appending_iterable_of_operations():
    print('\nAppending an iterable of Operations:')
    circuit = cirq.Circuit()
    ops = [cirq.H(q) for q in cirq.LineQubit.range(3)]
    circuit.append(ops)
    print(circuit)


def generator_of_operations():
    print('\nUsing a generator that yields Operations:')
    # Append with generator
    circuit = cirq.Circuit()
    circuit.append(cirq.H(q) for q in cirq.LineQubit.range(3))
    print(circuit)
    # Initializer with generator
    print(cirq.Circuit(cirq.H(q) for q in cirq.LineQubit.range(3)))


def consecutive_moments():
    print('\nGates in consecutive moments:')
    print(cirq.Circuit(cirq.SWAP(q, q + 1) for q in cirq.LineQubit.range(3)))


def separate_moments():
    print('\nGates in separate moments:')
    # Creates each gate in a separate moment by passing an iterable of Moments instead of Operations.
    print(cirq.Circuit(cirq.Moment([cirq.H(q)]) for q in cirq.LineQubit.range(3)))


if __name__ == '__main__':
    appending_operations_one_by_one()
    appending_iterable_of_operations()
    generator_of_operations()
    consecutive_moments()
    separate_moments()
