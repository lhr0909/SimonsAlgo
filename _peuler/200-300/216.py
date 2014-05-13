from MathLib import isPrime

def t(n):
    return 2*n*n - 1

count = 0

n = 50000000
#n = 10000

for i in xrange(2, n + 1):
    if isPrime(t(i)):
        count += 1
        print i, t(i), count

print count