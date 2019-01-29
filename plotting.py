import matplotlib.pyplot as plt
import numpy as np

import main


def plot(m1, m2, d, pp, single=True):

    fig, ax = plt.subplots()
    if single:
        plt.scatter(d, m1, color='blue', label='man')
        plt.scatter(d, m2, color='red', label='woman')
    else:
        b1 = ax.boxplot(m1, patch_artist=True, boxprops=dict(facecolor='blue', color='blue'), sym='')
        b2 = ax.boxplot(m2, patch_artist=True, boxprops=dict(facecolor='red', color='red'), sym='')

        for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
            plt.setp(b1[element], color='blue')
        for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
            plt.setp(b2[element], color='red')
        ax.legend([b1["boxes"][0], b2["boxes"][0]], ['Man', 'Woman'], loc='best', frameon=False)

    ax.set_yscale('log')
    ax.yaxis.grid(True)
    ax.set_title('Instability in the Stable Marriage Problem\n'
                 'Number of Men = 1,000')
    ax.set_xticklabels(str(i) for i in d)
    ax.set_xlabel('Number of Women')
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
    ax.set_ylabel('Energy')

    fig.savefig('outputs/fig_' + str(pp) + '.png')
    plt.close()
    # plt.show()


def gen_distribution(prob):
    # Generating distribution
    d = [x * 100 for x in range(1, 21)]
    d.insert(0, 1)
    d.insert(1, 50)
    d.insert(11, 950)
    d.insert(d.index(1000) + 1, 1050)

    # To keep mean results
    m_mean, f_mean = [], []
    for each in d:
        males, females = main.gen_groups(1000, each, prob)
        males, females = main.main(males, females)
        m_mean.append(np.mean([males[i].energy() for i in range(len(males))]))
        f_mean.append(np.mean([females[i].energy() for i in range(len(females))]))

    return m_mean, f_mean, d


if __name__ == '__main__':
    p = 1
    m, f, D = gen_distribution(p)
    plot(m, f, D, p)

    # m = np.loadtxt('outputs/mp7')
    # f = np.loadtxt('outputs/fp7')
    # D = np.loadtxt('outputs/Dp7')
    # p = 1

    # plot(m, f, D, p, False)
