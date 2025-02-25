# Copied from https://quantumai.google/cirq/start/basics#visualizing_results

import cirq
import matplotlib.pyplot as plt

from simulation import samples


def basic():
    cirq.plot_state_histogram(samples, plt.subplot())
    plt.show()


def ignore_non_seen_qubits():
    # Pull of histogram counts from the result data structure
    counts = samples.histogram(key='result')
    print(counts)

    # Graph the histogram counts instead of the results
    cirq.plot_state_histogram(counts, plt.subplot())
    plt.show()


if __name__ == '__main__':
    # basic()
    ignore_non_seen_qubits()
