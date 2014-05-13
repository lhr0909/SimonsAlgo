from Maple import *
from MathLib import makePrimes

maple = Maple()

openNumTheory(maple)

tc = dict()
tc[1] = 1

def TChain(n):
    if n in tc:
        return tc[n]
    else:
        tc[n] = 1 + TChain(totient(maple, n))
        return tc[n]

#27879191 233124418573
#26 mins from 6000000
ans = 233124418573
p = 27879191
while p < 40000000:
    print p, ans
    if TChain(p) == 25:
        print p
        ans += p
    p = nextPrime(maple, p)

print ans

del maple