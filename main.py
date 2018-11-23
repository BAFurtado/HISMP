""" Evolution of Instability in Stable Marriage Problem
    Shi et al 2018 Complexity Special Issue """

import numpy as np

from persons import Male, Female


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

    # 2. Messaging service
    [i.send_msg(females) for i in males]

    return males, females


if __name__ == '__main__':

    males, females = main(10, 2)
    # 3. Print Energy
    print('Final mean energy females {}'.format(np.mean([females[i].energy() for i in range(len(females))])))
    print('Final mean energy males {}'.format(np.mean([males[i].energy() for i in range(len(males))])))
