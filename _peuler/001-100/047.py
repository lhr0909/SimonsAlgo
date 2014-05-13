n = 200000
li = [True] * n
li[0] = False
li[1] = False
for i in range(2, n):
    if li[i]:
        for j in range(i*i, n, i):
            li[j] = False
            
primes = []
for i in range(n):
    if li[i]:
        primes.append(i)

def primeFactors(n):
    factors = set()
    k = n
    i = 0
    while k!=1:
        if k % primes[i] == 0:
            factors.add(primes[i])
            while k % primes[i] == 0:
                k = k / primes[i]
        else:
            i = i + 1
    return len(factors)
    

p = [primeFactors(647),primeFactors(648), primeFactors(649), primeFactors(650)]
i = 647
while p[0]!=4 or p[1]!=4 or p[2]!=4 or p[3]!=4:
    i += 1
    p.pop(0)
    p.append(primeFactors(i+3))
print i

    

