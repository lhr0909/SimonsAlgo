#Related: Project Euler 120

#(a+1)^n == an+1 (mod a^2)
#(a-1)^n == an-1 or 1-an (mod a^2) depending whether n is odd or even

from MathLib import makePrimes

p = makePrimes(250000)

def funPowMod(n):
    a = p[n-1]
    #print (pow(a - 1, n, a*a) + pow(a + 1, n, a*a)) % (a*a)
    if n % 2 == 1:
        return ((a*n+1) + (a*n-1)) % (a*a)
    else:
        return ((a*n+1) + (1-a*n)) % (a*a)

m = pow(10, 10)

for i in xrange(7037, len(p)):
    if funPowMod(i) > m:
        print i
        break