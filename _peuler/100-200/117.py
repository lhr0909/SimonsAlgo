#Related Problem: Project Euler 114, 115, 116

p = dict()

def putTiles(n):
    if n in p:
        return p[n]
    else:
        s = 0
        for i in xrange(2, 5):
            for j in xrange(n - i + 1):
                s += 1
                k = n - j - i
                if k >= 2:
                    s += putTiles(k)
        p[n] = s
        return s
    
print putTiles(50) + 1

#A quick adaptation of p116:
#f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4), f(n) = 0 for n < 0, f(0) = 1