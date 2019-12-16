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

    def get_lattice(self):
        return self.lattice

    def get_cluster_count(self):
        return self.cluster_count

    def update_cluster_count(self):
        self.cluster_count += 1

    def get_edges(self):
        self.north_side = self.lattice[0]
        self.south_side = self.lattice[self.size - 1]
        for i in range(self.size):
            self.west_side[i] = self.lattice[i][0]
        for i in range(self.size):
            self.east_side[i] = self.lattice[i][self.size - 1]

        return [self.north_side, self.south_side, self.west_side, self. east_side]
