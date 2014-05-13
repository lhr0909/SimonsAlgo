def solve(n):
    sol = dict()
    for i in xrange(1, n + 1):
        for j in xrange(i / 3, (n / 2) + 1):
            k = 3 * j * j + 2 * i * j - i * i
            if k > 0:
                if k < n:
                    if k not in sol:
                        sol[k] = 1
                    else:
                        sol[k] += 1
                else:
                    break
    return sol.values().count(1)

print solve(50000000)