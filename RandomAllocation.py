"""
Example 7.4 first algorithm for labeling
"""

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
import random

SEED = random.seed(1)
SIZE = 10


# rules for labeling
def search_neighbours(array, pos_array):
    origin = pos_array[0]
    n = pos_array[1]
    s = pos_array[2]
    w = pos_array[3]
    e = pos_array[4]

    n_val = array[np.split(n, 2)]
    s_val = array[np.split(s, 2)]
    w_val = array[np.split(w, 2)]
    e_val = array[np.split(e, 2)]

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
    if number_of_neighbours == 1:
        connect_to_cluster(array, neighbours, origin)

    # bridge clusters
    if number_of_neighbours == 2:
        bridge_clusters(array, neighbours, origin)


def assign_clusters(array, loc):
    count = cluster_count[0]
    array[np.split(loc, 2)] = count


def connect_to_cluster(array, loc, origin):
    for neighbour in loc:
        if neighbour[0] or neighbour[1]:
            array[np.split(origin, 2)] = array[np.split(neighbour, 2)]


def bridge_clusters(array, loc, origin):
    smallest = array[np.split(loc[0], 2)]
    for neighbour in loc[1:]:
        if array[np.split(neighbour, 2)] == smallest:
            array[np.split(origin, 2)] = array[np.split(neighbour, 2)]
        elif array[np.split(neighbour, 2)] < smallest:
            smallest = array[np.split(neighbour, 2)]

    # overwrite lattice with smallest neighbor where point in lattice contains a neighbour
    for row in array:
        for element in row:
            if element == (array[np.split(neighbour, 2)] for neighbour in loc):
                array[row, element] = array[np.split(neighbour, 2)]


# obtain random pos in lattice
def rand_pos():
    origin = np.empty(2)
    n, s, w, e = np.empty(2), np.empty(2), np.empty(2), np.empty(2)

    pos_x = random.randint(0, SIZE - 1)
    pos_y = random.randint(0, SIZE - 1)

    origin[0] = pos_x
    origin[1] = pos_y

    n[0] = pos_x
    if pos_y + 1 >= SIZE:
        n[1] = pos_y
    else:
        n[1] = pos_y + 1

    s[0] = pos_x
    if pos_y - 1 < 0:
        s[1] = pos_y
    else:
        s[1] = pos_y - 1

    if pos_x - 1 < 0:
        w[0] = pos_x
    else:
        w[0] = pos_x - 1
    w[1] = pos_y

    if pos_x + 1 >= SIZE:
        e[0] = pos_x
    else:
        e[0] = pos_x + 1
    e[1] = pos_x

    return np.array([origin.astype(int), n.astype(int), s.astype(int), w.astype(int), e.astype(int)])


def common_cluster(array):
    # TODO: check edges of 2d array for common cluster
    north_side = array[0]
    south_side = array[SIZE - 1]
    west_side = array[0]
    east_side = array[SIZE - 1]

    if (north_side == south_side == west_side == east_side) and north_side != 0:
        return True


if __name__ == "__main__":
    global cluster_count
    cluster_count = np.array([0])
    lattice = np.zeros((SIZE, SIZE))
    plt.imshow(lattice)

    while common_cluster(lattice) != True:
        pos = rand_pos()
        search_neighbours(lattice, pos)

    plt.imshow(lattice)
    plt.show()
