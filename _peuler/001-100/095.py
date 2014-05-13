#http://mathworld.wolfram.com/SociableNumbers.html

#found an inexpensive algorithm for finding the sum of divisors

from MathLib import makePrimes, sumOfDivisors

p = makePrimes(pow(10, 6))

SoPD = lambda n: sumOfDivisors(n, p) - n #sum of proper divisors

r = dict()

def findChain(n):
    if n in r: return r[n]
    k = n
    c = [k]
    s = set([k])
    k = SoPD(n)
    if k in s: #found a perfect number
        r[n] = c
        return c
    while k not in s and k < pow(10, 6):
        c.append(k)
        s.add(k)
        k = SoPD(k)
        if k == n: #found a chain
            t = c[:]
            for element in c:
                r[element] = t
                t = t[1:] + [t[0]]
            return c
        elif k in r:
            for i in xrange(len(c) - 1):
                r[c[i]] = False
            return False
        elif k in s: #found a smaller chain
            i = c.index(k)
            t = c[i:]
            u = c[:i]
            for element in t:
                r[element] = t
                t = t[1:] + [t[0]]
            for element in u:
                r[element] = False
            return False
        elif k == 0:
            for element in c:
                r[element] = False
            return False
    if k >= pow(10, 6):
        for element in c:
            r[element] = False
        return False
    return c

longest = 0
ans = 0
for n in xrange(1, pow(10, 6)):
    if n % 100000 == 0:
        print n, longest, ans
    t = findChain(n)
    if t != False:
        if len(t) > longest:
            longest = len(t)
            ans = min(t)
            #print t
print ans