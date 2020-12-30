import numpy as np
from collections import OrderedDict
from copy import deepcopy

tiles = OrderedDict(dict())
tile_id = 0

with open('day_20_input.txt', 'r') as f:
    for i in f.readlines():
        if i == '\n':
            continue
        elif i.startswith('Tile'):
            tile_id = i[5:-2]
            tiles[tile_id] = []
        else:
            tiles[tile_id].append(i.strip('\n'))


class Tile(object):

    def __init__(self, lines, key=None, adjacents=None):
        if adjacents is None:
            self.adjacents = dict()
        else:
            self.adjacents = adjacents
        self.key = key
        new_lines = []
        for l in lines:
            new_lines.append(list(l))
        self.lines = np.array(new_lines)

    @property
    def top(self):
        return self.lines[0]

    @property
    def bottom(self):
        return self.lines[-1]

    @property
    def left(self):
        return self.lines[:, 0]

    @property
    def right(self):
        return self.lines[:, -1]

    def left_rotate(self):
        self.lines = np.rot90(self.lines)

    @property
    def flipped(self):
        return Tile(np.flip(self.lines, axis=0), key=self.key, adjacents=self.adjacents)


class TileGrid(object):

    def __init__(self, n):
        self.coordinates = [[] for _ in range(n)]

    def swap(self, x1, y1, x2, y2):
        h = self.coordinates[x1][y1]
        self.coordinates[x1][y1] = self.coordinates[x2][y2]
        self.coordinates[x2][y2] = h


for k, t in tiles.items():
    tiles[k] = Tile(t, k)

SIDES = ['top', 'left', 'bottom', 'right']
SHIFTED_SIDES = ['bottom', 'right', 'top', 'left']
def check_match(tile_1, tile_2):
    for b, c in zip(SIDES, SHIFTED_SIDES):
        for i in range(4):

            if np.array_equal(getattr(tile_1, b), getattr(tile_2, c)):
                return True, b, i, False
            elif np.array_equal(getattr(tile_1, b), getattr(tile_2.flipped, c)):
                return True, b, i, True
            tile_2.left_rotate()

    return False, None, None, False


def get_rotation_difference(side_1, side_2):
    side_1_index = SIDES.index(side_1)
    side_2_index = SIDES.index(side_2)
    return np.abs(side_2_index - side_1_index)

def get_number_of_required_left_rotations(side_1, side_2):
    rotation_difference = get_rotation_difference(side_1, side_2)
    side_2_index = SIDES.index(side_2)
    required_rotations = 0
    while rotation_difference != 2:
        required_rotations += 1
        side_2_index += 1
        side_2_index %= 4
        side_2 = SIDES[side_2_index]
        rotation_difference = get_rotation_difference(side_1, side_2)
    return required_rotations



initial_key = list(tiles.keys())[0]
initial_tile = tiles[initial_key]
arranged_tiles = {initial_key: initial_tile}
finalised_keys = []


def get_opposite_side(side):
    return SHIFTED_SIDES[SIDES.index(side)]

for _ in range(20):
    for key, arranged_tile in deepcopy(arranged_tiles).items():
        if key in finalised_keys:
            continue
        if key == '2473':
            print()
        for k_2, t_2 in tiles.items():
            if key == k_2:
                continue
            if k_2 in list(arranged_tile.adjacents.values()):
                continue
            match, t_1_side, t_2_rots, flipped = check_match(arranged_tile, t_2)
            if match:
                arranged_tiles[key].adjacents[t_1_side] = k_2
                for _ in range(t_2_rots):
                    t_2.left_rotate()
                if flipped:
                    t_2 = t_2.flipped
                t_2.adjacents[get_opposite_side(t_1_side)] = key
                arranged_tiles[k_2] = t_2
                # tiles[k_2] = t_2
        finalised_keys.append(key)


prod = 1
for k, t in arranged_tiles.items():
    print(k)
    print(t.adjacents)
    if len(t.adjacents) == 2:
        prod *= int(k)
print(prod)


for k, t in arranged_tiles.items():
    if sorted(list(t.adjacents.keys())) == sorted(['bottom', 'right']):
        starting_tile = t
        starting_key = k

n = int(np.sqrt(len(arranged_tiles)))
tile_grid = []
tile_grid_keys = []
for y in range(n):
    if y == 0:
        line = [starting_tile]
        line_keys = [starting_tile.key]
    else:
        line = [arranged_tiles[tile_grid[y - 1][0].adjacents['bottom']]]
        line_keys = [arranged_tiles[tile_grid[y - 1][0].adjacents['bottom']].key]
    for x in range(1, n):
        try:
            line.append(arranged_tiles[line[x - 1].adjacents['right']])
            line_keys.append(arranged_tiles[line[x - 1].adjacents['right']].key)
        except KeyError:
            pass
    tile_grid.append(line)
    tile_grid_keys.append(line_keys)

for row in tile_grid:
    for column in row:
        print(column.key)
    print()
print(tile_grid)




