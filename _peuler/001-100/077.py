from MathLib import makePrimes

p = makePrimes(10000)

r = dict()
r[0] = set()
r[1] = set()
r[2] = set([tuple([2])])
r[3] = set([tuple([3])])
r[4] = set([tuple([2, 2])])
r[5] = set([tuple([2, 3]), tuple([5])])

def solve(n):
    global r
    if n in r:
        return len(r[n])
    else:
        largest = 0
        while p[largest] <= n:
            largest += 1
        r[n] = set()
        for i in xrange(largest - 1, -1, -1):
            q = n - p[i]
            if q == 0:
                s = tuple([p[i]])
                if s not in r[n]:
                    r[n].add(s)
            elif q == 1:
                continue
            else:
                if q in r:
                    for sums in list(r[q]):
                        s = tuple(sorted([p[i]] + list(sums)))
                        if s not in r[n]:
                            r[n].add(s)
        return len(r[n])

i = 0
t = solve(i)
while t <= 5000:
    i += 1
    t = solve(i)
    #print i, t
    #print r[i]
print i