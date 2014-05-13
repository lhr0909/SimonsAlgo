#solve x * Pwin + Plose = 0 for x
#find P(B >= 8)

from MathLib import choose_iter, product
from math import factorial

denom = factorial(16)

num = 0

for i in xrange(7, -1, -1):
    if i == 0:
        num += 1
    for j in choose_iter(range(1, 16), i):
        k = j
        while len(k) < 15:
            k = (1, ) + k
        num += product(j)

print -(-denom + num) / num + 1