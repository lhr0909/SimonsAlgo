'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''


from math import sqrt

def sieve(n):
    li = [True] * n
    li[0] = False
    li[1] = False
    for i in range(2, n):
        if li[i]:
            for j in range(i*i, n, i):
                li[j] = False
    prime = 0
    for i in range(n):
        if li[i]:
            prime = prime + 1
            if prime==10001:
                print i
    return prime

sieve(110000)
