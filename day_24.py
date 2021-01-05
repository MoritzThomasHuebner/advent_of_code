import numpy as np
from collections import Counter
from scipy.signal import convolve


lines = []

with open('day_24_input.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        lines.append(line)


def parse_steps(steps):
    result = []
    while len(steps) > 0:
        if steps[0] in ['w', 'e']:
            result.append(steps[0])
            steps = steps[1:]
        else:
            result.append(steps[:2])
            steps = steps[2:]
    return result


def reduce_steps(steps):
    new_steps = []
    for step in steps:
        if step == 'nw':
            new_steps.extend(['w', 'ne'])
        elif step == 'se':
            new_steps.extend(['e', 'sw'])
        else:
            new_steps.append(step)

    counts = Counter(new_steps)
    result = []
    for i in range(np.abs(counts['e'] - counts['w'])):
        if counts['e'] > counts['w']:
            result.append('e')
        else:
            result.append('w')

    for i in range(np.abs(counts['sw'] - counts['ne'])):
        if counts['sw'] > counts['ne']:
            result.append('sw')
        else:
            result.append('ne')
    return result


flipped_tiles = []
for line in lines:
    parsed_steps = parse_steps(line)
    reduced_steps = reduce_steps(parsed_steps)
    flipped_tiles.append("".join(reduced_steps))

c = Counter(flipped_tiles)

total_flips = 0
flipped_tiles = []

for tile, flips in c.items():
    if flips % 2 == 1:
        total_flips += 1
        flipped_tiles.append(tile)

# Part 2

grid_size = 200
grid = np.zeros(shape=(grid_size, grid_size))

mid_x = 100
mid_y = 100


for tile in flipped_tiles:
    x = mid_x
    y = mid_y
    c = Counter(parse_steps(tile))
    x += c.get('e', 0)
    x -= c.get('w', 0)

    x += int(c.get('ne', 0) / 2)
    y -= c.get('ne', 0)

    x -= int((c.get('sw', 0) + 1) / 2)
    y += c.get('sw', 0)
    grid[y][x] = 1

print(flipped_tiles)

kernel_odd = np.array([[1, 1, 0], [1, 0, 1], [1, 1, 0]])
kernel_even = np.array([[0, 1, 1], [1, 0, 1], [0, 1, 1]])
for day in range(100):
    convolved_grid_even = np.rint(convolve(grid, kernel_even, mode='same'))
    convolved_grid_odd = np.rint(convolve(grid, kernel_odd, mode='same'))
    final_grid = np.zeros(shape=(grid_size, grid_size))

    for y in range(grid_size):
        for x in range(grid_size):
            if y % 2 == 0:
                convolved_grid = convolved_grid_even
            else:
                convolved_grid = convolved_grid_odd

            if grid[y][x] == 1 and (convolved_grid[y][x] == 0 or convolved_grid[y][x] > 2):
                final_grid[y][x] = 0
            elif grid[y][x] == 0 and convolved_grid[y][x] == 2:
                final_grid[y][x] = 1
            else:
                final_grid[y][x] = grid[y][x]
    grid = final_grid

    print(int(np.sum(final_grid)))
