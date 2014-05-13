#Used UAD Tree and C++ to find the first 8, took up all the memory (8GB) in 4min
#See the Maple worksheet for the math
#Related Problem: 066
#http://mathworld.wolfram.com/PellEquation.html

from math import sqrt

def findCF(n):
    b = int(sqrt(n))
    d = 1
    cf = [b]
    cfSet = set()
    count = 0
    t = tuple([b, d])
    cfP = []
    while t not in cfSet:
        cfSet.add(t)
        d = (n - b*b) / d
        k = int((sqrt(n) + b) / float(d))
        cfP.append(k)
        b = k * d - b
        count += 1
        t = tuple([b, d])
    cf.append(cfP)
    return [cf, count]
    
def PellSolve(n, limit):
    #initialization
    temp = findCF(n)[0]
    a = temp[0]
    l = temp[1] #list of periodic continued fractions
    
    h_2 = 0
    h_1 = 1
    h = a*h_1 + h_2
    h_2 = h_1
    h_1 = h
    
    k_2 = 1
    k_1 = 0
    k = a*k_1 + k_2
    k_2 = k_1
    k_1 = k
    
    if h*h - n*k*k == 1 or h*h - n*k*k == -1:
        yield (h, k)
        count = 1
    else:
        count = 0
    
    while count < limit:
        for a in l:
            h = a*h_1 + h_2
            h_2 = h_1
            h_1 = h
            
            k = a*k_1 + k_2
            k_2 = k_1
            k_1 = k
            
            if h*h - n*k*k == 1 or h*h - n*k*k == -1:
                yield (h, k)
                count += 1
                
ans = 0
for x, y in PellSolve(5, 12):
    m, n = 2 * y + x, y
    ans += m*m + n*n
    print m*m - n*n, 4*m*n, m*m + n*n

print ans