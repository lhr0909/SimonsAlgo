#from itertools import *
from MathLib import choose_iter, allSubsets_iter

def allProperSubsets_iter(s):
    for i in xrange(1, len(s)):
        for j in choose_iter(s, i):
            yield j

def checkSet(s):
    for i in allProperSubsets_iter(s):
        t = tuple(set(s) - set(i))
        sb = sum(i)
        for j in allSubsets_iter(t):
            sc = sum(j)
            if sb == sc:
                return False
            if len(i) > len(j) and sb < sc:
                return False
            if len(i) < len(j) and sb > sc:
                return False
    return True

a = [11, 18, 19, 20, 22, 25]
i = 1
b = [i] + map(lambda x: x + i, a)
while not checkSet(b):
    i += 1
    b = [i] + map(lambda x: x + i, a)

b = map(str, b)
print ''.join(b)

#Gay because you just need to implement the fake algorithm in the problem statement to solve

#http://www.research.att.com/~njas/sequences/A037254
'''
x(1, 1) = 1
x(1, n) = x(floor[(n + 1) / 2], n - 1)
x(m, n) = x(m - 1, n - 1) + x(1, n)
'''