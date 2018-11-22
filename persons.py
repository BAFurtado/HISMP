import numpy as np


class Person:

    def __init__(self, name, active):
        self.id = name
        self.my_ranking = None
        self.my_partner = None
        self.my_energy = None
        self.status = active

    def ranking(self, other_group):
        group = other_group.copy()
        np.random.shuffle(group)
        self.my_ranking = group

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