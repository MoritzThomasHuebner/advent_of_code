lines = []
with open('day_03_q1_input.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.strip('\n'))

def count_trees(right_step, down_step, lines):
    counter = 0
    for i in range(0, len(lines), down_step):
        j = (right_step * int(i/down_step)) % len(lines[0])
        if lines[i][j] == '#':
            counter += 1
    return counter

c_1 = count_trees(1, 1, lines)
c_2 = count_trees(3, 1, lines)
c_3 = count_trees(5, 1, lines)
c_4 = count_trees(7, 1, lines)
c_5 = count_trees(1, 2, lines)
print(c_1)
print(c_2)
print(c_3)
print(c_4)
print(c_5)
print(c_1*c_2*c_3*c_4*c_5)