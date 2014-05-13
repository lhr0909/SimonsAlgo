#the following is not fast for large numbers, FUCK
'''
from MathLib import makePrimes, isPrime

pfs = dict()

def primeFactors(n, primes):
    if n in pfs:
        return pfs[n]
    else:
        factors = dict()
        k = n
        i = 0
        while k!=1:
            if k % primes[i] == 0:
                factors[primes[i]] = 0
                while k % primes[i] == 0:
                    factors[primes[i]] += 1
                    k /= primes[i]
                    if k in pfs:
                        x = pfs[k]
                        for j in x.keys():
                            if j not in factors:
                                factors[j] = x[j]
                            else:
                                factors[j] += x[j]
                        k = 1
            else:
                i = i + 1
        pfs[n] = factors
        return factors
    
n = 20000000
k = 15000000
p = makePrimes(n)

print "done with primes"
print len(p)

bin = dict()

for i in xrange(2, n + 1):
    if i % 200000 == 0:
        print i
    pf = primeFactors(i, p)
    if i <= k:
        for j in pf.keys():
            if j not in bin:
                bin[j] = -pf[j]
            else:
                bin[j] -= pf[j]
    else:
        if i > n - k and i <= n:
            for j in pf.keys():
                if j not in bin:
                    bin[j] = pf[j]
                else:
                    bin[j] += pf[j]
    
print bin

ans = 0
for i in bin.keys():
    ans += (i * bin[i])

print ans
'''

#found one implementation online somewhere
#http://www.numbertheory.org/php/binomial.html
#http://www.jstor.org/stable/2323099

from MathLib import makePrimes
from math import sqrt

def pE(n, k, p):
    e = 0
    r = 0
    if k > n / 2:
        k = n - k
    if p > n - k:
        return 1
    if p > n / 2:
        return 0
    f = sqrt(n)
    if p > f:
        if n % p < k % p:
            return 1
        else:
            return 0
    
    while n > 0:
        a = n % p
        n /= p
        b = k % p + r
        k /= p
        if a < b:
            e += 1
            r = 1
        else:
            r = 0
    return e

n = 20000000
k = 15000000

pl = makePrimes(n)
print len(pl)

ans = 0

for p in pl:
    ans += (p * pE(n, k, p))

print ans
