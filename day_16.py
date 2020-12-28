from collections import namedtuple
import re
import numpy as np


rule_descriptions = []
my_ticket = None
nearby_tickets = []
with open('day_16_input.txt', 'r') as f:
    mode = 0
    for i in f.readlines():
        if i == '\n':
            mode += 1
            continue
        if mode == 0:
            rule_descriptions.append(i.strip('\n'))
        elif mode == 1:
            if 'your ticket' in i:
                continue
            else:
                my_ticket = [int(j) for j in i.strip('\n').split(',')]
        elif mode == 2:
            if 'nearby tickets' in i:
                continue
            else:
                nearby_tickets.append([int(j) for j in i.strip('\n').split(',')])

Rule = namedtuple('Rule', ['name', 'minimum', 'maximum'])

rules = []

for r in rule_descriptions:
    sub_rules = r.split(' ')
    for sr in sub_rules:
        if not re.sub('\D', '', sr) == '':
            minmax = sr.split('-')
            rules.append(Rule(name=r.split(':')[0], minimum=int(minmax[0]), maximum=int(minmax[1])))


def check_rule(rule, val):
    return rule.minimum <= val <= rule.maximum



def check_rule_many_values(rule, values):
    for v in values:
        flags = np.logical_and(np.array(rule)[:, 0] <= v, v <= np.array(rule)[:, 1])
        if not np.any(flags):
            return False
    return True


combined = 0
invalid_ticket_indices = []
for i, nearby_ticket in enumerate(nearby_tickets):
    for val in nearby_ticket:
        valid = False
        for rule in rules:
            valid = check_rule(rule, val)
            if valid:
                break
        if not valid:
            combined += val
            invalid_ticket_indices.append(i)
print(combined)

# Part 2

nearby_tickets = [ticket for i, ticket in enumerate(nearby_tickets) if i not in invalid_ticket_indices]

rules = dict()

for r in rule_descriptions:
    sub_rules = r.split(' ')
    rule = []
    for sr in sub_rules:
        if not re.sub('\D', '', sr) == '':
            minmax = sr.split('-')
            rule.append((int(minmax[0]), int(minmax[1])))
    rules[r.split(':')[0]] = rule

possible_associated_fields = []

for column in range(len(nearby_tickets[0])):
    rule_names = []
    values = np.array(nearby_tickets)[:, column]
    for rule_name, rule in rules.items():
        check = check_rule_many_values(rule=rule, values=values)
        if check:
            rule_names.append(rule_name)
    possible_associated_fields.append(rule_names)


associations = dict()

while True:
    for i, field in enumerate(possible_associated_fields):
        if len(field) == 1:
            key = field[0]
            associations[key] = i
            for i in range(len(possible_associated_fields)):
                try:
                    possible_associated_fields[i].remove(key)
                except ValueError:
                    continue
    if len(associations) == len(possible_associated_fields):
        break

print(associations)
prod = 1
for k, v in associations.items():
    if k.startswith('departure'):
        prod *= int(my_ticket[i])
print(prod)