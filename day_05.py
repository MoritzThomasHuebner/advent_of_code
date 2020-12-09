import numpy as np

passes = []
with open('day_05_input.txt', 'r') as f:
    for line in f.readlines():
        passes.append(line.strip('\n'))


def convert_to_binary(boarding_pass):
    boarding_pass = boarding_pass.replace('F', '0')
    boarding_pass = boarding_pass.replace('B', '1')
    boarding_pass = boarding_pass.replace('L', '0')
    boarding_pass = boarding_pass.replace('R', '1')
    return boarding_pass


def convert_to_string_row(boarding_pass_column_id):
    boarding_pass = f'{boarding_pass_column_id:03b}'
    boarding_pass = boarding_pass.replace('0', 'L')
    boarding_pass = boarding_pass.replace('1', 'R')
    return boarding_pass


def get_row_binary(boarding_pass):
    return int(boarding_pass[:7], 2)


def get_column_binary(boarding_pass):
    return int(boarding_pass[7:], 2)


def get_id(row, column):
    return row * 8 + column


def get_id_list(boarding_passes):
    ids = []
    for p in boarding_passes:
        p = convert_to_binary(boarding_pass=p)
        row = get_row_binary(p)
        column = get_column_binary(p)
        ids.append(get_id(row, column))
    return ids


# Part 1

max_id = 0
id_list = get_id_list(boarding_passes=passes)
print(max(id_list))

# Part 2
id_list = sorted(id_list)
min_id = id_list[0]

my_id = -1

for i, current_id in enumerate(np.array(id_list)):
    enumerated_id = i + min_id
    if enumerated_id != current_id:
        my_id = enumerated_id
        break

print(my_id)
