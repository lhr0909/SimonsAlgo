from Maple import *

maple = Maple()

#maple.run("f:=n->n^3")
maple.run("f:=n->1-n+n^2-n^3+n^4-n^5+n^6-n^7+n^8-n^9+n^10")
correctNums = []
for i in xrange(11):
    correctNums.append(int(maple.execute("f(%d)" % i)))
#print correctNums

def FIT(k):
    if k == 1:
        return 1
    else:
        s = "g:=n->"
        for i in xrange(k - 1, 0, -1):
            s += "x%d*n^%d+" % (i, i)
        s += "x0"
        #print s
        maple.run(s)
        s = "sol:=solve({"
        for i in xrange(1, k):
            s += "g(%d)=%d," % (i, correctNums[i])
        s += "g(%d)=%d},{" % (k, correctNums[k])
        for i in xrange(k - 1):
            s += "x%d," % i
        s += "x%d})" % (k - 1)
        #print s
        maple.execute(s)
        maple.run("h:=n->subs(sol,g(n))")
        return int(maple.execute("h(%d)" % (k + 1)))

degree = 10
s = 0
for i in xrange(1, degree + 1):
    s += FIT(i)

print s

del maple

#http://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html
#http://en.wikipedia.org/wiki/Lagrange_polynomial