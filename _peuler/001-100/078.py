#partition function P(n)
#http://mathworld.wolfram.com/PartitionFunctionP.html
#item 11

#p(n) = sum((-1)^(k+1) * (P(n - k*(3*k-1)/2) + P(n - k*(3*k+1)/2)), k = 1 .. n)
#p(n) = 0 where n < 0
#p(0) = 1

p = dict()
p[0] = 1

n = 1
found = False
while not found:
    #if n % 1000 == 0:
    #    print n
    p[n] = 0
    #loop from k = 1 to whenever p[a] and p[b] are both zero
    k = 1
    a = n - k*(3*k-1) / 2
    a = 0 if a < 0 else p[a]
    b = n - k*(3*k+1) / 2
    b = 0 if b < 0 else p[b]
    while a != 0 or b != 0:
        t = a + b
        if (k + 1) % 2 == 1:
            t = -t
        p[n] += t
        k += 1
        a = n - k*(3*k-1) / 2
        a = 0 if a < 0 else p[a]
        b = n - k*(3*k+1) / 2
        b = 0 if b < 0 else p[b]
    #p[n] %= 1000000 (this one for some speed-up)
    if p[n] % 1000000 == 0:  #this one for keeping p[n]
        found = True
        break
    n += 1
print n