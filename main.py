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

    def partner(self, candidate):
        # Check if is Active
        # If Active and has partner stop
        # Else send proposals
        self.my_partner = candidate

    def energy(self, other_group):
        self.my_energy = [i.id for i in other_group].index(self.my_partner.id)


class Male(Person):
    pass


class Female(Person):
    pass


if __name__ == '__main__':
    m, f = 1000, 1000
    males, females = [], []
    for i in range(m):
        males.append(Male(i, True))
    for j in range(f):
        females.append(Female(j, False))
