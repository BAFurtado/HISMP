""" Evolution of Instability in Stable Marriage Problem
    Shi et al 2018 Complexity Special Issue """

import numpy as np

from persons import Male, Female


def main(males, females):
    # Running algorithm
    # Shuffle
    np.random.shuffle(males)
    np.random.shuffle(females)
    # Ranking
    [i.ranking(females) for i in males]
    [i.ranking(males) for i in females]

    max_singles = len(males) - len(females)

    # Messaging service
    control = 0
    for each in [males, females]:
        while sum(x.my_partner is None for x in each) > max(0, max_singles):
            [i.send_msg() for i in each]
            print(sum(x.my_partner is None for x in each))
            if control > 1000:
                break
            control += 1

    # Making sure all active messengers are rejected by all other counter partner
    control = 0
    while sum(x.j == len(females) - 1 for x in males if x.my_partner is None) != max(0, max_singles):
        [i.send_msg() for i in males]
        print(sum(x.my_partner is None for x in males))
        if control > 1000:
            break
        control += 1

    control = 0
    while sum(x.j == len(males) - 1 for x in females if x.my_partner is None) != max(0, max_singles):
        [i.send_msg() for i in females]
        print(sum(x.my_partner is None for x in females))
        if control > 1000:
            break
        control += 1

    return males, females


def gen_groups(group1, group2, alpha):
    # Generate groups with a percentage (alpha) of active status (actively sends messages)
    m1, f1 = [], []
    for i in range(group1):
        m1.append(Male(i, np.random.choice([True, False], p=[alpha, 1 - alpha])))
    for j in range(group2):
        f1.append(Female(j, np.random.choice([True, False], p=[1 - alpha, alpha])))
    return m1, f1


if __name__ == '__main__':
    g1 = 1
    g2 = 1000
    p = .8
    m, f = gen_groups(g1, g2, p)
    m, f = main(m, f)
    # 3. Print Energy
    print('Final mean energy females {}'.format(np.mean([f[i].energy() for i in range(len(f))])))
    print('Final mean energy males {}'.format(np.mean([m[i].energy() for i in range(len(m))])))
