import numpy as np

lines = []
with open('day_06_input.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.strip('\n'))

answers = []
answer = ''

for i, line in enumerate(lines):
    if line == '' or i == len(lines[-1]):
        answers.append(answer)
        answer = ''
    else:
        answer += line

sum_counts = np.sum([len(set(answer)) for answer in answers])
print(sum_counts)

# Part 2

group_answers = []
individual_answers = []

for i, line in enumerate(lines):
    if line == '' or i == len(lines[-1]):
        group_answers.append(individual_answers)
        individual_answers = []
    else:
        individual_answers.append(line)

for group_answer in group_answers:
    shared_answers = {}
    for individual_answer in group_answer:
        shared_answers = set(group_answer).intersection()
