from collections import namedtuple
from copy import deepcopy

Operation = namedtuple('Operation', ['command', 'value'])


operations = []
with open('day_08_input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        line = line.split(' ')
        operations.append(Operation(command=line[0], value=int(line[1])))


def nop(current_index, value):
    return current_index + 1, 0


def acc(current_index, value):
    return current_index + 1, value


def jmp(current_index, value):
    return current_index + value, 0


operations_dict = dict(jmp=jmp, acc=acc, nop=nop)


def check_ends(operations):
    visited_operations = []
    current_operation = 0
    accumulated = 0
    while current_operation not in visited_operations:
        if current_operation == len(operations):
            return True, accumulated
        visited_operations.append(current_operation)
        command = operations[current_operation].command
        value = operations[current_operation].value
        current_operation, increment = operations_dict[command](current_operation, value)
        accumulated += increment
    return False, accumulated

ends, accumulated = check_ends(operations=operations)

# Part 2
for i, operation in enumerate(operations):
    if operation.command == 'nop':
        modified_operations = deepcopy(operations)
        modified_operations[i] = Operation('jmp', modified_operations[i].value)
    elif operation.command == 'jmp':
        modified_operations = deepcopy(operations)
        modified_operations[i] = Operation('nop', modified_operations[i].value)
    else:
        continue
    ends, accumulated = check_ends(modified_operations)
    if ends:
        print(accumulated)
        break
