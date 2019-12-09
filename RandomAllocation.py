"""
Example 7.4 first algorithim for labeling
"""

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import random

SEED = random.seed(a = None)

# rules for labeling

def search_neighbours():
    return 0

def assign_clusters():
    return 0

def bridge_clusters(lattice):
    return 0

# obtain random pos in lattice

def rand_pos(lattice):
    pos = np.empty(2)
    N, S, W, E = np.empty(2), np.empty(2), np.empty(2), np.empty(2)
    
    pos_x = random.randint(0, 50)
    pos_y = random.randint(0, 50)
    
    pos[0] = pos_x
    pos[1] = pos_y
    
    N[0] = pos_x
    N[1] = pos_y + 1
    
    S[0] = pos_x
    S[1] = pos_y - 1
    
    W[0] = pos_x - 1
    W[1] = pos_y
    
    E[0] = pos_x + 1
    E[1] = pos_x
    
    return [pos, N, S, W, E]

if __name__ == "__main__":
    lattice = np.zeros((50, 50))
    print(rand_pos(lattice))
    plt.imshow(lattice)
    