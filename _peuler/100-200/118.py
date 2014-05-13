#Need to come back
#FUCK!!!!

from MathLib import perm_iter, choose_iter, isPrime, product

digit = dict()

for i in xrange(1, 9):
    for j in perm_iter('123456789', i):
        k = int(''.join(j))
        if isPrime(k):
            t = tuple(sorted(map(int, j)))
            if t not in digit:
                digit[t] = set()
            digit[t].add(k)

ss = set()

def solve(s, p):
    global ss
    if len(s) == 0:
        ss.add(p)
    else:
        for i in digit.keys():
            if set(i) <= set(s):
                k = tuple(sorted(set(s) - set(i)))
                solve(k, tuple(sorted(list(p) + [i])))

solve(tuple(range(1, 10)), tuple())

ans = 0

for i in ss:
    ans += product(map(lambda x: len(digit[x]), i))

print ans + 3416