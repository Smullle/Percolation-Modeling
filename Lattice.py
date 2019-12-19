import numpy as np


class Lattice:

    cluster_count = 0

    def __init__(self, size):
        self.size = size
        self.lattice = np.zeros((size, size))
        self.lattice = self.lattice.astype(int)
        self.north_side = np.empty(self.size)
        self.south_side = np.empty(self.size)
        self.west_side = np.empty(self.size)
        self.east_side = np.empty(self.size)

    def get_size(self):
        return self.size

    def get_lattice(self):
        return self.lattice

    def get_cluster_count(self):
        return self.cluster_count

    def update_cluster_count(self):
        self.cluster_count += 1

    def reduce_cluster_count(self, amount):
        self.cluster_count -= amount

    def get_edges(self):
        self.north_side = self.lattice[0]
        self.south_side = self.lattice[self.size - 1]
        for i in range(self.size):
            self.west_side[i] = self.lattice[i][0]
        for i in range(self.size):
            self.east_side[i] = self.lattice[i][self.size - 1]

        return [self.north_side, self.south_side, self.west_side, self. east_side]

    def set_lattice(self, array2d):
        self.lattice = np.copy(array2d)

    def filled(self):
        zero_count = 0
        for row in self.lattice:
            for element in row:
                if element == 0:
                    zero_count += 1
        if zero_count == 0:
            return True
        else:
            return False

    def perc_value(self):
        zero_count = 0
        for row in self.lattice:
            for element in row:
                if element != 0:
                    zero_count += 1
        return zero_count / (self.size * self.size)
