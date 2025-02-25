# Copied from https://quantumai.google/cirq/start/basics#gates_and_operations
import cirq


# stuff to run always here such as class/def
def main():
    # Example gates
    cnot_gate = cirq.CNOT
    pauli_z = cirq.Z

    # Use exponentiation to get square root gates.
    sqrt_x_gate = cirq.X ** 0.5

    # Some gates can also take parameters
    sqrt_sqrt_y = cirq.YPowGate(exponent=0.25)

    # Create two qubits at once, in a line.
    q0, q1 = cirq.LineQubit.range(2)

    # Example operations
    z_op = cirq.Z(q0)
    not_op = cirq.CNOT(q0, q1)
    sqrt_iswap_op = cirq.SQRT_ISWAP(q0, q1)

    # You can also use the gates you specified earlier.
    cnot_op = cnot_gate(q0, q1)
    pauli_z_op = pauli_z(q0)
    sqrt_x_op = sqrt_x_gate(q0)
    sqrt_sqrt_y_op = sqrt_sqrt_y(q0)


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
