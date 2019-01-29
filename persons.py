import numpy as np


class Person:

    def __init__(self, name, active):
        self.id = name
        self.j = 0
        self.my_ranking = None
        self.my_partner = None
        self.my_energy = None
        self.status = active
        self.messaged = False

    def ranking(self, other_group):
        group = other_group.copy()
        np.random.shuffle(group)
        self.my_ranking = group

    def match(self, candidate):
        self.my_partner = candidate

    def divorce(self):
        self.my_partner = None

    def send_msg(self):
        if self.status == True:
            if self.my_partner == None:
                for i in range(self.j, len(self.my_ranking)):
                    result = self.my_ranking[self.j].receive_msg(self)
                    self.j += 1
                    if self.j == len(self.my_ranking):
                        self.messaged = True
                    if result == '+':
                        break

    def receive_msg(self, candidate):
        if self.my_partner is None:
            self.match(candidate)
            candidate.match(self)
            return '+'
        elif [i.id for i in self.my_ranking].index(candidate.id) < \
                [i.id for i in self.my_ranking].index(self.my_partner.id):
            self.my_partner.divorce()
            self.match(candidate)
            candidate.match(self)
            return '+'
        else:
            return '-'

    def energy(self):
        if self.my_partner is not None:
            self.my_energy = [i.id for i in self.my_ranking].index(self.my_partner.id) + 1
            return self.my_energy
        else:
            self.my_energy = len(self.my_ranking) + 1
            return self.my_energy


class Male(Person):
    pass


class Female(Person):
    pass
