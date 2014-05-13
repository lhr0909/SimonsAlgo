#Related Problem: Project Euler 103 105

#http://jsomers.net/blog/pe-oeis

#number of disjoint subset pairs of length k in a set of length n is given by
#((n choose k) * (n-k choose k)) / 2

#number of strictly dominated subset pairs of length k in a set of length n is given by
#(n choose 2*k) * catalan(k)

#all you need to check is the subset pairs of length from 2 to floor(n / 2)

c = dict()
c[(0, 0)] = 1
c[(1, 0)] = 1
c[(1, 1)] = 1

def choose(n, k):
    if (n, k) in c:
        return c[(n, k)]
    else:
        if k == 0 or n == k:
            c[(n, k)] = 1
        else:
            c[(n, k)] = choose(n - 1, k - 1) + choose(n - 1, k)
        return c[(n, k)]

def catalan(n):
    return choose(2*n, n) - choose(2*n, n+1)

def disjointPairs(n, k):
    if n - k >= k:
        return (choose(n, k) * choose(n - k, k)) / 2
    else:
        return 0

def dominatedPairs(n, k):
    return choose(n, 2 * k) * catalan(k)
    
n = 12
ans = 0
for i in xrange(2, n / 2 + 1):
    ans += (disjointPairs(n, i) - dominatedPairs(n, i))

print ans