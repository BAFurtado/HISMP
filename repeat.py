import numpy as np

import main
from plotting import plot


def generate(n, alpha, beta=1):
    d = [x * 100 for x in range(1, 21)]
    d.insert(0, 1)
    d.insert(1, 50)
    d.insert(11, 950)
    d.insert(d.index(1000) + 1, 1050)

    m_matrix = np.zeros((n, len(d)))
    f_matrix = np.zeros((n, len(d)))
    
    for k in range(n):
        for j in range(len(d)):
            males, females = main.gen_groups(1000, d[j], alpha, beta)
            males, females = main.main(males, females)
            m_matrix[k, j] = np.mean([males[i].energy() for i in range(len(males))])
            f_matrix[k, j] = np.mean([females[i].energy() for i in range(len(females))])
            print('One more run done ...! {} Repetition {}'.format(j, k))
        print('One more repetition done ...!', k)

    return m_matrix, f_matrix, d


if __name__ == '__main__':
    number = 3  # Number of repetitions
    for p in np.linspace(1, 0, 11):
        # Two alternatives. b = 1, Beta, then males are all active
        # b = 1 - p, the full probability of being active is 1
        b = 1
        m, f, D = generate(number, p, b)
        np.savetxt('saved_data/m_{}_{}.txt'.format(p, b), m)
        np.savetxt('saved_data/f_{}_{}.txt'.format(p, b), f)
        plot(m, f, D, p, False)
        b = 1 - p
        m, f, D = generate(number, p, b)
        np.savetxt('saved_data/m_{}_{}.txt'.format(p, b), m)
        np.savetxt('saved_data/f_{}_{}.txt'.format(p, b), f)
        plot(m, f, D, p, False)