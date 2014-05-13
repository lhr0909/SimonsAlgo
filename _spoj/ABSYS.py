import re

formula_regex = re.compile(r"([0-9]*[machul]*[0-9]*) [+] ([0-9]*[machul]*[0-9]*) = ([0-9]*[machul]*[0-9]*)")
t = int(raw_input())
for tt in xrange(t):
    raw_input()
    formula = raw_input().strip()
    a, b, c = formula_regex.match(formula).groups()
    if a.find("machula") != -1:
        #a has machula
        print str(int(c) - int(b)) + " + " + b + " = " + c
    elif b.find("machula") != -1:
        #b has machula
        print a + " + " + str(int(c) - int(a)) + " = " + c
    elif c.find("machula") != -1:
        #c has machula
        print a + " + " + b + " = " + str(int(a) + int(b))
