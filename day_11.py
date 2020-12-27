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


# for i in range(100):
#     data = flip_seats(data)
#     occupied = len(np.where(np.array(data) == '#')[0])
#     print(occupied)

# Part two



from collections import namedtuple

Coordinate = namedtuple('Coordinate', ['x', 'y'])


def check_vertical_direction_down(x, y, y_max, data):
    ys = get_down_or_right_direction(y, y_max)
    xs = np.array([x]*len(ys))
    return check_direction(xs, ys, data=data)


def check_vertical_direction_up(x, y, data):
    ys = get_up_or_left_direction(y)
    xs = np.array([x]*len(ys))
    return check_direction(xs, ys, data=data)


def check_horizontal_direction_right(x, y, x_max, data):
    xs = get_down_or_right_direction(x, x_max)
    ys = np.array([y] * len(xs))
    return check_direction(xs, ys, data=data)


def check_horizontal_direction_left(x, y, data):
    xs = get_up_or_left_direction(x)
    ys = np.array([y] * len(xs))
    return check_direction(xs, ys, data=data)


def check_diagonal_direction_down_right(x, y, x_max, y_max, data):
    xs = get_down_or_right_direction(x, x_max)
    ys = get_down_or_right_direction(y, y_max)
    return check_direction(xs, ys, data=data)


def check_diagonal_direction_down_left(x, y, y_max, data):
    xs = get_up_or_left_direction(x)
    ys = get_down_or_right_direction(y, y_max)
    return check_direction(xs, ys, data=data)


def check_diagonal_direction_top_left(x, y, data):
    xs = get_up_or_left_direction(x)
    ys = get_up_or_left_direction(y)
    return check_direction(xs, ys, data=data)


def check_diagonal_direction_top_right(x, y, x_max, data):
    xs = get_down_or_right_direction(x, x_max)
    ys = get_up_or_left_direction(y)
    return check_direction(xs, ys, data=data)


def get_down_or_right_direction(input, limit):
    return np.arange(input + 1, limit)


def get_up_or_left_direction(input):
    return np.arange(input)[::-1]


def check_direction(xs, ys, data):
    coordinates = [Coordinate(x=i, y=j) for i, j in zip(xs, ys)]
    for coordinate in coordinates:
        x = coordinate[0]
        y = coordinate[1]
        if data[x][y] == 'L':
            return 0
        elif data[x][y] == '#':
            return 1
    return 0


def check_all_directions(x, y, x_max, y_max, data):
    counter = 0
    counter += check_vertical_direction_down(x=x, y=y, y_max=y_max, data=data)
    counter += check_vertical_direction_up(x, y, data)
    counter += check_horizontal_direction_right(x, y, x_max, data)
    counter += check_horizontal_direction_left(x, y, data)
    counter += check_diagonal_direction_down_right(x, y, x_max, y_max, data)
    counter += check_diagonal_direction_down_left(x, y, y_max, data)
    counter += check_diagonal_direction_top_left(x, y, data)
    counter += check_diagonal_direction_top_right(x, y, x_max, data)
    return counter

def flip_seats_part_2(data):
    new_data = deepcopy(data)
    for x, row in enumerate(data):
        for y in range(len(row)):
            if data[x][y] == '.':
                continue
            n_adjacent = check_all_directions(x=x, y=y, x_max=len(data), y_max=len(row), data=data)
            if n_adjacent == 0:
                new_data[x][y] = '#'
            elif n_adjacent >= 5:
                new_data[x][y] = 'L'
    return new_data

for i in range(1000):
    data = flip_seats_part_2(data)
    occupied = len(np.where(np.array(data) == '#')[0])
    print(occupied)