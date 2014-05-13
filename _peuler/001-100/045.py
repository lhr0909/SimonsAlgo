from math import sqrt

t = lambda n: n*(n+1)/2
p = lambda n: n*(3*n-1)/2
h = lambda n: n*(2*n-1)
testTrianglar = lambda n: sqrt(8*n+1) == int(sqrt(8*n+1))
testPentagonal = lambda n: (sqrt(24*n+1)+1) / 6 == int((sqrt(24*n+1)+1) / 6)
testHexagonal = lambda n: (sqrt(8*n+1)+1) / 4 == int((sqrt(8*n+1)+1) / 4)

#all the test formulas are grabbed from wiki

i = 286
flag = True
while flag:
    if testPentagonal(t(i)):
        if testHexagonal(t(i)):
            print t(i)
            flag = False
    i += 1

#Cheating BS:
#    http://mathworld.wolfram.com/HexagonalPentagonalNumber.html
#    http://www.research.att.com/~njas/sequences/A046180
#    recursive representation about the trianglar/pentagonal/hexagonal numbers
#    a(n) = 37634*a(n-1) - a(n-2) + 3136
#    and apparently the first two numbers are 1 and 40755...

print 37634 * 40755 - 1 + 3136

