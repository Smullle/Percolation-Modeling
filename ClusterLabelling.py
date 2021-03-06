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
    origin_val = lattice_object.get_lattice()[origin[0]][origin[1]]
    # check if point has been already found
    if origin_val == 0:
        n = pos_array[1]
        s = pos_array[2]
        w = pos_array[3]
        e = pos_array[4]

        n_val = lattice_object.get_lattice()[n[0]][n[1]]
        s_val = lattice_object.get_lattice()[s[0]][s[1]]
        w_val = lattice_object.get_lattice()[w[0]][w[1]]
        e_val = lattice_object.get_lattice()[e[0]][e[1]]

        # obtain neighbours that are not 0 or off edge of lattice
        neighbours = []
        neighbours_val = []
        if n_val != 0 and n_val != origin_val:
            neighbours.append(n)
            neighbours_val.append(n_val)
        if s_val != 0 and s_val != origin_val:
            neighbours.append(s)
            neighbours_val.append(s_val)
        if w_val != 0 and w_val != origin_val:
            neighbours.append(w)
            neighbours_val.append(w_val)
        if e_val != 0 and e_val != origin_val:
            neighbours.append(e)
            neighbours_val.append(e_val)

        neighbours = np.asarray(neighbours)

        number_of_neighbours = len(neighbours_val)

        # new cluster
        if number_of_neighbours == 0:
            lattice_object.update_cluster_count()
            assign_clusters(lattice_object, origin)

        # connect cluster to one neighbour
        elif number_of_neighbours == 1:
            connect_to_cluster(lattice_object, neighbours, origin)

        # bridge clusters
        elif number_of_neighbours >= 2:
            bridge_clusters(lattice_object, neighbours_val, origin)
        else:
            print("I should not be here, number of neighbours: ", number_of_neighbours)


def assign_clusters(lattice_object, loc):
    """
    Using a global variable storing cluster count, supplied with an input of a lattice and loc array
    the origin value will be assigned to a new cluster.
    """
    lattice_object.get_lattice()[loc[0]][loc[1]] = lattice_object.get_cluster_count()


def connect_to_cluster(lattice_object, loc, origin):
    """
    Takes lattice object, neighbour array and origin point, will combine origin to cluster
    """
    for neighbour in loc:
        # print(neighbour)
        # print(lattice_object.get_lattice()[neighbour[0]][neighbour[1]])
        if lattice_object.get_lattice()[neighbour[0]][neighbour[1]] != 0:
            lattice_object.get_lattice()[origin[0]][origin[1]] = \
                lattice_object.get_lattice()[neighbour[0]][neighbour[1]]


def bridge_clusters(lattice_object, loc, origin):
    """
    Takes lattice object neighbour values and origin, will find smallest value in neighbours and by looping through
    lattice will set any neighbouring clusters to match smallest valued cluster
    """
    smallest = loc[0]  # set smallest value to high
    for neighbour in loc:
        if neighbour <= smallest:
            smallest = neighbour

    lattice_object.get_lattice()[origin[0]][origin[1]] = smallest

    # overwrite lattice with smallest neighbor where point in lattice contains a neighbour
    for row in range(lattice_object.get_size()):
        for col in range(lattice_object.get_size()):
            for neighbour in loc:
                if lattice_object.get_lattice()[row][col] == neighbour:
                    lattice_object.get_lattice()[row][col] = smallest

    # lattice_object.reduce_cluster_count(len(loc))


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
        n[0] = row  # set to origin if neighbour off edge
    else:
        n[0] = row - 1

    s[1] = col
    if row + 1 >= size:
        s[0] = row  # set to origin if neighbour off edge
    else:
        s[0] = row + 1

    w[0] = row
    if col - 1 < 0:
        w[1] = col  # set to origin if neighbour off edge
    else:
        w[1] = col - 1

    e[0] = row
    if col + 1 >= size:
        e[1] = col  # set to origin if neighbour off edge
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

    common0 = np.intersect1d(north_side, south_side)
    common1 = np.intersect1d(common0, west_side)
    common = np.intersect1d(common1, east_side)

    # 0 will always be common on 4 sides at start
    if common.size == 1 and common[0] == 0:
        return False
    else:
        return True


def avg_pc(runs):
    """
    Given specified number of runs will calculate an average pc value on 50x50 lattice
    """
    pc = []

    for i in range(runs):
        lat10 = Lattice(50)

        while not common_cluster(lat10):
            pos1 = rand_pos(len(lat10.get_lattice()))
            search_neighbours(lat10, pos1)
            if lat10.filled():
                print("No spanning cluster found")
                break

        pc.append(lat10.perc_value())

    return sum(pc) / len(pc)


if __name__ == "__main__":

    # used for obtaining an average pc
    print("Average pc value: ", avg_pc(1000))

    # create lattice with specified size
    lattice = Lattice(10)

    error = False  # used if not span is found
    while not common_cluster(lattice):
        pos = rand_pos(len(lattice.get_lattice()))  # get random position
        search_neighbours(lattice, pos)  # pass neighbours to cluster assignment
        # precautionary measure
        if lattice.filled():
            print("Error: No spanning cluster found")
            error = True
            break

    # displaying of results
    if not error:
        print(lattice.get_lattice())
        print(lattice.perc_value())
        plt.imshow(lattice.get_lattice(), cmap="Greys",  vmax=1)
        plt.colorbar()
        plt.title("p = " + str(lattice.perc_value()))
        plt.show()
