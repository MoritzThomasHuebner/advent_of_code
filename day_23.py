from itertools import cycle
import numpy as np
from copy import deepcopy


def shuffle(cups, n_steps=100):

    current_cup = cups[0]
    n_cups = len(cups)

    for i in range(n_steps):

        current_cup_index = np.where(np.array(cups) == current_cup)[0][0]
        if current_cup_index + 4 > len(cups):
            removed_cups = cups[current_cup_index + 1:]
            removed_cups.extend(cups[:current_cup_index + 4 - len(cups)])
        else:
            removed_cups = cups[current_cup_index + 1:current_cup_index + 4]

        cups = [c for c in cups if c not in removed_cups]

        destination_label = current_cup - 1
        while True:
            if destination_label < 1:
                destination_label += n_cups
            if destination_label in cups:
                break
            destination_label -= 1

        destination_index = cups.index(destination_label)

        for rc in deepcopy(removed_cups)[::-1]:
            cups.insert(destination_index + 1, rc)

        current_cup = cups[(cups.index(current_cup) + 1) % len(cups)]
        print(i)
    return cups

# Part 1

# cups = [int(c) for c in list("389125467")]
# positions = [np.where(np.array(cups) == i)[0][0] for i in range(1, 10)]

cups = [int(c) for c in list("853192647")]
cups = shuffle(cups, 100)
result = "".join([str(c) for c in cups]).split('1')
result = result[1] + result[0]
print(result)


for i in range(10, 10000001):
    cups.append(i)

# print(len(cups))
# cups = shuffle(cups, 10)
