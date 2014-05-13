from Maple import *
from MathLib import product

#40 seconds. Not bad with Maple

maple = Maple()

def distinctPrimeFactors(n):
    return list(set(primeFactors(maple, n)))

rad = dict()

for i in xrange(1, pow(10, 5) + 1):
    rad[i] = product(distinctPrimeFactors(i))

ls = []

for i in rad.keys():
    ls.append(tuple([rad[i], i]))

print sorted(ls)[9999][1]

del maple