# Part 1

rule_lower_number = []
rule_higher_number = []
letter_rules = []
passwords = []
lines = []
with open('day_02_q1_input.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line)
        line = line.replace(':', '')
        substrings = line.split(' ')
        occurances = substrings[0].split('-')
        rule_lower_number.append(int(occurances[0]))
        rule_higher_number.append(int(occurances[1]))
        letter_rules.append(substrings[1])
        passwords.append(substrings[2])

n_valid = 0
for min_occurance, max_occurance, letter_rule, password in zip(rule_lower_number, rule_higher_number, letter_rules, passwords):
    if min_occurance <= password.count(letter_rule) <= max_occurance:
        n_valid += 1
print(n_valid)

# Part 2
n_valid = 0
for initial_position, final_position, letter_rule, password, line in zip(rule_lower_number, rule_higher_number, letter_rules, passwords, lines):
    condition_1 = password[initial_position - 1] == letter_rule and password[final_position - 1] != letter_rule
    condition_2 = password[initial_position - 1] != letter_rule and password[final_position - 1] == letter_rule
    if condition_1 or condition_2:
        n_valid += 1
    else:
        print(line)
print(n_valid)
