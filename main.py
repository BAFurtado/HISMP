""" Evolution of Instability in Stable Marriage Problem
    Shi et al 2018 Complexity Special Issue """

import numpy as np

from heterogeneousgsmp.persons import Male, Female


def main(g1, g2):
    males, females = [], []
    for i in range(g1):
        males.append(Male(i, True))
    for j in range(g2):
        females.append(Female(j, False))

    # Running algorithm
    # Shuffle
    np.random.shuffle(males)
    np.random.shuffle(females)
    # Ranking
    [i.ranking(females) for i in males]
    [i.ranking(males) for i in females]

    max_singles = len(males) - len(females)

    # Messaging service
    while sum(x.my_partner is None for x in males) > max(0, max_singles):
        [i.send_msg() for i in males]
        print(sum(x.my_partner is None for x in males))

    while sum(x.j == len(females) - 1 for x in males if x.my_partner is None) != max(0, max_singles):
        [i.send_msg() for i in males]
        print(sum(x.my_partner is None for x in males))
    return males, females


if __name__ == '__main__':

    males, females = main(1000, 1)
    # 3. Print Energy
    print('Final mean energy females {}'.format(np.mean([females[i].energy() for i in range(len(females))])))
    print('Final mean energy males {}'.format(np.mean([males[i].energy() for i in range(len(males))])))
