import numpy as np

data = np.loadtxt('day_10_input.txt', dtype=np.int64)
data = np.append(data, [0, np.max(data) + 3])

# Part 1

data = np.sort(data)
jolt_diffs = np.diff(data)

n_ones = len(np.where(jolt_diffs == 1)[0])
n_threes = len(np.where(jolt_diffs == 3)[0])
combined = n_ones * n_threes
print(combined)

# Part 2

combinations = [None] * len(data)
combinations[0] = 1


def count_combinations(adapter_joltage, joltage_adapters):
    diffs = adapter_joltage - data
    next_adapter_indices = np.where(np.logical_and(1 <= diffs, diffs <= 3))[0]
    next_adapters = joltage_adapters[next_adapter_indices]

    counter = 0
    for next_adapter_index, next_adapter in zip(next_adapter_indices, next_adapters):
        if combinations[next_adapter_index] is None:
            combinations[next_adapter_index] = count_combinations(adapter_joltage=next_adapter,
                                                                  joltage_adapters=joltage_adapters)
        counter += combinations[next_adapter_index]
    return counter

print(count_combinations(adapter_joltage=data[-1], joltage_adapters=data[:-1]))
