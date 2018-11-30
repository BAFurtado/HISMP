import numpy as np

import main
from plotting import plot


def generate():
    d = [x * 100 for x in range(1, 21)]
    n = 100  # numero de repeticoes
    
    m_matrix = np.zeros((n, len(d)))
    f_matrix = np.zeros((n, len(d)))
    
    for k in range(n):
        for j in range(len(d)):
                males, females = main.main(1000, d[j])
                m_matrix[k, j] = np.mean([males[i].energy() for i in range(len(males))])
                f_matrix[k, j] = np.mean([females[i].energy() for i in range(len(females))])

    return m_matrix, f_matrix, d


if __name__ == '__main__':
    m, f, D = generate()
    plot(m, f, D, False)