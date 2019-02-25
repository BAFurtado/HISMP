""" You can run the program from here.
    This is the program that runs:
    Heterogeneity and instability in the Stable Marriage Problem, by
    Bernardo Alves Furtado
"""
import os
import time
import sys

import numpy as np
from joblib import Parallel, delayed

import main
from plotting import plot
from pretty_time import pretty_time_delta as pt

t0 = time.time()


def get_d():
    # Generate the different size groups of Females
    d = [x * 100 for x in range(1, 21)]
    d.insert(0, 1)
    d.insert(1, 50)
    d.insert(11, 950)
    d.insert(d.index(1000) + 1, 1050)
    return d


def generate(n, alpha, beta=1):
    # Generate the groups of Males and Females
    # Calls the main script
    # Calculates the average energy and saves the data
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


def main_r(n, p1, b1):
    # If data is available, plot the data
    # Otherwise call the generation and saving of the data and then plot
    name1 = 'saved_data/m_{:.2f}_{:.2f}_{}rep.txt'.format(p1, b1, n)
    name2 = 'saved_data/f_{:.2f}_{:.2f}_{}rep.txt'.format(p1, b1, n)
    if (os.path.exists(name1) and os.path.exists(name2)) is False:
        m, f, D = generate(n, p1, b1)
        np.savetxt(name1, m)
        np.savetxt(name2, f)
    else:
        D = get_d()
        m = np.loadtxt(name1)
        f = np.loadtxt(name2)
    print(len(m), len(f))
    plot(m, f, D, p1, b1, number, False)
    print('Finished first set of plots')
    print('Elapsed total time {}'.format(pt(time.time() - t0)))


if __name__ == '__main__':
    # Accepts parameters from Terminal. First number of repetitions.
    # Then number of available cores to run in parallel.
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        cpus = int(sys.argv[2])

    else:
        number = 3  # Number of repetitions
        cpus = 3

    # Variations of probabilities of being active messengers
    # Find description in the paper, published at arXiv

    # Case 1
    Parallel(n_jobs=cpus)(delayed(main_r)(number, p, 1) for p in np.linspace(1, 0, 11))

    # Case 2
    Parallel(n_jobs=cpus)(delayed(main_r)(number, p, 1 - p) for p in np.linspace(1, 0, 11))

    # Case 3
    Parallel(n_jobs=cpus)(delayed(main_r)(number, 1, 1 - p) for p in np.linspace(1, 0, 11))
