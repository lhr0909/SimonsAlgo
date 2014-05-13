from MathLib import makePrimes
from math import log

m = pow(10, 9)
p = makePrimes(100 + 1)
q = map(lambda x: int(log(m, x)) + 1, p)

print q

r = []
for i in xrange(len(q)):
    r.append(0)

def add1(x):
    global r
    r[x] += 1
    for i in xrange(x, len(r) - 1):
        if r[i] > q[i]:
            r[i] = 0
            r[i + 1] += 1

def checkNum():
    s = 1
    for i in xrange(len(q)):
        s *= pow(p[i], r[i])
    return s

ans = 0

lr = r[15]

while r[len(q) - 1] < q[len(q) - 1]:
    if lr != r[15]:
        print r
        lr = r[15]
    s = checkNum()
    if s <= m:
        ans += 1
        add1(0)
    else:
        x = -1
        while s > m:
            x += 1
            if x >= len(r):
                break
            for i in xrange(q[x] - r[x] + 1):
                add1(x)
            s = checkNum()

print ans