import numpy as np

data = np.loadtxt('day_09_input.txt', dtype=np.int64)


def check_allowed(numbers, total, n_combined=2):
    if n_combined == 1:
        return total in numbers
    else:
        for i, number in enumerate(numbers):
            reduced_numbers = np.delete(numbers, i)
            if check_allowed(reduced_numbers, total-number, n_combined-1):
                return True
        return False

# Part 1

n_preamble = 25
weakness_number = -1
for i in range(n_preamble, len(data)):
    current_value = data[i]
    current_data = data[i - n_preamble:i]
    if not check_allowed(numbers=current_data, total=current_value, n_combined=2):
        weakness_number = current_value
print(weakness_number)

# Part 2


def find_weakness(weakness_number):
    for i in range(2, len(data)):
        for j in range(len(data) - i):
            subset = data[j:j+i]
            if np.sum(subset) == weakness_number:
                return subset

subset = find_weakness(weakness_number=weakness_number)
print(subset)
print(np.min(subset) + np.max(subset))
