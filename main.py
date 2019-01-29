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

    singles = max(0, len(males) - len(females))
    # Messaging service
    # Rule 1: No singles

    # All active people have sent messages to everyone on the other group
    current = sum([x for each in [males, females] for x in each if x.my_partner != None])
    not_msg = sum([1 for each in [males, females] for x in each if (x.status == True) and (x.my_partner == None)
                   and (x.messaged == False)])
    print('Still single: ', current)
    print('Theoretically single: ', singles)
    print('Not messaged: ', not_msg)

    while current > singles or not_msg > 0:
        [x.send_msg() for x in males]
        [x.send_msg() for x in females]
        current = sum([1 for each in [males, females] for x in each if x.my_partner == None])
        not_msg = sum([1 for each in [males, females] for x in each if (x.status == True) and (x.my_partner == None)
                       and (x.messaged == False)])
        print('Still single: ', current)
        print('Theoretically single: ', singles)
        print('Not messaged: ', not_msg)

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
    g1 = 1000
    g2 = 1000
    p = 1
    m, f = gen_groups(g1, g2, p)
    m, f = main(m, f)
    # 3. Print Energy
    print('Final mean energy females {}'.format(np.mean([f[i].energy() for i in range(len(f))])))
    print('Final mean energy males {}'.format(np.mean([m[i].energy() for i in range(len(m))])))
