#Related: Project Euler 114

p = dict()

def f(m, n):
    if (m, n) in p:
        return p[(m, n)] + 1
    else:
        s = 0
        for i in xrange(m, n+1):
            for j in xrange(n - i + 1):
                s += 1
                k = n - j - i - 1
                if k >= 3:
                    s += (f(m, k) - 1)
        p[(m, n)] = s
        return s + 1
    
m = 50
n = m
while f(m, n) < pow(10, 6):
    n += 1
print n