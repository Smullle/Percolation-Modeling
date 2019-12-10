"""
Example 7.4 first algorithm for labeling
"""

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
import random

SEED = random.seed(1)
SIZE = 50

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
        bridge_clusters(array, neighbours)
        # TODO: implement bridging


def assign_clusters(array, loc):
    count = cluster_count[0]
    array[np.split(loc, 2)] = count


def connect_to_cluster(array, loc, origin):
    for neighbour in loc:
        if neighbour[0] or neighbour[1]:
            array[np.split(origin, 2)] = array[np.split(neighbour, 2)]


def bridge_clusters(array, loc):
    return 0


# obtain random pos in lattice
def rand_pos():
    origin = np.empty(2)
    n, s, w, e = np.empty(2), np.empty(2), np.empty(2), np.empty(2)

    pos_x = random.randint(0, SIZE-1)
    pos_y = random.randint(0, SIZE-1)

    origin[0] = pos_x
    origin[1] = pos_y

    n[0] = pos_x
    if pos_y + 1 >= SIZE:
        n[1] = pos_y
    else:
        n[1] = pos_y + 1

    s[0] = pos_x
    if pos_y - 1 <= 0:
        s[1] = 0
    else:
        s[1] = pos_y - 1

    if pos_x - 1 <= 0:
        w[0] = 0
    else:
        w[0] = pos_x - 1
    w[1] = pos_y

    if pos_x + 1 >= SIZE:
        e[0] = 0
    else:
        e[0] = pos_x + 1
    e[1] = pos_x

    return np.array([origin.astype(int), n.astype(int), s.astype(int), w.astype(int), e.astype(int)])


if __name__ == "__main__":
    global cluster_count
    cluster_count = np.array([0])
    lattice = np.zeros((SIZE, SIZE))
    plt.imshow(lattice)

    for i in range(1000):
        pos = rand_pos()
        search_neighbours(lattice, pos)

    plt.imshow(lattice)
    plt.show()
