"""
Example 7.4 first algorithm for labeling
"""

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
import random

SEED = random.seed(a=None)  # seed used for testing (remove randomness)
SIZE = 20  # constant size of the lattice


# rules for labeling
def search_neighbours(array, pos_array):
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

    n_val = array[n[0]][n[1]]
    s_val = array[s[0]][s[1]]
    w_val = array[w[0]][w[1]]
    e_val = array[e[0]][e[1]]

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
        cluster_count[0] += 1
        assign_clusters(array, origin)

    # connect cluster to one neighbour
    elif number_of_neighbours == 1:
        connect_to_cluster(array, neighbours, origin)

    # bridge clusters
    elif number_of_neighbours >= 2:
        bridge_clusters(array, neighbours, origin)
    else:
        print("I should not be here, number of neighbours: ", number_of_neighbours)


def assign_clusters(array, loc):
    """
    Using a global variable storing cluster count, supplied with an input of a lattice and loc array
    the origin value will be assigned to a new cluster.
    """
    count = cluster_count[0]
    array[loc[0]][loc[1]] = count


def connect_to_cluster(array, loc, origin):
    for neighbour in loc:
        if neighbour[0] or neighbour[1]:
            array[origin[0]][origin[1]] = array[neighbour[0]][neighbour[1]]


def bridge_clusters(array, loc, origin):
    smallest = array[loc[0][0]][loc[0][1]]
    for neighbour in loc[1:]:
        if array[neighbour[0]][neighbour[1]] <= smallest:
            smallest = array[neighbour[0]][neighbour[1]]

    array[origin[0]][origin[1]] = smallest

    # overwrite lattice with smallest neighbor where point in lattice contains a neighbour
    for row in array:
        for element in row:
            if element == (array[neighbour[0]][neighbour[1]] for neighbour in loc):
                array[row, element] = smallest


# obtain random pos in lattice
def rand_pos():
    """
    Uses pseudo random number generator to obtain a point in the lattice, from this point the indexes of
    north, south, west and east are assigned and all 5 indexes returned as an array.
    """
    origin = np.empty(2)
    n, s, w, e = np.empty(2), np.empty(2), np.empty(2), np.empty(2)

    row = random.randint(0, SIZE - 1)
    col = random.randint(0, SIZE - 1)

    origin[0] = row
    origin[1] = col

    n[1] = col
    if row - 1 < 0:
        n[0] = row
    else:
        n[0] = row - 1

    s[1] = col
    if row + 1 >= SIZE:
        s[0] = row
    else:
        s[0] = row + 1

    w[0] = row
    if col - 1 < 0:
        w[1] = col
    else:
        w[1] = col - 1

    e[0] = row
    if col + 1 >= SIZE:
        e[1] = col
    else:
        e[1] = col + 1

    return np.array([origin.astype(int), n.astype(int), s.astype(int), w.astype(int), e.astype(int)])


def common_cluster(array):
    """
    Take square lattice as input and returns true if there is a common value in all 4 sides.
    """
    north_side = array[0]
    south_side = array[SIZE - 1]
    west_side = array[0]
    east_side = array[SIZE - 1]

    common0 = np.intersect1d(north_side, south_side)
    common1 = np.intersect1d(common0, west_side)
    common = np.intersect1d(common1, east_side)

    if common.size == 2:
        return True


if __name__ == "__main__":
    global cluster_count
    cluster_count = np.array([0])
    lattice = np.zeros((SIZE, SIZE))
    lattice = lattice.astype(int)
    # plt.imshow(lattice)

    while not common_cluster(lattice):
        pos = rand_pos()
        search_neighbours(lattice, pos)
        # print(lattice)

    # for i in range(100):
    #     pos = rand_pos()
    #     search_neighbours(lattice, pos)

    print(lattice)
    plt.imshow(lattice)
    plt.show()
