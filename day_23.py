from itertools import cycle
import numpy as np

cups = list("853192647")
reverse_sorted_labels = [str(b) for b in sorted([int(c) for c in cups])[::-1]]

current_cup = cups[0]
print(cups)
for i in range(100):

    cup_cycle = cycle(cups)
    label_cycle = cycle(reverse_sorted_labels)

    while True:
        if current_cup == next(cup_cycle):
            removed_cups = [next(cup_cycle) for _ in range(3)]
            break

    cups = [c for c in cups if c not in removed_cups]

    destination_label_found = False
    destination = int(current_cup) - 1 if not int(current_cup) - 1 == 0 else 9

    while True:
        destination_label = next(label_cycle)
        if int(destination_label) == destination:
            while True:
                if destination_label in cups:
                    destination_label_found = True
                    break
                destination_label = next(label_cycle)
        if destination_label_found:
            break
    destination_index = cups.index(destination_label)
    cups.insert(destination_index + 1, removed_cups)
    cups = [item for sublist in cups for item in sublist]
    current_cup = cups[(cups.index(current_cup) + 1) % len(cups)]
print(cups)

print("".join(cups))