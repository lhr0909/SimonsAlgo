#Farey Sequence
#Euler's Totient Function

#related problems: 069, 071

def makePrimes(n):
    li = [True] * n
    primes = []
    li[0] = False
    li[1] = False
    for i in range(2, n):
        if li[i]:
            primes.append(i)
            for j in range(i*i, n, i):
                li[j] = False
    return primes

primes = makePrimes(1000000)

def primeFactorsList(n):
    factors = []
    k = n
    i = 0
    while k!=1:
        if k % primes[i] == 0:
            factors.append(primes[i])
            while k % primes[i] == 0:
                k = k / primes[i]
        else:
            i = i + 1
    return factors
    
def product(ls):
    prod = 1
    for item in ls:
        prod *= item
    return prod
    
minus1 = lambda n: n-1
phi = lambda n, f: n * product(map(minus1, f)) / product(f)

def FareyLength(n):
    count = 1
    for i in xrange(1, n + 1):
        if i % 100000 == 0:
            print i
        factors = primeFactorsList(i)
        count += phi(i, factors)
    return count - 2
    
print FareyLength(1000000)
