#Related Problem: Project Euler 132

from MathLib import makePrimes

ps = makePrimes(100000)[2:]

ans = sum(ps) + 2 + 3

s = set()

for i in xrange(1, 21):
    for p in ps:
        if pow(10, pow(10, i), p) == 1:
            s.add(p)

ans -= sum(s)

print ans