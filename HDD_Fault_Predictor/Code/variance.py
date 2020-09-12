import matplotlib.pyplot as plt
import numpy as np


def plot_for_variance(eig_values, idx):
    cumsum = np.cumsum(eig_values[idx]) / np.sum(eig_values[idx])
    xint = range(1, len(cumsum) + 1)
    plt.plot(xint, cumsum)

    plt.xlabel("Number of components")
    plt.ylabel("Cumulative explained variance")
    plt.xticks(xint)
    plt.xlim(1, 4, 1)
    plt.show()


