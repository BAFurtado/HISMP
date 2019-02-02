import numpy as np
import time
import main
from plotting import plot
from pretty_time import pretty_time_delta as pt
import os

t0 = time.time()


def get_d():
    d = [x * 100 for x in range(1, 21)]
    d.insert(0, 1)
    d.insert(1, 50)
    d.insert(11, 950)
    d.insert(d.index(1000) + 1, 1050)
    return d


def generate(n, alpha, beta=1):
    d = get_d()
    m_matrix = np.zeros((n, len(d)))
    f_matrix = np.zeros((n, len(d)))
    
    for k in range(n):
        for j in range(len(d)):
            males, females = main.gen_groups(1000, d[j], alpha, beta)
            males, females = main.main(males, females)
            m_matrix[k, j] = np.mean([males[i].energy() for i in range(len(males))])
            f_matrix[k, j] = np.mean([females[i].energy() for i in range(len(females))])
            print('One more run done ...! {} Repetition {}'.format(j, k))
            print('Elapsed total time {}'.format(pt(time.time() - t0)))
        print('One more repetition done ...!', k)
        print('Elapsed total time {}'.format(pt(time.time() - t0)))

    return m_matrix, f_matrix, d


if __name__ == '__main__':
    t0 = time.time()
    number = 25  # Number of repetitions
    for p in np.linspace(1, 0, 11):
        # Two alternatives. b = 1, Beta, then males are all active
        # b = 1 - p, the full probability of being active is 1
        b = 1

        name1 = 'saved_data/m_{:.2f}_{:.2f}.txt'.format(p, b)
        name2 = 'saved_data/f_{:.2f}_{:.2f}.txt'.format(p, b)
        if (os.path.exists(name1) and os.path.exists(name2)) is False:
            m, f, D = generate(number, p, b)
            np.savetxt(name1, m)
            np.savetxt(name2, f)
        else:
            D = get_d()
            m = np.loadtxt(name1)
            f = np.loadtxt(name2)
        plot(m, f, D, p, b, number, False)
        print('Finished first set of plots')
        print('Elapsed total time {}'.format(pt(time.time() - t0)))
        b = 1 - p

        name1 = 'saved_data/m_{:.2f}_{:.2f}.txt'.format(p, b)
        name2 = 'saved_data/f_{:.2f}_{:.2f}.txt'.format(p, b)
        if (os.path.exists(name1) and os.path.exists(name2)) is False:
            m, f, D = generate(number, p, b)
            np.savetxt(name1, m)
            np.savetxt(name2, f)
        else:
            D = get_d()
            m = np.loadtxt(name1)
            f = np.loadtxt(name2)
        plot(m, f, D, p, b, number, False)

        print('Finished second set of plots')
        print('Elapsed total time {}'.format(pt(time.time() - t0)))
