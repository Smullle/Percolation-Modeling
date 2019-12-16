"""
Example 7.4 first algorithm for labeling
"""
from Lattice import Lattice
import numpy as np
import matplotlib.pyplot as plt
import random


SEED = random.seed(a=None)  # seed used for testing (remove randomness)


# rules for labeling
def search_neighbours(lattice_object, pos_array):
    """
    Determine the number of neighbouring clusters and decide if assign cluster number, connect to another
    cluster or bridge multiple clusters.
    """
    origin = pos_array[0]
    # check if point has been already found
    # if array[origin[0]][origin[1]] == 0:
    n = pos_array[1]
    s = pos_array[2]
    w = pos_array[3]
    e = pos_array[4]

    n_val = lattice_object.get_lattice()[n[0]][n[1]]
    s_val = lattice_object.get_lattice()[s[0]][s[1]]
    w_val = lattice_object.get_lattice()[w[0]][w[1]]
    e_val = lattice_object.get_lattice()[e[0]][e[1]]

    # print("assigning..", origin)
    # print(n, s, w, e)
    # print(n_val, s_val, w_val, e_val)

    neighbours = []
    if n_val:
        neighbours.append(n)
    if s_val:
        neighbours.append(s)
    if w_val:
        neighbours.append(w)
    if e_val:
        neighbours.append(e)

    neighbours = np.asarray(neighbours)

    number_of_neighbours = np.count_nonzero(neighbours)

    # new cluster
    if number_of_neighbours == 0:
        lattice_object.update_cluster_count()
        assign_clusters(lattice_object, origin)

    # connect cluster to one neighbour
    elif number_of_neighbours == 1:
        connect_to_cluster(lattice_object, neighbours, origin)

    # bridge clusters
    elif number_of_neighbours >= 2:
        bridge_clusters(lattice_object, neighbours, origin)
    else:
        print("I should not be here, number of neighbours: ", number_of_neighbours)


def assign_clusters(lattice_object, loc):
    """
    Using a global variable storing cluster count, supplied with an input of a lattice and loc array
    the origin value will be assigned to a new cluster.
    """
    lattice_object.get_lattice()[loc[0]][loc[1]] = lattice_object.get_cluster_count()


def connect_to_cluster(lattice_object, loc, origin):
    for neighbour in loc:
        if neighbour[0] or neighbour[1]:
            lattice_object.get_lattice()[origin[0]][origin[1]] = lattice_object.get_lattice()[neighbour[0]][neighbour[1]]


def bridge_clusters(lattice_object, loc, origin):
    smallest = lattice_object.get_lattice()[loc[0][0]][loc[0][1]]
    for neighbour in loc[1:]:
        if lattice_object.get_lattice()[neighbour[0]][neighbour[1]] <= smallest:
            smallest = lattice_object.get_lattice()[neighbour[0]][neighbour[1]]

    lattice_object.get_lattice()[origin[0]][origin[1]] = smallest

    # overwrite lattice with smallest neighbor where point in lattice contains a neighbour
    for row in lattice_object.get_lattice():
        for element in row:
            if element == (lattice_object.get_lattice()[neighbour[0]][neighbour[1]] for neighbour in loc):
                lattice_object.get_lattice()[row, element] = smallest


# obtain random pos in lattice
def rand_pos(size):
    """
    Uses pseudo random number generator to obtain a point in the lattice, from this point the indexes of
    north, south, west and east are assigned and all 5 indexes returned as an array.
    """
    origin = np.empty(2)
    n, s, w, e = np.empty(2), np.empty(2), np.empty(2), np.empty(2)

    row = random.randint(0, size - 1)
    col = random.randint(0, size - 1)

    origin[0] = row
    origin[1] = col

    n[1] = col
    if row - 1 < 0:
        n[0] = row
    else:
        n[0] = row - 1

    s[1] = col
    if row + 1 >= size:
        s[0] = row
    else:
        s[0] = row + 1

    w[0] = row
    if col - 1 < 0:
        w[1] = col
    else:
        w[1] = col - 1

    e[0] = row
    if col + 1 >= size:
        e[1] = col
    else:
        e[1] = col + 1

    return np.array([origin.astype(int), n.astype(int), s.astype(int), w.astype(int), e.astype(int)])


def common_cluster(lattice_object):
    """
    Take square lattice as input and returns true if there is a common value in all 4 sides.
    """
    north_side = lattice_object.get_edges()[0]
    south_side = lattice_object.get_edges()[1]
    west_side = lattice_object.get_edges()[2]
    east_side = lattice_object.get_edges()[3]

    # TODO: edge matching not working

    common0 = np.intersect1d(north_side, south_side)
    common1 = np.intersect1d(common0, west_side)
    common = np.intersect1d(common1, east_side)

    if common.size >= 2:
        return True


if __name__ == "__main__":
    lattice = Lattice(10)

    while not common_cluster(lattice):
        pos = rand_pos(len(lattice.get_lattice()))
        search_neighbours(lattice, pos)

    print(lattice.get_lattice())
    plt.imshow(lattice.get_lattice())
    plt.show()
