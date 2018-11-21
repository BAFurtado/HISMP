""" Evolution of Instability in Stable Marriage Problem
    Shi et al 2018 Complexity Special Issue """

import numpy as np


class Person:

    def __init__(self, name, active):
        self.id = name
        self.my_ranking = None
        self.my_partner = None
        self.my_energy = None
        self.status = active

    def ranking(self, other_group):
        my_group = other_group.copy()
        np.random.shuffle(my_group)
        self.my_ranking = my_group

    def match(self, candidate):
        self.my_partner = candidate

    def send_msg(self, other_group):
        if self.my_partner is None:
            for j in range(len(other_group)):
                result = self.my_ranking[j].receive_msg(self)
                if result == '+':
                    break

    def receive_msg(self, candidate):
        if self.my_partner is None:
            self.match(candidate)
            candidate.match(self)
            return '+'
        elif [i.id for i in self.my_ranking].index(candidate.id) < \
                [i.id for i in self.my_ranking].index(self.my_partner.id):
            self.match(candidate)
            candidate.match(self)
            return '+'
        else:
            return '-'

    def energy(self, own_group):
        if self.my_partner is not None:
            self.my_energy = [i.id for i in self.my_ranking].index(self.my_partner.id)
            return self.my_energy
        else:
            self.my_energy = len(own_group) + 1
            return self.my_energy


class Male(Person):
    pass


class Female(Person):
    pass


if __name__ == '__main__':

    # Generation
    m, f = 1000, 500
    males, females = [], []
    for i in range(m):
        males.append(Male(i, True))
    for j in range(f):
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

    # 3. Print Energy
    print('Final mean energy females {}'.format(np.mean([females[i].energy(females) for i in range(len(females))])))
    print('Final mean energy males {}'.format(np.mean([males[i].energy(males) for i in range(len(males))])))
