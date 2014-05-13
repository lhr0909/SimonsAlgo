#continued fraction

from math import sqrt

def findCF(n):
    b = int(sqrt(n))
    d = 1
    cf = [b]
    cfSet = set()
    count = 0
    t = tuple([b, d])
    cfP = []
    while t not in cfSet:
        cfSet.add(t)
        d = (n - b*b) / d
        k = int((sqrt(n) + b) / float(d))
        cfP.append(k)
        b = k * d - b
        count += 1
        t = tuple([b, d])
    cf.append(cfP)
    return [cf, count]

n = 10000
ans = 0

for i in xrange(2, n + 1):
    if sqrt(i) != int(sqrt(i)):
        temp = findCF(i)
        #print "sqrt(%d) = %s, period = %d" % (i, temp[0], temp[1])
        if temp[1] % 2 == 1:
            ans += 1
print ans