import numpy as np
from copy import deepcopy

data = []
with open('day_11_input.txt', 'r') as f:
    for line in f.readlines():
        line = list(line.strip('\n'))
        data.append(line)


def get_mask(x, y, x_max, y_max):
    mask = np.zeros(shape=(x_max, y_max), dtype=int)
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if not 0 <= i < x_max or not 0 <= j < y_max or (x == i and y == j):
                continue
            mask[i, j] = 1
    return mask


def flip_seats(data):
    new_data = deepcopy(data)
    for x, row in enumerate(data):
        for y in range(len(row)):
            if data[x][y] == '.':
                continue
            mask = get_mask(x=x, y=y, x_max=len(data), y_max=len(row))
            adjacent = np.where(mask == 1)
            n_occupied = 0
            for i, j in zip(adjacent[0], adjacent[1]):
                if data[i][j] == '#':
                    n_occupied += 1
            if n_occupied == 0:
                new_data[x][y] = '#'
            elif n_occupied >= 4:
                new_data[x][y] = 'L'
    return new_data


for i in range(100):
    data = flip_seats(data)
    occupied = len(np.where(np.array(data) == '#')[0])
    print(occupied)