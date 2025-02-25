# Copied from https://quantumai.google/cirq/start/basics#decompositions

import cirq


def hadamard_H():
    print(cirq.decompose(cirq.H(cirq.LineQubit(0))))


def toffoli_gate():
    q0, q1, q2 = cirq.LineQubit.range(3)
    print(cirq.Circuit(cirq.decompose(cirq.TOFFOLI(q0, q1, q2))))
