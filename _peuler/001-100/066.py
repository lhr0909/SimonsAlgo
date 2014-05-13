#Find Fundamental Solutions of Pell's Equation
#Use continued fraction of square root
#and its convergents
#Related Problem: 064 065

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

def minPell(n):
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
    
    while h*h - n*k*k != 1:
        for a in l:
            h = a*h_1 + h_2
            h_2 = h_1
            h_1 = h
            
            k = a*k_1 + k_2
            k_2 = k_1
            k_1 = k
            
            if h*h - n*k*k == 1:
                break
    return [h, k]

ans = 0
maxH = 0
for i in xrange(2, 1000 + 1):
    if sqrt(i) != int(sqrt(i)):
        t = minPell(i)[0]
        if t > maxH:
            maxH = t
            ans = i

#print maxH
print ans
