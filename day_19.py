RULES = dict()
messages = []
with open('day_19_input.txt', 'r') as f:
    mode = 0
    for i in f.readlines():
        if i == '\n':
            mode += 1
            continue
        if mode == 0:
            r = i.strip('\n').split(':')
            RULES[r[0]] = r[1][1:]
        elif mode == 1:
            messages.append(i.strip('\n'))


def evaluate_single(rule_number, message):
    rule = RULES[rule_number]
    if rule.startswith("\""):
        return rule[1] == message[0], 1
    elif "|" in rule:
        or_rule = rule.split("|")
        first, count_first = evaluate_multiple(or_rule[0], message)
        second, count_second = evaluate_multiple(or_rule[1], message)
        # if first and second:
        #     return first, [count_first, count_second]
        if first:
            return first, count_first
        else:
            return second, count_second
    else:
        return evaluate_multiple(rule, message)


def evaluate_multiple(rule_numbers, message):
    if len(message) == 0:
        return False, 0
    rule_numbers = rule_numbers.rstrip(' ').lstrip(' ').split(' ')
    counter = 0
    for i, r in enumerate(rule_numbers):
        evaluation, count = evaluate_single(r, message[counter:])
        # for c in counter:
        #     evaluation, count = evaluate_single(r, message[c:])

        if not evaluation:
            return False, counter
        else:
            # for c in count:
            #     counter
            counter += count
    return True, counter


def evaluate(rule_number, message):
    evaluation, check_len = evaluate_single(rule_number, message=message)
    return check_len == len(message) and evaluation


results = [evaluate("0", message=i) for i in messages]
print(sum(results))

RULES["8"] = "42 | 42 8"
RULES["11"] = "42 31 | 42 11 31"

# results = [evaluate("0", message=i) for i in messages]
# print(sum(results))

expected = ["bbabbbbaabaabba",
            "babbbbaabbbbbabbbbbbaabaaabaaa",
            "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
            "bbbbbbbaaaabbbbaaabbabaaa",
            "bbbababbbbaaaaaaaabbababaaababaabab",
            "ababaaaaaabaaab",
            "ababaaaaabbbaba",
            "baabbaaaabbaaaababbaababb",
            "abbbbabbbbaaaababbbbbbaaaababb",
            "aaaaabbaabaaaaababaa",
            "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
            "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"]
# j = 0
# for i in inputs:
#     if evaluate("0", input=i):
#         print(i)
#         print(expected[j])
#         print()
#         j += 1
#
