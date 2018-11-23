import matplotlib.pyplot as plt
import numpy as np
import main


def plot(m1, m2, m):
    plt.scatter(m, m1, color='blue', label='man')
    plt.scatter(m, m2, color='red', label='woman')
    plt.yscale('log')
    plt.legend()
    plt.savefig('fig1.png')
    plt.show()


def generate():
    # Generating distribution
    d = [x * 100 for x in range(1, 21)]
    d.insert(0, 1)

    # To keep mean results
    m_mean, f_mean = [], []
    for each in d:
        males, females = main.main(1000, each)
        m_mean.append(np.mean([males[i].energy() for i in range(len(males))]))
        f_mean.append(np.mean([females[i].energy() for i in range(len(females))]))

    return m_mean, f_mean, d


if __name__ == '__main__':
    m, f, D = generate()
    plot(m, f, D)
