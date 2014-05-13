def sieve(n):
    li = [True] * n
    li[0] = False
    li[1] = False
    for i in range(2, n):
        if li[i]:
            for j in range(i*i, n, i):
                li[j] = False
    return li

primes = sieve(10000)
for i in range(1000,10000):
    if primes[i]:
        for j in range(1, 10000):
            if i+j<10000:
                if set(str(i))==set(str(i+j)) and primes[i+j]:
                    if i+j+j<10000:
                        if set(str(i))==set(str(i+j+j)) and primes[i+j+j]:
                            print str(i) + str(i+j) + str(i+j+j)
                            break
