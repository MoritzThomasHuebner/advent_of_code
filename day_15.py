from copy import deepcopy
import numpy as np


input = [14, 8, 16, 0, 1, 17]

for i in range(2020 - len(input)):
    age = 0
    if input[-1] in input[:-1]:
        age = len(input) - 1 - np.where(np.array(input[:-1]) == np.array(input[-1]))[0][-1]
    input.append(age)
print(input[-1])

# Part 2


input = [14, 8, 16, 0, 1, 17]
n_steps = 30000000 - 1

least_recent_number = input[-1]
numbers_pos = {i: position for position, i in enumerate(input[:-1])}

for current_pos in range(len(input) - 1, n_steps):
    if least_recent_number in numbers_pos:
        current_number = current_pos - numbers_pos[least_recent_number]
    else:
        current_number = 0
    numbers_pos[least_recent_number] = current_pos
    least_recent_number = current_number
    if current_pos % 1000 == 0:
        print(current_pos)
print(least_recent_number)

