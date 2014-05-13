p = dict()

def putTiles(n):
    if n in p:
        return p[n]
    else:
        s = 0
        for i in xrange(3, n+1):
            for j in xrange(n - i + 1):
                s += 1
                k = n - j - i - 1
                if k >= 3:
                    s += putTiles(k)
        p[n] = s
        return s
    
print putTiles(50) + 1

#http://www.research.att.com/~njas/sequences/A005252
#WTF

#a(n) = 2a(n-1) - a(n-2) + a(n-4) 