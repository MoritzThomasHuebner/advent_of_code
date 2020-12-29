import numpy as np
import itertools
from copy import deepcopy

data = []

with open('day_17_input.txt', 'r') as f:
    for i in f.readlines():
        data.append(list(i.strip('\n')))

expanded_data_space = np.zeros((22, 22, 22))

for i in range(8, 8 + len(data)):
    for j in range(8, 8 + len(data)):
        val = 0 if data[i - 8][j - 8] == '.' else 1
        expanded_data_space[i][j][11] = val


def get_mask(x, y, z, grid):
    max_length = len(grid)
    xs = [i for i in range(np.maximum(x - 1, 0), np.minimum(x + 2, max_length))]
    ys = [i for i in range(np.maximum(y - 1, 0), np.minimum(y + 2, max_length))]
    zs = [i for i in range(np.maximum(z - 1, 0), np.minimum(z + 2, max_length))]
    return itertools.product(xs, ys, zs)


def count_adjecents(x, y, z, grid):
    mask = get_mask(x, y, z, grid)
    return np.sum([grid[xm][ym][zm] for xm, ym, zm in mask])


def step(grid):
    new_grid = deepcopy(grid)
    xs = [i for i in range(0, len(grid))]
    coords = itertools.product(xs, xs, xs)
    for coord in coords:
        adjecents = count_adjecents(x=coord[0], y=coord[1], z=coord[2], grid=grid)
        active = grid[coord[0], coord[1], coord[2]]
        if active == 1 and (adjecents not in [3, 4]):
            new_grid[coord[0], coord[1], coord[2]] = 0
        elif active == 0 and adjecents == 3:
            new_grid[coord[0], coord[1], coord[2]] = 1
    return new_grid


for i in range(6):
    expanded_data_space = step(expanded_data_space)
    print(np.sum(expanded_data_space))


# Part 2


expanded_data_space = np.zeros((22, 22, 22, 22))


for i in range(8, 8 + len(data)):
    for j in range(8, 8 + len(data)):
        val = 0 if data[i - 8][j - 8] == '.' else 1
        expanded_data_space[i][j][11][11] = val


def get_mask_part_2(x, y, z, w, grid):
    max_length = len(grid)
    xs = [i for i in range(np.maximum(x - 1, 0), np.minimum(x + 2, max_length))]
    ys = [i for i in range(np.maximum(y - 1, 0), np.minimum(y + 2, max_length))]
    zs = [i for i in range(np.maximum(z - 1, 0), np.minimum(z + 2, max_length))]
    ws = [i for i in range(np.maximum(w - 1, 0), np.minimum(w + 2, max_length))]
    return itertools.product(xs, ys, zs, ws)


def count_adjecents_part_2(x, y, z, w, grid):
    mask = get_mask_part_2(x, y, z, w, grid)
    return np.sum([grid[xm][ym][zm][wm] for xm, ym, zm, wm in mask])


def step(grid):
    new_grid = deepcopy(grid)
    xs = [i for i in range(0, len(grid))]
    coords = itertools.product(xs, xs, xs, xs)
    for coord in coords:
        adjecents = count_adjecents_part_2(x=coord[0], y=coord[1], z=coord[2], w=coord[3], grid=grid)
        active = grid[coord[0], coord[1], coord[2], coord[3]]
        if active == 1 and (adjecents not in [3, 4]):
            new_grid[coord[0], coord[1], coord[2], coord[3]] = 0
        elif active == 0 and adjecents == 3:
            new_grid[coord[0], coord[1], coord[2], coord[3]] = 1
    return new_grid


for i in range(6):
    expanded_data_space = step(expanded_data_space)
    print(np.sum(expanded_data_space))
