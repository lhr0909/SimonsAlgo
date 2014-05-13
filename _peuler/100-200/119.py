def sumOfDigits(n):
    return sum(map(int, str(n)))

a = set()

for i in xrange(2, 100):
    for j in xrange(2, 10):
        k = pow(i, j)
        if k < 10:
            continue
        if sumOfDigits(k) == i:
            #print "%d ^ %d = %d" % (i, j, k)
            #a.add(tuple([k, i, j]))
            a.add(k)

a = sorted(a)

print a[29]