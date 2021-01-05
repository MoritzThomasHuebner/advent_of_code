from itertools import cycle
import numpy as np
from copy import deepcopy



def shuffle(cups, n_steps=100):
    n_cups = len(cups)
    current_cup_index = 0
    current_cup = cups[current_cup_index]
    for i in range(n_steps):

        if current_cup_index + 4 > len(cups):
            removed_cups = cups[current_cup_index + 1:]
            removed_cups.extend(cups[:current_cup_index + 4 - len(cups)])
        else:
            removed_cups = cups[current_cup_index + 1:current_cup_index + 4]

        for rc in removed_cups:
            cups.remove(rc)

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

        for index in range(current_cup_index - 5, current_cup_index + 5):
            index += n_cups
            index %= n_cups
            if cups[index] == current_cup:
                current_cup_index = index
                break
    return cups


cups = [int(c) for c in list("853192647")]
cups = shuffle(cups, 100)
result = "".join([str(c) for c in cups]).split('1')
result = result[1] + result[0]
print(result)

# Part 2


class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def shuffle_part_2(cups, n_steps=100):
    n_cups = len(cups)

    nodes = {}
    for c in range(1, len(cups) + 1):
        nodes[c] = Node(c)

    shifted_cups = cups[1:] + cups[:1]
    for x, y in zip(cups, shifted_cups):
        nodes[x].next = nodes[y]

    head = nodes[cups[0]]
    current_cup = nodes[cups[0]]
    removed_cups_vals = [current_cup.next.val, current_cup.next.next.val, current_cup.next.next.next.val]
    next_cup = current_cup.next.next.next.next

    destination_label = current_cup.val - 1
    while True:
        if destination_label < 1:
            destination_label += n_cups
        if destination_label not in [removed_cups_vals]:
            break

    for k, n in nodes.items():
        if n.val == destination_label:
            destination_key = k
            break
    current_cup.next = nodes[destination_key]

    destination_key = nodes.index(destination_label)

    current_cup.next.next.next.next = nodes[destination_key].next
    nodes[destination_key].next = current_cup.next


    for key, node in nodes.items():
        print(key)
        print(node.val)
        print(node.next.val)
        print()

    # n_cups = len(cups)
    # current_cup_index = 0
    # current_cup = cups[current_cup_index]
    # for i in range(n_steps):
    #
    #     if current_cup_index + 4 > len(cups):
    #         removed_cups = cups[current_cup_index + 1:]
    #         removed_cups.extend(cups[:current_cup_index + 4 - len(cups)])
    #     else:
    #         removed_cups = cups[current_cup_index + 1:current_cup_index + 4]
    #
    #     for rc in removed_cups:
    #         cups.remove(rc)
    #
    #     destination_label = current_cup - 1
    #     while True:
    #         if destination_label < 1:
    #             destination_label += n_cups
    #         if destination_label in cups:
    #             break
    #         destination_label -= 1
    #
    #     destination_index = cups.index(destination_label)
    #
    #     for rc in deepcopy(removed_cups)[::-1]:
    #         cups.insert(destination_index + 1, rc)
    #
    #     current_cup = cups[(cups.index(current_cup) + 1) % len(cups)]
    #
    #     for index in range(current_cup_index - 5, current_cup_index + 5):
    #         index += n_cups
    #         index %= n_cups
    #         if cups[index] == current_cup:
    #             current_cup_index = index
    #             break
    #     if i % 1000 == 0:
    #         print(i)

    return cups



# cups = [int(c) for c in list("853192647")] + list(range(10, 10000001))
cups = [int(c) for c in list("853192647")]

cups = shuffle_part_2(cups, 10000000)

idx = cups.index(1)
print(cups[idx+1])
print(cups[idx+2])
print(cups[idx+1] * cups[idx+2])
