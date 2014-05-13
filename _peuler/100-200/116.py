from math import factorial

def choose(m, n):
    return factorial(m) / (factorial(n) * factorial(m - n))

def fillTiles(l, n, x):
    k = x - l * n
    return choose(k + n, n)
    
def findTotal(n):
    s = 0
    for i in xrange(2, 5):
        for j in xrange(1, n / i + 1):
            s += fillTiles(i, j, n)
    return s

print findTotal(50)