"""
Example 7.4 first algorithim for labeling
"""

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
import random

SEED = random.seed(1)

# rules for labeling


def search_neighbours(array, pos_array):
    print(pos_array)
    origin = pos_array[0]
    n = pos_array[1]
    s = pos_array[2]
    w = pos_array[3]
    e = pos_array[4]
    # 0 is falsy
    if not (array[np.split(n, 2)] and array[np.split(s, 2)] and array[np.split(w, 2)] and array[np.split(e, 2)]):
        # TODO add cluster count
        assign_clusters(origin)

    if array[np.split(n, 2)] and not (array[np.split(s, 2)] and array[np.split(w, 2)] and array[np.split(e, 2)]):
        # TODO add cluster count
        assign_clusters(origin)

    elif array[np.split(n, 2)] and not (array[np.split(s, 2)] and array[np.split(w, 2)] and array[np.split(e, 2)]):
        # TODO add custer number
        assign_clusters(origin)

    elif not array[np.split(n, 2)] and array[np.split(s, 2)] and not (array[np.split(w, 2)] and array[np.split(e, 2)]):
        # TODO add custer number
        assign_clusters(origin)

    elif not (array[np.split(n, 2)] and array[np.split(s, 2)] and array[np.split(w, 2)]) and not array[np.split(e, 2)]:
        # TODO add custer number
        assign_clusters(origin)

    return 0


def assign_clusters(array, loc):
    return 0


def bridge_clusters(array, loc):
    return 0

# obtain random pos in lattice


def rand_pos():
    origin = np.empty(2)
    n, s, w, e = np.empty(2), np.empty(2), np.empty(2), np.empty(2)

    pos_x = random.randint(0, 50)
    pos_y = random.randint(0, 50)
    
    origin[0] = pos_x
    origin[1] = pos_y
    
    n[0] = pos_x
    n[1] = pos_y + 1
    
    s[0] = pos_x
    s[1] = pos_y - 1
    
    w[0] = pos_x - 1
    w[1] = pos_y
    
    e[0] = pos_x + 1
    e[1] = pos_x
    
    return np.array([origin.astype(int), n.astype(int), s.astype(int), w.astype(int), e.astype(int)])


if __name__ == "__main__":
    lattice = np.zeros((50, 50))
    lattice[8][37] = 1
    plt.imshow(lattice)

    pos = rand_pos()
    print(pos)
    neighbour_clusters = search_neighbours(lattice, pos)
