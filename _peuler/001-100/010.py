from math import sqrt

def sieve(n):
    li = [True] * n
    li[0] = False
    li[1] = False
    for i in range(2, n):
        if li[i]:
            for j in range(i*i, n, i):
                li[j] = False
    sumofprime = 0
    for i in range(n):
        if li[i]:
            sumofprime = sumofprime + i
    return sumofprime

print sieve(2000000)


