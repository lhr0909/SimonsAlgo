

def prime(n):
    li = [True] * n
    li[0] = False
    li[1] = False
    for i in range(2, n):
        if li[i]:
            for j in range(i*i, n, i):
                li[j] = False
    prime = []
    for i in range(n):
        if li[i]:
            prime.append(i)
    return prime

prime = prime(1100)


def nonrec(n):
    i = 0
    pfac = []
    while prime[i]<=n:
        if n % prime[i] == 0:
            pfac.append(prime[i])
        i = i + 1
    if (pfac==[2])or(pfac==[5])or(pfac==[2,5]):
        return True
    else:
        return False

longest = 0
ans = 0
for i in range(3, 1000):
    if (not(nonrec(i)))and(i in prime):
        temp = 1
        while pow(10,temp,i)!=1:
            temp = temp + 1
        if temp>longest:
            longest = temp
            ans = i
print ans, longest