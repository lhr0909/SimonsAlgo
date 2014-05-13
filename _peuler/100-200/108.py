#http://www.research.att.com/~njas/sequences/A048691
'''
If you are allowing negative integers, the answer is the number of
factors of (n^2). If you want only positive solutions, take the number
of factors of n^2, add 1, and then divide the whole thing by 2.
'''
#so the final sequence is
#http://www.research.att.com/~njas/sequences/A018892

#    1/x + 1/y = 1/n
#   (x+y) / xy = 1/n
#   n(x+y) / xy = 1
#   nx + ny = xy
#   0 = xy - nx - ny
#   n^2 = xy - nx - ny + n^2
#   n^2 = (x - n)(y - n)

#find all the divisors for n^2, and eliminate the negative solutions.

#That's why you need to find (tau(n^2) + 1) / 2

#http://d.hatena.ne.jp/inamori/20100624/p1

from Maple import *

maple = Maple()
openNumTheory(maple)

def nSol(n):
    return (len(divisors(maple, n*n)) + 1) / 2
    
n = 1
s = nSol(n)
while s <= 1000:
    n += 1
    s = nSol(n)
    print n, s

del maple