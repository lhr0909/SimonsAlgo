#let z = f(n, k) = n^2 - (n - k)^2 - (n - 2*k)^2
#            = (5*k - n) * (n - k)

#let x be a divisor of z, and let y = z / x

#solve n - k = x, 5*k - n = y for n and k, we have
#n = (5*x + y) / 4, k = (x + y) / 4

#need to make sure both (x + y) and (5 * x + y) is divisible by 4.

from Maple import *

maple = Maple()
openNumTheory(maple)

def solve(start, limit, ns):
    ans = 0
    z = start
    while z < limit:
        s = 0
        div = divisors(maple, z)
        for x in div:
            y = z / x
            if ((5*x + y) % 4 == 0) and ((x + y) % 4 == 0):
                n = (5*x + y) / 4
                k = (x + y) / 4
                if n > 2 * k:
                    #print "%d^2 - %d^2 - %d^2 = %d" % (n, n - k, n - k - k, z)
                    s += 1
        if s == ns:
            #print z
            ans += 1
        z += 1
    return ans

print solve(1155, pow(10, 6), 10)

del maple