def sieve(n):
    li = [True] * n
    primes = []
    li[0] = False
    li[1] = False
    for i in range(2, n):
        if li[i]:
            primes.append(i)
            for j in range(i*i, n, i):
                li[j] = False
    return primes
    
n = 10**6
p = sieve(n)
s = set(p)
l = len(p)
ans = [2, 1]
for i in range(l):
    for j in range(i+ans[1], l):
        k = sum(p[i:j+1])
        if k < ans[0]:
            continue
        if k > n:
            break
        if k in s:
            if j-i+1>ans[1]:
                ans = [k, j-i+1]

print ans[0]
                

