def fill_to_length(s, l):
    while len(s) < l:
        s = " " + s
    return s


def print_exp(operands, op):
    a = operands[0]
    b = operands[1]
    lines = []
    length = max(len(op+b), len(a))
    lines.append(fill_to_length(a, length))
    lines.append(fill_to_length(op+b, length))
    lines.append("-"*length)
    if op == '+' or op == '-' or (op == "*" and len(b) == 1):
        result = str(eval(a+op+b))
        if len(result) > length:
            length = len(result)
            lines[len(lines)-1] = "-" * length
            lines = map(lambda x: fill_to_length(x, length), lines)
        lines.append(fill_to_length(result, length))
    else:
        for idx, digit in enumerate(b[::-1]):
            partial_result = str(eval(a+op+digit)) + " " * idx
            if len(partial_result) > length:
                length = len(partial_result)
                if idx == 0:
                    lines[len(lines)-1] = "-" * length
                lines = map(lambda x: fill_to_length(x, length), lines)
            lines.append(fill_to_length(partial_result, length))
        lines.append("-"*length)
        result = str(eval(a+op+b))
        if len(result) > length:
            length = len(result)
            lines[len(lines)-1] = "-" * length
            lines = map(lambda x: fill_to_length(x, length), lines)
        lines.append(fill_to_length(result, length))

    return '\n'.join(lines)


T = int(raw_input())

operators = ['+', '-', '*']

for case in xrange(T):
    expression = raw_input().strip()
    parsed_expressions = map(lambda x: expression.split(x), operators)
    for i in xrange(len(operators)):
        if len(parsed_expressions[i]) == 2:
            op = operators[i]
            operands = parsed_expressions[i]
            print print_exp(operands, op)
            print
            break