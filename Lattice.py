import numpy as np


class Lattice:

    cluster_count = 0

    def __init__(self, size):
        self.size = size
        self.lattice = np.zeros((size, size))

    def get_lattice(self):
        return self.lattice

    def get_cluster_count(self):
        return self.cluster_count

    def update_cluster_count(self):
        self.cluster_count += 1
