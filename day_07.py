from collections import namedtuple

rules = []
with open('day_07_input.txt', 'r') as f:
    for rule in f.readlines():
        rules.append(rule.strip('\n'))

ContentRule = namedtuple('ContentRule', ['contents', 'quantities'])

compiled_rules = dict()

for rule in rules:
    split_rule = rule.split('contain')
    bag_color = split_rule[0]
    bag_color = bag_color.replace('bags', '').replace('bag', '').replace(' ', '')

    contents = split_rule[1]
    contents = contents.split(',')
    content_colors = []
    quantities = []
    for content in contents:
        if content == ' no other bags.':
            continue
        else:
            content = content.replace('bags', '').replace('bag', '').replace(' ', '').replace('.', '')
            content_colors.append(content[1:])
            quantities.append(int(content[0]))
    compiled_rules[bag_color] = ContentRule(contents=content_colors, quantities=quantities)


def check_contains(content_rules, bag_color, searched_color):
    if bag_color == searched_color:
        return True
    for content_bag in content_rules[bag_color].contents:
        if check_contains(content_rules=content_rules, bag_color=content_bag, searched_color=searched_color):
            return True
    return False

counter = 0
for bag_color in compiled_rules.keys():
    if bag_color == 'shinygold':
        continue
    if check_contains(content_rules=compiled_rules, bag_color=bag_color, searched_color='shinygold'):
        counter += 1
print(counter)

# Part 2

def count_contains(content_rules, bag_color):
    counter = 1
    for content, quantity in zip(content_rules[bag_color].contents, content_rules[bag_color].quantities):
        counter += count_contains(content_rules, content) * quantity
    return counter

print(count_contains(content_rules=compiled_rules, bag_color='shinygold') - 1)
