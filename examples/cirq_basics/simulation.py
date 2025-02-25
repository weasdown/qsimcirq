# Copied and modified from https://quantumai.google/cirq/start/basics#simulation
import cirq


def bell_state_circuit() -> cirq.Circuit:
    # Create a circuit to generate a Bell State:
    # 1/sqrt(2) * ( |00⟩ + |11⟩ )
    bell_circuit: cirq.Circuit = cirq.Circuit()
    q0, q1 = cirq.LineQubit.range(2)
    bell_circuit.append(cirq.H(q0))
    bell_circuit.append(cirq.CNOT(q0, q1))

    # For sampling, we need to add a measurement at the end
    bell_circuit.append(cirq.measure(q0, q1, key='result'))

    return bell_circuit


# Initialize Simulator
s = cirq.Simulator()


def simulate(circuit: cirq.Circuit):
    print('Simulate the circuit:')
    results = s.simulate(circuit)
    print(results)


# Sample the circuit
samples = s.run(bell_state_circuit(), repetitions=1000)

if __name__ == '__main__':
    bell: cirq.Circuit = bell_state_circuit()
    simulate(bell)
