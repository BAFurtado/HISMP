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
        np.random.shuffle(other_group)
        self.my_ranking = other_group

    def send_msg(self, other_group):
        if self.my_partner is None:
            for j in range(len(other_group)):
                result = self.my_ranking[j].receive_msg(self)
                if result == '+':
                    break

    def receive_msg(self, candidate):
        if self.my_partner is None:
            self.my_partner = candidate
            candidate.partner(self)
            return '+'
        elif self.my_ranking.index(candidate.id) < self.my_ranking.index(self.my_partner.id):
            self.my_partner = candidate
            candidate.partner(self)
            return '+'
        else:
            return '-'

    def energy(self, other_group, own_group):
        if self.my_partner is not None:
            self.my_energy = [i.id for i in other_group].index(self.my_partner.id)
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
    m, f = 105, 100
    males, females = [], []
    for i in range(m):
        males.append(Male(i, True))
    for j in range(f):
        females.append(Female(j, False))

    # Running algorithm

    # 1. Ranking
    [i.ranking(females) for i in males]
    [i.ranking(males) for i in females]

    # 2. Print Energy
    print(sum([females[i].energy(males, females) for i in range(len(females))]))
