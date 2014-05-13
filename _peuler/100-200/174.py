#Let x(t) be the number of distinct number of laminae that use exactly t tiles

def lamina(n, k):
    return 4 * k * k + 4 * n * k - 8 * k

x = dict()
n = dict()

limit = pow(10, 6)

m = limit / 4 + 2

for i in xrange(3, m):
    j = 1
    k = lamina(i, j)
    while k <= limit:
        if k not in x:
            x[k] = 1
        else:
            x[k] += 1
        j += 1
        k = lamina(i, j)

for i in x.keys():
    if x[i] not in n:
        n[x[i]] = 1
    else:
        n[x[i]] += 1

ans = 0

for i in xrange(1, 11):
    ans += n[i]
    
print ans
