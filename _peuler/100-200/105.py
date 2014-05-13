#Related Problem: Project Euler 103
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

f = map(lambda x: eval('[%s]' % x), open('105.txt', 'r').read().split('\r\n'))
ans = 0
for seq in f:
    if checkSet(seq):
        ans += sum(seq)
        print sum(seq)

print ans
