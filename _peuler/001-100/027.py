

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

prime = set(prime(100000))
longest = 0
ansa = 0
ansb = 0
for a in range(-999,0):
    for b in range(1000,1,-1):
        if not(b in prime):
            continue
        else:
            print a, b,
            n = 0
            temp = n**2+a*n+b
            while (temp>0)and(temp in prime):
                n = n + 1
                temp = n**2+a*n+b
            print n
            if n>longest:
                longest = n
                ansa = a
                ansb = b

print "Answer:", ansa, ansb, ansa*ansb, longest