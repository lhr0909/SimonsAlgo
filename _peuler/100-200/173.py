def L(n, k):
    return 4 * k * k + 4 * n * k - 8 * k

t = pow(10, 6)

m = t / 4 + 2
s = 0

for i in xrange(3, m):
    j = 1
    k = L(i, j)
    while k <= t:
        j += 1
        k = L(i, j)
        s += 1

print s