import matplotlib.pyplot as plt
import numpy as np

import main


def plot(m1, m2, d, single=True):

    fig, ax = plt.subplots()
    if single:
        plt.scatter(d, m1, color='blue', label='man')
        plt.scatter(d, m2, color='red', label='woman')
    else:
        b1 = ax.boxplot(m1, patch_artist=True, boxprops=dict(facecolor='blue'))
        b2 = ax.boxplot(m2, patch_artist=True, boxprops=dict(facecolor='red'))

    ax.set_yscale('log')
    ax.yaxis.grid(True)
    ax.set_title('Instability in the Stable Marriage Problem\n'
                 'Number of Men = 1,000')
    ax.set_xticklabels(str(i) for i in d)
    ax.set_xlabel('Number of Women')
    ax.set_ylabel('Energy')
    ax.legend([b1["boxes"][0], b2["boxes"][0]], ['Man', 'Woman'], loc='upper right', frameon=False)
    fig.savefig('fig1.png')
    plt.show()


def generate():
    # Generating distribution
    d = [x * 100 for x in range(1, 21)]
    d.insert(0, 1)
    d.insert(1, 50)
    d.insert(11, 950)
    d.insert(d.index(1000) + 1, 1050)

    # To keep mean results
    m_mean, f_mean = [], []
    for each in d:
        males, females = main.main(1000, each)
        m_mean.append(np.mean([males[i].energy() for i in range(len(males))]))
        f_mean.append(np.mean([females[i].energy() for i in range(len(females))]))

    return m_mean, f_mean, d


if __name__ == '__main__':
    # m, f, D = generate()
    # plot(m, f, D)

    m = np.array([[95.345, 179.077],
           [99.323, 180.016],
           [91.091, 189.763]])
    f = np.array([[2.01, 1.97],
           [1.06, 1.45],
           [5.02, 1.09]])
    D = [100, 200]
    plot(m, f, D, False)
