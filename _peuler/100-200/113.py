di = dict()
dd = dict()

def iN(k, n):
    if (k, n) in di:
        return di[(k, n)]
    else:
        s = 0
        if n == 1:
            s += 10 - k
        else:
            for i in xrange(k, 10):
                s += iN(i, n - 1)
        di[(k, n)] = s
        return s

'''
def iN(k, n):
    if (k, n) in di:
        return di[(k, n)]
    else:
        s = 0
        for i in xrange(k, 10):
            if n == 1:
                s += 1
            else:
                for next in xrange(iN(i, n - 1)):
                    s += 1
        di[(k, n)] = s
        return s

def iN(k, n):
    for i in xrange(k, 10):
        if n == 1:
            yield (i, )
        else:
            for next in iN(i, n - 1):
                yield (i, ) + next
'''

def increaseNum(n):
    return iN(1, n)
    
def dN(k, n):
    if (k, n) in dd:
        return dd[(k, n)]
    else:
        s = 0
        if n == 1:
            s += k + 1
        else:
            for i in xrange(k, -1, -1):
                s += dN(i, n - 1)
        dd[(k, n)] = s
        return s
    
'''
def dN(k, n):
    if (k, n) in dd:
        return dd[(k, n)]
    else:
        s = 0
        for i in xrange(k, -1, -1):
            if n == 1:
                s += 1
            else:
                for next in xrange(dN(i, n - 1)):
                    s += 1
        dd[(k, n)] = s
        return s

def dN(k, n):
    for i in xrange(k, -1, -1):
        if n == 1:
            yield (i, )
        else:
            for next in dN(i, n - 1):
                yield (i, ) + next
'''

def decreaseNum(n):
    #make sure to declude digits with same number in the end
    return dN(9, n) - 10

def checkNotBouncy(n):
    s = 9
    for i in xrange(2, n + 1):
        s += increaseNum(i)
        s += decreaseNum(i)
    return s

print checkNotBouncy(100)

'''
#The code is really simple
#(the following assumes the nCr function is written somewhere):

count = 0
for i in range(1,101):
    count += nCr(8+i,i)
    count += nCr(9+i,i)
    count -= 10
print count
'''