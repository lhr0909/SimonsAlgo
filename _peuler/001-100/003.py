'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt

def maxprime(m):
    n = int(sqrt(m))
    li = [True] * n
    li[0] = False
    li[1] = False
    for i in range(2, n):
        if li[i]:
            for j in range(i*i, n, i):
                li[j] = False
    primes = []
    for i in range(n):
        if (li[i])and(m % i==0):
            primes.append(i)
    return primes.pop()

print maxprime(600851475143)
