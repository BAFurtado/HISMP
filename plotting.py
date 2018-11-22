import matplotlib.pyplot as plt
import numpy as np
import main
from math import log


def plot(m1, m2, m):
    for x, y in zip(m, m1):
        try:
            plt.plot(x, log(y), color='red', label='woman')
        except ValueError:
            plt.plot(x, 0, color='red', label='woman')
    for i, j in zip(m, m2):
        try:
            plt.plot(i, log(j), color='blue', label='man')
        except ValueError:
            plt.plot(i, 0, color='blue', label='man')
    plt.savefig('fig1.png')
    plt.show()


def generate():
    # Generating distribution
    d = [x * 100 for x in range(1, 21)]
    d.insert(0, 1)

    # To keep mean results
    f_mean, m_mean = [], []
    for each in d:
        males, females = main.main(1000, each)
        f_mean.append(np.mean([females[i].energy(females) for i in range(len(females))]))
        m_mean.append(np.mean([males[i].energy(males) for i in range(len(males))]))
    return f_mean, m_mean, d


if __name__ == '__main__':
    f, m, D = generate()
    plot(f, m, D)
