def build_rpn(a, b, op):
    return "%s%s%s" % (a, b, op)

letters = map(lambda x: chr(x+96), range(1, 26+1))

n = int(raw_input())
for c in xrange(n):
    expression = raw_input().strip()

    operands = []
    operators = []
    level = 0

    for letter in expression:
        if letter in letters:
            operands.append(letter)
        elif letter == "(":
            level += 1
        elif letter == ")":
            b = operands.pop()
            a = operands.pop()
            op = operators.pop()
            operands.append(build_rpn(a, b, op))
            level -= 1
        else:
            operators.append(letter)
    print operands.pop()