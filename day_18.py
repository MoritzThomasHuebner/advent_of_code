
def evaluate_expression(expression):
    if len(expression) == 1:
        return expression[0]
    elif len(expression) == 3:
        return str(eval("".join(expression)))
    elif expression[0] == '(':
        closing_parenthesis_position = find_closing_parenthesis(expression)
        evaluated_parenthesis_expression = evaluate_expression(expression[1:closing_parenthesis_position])
        remaining_expression = [evaluated_parenthesis_expression]
        remaining_expression.extend(expression[closing_parenthesis_position + 1:])
        return evaluate_expression(remaining_expression)
    elif expression[2] == '(':
        closing_parenthesis_position = find_closing_parenthesis(expression)
        evaluated_parenthesis_expression = evaluate_expression(expression[3:closing_parenthesis_position])
        remaining_expression = expression[:2]
        remaining_expression.extend([evaluated_parenthesis_expression])
        remaining_expression.extend(expression[closing_parenthesis_position + 1:])
        return evaluate_expression(remaining_expression)
    else:
        evaluated_starting_expression = evaluate_expression(expression[:3])
        remaining_expression = [evaluated_starting_expression]
        remaining_expression.extend(expression[3:])
        return evaluate_expression(remaining_expression)


def find_closing_parenthesis(expression):
    parenthesis_counter = 0
    flag = False
    for i, expr in enumerate(expression):
        if expr == '(':
            parenthesis_counter += 1
            flag = True
        elif expr == ')':
            parenthesis_counter -= 1
            flag = True
        if parenthesis_counter == 0 and flag:
            return i


expressions = []
with open('day_18_input.txt', 'r') as f:
    for i in f.readlines():
        expressions.append(list(i.strip('\n').replace(' ', '')))

sum = 0
for expresssion in expressions:
    sum += int(evaluate_expression(expresssion))
print(sum)


# Part 2


def evaluate_additions(expression):
    new_expression = []
    i = 0
    while i < len(expression):
        if isinstance(expression, str):
            return expression
        elif i + 2 == len(expression):
            new_expression.extend(expression[i:])
            break
        elif expression[i+1] == '+':
            res = evaluate_expression(expression[i:i+3])
            new_expression.append(res)
            i += 3
        else:
            new_expression.append(expression[i])
            i += 1
    if '+' in new_expression:
        return evaluate_additions(new_expression)
    return new_expression


def evaluate_multiplications(expression):
    return str(eval("".join(expression)))


def evaluate_parenthesis(expression):
    try:
        starting_index = expression.index('(')
        ending_index = find_closing_parenthesis(expression)
    except ValueError:
        return evaluate_multiplications(evaluate_additions(expression))

    new_expression = expression[:starting_index]

    parenthesis_expression = expression[starting_index + 1:ending_index]
    new_expression.extend([evaluate_parenthesis(parenthesis_expression)])
    new_expression.extend(expression[ending_index + 1:])
    return evaluate_parenthesis(evaluate_additions(evaluate_multiplications(new_expression)))

sum = 0
for expresssion in expressions:
    sum += int(evaluate_parenthesis(expresssion))
print(sum)