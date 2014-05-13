#http://en.wikipedia.org/wiki/Repunit

#Since R(n) = (10^n - 1) / 9,
#then R(n) * 9 + 1 = 10^n

#So to find the factors of R(n),
#ALL YOU HAVE TO CHECK is just
#if pow(10, n, p) == 1
#where p is prime...

#I AM SO DUMB

from MathLib import isPrime
from Maple import *

s = []
n = pow(10, 9)
p = 3
while len(s) < 40:
    if isPrime(p) and pow(10, n, p) == 1:
        s.append(p)
    p += 2

print sum(s)