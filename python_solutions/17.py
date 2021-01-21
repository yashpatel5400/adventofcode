import numpy as np

with open("input_17.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
init_dim = len(lines[0])
grid = np.zeros([init_dim, init_dim, 1, 1])

for i in range(init_dim):
    for j in range(init_dim):
        grid[i, j, 0, 0] = lines[i][j] == '#'


for step in range(6):
    old_shape = grid.shape
    new_shape = [old + 2 for old in old_shape]
    new_grid = np.zeros(new_shape)
    
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            for k in range(new_shape[2]):
                for l in range(new_shape[3]):
                
                    # check +/- 1
                    cur_val = 0
                    active_neighbors = 0
                    for delta_i in range(-1, 2):
                        for delta_j in range(-1, 2):
                            for delta_k in range(-1, 2):
                                for delta_l in range(-1, 2):
                                    pos = [
                                        i + delta_i - 1,
                                        j + delta_j - 1,
                                        k + delta_k - 1,
                                        l + delta_l - 1,
                                    ]

                                    if pos[0] < 0 or pos[0] >= grid.shape[0] or\
                                       pos[1] < 0 or pos[1] >= grid.shape[1] or\
                                       pos[2] < 0 or pos[2] >= grid.shape[2] or\
                                       pos[3] < 0 or pos[3] >= grid.shape[3]:
                                        active = False
                                    else:
                                        active = grid[pos[0], pos[1], pos[2], pos[3]] == 1

                                    if delta_i == 0 and delta_j == 0 and delta_k == 0 and delta_l == 0:
                                        cur_val = active
                                    else:
                                        active_neighbors += int(active)
                    
                    if cur_val == 1:
                        new_grid[i,j,k,l] = int(active_neighbors == 2 or active_neighbors == 3)
                    else:
                        new_grid[i,j,k,l] = int(active_neighbors == 3)
    grid = new_grid
    print(np.sum(new_grid))