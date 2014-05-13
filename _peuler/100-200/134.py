from MathLib import makePrimes

'''
p = makePrimes(10000)

#old version, extremely slow
MT = dict()
for i in xrange(1, 10):
    for j in xrange(1, 10):
        MT[((i * j) % 10, i)] = j
        
ans = 0

for i in xrange(2, len(p) - 1):
    p1 = p[i]
    p2 = p[i + 1]
    k = MT[(p1 % 10, p2 % 10)]
    x = int(str(k * p2)[-len(str(p1)):])
    while x != p1:
        k += 10
        x = int(str(k * p2)[-len(str(p1)):])
    s = k * p2
    ans += s
    print p1, p2, s, k
    
print ans
'''

#multiplication table
mt = dict()
for i in [1, 3, 7, 9]:
    for j in range(1, 10):
        mt[(i, j)] = (i * j) % 10

def makeMult(p1, p2):
    r = 0
    addList = []
    m = 1
    i = p2 % 10
    x = p1
    c = 0
    while x != 0:
        k = (x - c) % 10
        if k == 0:
            m *= 10
            c = sum(addList) % (m * 10) / m
        else:
            for j in xrange(1, 10):
                if mt[(i, j)] == k:
                    r += m * j
                    addList.append(m * j * p2)
                    m *= 10
                    c = sum(addList) % (m * 10) / m
                    break
        x /= 10
    return r

p = makePrimes(1000010)
ans = 0

for i in xrange(2, len(p) - 1):
    p1 = p[i]
    p2 = p[i + 1]
    ans += p2 * makeMult(p1, p2)
print ans
